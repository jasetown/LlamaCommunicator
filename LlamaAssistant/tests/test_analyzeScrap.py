import os
import pytest
from analyzeScrap import collectComments, analyzeComments, createGraph

# Define paths relative to the tests directory
TEST_DIR = os.path.dirname(__file__)
TEST_COMMENTS_DIR = os.path.join(TEST_DIR, "test_comments")
TEST_SENTIMENTS_DIR = os.path.join(TEST_DIR, "test_sentiments")
TEST_PRODUCTS_FILE = os.path.join(TEST_DIR, "test_Products.txt")

@pytest.fixture(scope="module", autouse=True)
def setup_test_directories():
    os.makedirs(TEST_COMMENTS_DIR, exist_ok=True)
    os.makedirs(TEST_SENTIMENTS_DIR, exist_ok=True)
    # Create a test_Products.txt file
    with open(TEST_PRODUCTS_FILE, "w", encoding="utf-8") as f:
        f.writelines([
            "https://www.ebay.com/itm/364027692443?_skw=iphone+13&epid=10049287446&itmmeta=01JB2HGNKTJ1R5CGH28QZN8792&hash=item54c1bdc59b%3Ag%3AV7EAAOSwbhFjLLxB&itmprp=enc%3AAQAJAAAA4HoV3kP08IDx%2BKZ9MfhVJKk9sw9rsh5DhJEB1dzyJtbFDFxUitpw1uIX6b3%2FYNen0oY1Ci4hGKT--%2F9P9WkJtPkR0Eam6qWvKmhQg%2B10YgiQ%2Bz48YFh6C4943q4EkfObzJXhOnjIVmlmDVSUKuM733nDmkoUkvth16eSdz8XdOMdSI%2B0uXKZCjXUKYmv6K24okXENbwxPIQIRar9qOKeDRG%2Bq9Kf4uVSRwzqWzNZ78kmEOJ%2BmhiTEs5vbnC%2Fkts9OVPUVUTTHm22R8or%2FUZfbjsNxnPSkt5omrv0HXhne%2BQG%7Ctkp%3ABFBM_tnC0dhk&var=633337981704",
            "https://www.ebay.com/itm/384501272640?_skw=iphone+12&epid=12041705134&itmmeta=01JB2HGY81EJ7QCG0KF0RFF1SE&hash=item59860fd040%3Ag%3AngcAAOSwy9RhkpBT&itmprp=enc%3AAQAJAAAAwHoV3kP08IDx%2BKZ9MfhVJKlO%2FX28bCwvOhRSYnX0TmCcOxH9KvQmHNW19ClVYQuc8%2Ft9NGDce6Co8A%2BJ00rUDsAoo7R%2F9EyXb1c3JNCW2h54I3eiiDuaeHZIq2VxITOklHt%2FgYIZUM8y6Ppw7jh%2FgBXmcSLPWo4%2B7bqodo3A5UIekx6R652uxB%2BSqjnaikuvFgAVekQkwz9n0lnKa5glYnfGErq6%2BSGbB16PXprIW6E1kuTiQHRClyC779mR67Bb0A%3D%3D%7Ctkp%3ABk9SR5Dkw9HYZA&var=652602897249",
        ])

def test_collectComments():
    collector = collectComments(TEST_PRODUCTS_FILE, TEST_COMMENTS_DIR)
    collector.getComments()
    assert len(os.listdir(TEST_COMMENTS_DIR)) > 0

def test_analyzeComments():
    analyzer = analyzeComments()
    input_file = os.path.join(TEST_COMMENTS_DIR, "TestProduct.txt")  # Mock file
    output_file = os.path.join(TEST_SENTIMENTS_DIR, "TestProduct.txt")
    with open(input_file, "w", encoding="utf-8") as f:
        f.writelines(["Comment 1: This is great!\n", "Comment 2: Not bad.\n"])
    analyzer.analyzeSentiment(input_file, output_file)
    assert os.path.exists(output_file)

def test_createGraph():
    test_sentiments_folder = "test_Sentiments"
    test_output_chart = "test_SentimentChart.png"

    # Create dummy sentiment files
    os.makedirs(test_sentiments_folder, exist_ok=True)
    with open(os.path.join(test_sentiments_folder, "TestProduct.txt"), "w") as f:
        f.writelines(["positive\n", "negative\n", "neutral\n"])

    # Call the graphing function with a custom output path
    graph_creator = createGraph()
    graph_creator.graphData(test_sentiments_folder, output=test_output_chart)

    # Assert that the test-specific chart was created
    assert os.path.exists(test_output_chart)

    # Clean up test files (optional)
    os.remove(test_output_chart)
    for file in os.listdir(test_sentiments_folder):
        os.remove(os.path.join(test_sentiments_folder, file))
    os.rmdir(test_sentiments_folder)