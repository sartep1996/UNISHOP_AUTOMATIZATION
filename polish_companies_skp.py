from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = 'https://pl.bizin.eu/eng/'

while url:

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        categoriy_elements = soup.find_all('a', href=True, title = True)

        for category_element in categoriy_elements:
            category_name = category_element['title']
            category_url = category_element['href']

            category_number = category_element.text.split('(')[-1].split(')')[0].strip()

            if '/eng/cat/' in category_url and category_number.isdigit():

        #         print(f'Category Name: {category_name}\nCategory URL: {category_url}\nCategory Number: {category_number}\n')

        # next_page_link = soup.select_one('#pagination_categories ul li:nth-child(3) a')  # Look for the link to the next page
        # # next_page_link = soup.find('a', text=str)

        # if next_page_link:
        #     url = urljoin(url, next_page_link['href'])  # Construct the absolute URL
        # else:~
        #     url = None  # Stop if there's no next page

    else:
        print(f'Error: {response.status_code}')