import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def find_and_download_excel_files(url, download_path='"C:\\Users\\localadmin\\Downloads"'):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad requests

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links that point to Excel files (you may need to adjust the regex pattern)
        excel_links = [link['href'] for link in soup.find_all('a', href=re.compile(r'\.xlsx$|\.xls$'))]

        # Download each Excel file
        for link in excel_links:
            download_url = urljoin(url, link)
            download_file(download_url, download_path)

    except Exception as e:
        print(f"An error occurred: {e}")

def download_file(url, download_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Extract the file name from the URL
        file_name = url.split("/")[-1]

        # Save the file to the specified download path
        with open(f"{download_path}/{file_name}", 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File downloaded: {file_name}")

    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")

# Example usage
url_to_scrape = 'https://ukbusinessdatabases.club//downloads//uk-companies-list//'
find_and_download_excel_files(url_to_scrape)
