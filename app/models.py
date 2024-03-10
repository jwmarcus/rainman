from typing import Optional, List, Any
from pydantic import BaseModel
import json

# TODO: Clean up all the "Any" types to be more specific and make Pydantic calm down


class Cloud(BaseModel):
    """
    Represents a cloud object. Based on https://aviationweather.gov/data/api/#/Data/dataTaf.

    Attributes:
        cover (str): The cloud cover type.
        base (int): The cloud base height.
        type (Optional[Any]): The cloud type (optional).
    """

    cover: str
    base: int
    type: Optional[Any] = None

    class Config:
        arbitrary_types_allowed = True


class Forecast:
    """
    Represents a weather forecast. Based on https://aviationweather.gov/data/api/#/Data/dataTaf.

    Attributes:
        timeGroup (int): The time group of the forecast.
        timeFrom (int): The starting time of the forecast.
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
    timeFrom: int
    timeTo: int
    timeBec: Optional[Any] = None
    fcstChange: Optional[str] = None
    probability: Optional[Any] = None
    wdir: int
    wspd: int
    wgst: Optional[int] = None
    wshearHgt: Optional[Any] = None
    wshearDir: Optional[Any] = None
    wshearSpd: Optional[Any] = None
    visib: str
    altim: Optional[Any] = None
    vertVis: Optional[Any] = None
    wxString: Optional[Any] = None
    notDecoded: Optional[Any] = None
    clouds: List[Cloud]
    icgTurb: List[Any]
    temp: List[Any]

    class Config:
        arbitrary_types_allowed = True


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
    dbPopTime: str
    bulletinTime: str
    issueTime: str
    validTimeFrom: int
    validTimeTo: int
    rawTAF: str
    mostRecent: int
    remarks: str
    lat: float
    lon: float
    elev: int
    prior: int
    name: str
    fcsts: List[Forecast]

    class Config:
        arbitrary_types_allowed = True


def load_taf_from_json(json_data: str) -> List[TAF]:
    return TAF.model_validate_json(json_data)



# Assuming your JSON data is in a string named json_str
json_str = """[{"tafId":14824092,"icaoId":"KBOS","dbPopTime":"2024-03-09 21:06:34","bulletinTime":"2024-03-09 19:10:00","issueTime":"2024-03-09 19:10:00","validTimeFrom":1710010800,"validTimeTo":1710115200,"rawTAF":"KBOS 091910Z 0919\/1024 11012KT P6SM BKN020 FM100000 13012G19KT P6SM VCSH OVC008 FM100200 11018G30KT 4SM -RA BR OVC008 FM100700 10023G37KT 2SM RA BR OVC008 WS020\/13060KT FM101100 14021G25KT P6SM VCSH OVC008 FM101400 22014G24KT P6SM SCT030","mostRecent":0,"remarks":"AMD","lat":42.3606,"lon":-71.0097,"elev":4,"prior":2,"name":"Boston\/Logan Intl, MA, US","fcsts":[{"timeGroup":0,"timeFrom":1710010800,"timeTo":1710028800,"timeBec":null,"fcstChange":null,"probability":null,"wdir":110,"wspd":12,"wgst":null,"wshearHgt":null,"wshearDir":null,"wshearSpd":null,"visib":"6+","altim":null,"vertVis":null,"wxString":null,"notDecoded":null,"clouds":[{"cover":"BKN","base":2000,"type":null}],"icgTurb":[],"temp":[]}]}]"""

# Now, use the function to parse the JSON string
tafs = load_taf_from_json(json_str)

# Example usage
print(tafs[0])  # Prints the first TAF object in the list
