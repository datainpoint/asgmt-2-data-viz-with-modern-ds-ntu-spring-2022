import unittest
import sqlite3
import numpy as np
import pandas as pd
import exercises as ex

connection = sqlite3.connect('covid19.db')
class TestAssignmentTwo(unittest.TestCase):
    def test_01_select_all_from_daily_report(self):
        all_from_daily_report = ex.function_select_all_from_daily_report(connection)
        self.assertEqual(all_from_daily_report.shape, (4010, 4))
    def test_02_select_variables_from_time_series(self):
        variables_from_time_series = ex.function_select_variables_from_time_series(connection)
        self.assertEqual(variables_from_time_series.shape, (152262, 4))
        columns = variables_from_time_series.columns
        self.assertIn("Date", columns)
        self.assertIn("Country_Region", columns)
        self.assertIn("Confirmed", columns)
        self.assertIn("Daily_Cases", columns)
    def test_03_find_taiwan_from_time_series(self):
        taiwan_from_time_series = ex.function_find_taiwan_from_time_series(connection)
        self.assertEqual(taiwan_from_time_series.shape, (769, 6))
        np.testing.assert_equal(taiwan_from_time_series['Country_Region'].unique(),
                               np.array(['Taiwan']))
    def test_04_find_taiwan_plus_zero_from_time_series(self):
        taiwan_plus_zero_from_time_series = ex.function_find_taiwan_plus_zero_from_time_series(connection)
        self.assertEqual(taiwan_plus_zero_from_time_series.shape, (173, 3))
        np.testing.assert_equal(taiwan_plus_zero_from_time_series['Country_Region'].unique(),
                               np.array(['Taiwan']))
        self.assertEqual(taiwan_plus_zero_from_time_series['Daily_Cases'].sum(), 0)
    def test_05_find_distinct_last_update_from_daily_report(self):
        distinct_last_update_from_daily_report = ex.function_find_distinct_last_update_from_daily_report(connection)
        self.assertEqual(distinct_last_update_from_daily_report.shape, (10, 1))
    def test_06_find_distinct_date_from_time_series(self):
        distinct_date_from_time_series = ex.function_find_distinct_date_from_time_series(connection)
        self.assertEqual(distinct_date_from_time_series.shape, (769, 1))
    def test_07_find_us_from_daily_report(self):
        us_from_daily_report = ex.function_find_us_from_daily_report(connection)
        self.assertEqual(us_from_daily_report.shape, (3278, 3))
    def test_08_find_us_most_ten_confirmed_from_daily_report(self):
        us_most_ten_confirmed_from_daily_report = ex.function_find_us_most_ten_confirmed_from_daily_report(connection)
        self.assertEqual(us_most_ten_confirmed_from_daily_report.shape, (10, 1))
        combined_keys = us_most_ten_confirmed_from_daily_report["Combined_Key"].values
        self.assertIn("Los Angeles, California, US", combined_keys)
        self.assertIn("Maricopa, Arizona, US", combined_keys)
        self.assertIn("Miami-Dade, Florida, US", combined_keys)
        self.assertIn("Cook, Illinois, US", combined_keys)
        self.assertIn("Harris, Texas, US", combined_keys)
    def test_09_find_us_from_lookup_table(self):
        us_from_lookup_table = ex.function_find_us_from_lookup_table(connection)
        self.assertEqual(us_from_lookup_table.shape, (3406, 10))
        np.testing.assert_equal(us_from_lookup_table['Country_Region'].unique(),
                                np.array(['US']))
    def test_10_find_russia_and_ukraine_from_lookup_table(self):
        russia_and_ukraine_from_lookup_table = ex.function_find_russia_and_ukraine_from_lookup_table(connection)
        self.assertEqual(russia_and_ukraine_from_lookup_table.shape, (114, 10))
        country_regions = russia_and_ukraine_from_lookup_table["Country_Region"].values
        self.assertIn("Russia", country_regions)
        self.assertIn("Ukraine", country_regions)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentTwo)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))