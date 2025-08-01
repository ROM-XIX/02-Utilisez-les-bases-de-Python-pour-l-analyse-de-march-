# version du code final,
# Parcours l'ensemblde des catégories du site
# et fait l'extraction de l'ensemble des données de
# chaque livre, trié par catégorie.

import requests
from bs4 import BeautifulSoup
import csv
import re
import os
from urllib.parse import urljoin

OUTPUT_DIR_ = (
        "/home/athena6/Documents/OpenClasseRooms/"
        "02_BaseDeDonnees/datas"
    )

BASE_URL = "https://books.toscrape.com/"


def fetch_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")


def extract_text(soup, th_name):
    tag = soup.find("th", string=th_name)
    return tag.find_next_sibling("td").text if tag else "N/A"


def extract_title(soup):
    return soup.find("h1").text


def extract_description(soup):
    tag = soup.select_one("#product_description ~ p")
    return tag.text.strip() if tag else "N/A"


def extract_category(soup):
    return soup.select("ul.breadcrumb li")[2].text.strip()


def extract_rating(soup):
    tag = soup.select_one("p.star-rating")
    return tag.get("class")[1] if tag else "N/A"


def extract_number_available(availability_text):
    match = re.search(r"\((\d+) available\)", availability_text)
    return match.group(1) if match else "N/A"


def extract_image_url(soup, title):
    tag = soup.find("img", alt=title)
    if tag and "src" in tag.attrs:
        return urljoin(BASE_URL, tag["src"].replace("../", ""))
    return None


def download_image(url, title, image_dir):
    os.makedirs(image_dir, exist_ok=True)
    filename = f"{title}.jpg".replace("/", "-").replace(" ", "_")
    path = os.path.join(image_dir, filename)
    response = requests.get(url)
    with open(path, "wb") as f:
        f.write(response.content)
    return path


def save_to_csv(data, filename, headers):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(data)


def scrape_book_page(url, image_dir, csv_file):
    soup = fetch_html(url)
    title = extract_title(soup)
    upc = extract_text(soup, "UPC")
    price_excl_tax = extract_text(soup, "Price (excl. tax)")
    price_incl_tax = extract_text(soup, "Price (incl. tax)")
    tax = extract_text(soup, "Tax")
    availability = extract_text(soup, "Availability")
    num_reviews = extract_text(soup, "Number of reviews")
    description = extract_description(soup)
    category = extract_category(soup)
    rating = extract_rating(soup)
    num_available = extract_number_available(availability)
    image_url = extract_image_url(soup, title)

    # Télécharger image
    if image_url:
        download_image(image_url, title, image_dir)

    # Préparer les données
    data = [
        title,
        upc,
        price_excl_tax,
        price_incl_tax,
        tax,
        availability,
        num_available,
        num_reviews,
        category,
        rating,
        description,
        image_url or "N/A",
    ]

    headers = [
        "Title",
        "UPC",
        "Price (excl. tax)",
        "Price (incl. tax)",
        "Tax",
        "Availability",
        "Number Available",
        "Number of Reviews",
        "Category",
        "Rating",
        "Description",
        "Image URL",
    ]

    save_to_csv(data, csv_file, headers)


def get_all_category_links():
    soup = fetch_html(BASE_URL)
    category_links = []
    for a in soup.select("ul.nav-list ul li a"):
        href = a.get("href")
        full_url = urljoin(BASE_URL, href)
        category_name = a.text.strip()
        category_links.append((category_name, full_url))
    return category_links


def get_all_book_links_in_category(category_url):
    book_links = []
    while category_url:
        soup = fetch_html(category_url)
        for h3 in soup.select("h3 a"):
            href = h3.get("href")
            full_url = urljoin(
                category_url, href
                ).replace("../../../", BASE_URL + "catalogue/")
            book_links.append(full_url)

        next_button = soup.select_one("li.next a")
        if next_button:
            next_href = next_button.get("href")
            category_url = urljoin(category_url, next_href)
        else:
            category_url = None
    return book_links


def scrape_all_books(output_dir):
    categories = get_all_category_links()

    for category_name, category_url in categories:
        print(f"\n* Catégorie : {category_name}")

        # Dossiers pour cette catégorie
        category_folder = os.path.join(output_dir, "datas", category_name)
        image_dir = os.path.join(output_dir, "images", category_name)
        csv_file = os.path.join(category_folder, "books.csv")

        book_urls = get_all_book_links_in_category(category_url)

        for book_url in book_urls:
            print(f"  -> Scraping : {book_url}")
            try:
                scrape_book_page(book_url, image_dir, csv_file)
            except Exception as e:
                print(f" !!  Erreur avec {book_url} : {e}")


# === Lancement ===
if __name__ == "__main__":
    OUTPUT_DIR = OUTPUT_DIR_
    scrape_all_books(OUTPUT_DIR)
