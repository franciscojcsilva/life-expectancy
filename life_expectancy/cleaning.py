from typing import Optional
import pandas as pd

from life_expectancy.regions import Region


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

    df = pd.melt(
        expectancy_data,
        id_vars=[expectancy_data.columns[0]],
        value_vars=list(expectancy_data.columns[1:]),
        value_name="value",
        var_name="year",
    )

    df[["unit", "sex", "age", "region"]] = df[r"unit,sex,age,geo\time"].str.split(
        ",", n=4, expand=True
    )

    df = df.drop(columns=[r"unit,sex,age,geo\time"])
    df["year"] = df["year"].astype("int")
    df["value"] = df["value"].str.extract("([0-9]+[,./]*[0-9]*)").astype("float")
    df = df.dropna(subset=["value"])
    df = df[["unit", "sex", "age", "region", "year", "value"]]
    df = df[df.region == region.value] if region else df

    return df.reset_index(drop=True)
