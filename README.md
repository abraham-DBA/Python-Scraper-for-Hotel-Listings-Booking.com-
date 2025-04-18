# Python-Scraper-for-Hotel-Listings-Booking.com-
A Python web scraper that extracts hotel listings from Booking.com and saves them to an Excel/CSV file. Perfect for travelers, researchers, or data analysts who need structured hotel data (name, price, location, ratings, and more).

✨ Features
Scrapes key hotel details:
Hotel name
Price (cleaned of currency symbols)
Location
Guest ratings & review scores
Number of reviews
Direct booking links
Exports to Excel/CSV (Pandas-powered)

User-friendly: 
Just input a Booking.com search URL and filename.

Anti-blocking measures:
Randomized delays between requests

Browser-like headers

🚀 Quick Start
Prerequisites
Python 3.x

Libraries:
requests, BeautifulSoup, pandas, lxml

Installation
bash
Copy
pip install requests beautifulsoup4 pandas lxml

How to Use
Run the script:python booking_scraper.py

Enter:
A Booking.com search URL (e.g., https://www.booking.com/searchresults.html?ss=Paris)
Your desired output filename (e.g., paris_hotels.xlsx)
Wait for the scrape to complete.
Check your folder for the exported data!
