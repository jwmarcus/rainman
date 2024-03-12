from app.models import TAF

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import requests


def main():

    # Define the format for the datetime strings.
    datetime_format = "%a %m-%d %I:%M %p"
    eastern_tz = ZoneInfo("America/New_York")

    # Define the airport and the current datetime.
    airport = "KBOS"
    current_datetime = datetime.now(timezone.utc)
    base_url = f"https://aviationweather.gov/api/data/taf"

    # Make the request to the API.
    response = requests.get(
        base_url,
        params={
            "ids": airport,
            "format": "json",
            "date": current_datetime.isoformat(),
        },
    )
    data = response.json()

    # Print the TAF data.
    for taf in data:
        model = TAF(**taf)
        print(f"Station:    {model.icaoId}")
        print(
            f"Issue Time: {model.issueTime.astimezone(eastern_tz).strftime(datetime_format)}"
        )
        print(
            f"Valid From: {model.validTimeFrom.astimezone(eastern_tz).strftime(datetime_format)}"
        )
        print(
            f"Valid To:   {model.validTimeTo.astimezone(eastern_tz).strftime(datetime_format)}"
        )
        print("")

        for forecast in model.fcsts:
            if forecast.wxString is not None:
                print(
                    f"TimeFrom: {forecast.timeFrom.astimezone(eastern_tz).strftime(datetime_format)}"
                )
                print(
                    f"TimeTo:   {forecast.timeTo.astimezone(eastern_tz).strftime(datetime_format)}"
                )
                print(f"WxString: {forecast.wxString}")
                print("")


if __name__ == "__main__":
    main()
