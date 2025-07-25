import requests
from bs4 import BeautifulSoup
import csv
import re
import os

# URL d'une page produit spécifique - product_page_url
url = (
  "https://books.toscrape.com/catalogue/"
  "dune-dune-1_151/index.html"
)
# url = (
#     "https://books.toscrape.com/catalogue/"
#     "a-light-in-the-attic_1000/index.html"
# )

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# - Extraire les données - #

# title
title = soup.find("h1").text

# prix HT - price_excluding_tax
price_excl_tax = (
    soup.find("th", string="Price (excl. tax)").find_next_sibling("td").text
)

# prix TTC - price_including_tax
price_incl_tax = (
    soup.find("th", string="Price (incl. tax)").find_next_sibling("td").text
)

# tax
tax = soup.find("th", string="Tax").find_next_sibling("td").text

# number_available
availability = (
    soup.find("th", string="Availability").find_next_sibling("td").text.strip()
)

# universal_ product_code (upc)
upc = soup.find("th", string="UPC").find_next_sibling("td").text

# nbr de review
num_reviews = soup.find(
    "th",
    string="Number of reviews").find_next_sibling("td").text

# Description - product_description
description_tag = soup.select_one("#product_description ~ p")
description = description_tag.text if description_tag else "N/A"

# Catégorie - category
category = soup.select("ul.breadcrumb li")[2].text.strip()

# Note - review_rating
rating_tag = soup.select_one("p.star-rating")
rating = rating_tag.get("class")[1] if rating_tag else "N/A"

# Nettoyage de la disponibilité
match = re.search(r"\((\d+) available\)", availability)
num_available = match.group(1) if match else "N/A"

# Image - récupération par alt = title
img_tag = soup.find("img", alt=title)
image_url = img_tag["src"] if img_tag else None

if image_url:
    image_url_ = "https://books.toscrape.com/" + image_url.replace("../", "")

    # Créer le dossier images s'il n'existe pas
    image_dir = (
        "/home/athena6/Documents/OpenClasseRooms/"
        "02_BaseDeDonnees/images"
    )
    os.makedirs(image_dir, exist_ok=True)

    # Télécharger et sauvegarder l'image
    image_response = requests.get(image_url_)
    image_path = os.path.join(image_dir, f"{title}.jpg")

    with open(image_path, "wb") as img_file:
        img_file.write(image_response.content)

    print(f"Image enregistrée dans : {image_path}")
else:
    image_url = "N/A"
    print("Image non trouvée.")

# Nom du fichier de sortie
filename = (
    "/home/athena6/Documents/OpenClasseRooms/02_BaseDeDonnees/datas/"
    "a_light_in_the_attic.csv"
)

# Enregistrement dans un CSV
with open(filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(
        [
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
    )

    writer.writerow(
        [
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
    )

print(f"Données extraites et sauvegardées dans '{filename}'")
