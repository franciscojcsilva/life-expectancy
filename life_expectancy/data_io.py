from pathlib import Path
import pandas as pd

from life_expectancy.regions import Region


def load_life_expectancy_data(data_dir: Path) -> pd.DataFrame:
    """
    Loads EU life expectancy data .tsv file.

    Parameters
    ----------
    data_dir : Path
        Path to the data directory.

    Returns
    -------
    pd.DataFrame
        Output dataframe.
    """

    return pd.read_csv(data_dir / "eu_life_expectancy_raw.tsv", sep="\t", header=0)


def save_life_expectancy_data(data_dir: Path, data: pd.DataFrame, region: Region) -> None:
    """
    Saves life expectancy dataframe for a given country as csv file.

    Parameters
    ----------
    data_dir : Path
        Path to the data directory.
    data : pd.DataFrame
        Input data to save locally.
    region : Region
        Region of the data subset we want to process.
    """

    data.to_csv(data_dir / f"{region.value.lower()}_life_expectancy.csv", index=False)
