import pytest
from unittest.mock import MagicMock, patch

mocker = MagicMock()

from clean_code_2.utils.generate import (generate_random_string,
                                        generate_random_number,
                                        generate_random_number_from_api)

@pytest.mark.parametrize("min, max", [(1, 100),
                                      (0, 10),
                                      (5, 15),
                                      (10, 20)
                                      ])
def test_generate_random_number(min, max):
    number = generate_random_number(min, max)
    assert isinstance(number, int), "Number should be an integer"
    assert min <= number <= max, f"Number should be between {min} and {max}"

def test_generate_random_number_from_api():
    with patch("clean_code_2.utils.generate.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "42"
        mock_get.return_value = mock_response

        number = generate_random_number_from_api()
        assert isinstance(number, int), "Number should be an integer"
        assert 1 <= number <= 100, "Number should be between 1 and 100"



if __name__ == "__main__":
    import sys
    print(sys.path)
