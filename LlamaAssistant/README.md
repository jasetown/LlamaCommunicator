
# Llama Product Assistant

**Llama Product Assistant** is a Python-based project that combines web scrapping with sentiment analysis using an LLM (Phi-3-Mini). This tool is designed for extracting product reviews from ebay, analyzing sentiments / impressions, and visualizing the data in a user-friendly format.

---

## Features

- **Web Scrapping with Beautiful Soup 4**: Collects product reviews from specified ebay URLs using Beautiful Soup and Python's requests library.
- **Sentiment Analysis using GPT4ALL with Phi-3-Mini**: Leverages the GPT4All-based Llama model for classifying reviews as positive, negative, or neutral.
- **Visualization with Matplotlib**: Generates stacked bar charts for product insights.
- **Extensibility**: Modular design allows easy integration with other functionalities.

---

## Installation

### Prerequisites
Ensure you have **Conda** installed on your system. If not, download it [here](https://docs.conda.io/en/latest/miniconda.html).

### Setup

1. Clone this repository and navigate to the project directory:

   ```bash
   git clone https://github.com/your-repo/LlamaProductAssistant.git
   cd LlamaProductAssistant
   ```

2. Create the required Conda environment:

   ```bash
   conda env create -f requirements.yaml
   conda activate llama_product_assistant
   ```

3. Verify the installation:

   ```bash
   python --version
   ```

---

## Usage

### 1. **Prepare Input**
- Add product URLs to `Products.txt`. Each line should contain one URL.

### 2. **Run the Program**
Execute the main script to perform scraping, sentiment analysis, and visualization.

```bash
python analyzeScrap.py
```

### 3. **Outputs**
- **Comments**: Saved in the `Comments` folder.
- **Sentiments**: Saved in the `Sentiments` folder.
- **Visualization**: A bar chart is generated as `SentimentChart.png`.

---

## Example Workflow

### Input (`Products.txt`):
```text
https://www.ebay.com/itm/166978620935
https://www.ebay.com/itm/355685944723
```

### Output (Sample Sentiments):
```
Positive
Negative
Neutral
Positive
```

### Visualization:
The program generates a grouped bar chart categorizing sentiments per product.
![SentimentChart](https://github.com/user-attachments/assets/e518f3e3-f11d-4431-85f1-2aa78138d183)

---

## Code Structure

### `webScrap.py`
Handles web scraping:
- `collectData(url)`: Fetches HTML content from a given URL.
- `analyzeData(soup, url)`: Extracts product title and comments from the parsed HTML.

### `GPTCommunicator.py`
Interacts with the Llama model:
- `askLlama(model, prompt)`: Sends a prompt to the Llama model and retrieves a response.
- `storetoFile(filename, responses)`: Saves generated responses to a file.

### `analyzeScrap.py`
Integrates the functionality:
- `collectComments`: Fetches comments from URLs and saves them to text files.
- `analyzeComments`: Classifies comments into sentiments using the Llama model.
- `createGraph`: Visualizes sentiment distribution.

---

## Requirements

- Python 3.11
- [GPT4All](https://github.com/nomic-ai/gpt4all)
- Beautiful Soup 4
- Requests
- Matplotlib
- Conda for environment management

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For questions or contributions, feel free to submit an issue or a pull request. Let the **Llama Product Assistant** simplify your data scraping and sentiment analysis needs!
