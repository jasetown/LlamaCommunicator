# Import GPT4ALL class to interact with model.
from gpt4all import GPT4All

# Create function to read prompts from {filename} and return prompt list.
def getPrompt(filename, prompts=3):
    # Open in Read mode.
    with open(filename, 'r') as file:
        # Read the file line by line, strip any whitespace from each line, and collect the specified number of prompts into a list.
        promptCollection = [line.strip() for line in file.readlines()[:prompts]]
    # Return the list of prompts.
    return promptCollection

# Create function to generate a response from the Llama model based on a given prompt.
def askLlama(model, prompt):
    # Use the generate function of the GPT4All model.
    response = model.generate(prompt)
    # Return the generated response.
    return response

# Create function to store the generated responses into a file.
def storetoFile(filename, responses):
    # Open the file in Write mode (THIS WILL OVERWRITE EXISTING FILE).
    with open(filename, 'w') as file:
        # Loop through each generated response and write to file.
        for i, response in enumerate(responses):
            #Precede each response with "Answer{number}:".
            file.write(f"Answer {i+1}: {response}\n\n")

def main():

    # Initialize the GPT4All model by loading a specific Llama model ("Meta-Llama-3-8B-Instruct.Q4_0.gguf") (THIS WILL DOWNLOAD THE MODEL TO YOUR SYSTEM).
    model = GPT4All(model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf")

    # Define the Input file
    filePrompts = 'prompts.txt'
    # Define the Output file
    fileResponses = 'responses.txt'

    # Get the list of prompts from the prompts.txt file.
    prompts = getPrompt(filePrompts)
    # Create an empty list to store the responses.
    responses = []
    # Loop through every prompt (3).
    for prompt in prompts:
        # Generate a response through askLlama and store it into the response list.
        response = askLlama(model, prompt)
        responses.append(response)

    # Store all responses to file by passing responses[] to storetoFile
    storetoFile(fileResponses, responses)
    
    #Completion Message
    print(f"Done! check {fileResponses}.")

# Stop accidental execution of script
if __name__ == "__main__":
    main()