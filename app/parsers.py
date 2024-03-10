import json
from typing import List
from .models import Cloud, Forecast, TAF

# Assuming the data classes Cloud, Forecast, and TAF are already defined as previously discussed


def _parse_cloud(cloud_data: dict) -> Cloud:
    """
    Parse cloud data and return a Cloud object.

    Args:
        cloud_data (dict): A dictionary containing cloud data.

    Returns:
        Cloud: A Cloud object with parsed cloud data.
    """
    return Cloud(
        cover=cloud_data.get("cover"),
        base=cloud_data.get("base"),
        type=cloud_data.get("type"),
    )


def _parse_forecast(forecast_data: dict) -> Forecast:
    """
    Parse forecast data and return a Forecast object.

    Args:
        forecast_data (dict): The forecast data to be parsed.

    Returns:
        Forecast: The parsed forecast object.

    """
    clouds = [_parse_cloud(cloud) for cloud in forecast_data.get("clouds", [])]
    return Forecast(
        timeGroup=forecast_data.get("timeGroup"),
        timeFrom=forecast_data.get("timeFrom"),
        timeTo=forecast_data.get("timeTo"),
        timeBec=forecast_data.get("timeBec"),
        fcstChange=forecast_data.get("fcstChange"),
        probability=forecast_data.get("probability"),
        wdir=forecast_data.get("wdir"),
        wspd=forecast_data.get("wspd"),
        wgst=forecast_data.get("wgst"),
        wshearHgt=forecast_data.get("wshearHgt"),
        wshearDir=forecast_data.get("wshearDir"),
        wshearSpd=forecast_data.get("wshearSpd"),
        visib=forecast_data.get("visib"),
        altim=forecast_data.get("altim"),
        vertVis=forecast_data.get("vertVis"),
        wxString=forecast_data.get("wxString"),
        notDecoded=forecast_data.get("notDecoded"),
        clouds=clouds,
        icgTurb=forecast_data.get("icgTurb", []),
        temp=forecast_data.get("temp", []),
    )


def parse_taf(json_data: str) -> List[TAF]:
    """
    Parse TAF data from JSON format.

    Args:
        json_data (str): The JSON data containing TAF information.

    Returns:
        List[TAF]: A list of TAF objects parsed from the JSON data.
    """
    data = json.loads(json_data)
    tafs = []
    for item in data:
        fcsts = [_parse_forecast(fcst) for fcst in item.get("fcsts", [])]
        taf = TAF(
            tafId=item.get("tafId"),
            icaoId=item.get("icaoId"),
            dbPopTime=item.get("dbPopTime"),
            bulletinTime=item.get("bulletinTime"),
            issueTime=item.get("issueTime"),
            validTimeFrom=item.get("validTimeFrom"),
            validTimeTo=item.get("validTimeTo"),
            rawTAF=item.get("rawTAF"),
            mostRecent=item.get("mostRecent"),
            remarks=item.get("remarks"),
            lat=item.get("lat"),
            lon=item.get("lon"),
            elev=item.get("elev"),
            prior=item.get("prior"),
            name=item.get("name"),
            fcsts=fcsts,
        )
        tafs.append(taf)
    return tafs


# Use the parse_taf function with your JSON data as input
# json_data = '...'  # Your JSON string here
# tafs = parse_taf(json_data)
