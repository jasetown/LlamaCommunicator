import os
import pytest
from webScrap import collectData, analyzeData
from bs4 import BeautifulSoup

# Define paths relative to the tests directory
TEST_DIR = os.path.dirname(__file__)
TEST_OUTPUTS_DIR = os.path.join(TEST_DIR, "test_outputs")

@pytest.fixture(scope="module", autouse=True)
def setup_test_directory():
    # Create the test_outputs directory if it doesn't exist
    os.makedirs(TEST_OUTPUTS_DIR, exist_ok=True)

# Test analyzeData with missing elements
def test_analyzeData_missing_elements():
    html_content = "<html></html>"
    soup = BeautifulSoup(html_content, 'lxml')
    output = analyzeData(soup, "test_url")
    expected_output = ["No Title Found\n",
                        "\n",
                        "-" * 100 + "\n\n"]

    # Write the result to a test file
    output_file = os.path.join(TEST_OUTPUTS_DIR, "test_output.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(output)

    # Verify the content of the file
    with open(output_file, "r", encoding="utf-8") as f:
        result = f.readlines()

    assert result == expected_output
