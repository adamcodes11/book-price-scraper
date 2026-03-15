import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.styles import Font
from datetime import datetime
import os


def scrape_books(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    books = []
    for article in soup.select("article.product_pod"):
        title = article.select_one("h3 a")["title"]
        price = article.select_one(".price_color").text.strip()
        rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating_class = article.select_one(".star-rating")["class"][1]
        rating = rating_map.get(rating_class, 0)
        availability = article.select_one(".availability").text.strip()
        books.append({
            "Title": title,
            "Price": price,
            "Rating (1-5)": rating,
            "Availability": availability
        })
    return books


def save_to_excel(books, filename=None):
    os.makedirs("books", exist_ok=True)
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"books/books_{timestamp}.xlsx"

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Books"

    headers = ["Title", "Price", "Rating (1-5)", "Availability", "Scraped At"]
    ws.append(headers)

    for col in range(1, len(headers) + 1):
        ws.cell(1, col).font = Font(bold=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    for book in books:
        ws.append([book["Title"], book["Price"], book["Rating (1-5)"], book["Availability"], now])

    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_len + 2

    wb.save(filename)
    print(f"Saved {len(books)} books to {filename}")


def main():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    all_books = []

    print("Scraping books.toscrape.com...")
    for page in range(1, 4):
        print(f"  Page {page}...")
        books = scrape_books(base_url.format(page))
        all_books.extend(books)

    save_to_excel(all_books)
    print(f"\nDone! Total books scraped: {len(all_books)}")


main()
