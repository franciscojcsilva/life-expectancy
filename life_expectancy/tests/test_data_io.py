"""Tests for the IO module"""

from unittest.mock import patch, Mock
import pandas as pd

from life_expectancy.data_io import load_life_expectancy_data, save_life_expectancy_data
from life_expectancy.regions import Region

from . import FIXTURES_DIR


def test_load_life_expectancy_data(eu_life_expectancy_raw: pd.DataFrame) -> None:
    """Run the `load_data` function and compare the output to the expected output"""

    loaded_data = load_life_expectancy_data(FIXTURES_DIR / "eu_life_expectancy_raw.tsv")
    pd.testing.assert_frame_equal(loaded_data, eu_life_expectancy_raw)


@patch("life_expectancy.data_io.pd.DataFrame.to_csv")
def test_save_life_expectancy_data(to_csv: Mock, pt_life_expectancy_expected: pd.DataFrame) -> None:
    """Test the save_data function"""
    to_csv.side_effect = lambda *args, **kwargs: print("saving data to CSV")
    save_life_expectancy_data(FIXTURES_DIR, pt_life_expectancy_expected, Region.PT)
    to_csv.assert_called_once_with(FIXTURES_DIR / "pt_life_expectancy.csv", index=False)
