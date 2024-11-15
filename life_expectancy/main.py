import argparse
import pandas as pd

from life_expectancy.io import load_data, save_data
from life_expectancy.cleaning import clean_data


def main() -> pd.DataFrame:
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--region", default="PT")
    args = parser.parse_args()

    life_expectancy_data = load_data()
    processed_expectancy_data = clean_data(life_expectancy_data, args.region)
    save_data(processed_expectancy_data, args.region)


if __name__ == "__main__":  # pragma: no cover
    main()
