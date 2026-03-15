# 📦 Book Price Scraper

A Python script that scrapes book titles, prices, ratings, and availability from [books.toscrape.com](https://books.toscrape.com) and exports the data to a formatted Excel file.

## Features
- Scrapes multiple pages automatically
- Exports to Excel with bold headers and auto-sized columns
- Adds timestamp to each row

## Requirements
```
Python 3.8+ installed
```
```
pip install -r requirements.txt
```


## Usage
```bash
python price_scraper.py
```
Output: `books.xlsx`

## Example Output
| Title | Price | Rating (1-5) | Availability | Scraped At |
|---|---|---|---|---|
| A Light in the Attic | £51.77 | 3 | In stock | 2025-03-15 12:00 |
