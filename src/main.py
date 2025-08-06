# version du code qui fait l'extraction des datas d'une page de livre
# comme le code du main
# restrucuté avec par fonction

import requests
from bs4 import BeautifulSoup
import csv
import re
import os


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
        return "https://books.toscrape.com/" + tag["src"].replace("../", "")
    return None


def download_image(url, title, image_dir):
    os.makedirs(image_dir, exist_ok=True)
    response = requests.get(url)
    image_path = os.path.join(image_dir, f"{title}.jpg")
    with open(image_path, "wb") as f:
        f.write(response.content)
    return image_path


def save_to_csv(data, filename):
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
        "Image URL"
    ]
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerow(data)


def scrape_book_page(url, image_dir, output_csv):
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

    if image_url:
        image_path = download_image(image_url, title, image_dir)
        print(f"Image enregistrée dans : {image_path}")
    else:
        image_url = "N/A"
        print("Image non trouvée.")

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
        image_url
    ]

    save_to_csv(data, output_csv)
    print(f"Données extraites et sauvegardées dans '{output_csv}'")


# === MAIN EXECUTION ===
if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/dune-dune-1_151/index.html"
    image_dir = (
        "/home/athena6/Documents/OpenClasseRooms/"
        "02_BaseDeDonnees/images"
    )
    output_csv = (
        "/home/athena6/Documents/OpenClasseRooms/02_BaseDeDonnees/"
        "datas/a_light_in_the_attic.csv"
    )
    scrape_book_page(url, image_dir, output_csv)
