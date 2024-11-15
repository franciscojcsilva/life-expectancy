import argparse
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"


def load_data() -> pd.DataFrame:
    """
    Loads EU life expectancy data .tsv file.

    Returns
    -------
    pd.DataFrame
        Output dataframe.
    """

    return pd.read_csv(
        DATA_DIR / "eu_life_expectancy_raw.tsv",
        sep='\t',
        header=0
    )

def save_data(data: pd.DataFrame, region: str) -> None:
    """
    Saves life expectancy dataframe for a given country as csv file.

    Parameters
    ----------
    data : pd.DataFrame
        Input data to save locally.
    region : str
        Region of the data subset we want to process.
    """

    data.to_csv(DATA_DIR / f"{region.lower()}_life_expectancy.csv", index=False)