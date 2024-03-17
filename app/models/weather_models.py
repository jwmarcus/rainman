from typing import Optional, Any
from pydantic import BaseModel, validator
from datetime import datetime, timezone


# TODO: Encode this into an enum or something
# https://en.wikipedia.org/wiki/METAR#METAR_weather_codes


class Cloud(BaseModel):
    """
    Represents a cloud object.
    Based on https://aviationweather.gov/data/api/#/Data/dataTaf.

    Attributes:
        cover (str): The cover of the cloud.
        base (int): The base of the cloud.
        type (Optional[str]): The type of the cloud (optional).
    """

    cover: str
    base: Optional[int] = None
    type: Optional[str] = None


class Forecast(BaseModel):
    """
    Represents a weather forecast.
    Based on https://aviationweather.gov/data/api/#/Data/dataTaf.

    Attributes:
        timeGroup (int): The time group of the forecast.
        timeFrom (datetime): The starting time of the forecast.
        timeTo (datetime): The ending time of the forecast.
        timeBec (Optional[datetime]): The time when the forecast becomes valid.
        fcstChange (Optional[str]): The forecast change information.
        probability (Optional[str]): The probability of the forecast.
        wdir (int): The wind direction.
        wspd (int): The wind speed.
        wgst (Optional[int]): The wind gust speed.
        wshearHgt (Optional[int]): The wind shear height.
        wshearDir (Optional[int]): The wind shear direction.
        wshearSpd (Optional[int]): The wind shear speed.
        visib (int | str): The visibility.
        altim (Optional[str]): The altimeter setting.
        vertVis (Optional[str]): The vertical visibility.
        wxString (Optional[str]): The weather string.
        notDecoded (Optional[str]): The not decoded information.
        clouds (list[Cloud]): The list of cloud information.
        icgTurb (list[str]): The list of icing and turbulence information.
        temp (list[str]): The list of temperature information.
    """

    timeGroup: int
    timeFrom: datetime
    timeTo: datetime
    timeBec: Optional[datetime]
    fcstChange: Optional[str]
    probability: Optional[str]
    wdir: Optional[int] = None
    wspd: Optional[int] = None
    wgst: Optional[int] = None
    wshearHgt: Optional[int] = None
    wshearDir: Optional[int] = None
    wshearSpd: Optional[int] = None
    visib: int | str
    altim: Optional[str] = None
    vertVis: Optional[str] = None
    wxString: Optional[str] = None
    notDecoded: Optional[str] = None
    clouds: list[Cloud]
    icgTurb: list[str]
    temp: list[str]


class TAF(BaseModel):
    """
    Represents a Terminal Aerodrome Forecast (TAF) object.
    Based on https://aviationweather.gov/data/api/#/Data/dataTaf.

    Attributes:
        tafId (int): The unique identifier for the TAF.
        icaoId (str): The ICAO code for the location associated with the TAF.
        dbPopTime (datetime): The database population time for the TAF.
        bulletinTime (datetime): The bulletin time for the TAF.
        issueTime (datetime): The issue time for the TAF.
        validTimeFrom (datetime): The start time of the validity period for the TAF.
        validTimeTo (datetime): The end time of the validity period for the TAF.
        rawTAF (str): The raw text of the TAF.
        mostRecent (int): Indicator for the most recent TAF.
        remarks (str): Additional remarks for the TAF.
        lat (float): The latitude of the location associated with the TAF.
        lon (float): The longitude of the location associated with the TAF.
        elev (int): The elevation of the location associated with the TAF.
        prior (int): Indicator for a prior TAF.
        name (str): The name of the location associated with the TAF.
        fcsts (list[Forecast]): A list of forecast objects associated with the TAF.
    """

    tafId: int
    icaoId: str
    dbPopTime: datetime
    bulletinTime: datetime
    issueTime: datetime
    validTimeFrom: datetime
    validTimeTo: datetime
    rawTAF: str
    mostRecent: int
    remarks: str
    lat: float
    lon: float
    elev: int
    prior: int
    name: str
    fcsts: list[Forecast] = []

    @validator("dbPopTime", "bulletinTime", "issueTime", pre=True)
    def convert_time(cls, v):
        """
        Convert a string representation of a datetime to an aware datetime object.
        The avaiationweather.gov API returns datetime objects as strings in the format "YYYY-MM-DD HH:MM:SS".
        This means we need to set it as an aware datetime object with the timezone set to UTC.

        Args:
            v (str): The string representation of the datetime (lacking an offset).

        Returns:
            datetime: The aware datetime object.

        Raises:
            ValueError: If the string representation is not in the expected format.
        """
        unaware_time = datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
        aware_time = unaware_time.replace(tzinfo=timezone.utc)
        return aware_time
