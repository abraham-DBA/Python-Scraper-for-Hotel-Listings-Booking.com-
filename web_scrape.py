import requests 
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import random
import os

def web_scraper(web_url, file_path):
    print("Starting the web scraping process...")
    
    # Validate URL
    if not web_url.startswith('http'):
        print("Error: Please enter a valid URL starting with http:// or https://")
        return

    # Create directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    try:
        response = requests.get(web_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        print("Connected to the website successfully!")
        
        soup = BeautifulSoup(response.text, 'lxml')
        hotel_divs = soup.find_all('div', role="listitem")

        if not hotel_divs:
            print("No hotels found on the page. Check if the page structure has changed.")
            return

        data = {
            'hotel_name': [],
            'locality': [],
            'price': [],
            'rating': [],
            'score': [],
            'review': [],
            'link': []
        }

        for hotel in hotel_divs:
            # Hotel Name
            try:
                name = hotel.find('div', class_="f6431b446c a15b38c233").text.strip()
            except AttributeError:
                name = "NA"
            data['hotel_name'].append(name)

            # Location
            try:
                location = hotel.find('span', class_="aee5343fdb def9bc142a").text.strip()
            except AttributeError:
                location = "NA"
            data['locality'].append(location)

            # Price
            try:
                price = hotel.find('span', class_="f6431b446c fbfd7c1165 e84eb96b1f").text.strip().replace('US$', '')
            except AttributeError:
                price = "NA"
            data['price'].append(price)

            # Rating
            try:
                rating = hotel.find('div', class_="a3b8729ab1 e6208ee469 cb2cbb3ccb").text.strip()
            except AttributeError:
                rating = "NA"
            data['rating'].append(rating)

            # Score
            try:
                score = hotel.find('div', class_="a3b8729ab1 d86cee9b25").text.strip().split(' ')[-1]
            except (AttributeError, IndexError):
                score = "NA"
            data['score'].append(score)

            # Reviews
            try:
                review = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47").text.strip()
            except AttributeError:
                review = "NA"
            data['review'].append(review)

            # Link
            try:
                link = hotel.find('a', class_="a83ed08757 f88a5204c2 c057617e1a b98133fb50")['href']
                link = f"https://www.booking.com{link}" if not link.startswith('http') else link
            except (AttributeError, TypeError):
                link = "NA"
            data['link'].append(link)

        df = pd.DataFrame(data)
        
        # Ensure file has .xlsx extension
        if not file_path.lower().endswith('.xlsx'):
            file_path += '.xlsx'
            
        df.to_excel(file_path, index=False)
        print(f"Data successfully saved to {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print("Booking.com Web Scraper")
    print("-----------------------")
    
    url = input("Please enter the Booking.com search URL: ").strip()
    file_path = input("Please enter the full file path to save the data (e.g., C:/data/hotels.xlsx): ").strip()
    
    web_scraper(url, file_path)