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

## Usage
```bash
Commands*:
pip3 / python3     - Mac/Linux
pip  / python      - Windows

# 1. Download repo
git clone https://github.com/adamcodes11/book-price-scraper.git
cd book-price-scraper
# or simply download zip file

# 2. Create venv (optional but recommended)
python* -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip* install -r requirements.txt

# 4. Run
python* price_scraper.py
```
Output: `books.xlsx`

## Example Output
| Title | Price | Rating (1-5) | Availability | Scraped At |
|---|---|---|---|---|
| A Light in the Attic | £51.77 | 3 | In stock | 2025-03-15 12:00 |
