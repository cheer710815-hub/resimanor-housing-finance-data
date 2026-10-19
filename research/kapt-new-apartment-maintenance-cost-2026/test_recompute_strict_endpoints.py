#!/usr/bin/env python3
"""Offline synthetic regression tests: no API key, no network or real resident data."""
import csv
import json
import pathlib
import tempfile
import unittest

from recompute_strict_endpoints import audit, FIELDS

class EndpointRegressionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = pathlib.Path(self.tmp.name) / "A10000001_202301"
        self.path.mkdir()
        self.csvfile = self.path / "cost_raw_long.csv"

    def build(self, modifications=None, duplicate=False, months=24):
        modifications = modifications or {}
        with self.csvfile.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["kaptCode","operation","searchDate","result_json"])
            writer.writeheader()
            for i in range(months):
                date=f"{2023+(i//12):04}{1+(i%12):02}"
                for field, method in FIELDS.items():
                    amount = modifications.get((field,i), 100 if i < 3 else 110 if i >= 21 else 105)
                    row={"kaptCode":"A10000001","operation":method,"searchDate":date,"result_json":json.dumps({"response":{"body":{"item":{field:amount}}}})}
                    writer.writerow(row)
                    if duplicate and i==0 and field=="pay":
                        writer.writerow(row)

    def locate(self, rows, field):
        return next(r for r in rows if r[1] == field)

    def test_complete_first_last_three(self):
        self.build()
        rows, problems=audit([self.csvfile])
        self.assertEqual(problems, [])
        self.assertEqual(len(rows),3)
        for field in FIELDS:
            row=self.locate(rows,field)
            self.assertEqual(row[2],24)
            self.assertEqual(row[3],"eligible")
            self.assertAlmostEqual(float(row[4]),10.0)

    def test_null_exclusion_is_field_specific(self):
        self.build({("pay",0):None})
        rows, problems=audit([self.csvfile])
        self.assertEqual(problems, [])
        self.assertEqual(self.locate(rows,"pay")[3],"null_or_nonnumeric")
        self.assertEqual(self.locate(rows,"cleanCost")[3],"eligible")

    def test_zero_exclusion_is_field_specific(self):
        self.build({("guardCost",23):0})
        rows,_=audit([self.csvfile])
        self.assertEqual(self.locate(rows,"guardCost")[3],"zero_or_nonpositive")
        self.assertEqual(self.locate(rows,"pay")[3],"eligible")

    def test_duplicate_is_reported(self):
        self.build(duplicate=True)
        _,problems=audit([self.csvfile])
        self.assertEqual(len(problems),1)
        self.assertIn("duplicate",problems[0][1])

    def test_short_observation_window_is_ineligible(self):
        self.build(months=23)
        rows,_=audit([self.csvfile])
        self.assertTrue(all(r[3]=="month_count_not_24" for r in rows))

if __name__=="__main__":
    unittest.main()
