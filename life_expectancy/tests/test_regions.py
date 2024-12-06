from life_expectancy.regions import Region


def test_get_countries():
    """
    Test that get_countries returns only actual countries.
    """

    countries = Region.get_countries()

    # Test that known countries are included
    assert Region.PT in countries
    assert Region.FR in countries
    assert Region.DE in countries

    # Test that non-country regions are excluded
    assert Region.EU27_2020 not in countries
    assert Region.EFTA not in countries
    assert Region.EEA31 not in countries
    assert Region.DE_TOT not in countries

    # Test that all returned values are Region enums
    assert all(isinstance(country, Region) for country in countries)

    # Test that we have a reasonable number of countries
    # The EU has ~27 countries plus some additional European countries
    assert 30 <= len(countries) <= 50
