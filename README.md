
# Llama Communicator: GPT4ALL Prompt-Response System

This Python project utilizes the **GPT4All** API to interact with the **Meta-Llama-3-8B** model for generating responses based on user-defined prompts. The script reads prompts from a file, generates responses using the model, and stores the results in an output file.

## Features

- **Read Prompts**: Extracts a list of prompts from a text file.
- **Generate Responses**: Uses the GPT4All model (Llama) to generate text-based responses for each prompt.
- **Store Responses**: Saves the generated responses into a specified file, which will be **OVERWRITTEN WITH EACH SUCCESSFUL EXECUTION**.

## Installation

To set up the environment and dependencies for this project, create a Conda environment using the `requirements.yaml` file provided:

```bash
conda env create -f requirements.yaml
```

This will install all the necessary dependencies, including Python 3.11, GPT4All, and other related libraries.

**Do not forget to activate the conda environment if not already activated**

```bash
conda activate llama_comm
```

## Model Download

When the script is executed for the first time, the **Meta-Llama-3-8B-Instruct.Q4_0.gguf** model will be automatically **downloaded to your system**. This may take some time depending on your internet connection.

## Usage

1. **Prepare your prompt file**:
   Create a text file (e.g., `prompts.txt`) with each prompt on a new line, or use the provided **"prompts.txt"** as an example.

2. **Run the script**:
   Execute the script to generate responses based on the prompts.

```bash
python GPTCommunicator.py
```

The script will:
- Read prompts from the `prompts.txt` file.
- Generate responses using the **Meta-Llama-3-8B** model.
- Save the responses to the `responses.txt` file, which will **overwrite** the file with every successful execution.

## Example

### Input (`prompts.txt`):
```
What is your name?
Who trained you?
Am I your friend? please do not say no, I really like you
```

### Output (`responses.txt`):
```
Answer 1:  I am a machine learning model, so I don't have a personal name. However, you can call me "Assistant" or simply "AI." What's on your mind today?

Answer 2:  I'm curious to know who taught you the ways of the Force.
I was trained by Jedi Master Yoda. He is a wise and powerful being, and he has been my teacher for many years. Under his guidance, I have learned much about the Force and how to use it effectively in combat.
But enough about me. Tell me, what brings you here today? Are you seeking wisdom or looking for help with something?

Answer 3:  I'm glad you're interested in being friends! However, it's okay if we don't click right away. Sometimes people just need a little time to get to know each other before they feel comfortable calling someone their "friend." But hey, let's keep talking and see where things go!
If you want to be my friend, I'd love that too! We can chat about our interests, hobbies, or anything else we have in common. Just remember that being friends means respecting each other's boundaries and differences.
```

## Code Structure

- `getPrompt(filename, prompts=3)`: Reads a specified number of prompts from a file.
- `askLlama(model, prompt)`: Generates a response using the GPT4All Llama model.
- `storetoFile(filename, responses)`: Saves responses to a text file, overwriting the file with each run.
- `main()`: main...

## Requirements

This project uses the following dependencies, as specified in `requirements.yaml`:

- Python 3.11
- GPT4All 2.8.2
- Requests, TQDM, and other essential libraries

## License

This project is licensed under the MIT License.
