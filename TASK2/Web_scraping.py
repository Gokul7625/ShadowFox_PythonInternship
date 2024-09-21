import requests
from bs4 import BeautifulSoup
import csv
# Function to fetch webpage content
def fetch_webpage(url):
    try:
        # Send a GET request
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return None

# Function to scrapedata
def scrape_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        books.append({'Title': title, 'Price': price})

    return books

# Function to save scrapeddata
def save_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Price'])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

def main():
    url = "http://books.toscrape.com/"
    page_content = fetch_webpage(url)
    if page_content:
        scraped_data = scrape_data(page_content)
        save_data_to_csv(scraped_data, 'Book_Data.csv')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
