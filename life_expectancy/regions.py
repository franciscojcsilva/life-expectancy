from enum import Enum, unique


@unique
class Region(Enum):
    """
    Enum representing regions in life expectancy data.
    """

    AT = "AT"
    BE = "BE"
    BG = "BG"
    CH = "CH"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    EE = "EE"
    EL = "EL"
    ES = "ES"
    EU27_2020 = "EU27_2020"
    FI = "FI"
    FR = "FR"
    HR = "HR"
    HU = "HU"
    IS = "IS"
    IT = "IT"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    MT = "MT"
    NL = "NL"
    NO = "NO"
    PL = "PL"
    PT = "PT"
    RO = "RO"
    SE = "SE"
    SI = "SI"
    SK = "SK"
    DE = "DE"
    DE_TOT = "DE_TOT"
    AL = "AL"
    EA18 = "EA18"
    EA19 = "EA19"
    EFTA = "EFTA"
    IE = "IE"
    ME = "ME"
    MK = "MK"
    RS = "RS"
    AM = "AM"
    AZ = "AZ"
    GE = "GE"
    TR = "TR"
    UA = "UA"
    BY = "BY"
    EEA30_2007 = "EEA30_2007"
    EEA31 = "EEA31"
    EU27_2007 = "EU27_2007"
    EU28 = "EU28"
    UK = "UK"
    XK = "XK"
    FX = "FX"
    MD = "MD"
    SM = "SM"
    RU = "RU"

    @classmethod
    def __missing__(cls, value: str) -> None:
        valid_regions = ", ".join(region.name for region in cls)
        raise ValueError(f"'{value}' is not a valid region. Valid regions are: {valid_regions}")

    @classmethod
    def get_countries(cls) -> list["Region"]:
        """
        Returns a list of Region enums that represent actual countries
        (excluding groups like EU27, EFTA, etc.)

        Returns:
            list[Region]: List of Region enums that represent actual countries
        """
        excluded_prefixes = ("EU", "EA", "EEA", "EFTA")
        excluded_regions = {"UK", "DE_TOT"}

        return [
            region
            for region in cls
            if not region.value.startswith(excluded_prefixes)
            and region.value not in excluded_regions
        ]
