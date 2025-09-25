# Foundations Learning Path Assignments

[![Python package](https://github.com/francisco3511/lp-foundations/actions/workflows/python-package.yml/badge.svg)](https://github.com/francisco3511/lp-foundations/actions/workflows/python-package.yml)

## Introduction

A Python package for processing and analyzing European life expectancy data from Eurostat. This tool transforms raw TSV data into clean, analyzable CSV files with filtering capabilities by country/region.

## Features

- **Multi-format Data Loading**: Supports TSV, CSV, and zipped JSON files
- **Data Cleaning Pipeline**: Transforms raw Eurostat format into clean, structured data
- **Regional Filtering**: Filter data by specific countries or European regions
- **Comprehensive Coverage**: Supports 40+ European countries and regions

## 📊 Data Format

The pipeline processes Eurostat life expectancy data with the following structure:

**Input**: Raw TSV data with pivoted years as columns
**Output**: Clean CSV with columns:
- `unit`: Measurement unit (years)
- `sex`: Gender (M/F)
- `age`: Age group
- `country`: Country/region code
- `year`: Year of measurement
- `life_expectancy`: Life expectancy value

## 🛠️ Installation

### Prerequisites

Ensure you have Python 3.8+ and an up-to-date pip:

```bash
python --version  # Should be 3.8 or higher
pip --version
pip install --upgrade pip
```

### Install the Package

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd life-expectancy
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install the package**:
   ```bash
   pip install -e .
   ```

4. **Install development dependencies** (optional):
   ```bash
   pip install -e .[dev]
   ```

## 📖 Usage

### Command Line Interface

Process life expectancy data for a specific region:

```bash
# Process data for Portugal (default)
life-expectancy

# Process data for a specific country
life-expectancy --region DE  # Germany
life-expectancy --region FR  # France
life-expectancy --region ES  # Spain

# Short form
life-expectancy -r IT  # Italy
```

### Supported Regions

The package supports 40+ European countries and regions including:

- **EU Countries**: AT, BE, BG, CZ, DK, EE, FI, FR, DE, EL, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- **EFTA Countries**: CH, IS, LI, NO
- **Candidate Countries**: AL, ME, MK, RS, TR
- **Other European**: UK, UA, BY, MD, RU
- **Regional Groups**: EU27_2020, EA19, EFTA

## 🏗️ Architecture

The project follows clean architecture principles with modular components:

- **`main.py`**: CLI entry point and orchestration
- **`data_io.py`**: Data loading and saving with strategy pattern
- **`data_strategies.py`**: File format handling strategies (TSV, CSV, ZIP)
- **`cleaning.py`**: Data transformation and validation pipeline
- **`regions.py`**: Country/region definitions and validation

## 🧪 Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=life_expectancy

# Run specific test file
pytest life_expectancy/tests/test_cleaning.py
```

### Project Structure


life_expectancy/
├── data/ # Raw data files
│ ├── eu_life_expectancy_raw.tsv
│ └── eurostat_life_expect.zip
├── tests/ # Test suite
│ ├── fixtures/ # Test data
│ ├── test_cleaning.py
│ ├── test_data_io.py
│ └── test_regions.py
├── cleaning.py # Data cleaning pipeline
├── data_io.py # Data I/O operations
├── data_strategies.py # File loading strategies
├── main.py # CLI entry point
└── regions.py # Region definitions

## 📋 Requirements

- **Python**: 3.8+
- **Dependencies**:
  - `pandas`: Data manipulation and analysis
- **Development Dependencies**:
  - `pytest`: Testing framework
  - `pylint`: Code linting
  - `black`: Code formatting
  - `pytest-cov`: Coverage reporting
  - `pre-commit`: Git hooks


## 📄 License

This project is licensed under the terms specified in `LICENSE.md`.

## 📞 Contact

**Francisco Silva** - francisco.silva@ren.pt

Project Link: [https://github.com/francisco3511/lp-foundations](https://github.com/francisco3511/lp-foundations)