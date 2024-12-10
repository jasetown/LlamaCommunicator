import os
from webScrap import collectData, analyzeData
from GPTCommunicator import GPT4All, askLlama, storetoFile
import matplotlib.pyplot as plt

# Class to Collect Comments
class collectComments:

    # Initialize Input and Outputs (Input File and Output Folder)
    def __init__(self, input_file, output_folder):
        self.input_file = input_file
        self.output_folder = output_folder
        # Check Output Folder
        os.makedirs(output_folder, exist_ok=True)

    # Get Comments from URLs in Input File and Save to Text Files in Output Folder
    def getComments(self):
        # Open Input File and Read URLs
        with open(self.input_file, 'r') as file:
            urls = file.readlines()
        
        # Loop Through URLs
        for i, url in enumerate(urls):
            # Trim Whitespace
            url = url.strip()
            # Get HTML
            soup = collectData(url)
            # Parse for Comments
            output = analyzeData(soup, url)
            # Save Comments to Text File
            productName = output[0].strip()
            output_file = os.path.join(self.output_folder, f"{productName}.txt")
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.writelines(output)

        print(f"Comments Placed in {self.output_folder}")

# Class to Analyze Comments
class analyzeComments:

    # Initialize LLM Meta 3 8B
    print("Initializing Model")
    def __init__(self, model_name="Phi-3-mini-4k-instruct.Q4_0.gguf"):
        self.model = GPT4All(model_name=model_name)
        print("Model Initialized")

    # Grab Comments and Prompt LLM for Sentiment Analysis
    def analyzeSentiment(self, input_file, output_file):
        os.makedirs("Sentiments", exist_ok=True)
        # Read Comments from Input
        with open(input_file, 'r') as file:
            comments = [line.strip() for line in file.readlines() if line.startswith("Comment")]
        
        # Analyze Comments
        responses = []
        for comment in comments:
            print(f"Processing Comment: {comment}")
            # Create Query for LLM
            prompt = f"'Please classify this comment as positive, negative, or neutral using one word only and nothing else: \"{comment}\".'"
            # Get Sentiments from LLM
            response = askLlama(self.model, prompt)
            responses.append(response)
        # Save to Output File
        storetoFile(output_file, responses)
        print(f"Sentiments Placed in {output_file}")

# Class to Visualize Data
class createGraph:
    @staticmethod
    def graphData(sentimentsFolder, output = "SentimentChart.png"):
        import numpy as np  
        # Initialize Data
        deviceSentiments = {}    
        # Read Sentiments from Each Device's File
        for file in os.listdir(sentimentsFolder):
            if file.endswith(".txt"):
                deviceName = file.replace(".txt", "")
                sentimentsCounts = {'positive': 0, 'negative': 0, 'neutral': 0}
                with open(os.path.join(sentimentsFolder, file), 'r') as infile:
                    sentiments = infile.readlines()
                    # Count Sentiments
                    for sentiment in sentiments:
                        for key in sentimentsCounts.keys():
                            if key in sentiment.lower():
                                sentimentsCounts[key] += 1
                
                deviceSentiments[deviceName] = sentimentsCounts
        
        # Get Variables to Plot
        devices = list(deviceSentiments.keys())
        categories = ['positive', 'negative', 'neutral']
        counts = {category: [deviceSentiments[device].get(category, 0) for device in devices] for category in categories}
        
        # Create Grouped Bar Chart
        x = np.arange(len(devices))
        width = 0.2
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Plot Sentiments
        for i, category in enumerate(categories):
            ax.bar(x + i * width, counts[category], width, label=category)
        
        # Add Labels and Title
        ax.set_xlabel('Devices')
        ax.set_ylabel('Count')
        ax.set_title('Sentiment Analysis per Device')
        ax.set_xticks(x + width)
        ax.set_xticklabels(devices, rotation=45, ha='right', fontsize=8)
        ax.legend(title='Sentiments')
        
        # Save or Display Graph
        plt.tight_layout()
        plt.savefig(output)

def main():
    # Collect Comments
    scrapper = collectComments(input_file="Products.txt", output_folder="Comments")
    scrapper.getComments()

    # Analyze Comments
    analyzer = analyzeComments()
    for file in os.listdir("Comments"):
        if file.endswith(".txt"):
            input_path = os.path.join("Comments", file)
            output_path = os.path.join("Sentiments", file)
            analyzer.analyzeSentiment(input_path, output_path)

    # Graph Results
    createdGraph = createGraph()
    createdGraph.graphData("Sentiments")
    print("Graph Created in Root Folder. Program has Finished. Goodbye :)")

# Prevent Accidental Execution
if __name__ == "__main__":
    main()