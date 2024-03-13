from app.models import TAF
from datetime import datetime, timezone
import pytest


def test_convert_time_valid_format() -> None:
    # Arrange
    input_time = "2022-01-01 12:00:00"
    expected_output = datetime(2022, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    # Act
    result = TAF.convert_time(input_time)

    # Assert
    assert result == expected_output


def test_convert_time_invalid_format() -> None:
    # Arrange
    input_time = "2022-01-01 12:00"  # Invalid format

    # Act and Assert
    with pytest.raises(ValueError):
        TAF.convert_time(input_time)
