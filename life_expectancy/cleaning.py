import argparse
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"


def clean_data(country: str) -> None:
    """
    Cleans life expectancy data by unpivoting and removing unwanted values.
    Saves Portugal life expectancy records.
    """

    df = pd.read_csv(
        DATA_DIR / "eu_life_expectancy_raw.tsv",
        sep='\t',
        header=0
    )

    df = pd.melt(
        df,
        id_vars=df.columns[0],
        value_vars=df.columns[1:],
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

    df = df.loc[
        df.region == country,
        ['unit', 'sex', 'age', 'region', 'year', 'value']
    ].to_csv(DATA_DIR / f"{country.lower()}_life_expectancy.csv", index=False)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--country", default="PT", action="store_true")
    args = parser.parse_args()
    clean_data(args.country)
