from typing import Optional, Any
from pydantic import BaseModel
from datetime import datetime

import json
import requests


class Cloud(BaseModel):
    """
    Represents a cloud object. Based on https://aviationweather.gov/data/api/#/Data/dataTaf.

    Attributes:
        cover (str): The cloud cover type.
        base (int): The cloud base height.
        type (Optional[str]): The cloud type (optional). Only value is "CB"
    """

    cover: str
    base: int
    type: Optional[str]


class Forecast(BaseModel):
    """
    Represents a weather forecast. Based on https://aviationweather.gov/data/api/#/Data/dataTaf.

    Attributes:
        timeGroup (int): The time group of the forecast.
        timeFrom (int): The starting time of the forecast. In UNIX Epoch format
        timeTo (int): The ending time of the forecast.
        timeBec (Optional[Any]): The time when the forecast becomes valid.
        fcstChange (Optional[str]): The forecast change information.
        probability (Optional[Any]): The probability of the forecast.
        wdir (int): The wind direction.
        wspd (int): The wind speed.
        wgst (Optional[int]): The wind gust speed.
        wshearHgt (Optional[Any]): The height of wind shear.
        wshearDir (Optional[Any]): The direction of wind shear.
        wshearSpd (Optional[Any]): The speed of wind shear.
        visib (str): The visibility.
        altim (Optional[Any]): The altimeter setting.
        vertVis (Optional[Any]): The vertical visibility.
        wxString (Optional[Any]): The weather string.
        notDecoded (Optional[Any]): The not decoded information.
        clouds (List[Cloud]): The list of cloud information.
        icgTurb (List[Any]): The list of icing and turbulence information.
        temp (List[Any]): The list of temperature information.
    """

    timeGroup: int
    timeFrom: datetime
    timeTo: datetime
    timeBec: Optional[datetime]
    fcstChange: Optional[str]
    probability: Optional[str]
    wdir: int
    wspd: int
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
    Represents a Terminal Aerodrome Forecast (TAF).  Based on https://aviationweather.gov/data/api/#/Data/dataTaf.

    Attributes:
        tafId (int): The TAF ID.
        icaoId (str): The ICAO ID.
        dbPopTime (str): The database population time.
        bulletinTime (str): The bulletin time.
        issueTime (str): The issue time.
        validTimeFrom (int): The valid time from.
        validTimeTo (int): The valid time to.
        rawTAF (str): The raw TAF data.
        mostRecent (int): The most recent flag.
        remarks (str): The remarks.
        lat (float): The latitude.
        lon (float): The longitude.
        elev (int): The elevation.
        prior (int): The prior flag.
        name (str): The name of the location.
        fcsts (List[Forecast]): The list of forecasts.

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


def main():
    url = "https://aviationweather.gov/api/data/taf?ids=KBOS&format=json&date=2024-03-09T020:00:00Z"
    response = requests.get(url)
    data = response.json()

    for taf in data:
        model = TAF(**taf)
        print(model.rawTAF)


if __name__ == "__main__":
    main()