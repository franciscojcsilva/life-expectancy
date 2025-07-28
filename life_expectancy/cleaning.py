from typing import Optional
import pandas as pd

from life_expectancy.regions import Region


REQUIRED_COLUMNS = ["unit", "sex", "age", "country", "year", "life_expectancy"]


def validate_and_filter_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validates that all required columns exist and returns DataFrame with only those columns.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to validate

    Returns
    -------
    pd.DataFrame
        DataFrame containing only the required columns

    Raises
    ------
    ValueError
        If any required columns are missing from the DataFrame
    """
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}. "
            f"Available columns: {', '.join(df.columns)}"
        )

    return df[REQUIRED_COLUMNS]


def clean_data(expectancy_data: pd.DataFrame, region: Optional[Region] = None) -> pd.DataFrame:
    """
    Cleans life expectancy data by unpivoting and removing unwanted values
    and returning data for a specified region.

    Parameters
    ----------
    expectancy_data : pd.DataFrame
        Main EU life expectancy historical records dataframe.
    region : str
        Region of interest for output.

    Returns
    -------
    pd.DataFrame
        Processed life expectancy data.
    """

    if r"unit,sex,age,geo\time" in expectancy_data.columns:
        df = pd.melt(
            expectancy_data,
            id_vars=[expectancy_data.columns[0]],
            value_vars=list(expectancy_data.columns[1:]),
            value_name="life_expectancy",
            var_name="year",
        )

        df[["unit", "sex", "age", "country"]] = df[r"unit,sex,age,geo\time"].str.split(
            ",", n=4, expand=True
        )

        df = df.drop(columns=[r"unit,sex,age,geo\time"])
        df["year"] = df["year"].astype("int")
        df["life_expectancy"] = (
            df["life_expectancy"].str.extract("([0-9]+[,./]*[0-9]*)").astype("float")
        )
        df = df.dropna(subset=["life_expectancy"])
    else:
        df = expectancy_data.copy()

    df = validate_and_filter_columns(df)
    df = df[df.country == region.value] if region else df

    return df.reset_index(drop=True)
