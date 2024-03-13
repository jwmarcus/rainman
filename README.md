# Weather Data Parser

This project demonstrates the parsing and validation of weather forecast data (Terminal Aerodrome Forecasts, TAF) into Python objects using `pydantic`. The project structures the data with `pydantic` models for better type checking and validation.

## Project Structure

- `models.py`: Contains `pydantic` models that represent the structure of the weather data.
- `main.py`: An example script that shows how to load, parse, and validate JSON weather data.

Install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

1. run the app using `uvicorn app:app --reload`

## Example

### Defining Models

In `models.py`, define models that represent your data structure:

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class Cloud(BaseModel):
    cover: str
    base: int
    type: Optional[str] = None

class Forecast(BaseModel):
    timeGroup: int
    timeFrom: int
    timeTo: int
    clouds: List[Cloud]

class TAF(BaseModel):
    tafId: int
    icaoId: str
    forecasts: List[Forecast]
```

### Parsing JSON

In `main.py`, load your JSON data and parse it:

```python
from models import TAF
import json

def load_and_parse_data(json_file_path: str) -> TAF:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return TAF(**data)

if __name__ == "__main__":
    json_file_path = 'path_to_your_json_file.json'
    taf_data = load_and_parse_data(json_file_path)
    print(taf_data)
```

This will load the JSON data, validate it against the `pydantic` model, and print the parsed object.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
