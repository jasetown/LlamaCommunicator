import os
import pytest
from GPTCommunicator import getPrompt, askLlama, storetoFile

# Define paths relative to the tests directory
TEST_DIR = os.path.dirname(__file__)
TEST_PROMPTS_FILE = os.path.join(TEST_DIR, "test_prompts.txt")
TEST_RESPONSES_FILE = os.path.join(TEST_DIR, "test_responses.txt")

@pytest.fixture(scope="module", autouse=True)
def setup_test_files():
    # Create test_prompts.txt
    with open(TEST_PROMPTS_FILE, "w", encoding="utf-8") as f:
        f.writelines(["Prompt 1\n", "Prompt 2\n", "Prompt 3\n"])

def test_getPrompt():
    prompts = getPrompt(TEST_PROMPTS_FILE, 2)
    assert len(prompts) == 2

def test_askLlama():
    class MockModel:
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_value, traceback): pass
        def chat_session(self): return self
        def generate(self, prompt): return "Positive"

    mock_model = MockModel()
    response = askLlama(mock_model, "Test prompt")
    assert response == "Positive"

def test_storetoFile():
    responses = ["Positive", "Negative", "Neutral"]
    storetoFile(TEST_RESPONSES_FILE, responses)
    with open(TEST_RESPONSES_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 3
