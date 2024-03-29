# Standard library imports
from typing import Dict, Any
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# Related third party imports
from fastapi import APIRouter, Depends
from starlette.requests import Request
import httpx
import asyncio

# Local application/library specific imports
from ..models.weather_models import TAF

WEATHER_API = "https://aviationweather.gov/api/data/taf"
# Define the format for the datetime strings.
DT_FMT = "%a %m-%d %I:%M %p"
EASTERN_TZ = ZoneInfo("America/New_York")

router = APIRouter()


async def get_taf_data(airport: str, format: str, date: str):
    # Make the request to the API.
    async with httpx.AsyncClient() as client:
        response = await client.get(
            WEATHER_API,
            params={
                "ids": airport,
                "format": format,
                "date": date,
            },
        )
        data = response.json()
    return data


@router.get("/weather/{airport}")
async def get_current_weather(airport: str) -> Dict[str, Any]:
    # Get the weather data for the provided airport.
    current_datetime = datetime.now(timezone.utc)
    data = await get_taf_data(airport, "json", current_datetime.isoformat())
    
    weather_events = []
    for taf in data:
        model = None
        try:
            model = TAF(**taf)
            for forecast in model.fcsts:
                if forecast.wxString is not None:
                    weather_event = {
                        "TimeFrom": {forecast.timeFrom.astimezone(EASTERN_TZ).strftime(DT_FMT)},
                        "TimeTo":   {forecast.timeTo.astimezone(EASTERN_TZ).strftime(DT_FMT)},
                        "WxString": {forecast.wxString},
                    }
                    weather_events.append(weather_event)

        except Exception as e:
            print(f"Error: {e}")
            print(f"Data: {taf}")
            continue

    return {"weather_events": weather_events}


@router.get("/weather")
async def get_current_weather_default():
    # Default to Boston Logan if no airport given
    return await get_current_weather("KBOS")


def main():
    # This mucst be called as a module like `python app.routers.weather`
    weather_json = asyncio.run(get_current_weather_default())
    print(weather_json)


if __name__ == "__main__":
    main()


# Print the TAF data.
# for taf in data:
#     model = TAF(**taf)
#     print(f"Station:    {model.icaoId}")
#     print(
#         f"Issue Time: {model.issueTime.astimezone(eastern_tz).strftime(datetime_format)}"
#     )
#     print(
#         f"Valid From: {model.validTimeFrom.astimezone(eastern_tz).strftime(datetime_format)}"
#     )
#     print(
#         f"Valid To:   {model.validTimeTo.astimezone(eastern_tz).strftime(datetime_format)}"
#     )
#     print("")

#     for forecast in model.fcsts:
#         if forecast.wxString is not None:
#             print(
#                 f"TimeFrom: {forecast.timeFrom.astimezone(eastern_tz).strftime(datetime_format)}"
#             )
#             print(
#                 f"TimeTo:   {forecast.timeTo.astimezone(eastern_tz).strftime(datetime_format)}"
#             )
#             print(f"WxString: {forecast.wxString}")
#             print("")
