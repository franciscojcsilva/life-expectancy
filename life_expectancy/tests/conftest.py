"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR


@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load the input life expectancy data sample"""
    return pd.read_csv(
        FIXTURES_DIR / "eu_life_expectancy_raw.tsv",
        sep='\t',
        header=0
    )


@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv")


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script for pt data"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
