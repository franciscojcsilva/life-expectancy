from abc import ABC, abstractmethod
from pathlib import Path
import json
import zipfile

import pandas as pd


class DataStrategy(ABC):
    """
    Abstract class for data strategies
    """

    @abstractmethod
    def load(self, file_path: Path) -> pd.DataFrame:
        """Load data from a file"""


class TSVStrategy(DataStrategy):
    """
    Strategy for loading data from a .tsv file
    """

    def load(self, file_path: Path) -> pd.DataFrame:
        return pd.read_csv(file_path, sep="\t", header=0)


class CSVStrategy(DataStrategy):
    """
    Strategy for loading data from a .csv file
    """

    def load(self, file_path: Path) -> pd.DataFrame:
        return pd.read_csv(file_path, header=0)


class ZippedJSONStrategy(DataStrategy):
    """
    Strategy for loading data from a zipped JSON file
    """

    def load(self, file_path: Path) -> pd.DataFrame:
        """
        Load data from a zipped JSON file.
        Assumes the ZIP contains a single JSON file.
        """
        with zipfile.ZipFile(file_path, "r") as zip_file:
            json_filename = zip_file.namelist()[0]
            with zip_file.open(json_filename) as json_file:
                json_data = json.loads(json_file.read().decode("utf-8"))
                return pd.DataFrame(json_data)


class DataStrategyFactory:
    """
    Factory class for creating data loading strategies
    """

    @staticmethod
    def create_strategy(file_path: Path) -> DataStrategy:
        """
        Creates the appropriate strategy based on file extension

        Parameters
        ----------
        file_name : str
            Name of the file to load

        Returns
        -------
        DataStrategy
            The appropriate strategy for the file type

        Raises
        ------
        ValueError
            If the file extension is not supported
        """
        extension = file_path.suffix.lower()
        strategy_map = {
            ".tsv": TSVStrategy(),
            ".csv": CSVStrategy(),
            ".zip": ZippedJSONStrategy(),
        }

        if extension not in strategy_map:
            raise ValueError(
                f"Unsupported file extension: {extension}. "
                f"Supported extensions are: {', '.join(strategy_map.keys())}"
            )

        return strategy_map[extension]
