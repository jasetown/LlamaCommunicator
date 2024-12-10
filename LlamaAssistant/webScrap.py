# Import Requests for HTTP requests
import requests
# Import Beautiful Soup for Parsing
from bs4 import BeautifulSoup

# Function to get content from URL
def collectData(url):
    # Set data to Response from requests.get(url)
    data = requests.get(url)
    # Parse using BeautifulSoup and lxml parser
    soup = BeautifulSoup(data.text, 'lxml')
    # Return the Parsed Object
    return soup

# Function to Piece Together Data from collectData
def analyzeData(soup, url):
    # Initialize an Empty List to Store Output Data
    output = []
    
    title = None  # Default value if the chain fails
    if soup.find('h1', class_='x-item-title__mainTitle') and soup.find('h1', class_='x-item-title__mainTitle').find('span'):
        title = soup.find('h1', class_='x-item-title__mainTitle').find('span').get_text()

    # Append the Title to the Output List
    output.append(f"{title}\n" if title else "No Title Found\n")

    
    # Locate all Review Comments Within Specific div Tags by Class
    numComments = soup.find_all('div', class_='fdbk-container__details__comment')
    # Extract the Text from Each Comment Span and Store in a List
    comments = [comment.find('span').get_text() for comment in numComments]
    
    # Loop Through the Comments, Adding Each One With its Index to the Output
    for i, comment in enumerate(comments, 1):
        output.append(f"Comment {i}: {comment}\n")
    
    # Append a Divider to Separate Content from Different URLs
    output.append("\n" + "-"*100 + "\n\n")
    
    # Return the List Containing the Processed data for One Product Page
    return output

# Main Function to Trigger Processes
def main():
    # Open the File with Product URLs in Read Mode
    with open('products.txt', 'r') as file:
        # Read All Lines
        urls = file.readlines() 
    
    # Open or Create outputs.txt in Write Mode
    with open('outputs.txt', 'w', encoding='utf-8') as outfile:
        # Loop Through Each URL, Write to outputs.txt
        for url in urls:
            # Remove any leading or trailing whitespace
            url = url.strip()
            # Collect HTML data from the URL
            soup = collectData(url)
            # Analyze the collected data
            output = analyzeData(soup, url)
            # Write the analyzed data to the output file
            outfile.writelines(output)

# Stop Accidental Execution
if __name__ == '__main__':
    main()
