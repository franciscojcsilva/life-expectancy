from pathlib import Path

import pandas as pd

from life_expectancy.regions import Region
from life_expectancy.data_strategies import DataStrategyFactory


def load_life_expectancy_data(file_path: Path) -> pd.DataFrame:
    """
    Loads EU life expectancy data using the appropriate strategy based on file extension.

    Parameters
    ----------
    file_name : str
        Name of the file to load.

    Returns
    -------
    pd.DataFrame
        Output dataframe.
    """
    strategy = DataStrategyFactory.create_strategy(file_path)
    return strategy.load(file_path)


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
