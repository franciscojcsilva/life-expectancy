import argparse
from pathlib import Path

from life_expectancy.data_io import load_life_expectancy_data, save_life_expectancy_data
from life_expectancy.cleaning import clean_data
from life_expectancy.regions import Region

DATA_DIR = Path(__file__).parent / "data"


def main() -> None:
    """
    Main function to read, clean and save life expectancy data.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--region", default="PT", type=lambda x: Region[x])
    args = parser.parse_args()

    life_expectancy_data = load_life_expectancy_data(DATA_DIR / "eu_life_expectancy_raw.tsv")
    processed_expectancy_data = clean_data(life_expectancy_data, args.region)
    save_life_expectancy_data(DATA_DIR, processed_expectancy_data, args.region)


if __name__ == "__main__":  # pragma: no cover
    main()
