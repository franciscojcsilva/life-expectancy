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


def clean_data(expectancy_data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans life expectancy data by unpivoting and removing unwanted values.

    Parameters
    ----------
    expectancy_data : pd.DataFrame
        Main EU life expectancy historical records dataframe.

    Returns
    -------
    pd.DataFrame
        Processed life expectancy data.
    """

    df = pd.melt(
        expectancy_data,
        id_vars=expectancy_data.columns[0],
        value_vars=expectancy_data.columns[1:],
        value_name='value',
        var_name='year'
    )

    df[['unit', 'sex', 'age', 'region']] = (
        df[r"unit,sex,age,geo\time"]
        .str
        .split(',', n=4, expand=True)
    )

    df = df.drop(columns=[r"unit,sex,age,geo\time"])
    df['year'] = df['year'].astype('int')
    df['value'] = df['value'].str.extract('([0-9]+[,./]*[0-9]*)').astype('float')
    df = df.dropna(subset=['value'])

    return df[['unit', 'sex', 'age', 'region', 'year', 'value']]


def save_data(data: pd.DataFrame, country: str) -> None:
    """
    Saves life expectancy dataframe for a given country as csv file.

    Parameters
    ----------
    data : pd.DataFrame
        Input data to save locally.
    country : str
        Country of the data subset we want to process.
    """

    df = data.loc[data.region == country, :]
    df.to_csv(DATA_DIR / f"{country.lower()}_life_expectancy.csv", index=False)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--country", default="PT", action="store_true")
    args = parser.parse_args()

    life_expectancy_data = load_data()
    processed_expectancy_data = clean_data(life_expectancy_data)
    save_data(processed_expectancy_data, args.country)
