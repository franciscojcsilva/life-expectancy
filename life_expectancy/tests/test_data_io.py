"""Tests for the IO module"""
from unittest.mock import patch
import pandas as pd

from life_expectancy.data_io import load_life_expectancy_data, save_life_expectancy_data

from . import FIXTURES_DIR


def test_load_life_expectancy_data(eu_life_expectancy_raw):
    """Run the `load_data` function and compare the output to the expected output"""

    loaded_data = load_life_expectancy_data(FIXTURES_DIR)
    pd.testing.assert_frame_equal(
        loaded_data, eu_life_expectancy_raw
    )


def test_save_life_expectancy_data(pt_life_expectancy_expected):
    """Test the save_data function using a mock for pd.DataFrame.to_csv"""
    with patch.object(pd.DataFrame, 'to_csv') as mock_to_csv:
        save_life_expectancy_data(FIXTURES_DIR, pt_life_expectancy_expected, "PT")
        mock_to_csv.assert_called_once_with(FIXTURES_DIR / "pt_life_expectancy.csv", index=False)
