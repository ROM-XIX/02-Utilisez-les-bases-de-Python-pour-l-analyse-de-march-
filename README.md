
# Context : 

Dans le cadre de la formation OpenClassRooms, pour la formation de développeur logiciel Python.

Le projet numéro 2 demande de pouvoir extraire l'ensemble des données d'un site de vente de livres en ligne.

# L'objectif du code :

les données du site à récolter sont les suivantes :

1. product_page_url
2. universal_ product_code (upc)
3. title
4. price_including_tax
5. price_excluding_tax 
6. number_available
7. product_description
8. category
9. review_rating
10. image_ur
11. Extraire et enregistrer les fichiers images de chaque livre

# Ce que le code fait :

le code récupérer l'index de l'ensemble des catégories du site https://books.toscrape.com sur la page d'index. 

puis parcourt chaque livre de chaque catégorie, pendant ce parcours il ce passe 4 choses:

1. On crée un répertoire pour stocker les CSV des données produit, par catégorie.
2. On crée un repertoire pour stocker les images produit, par catégorie.
3. On crée un CSV par catégorie qui contient l'ensemble des données demandé ***l'objectif du code*** [Link Text](#lobjectif-du-code-).
4. On récupère le lien de l'image du produit, et on enregistre cette image dans le répertoire indiqué.

Voici une représentation de l'arborescence générée :

```
02_BaseDeDonnees/
├── .env_oc_p02/
│
├── src/
│   └── main3.py
├── datas/
│   ├── Travel/
│   │   └── books.csv
│   ├── Poetry/
│   │   └── books.csv
│   └── ...
├── images/
│   ├── Travel/
│   │   └── book1.jpg
│   ├── Poetry/
│   │   └── book2.jpg
│   └── ...
```

# procédure d'utilisation :

## 1. Récupérer le repo depuis github :

Téléchargé le github depuis le lien du dépot github.

Pour cela une fois sur la page du dépot github, dans la barre au dessous du nom du dépot, cliquez sur le bouton **<>CODE** puis, dans l’onglet local, cliquez sur  **DownloadZIP**,
enregistrez le fichier ZIP à l’emplacement souhaité sur votre ordinateur.

Puis extraire le zip. Vous aurez l'ensembles des fichiers pour l'utilisation du code.

## 2.  Créer un environnement Python :

### 2.1. <ins>Ouvrir un terminal</ins>
Ouvrez une fenêtre de terminal sur votre système Linux.

### 2.2 <ins>Vérifier la version de Python installée</ins>
Vérifiez que Python 3 est installé en exécutant :
```
python3 --version
```
Vous devriez voir une version du type ` Python 3.x.x. `
Si ce n’est pas le cas, installez Python 3 avec la commande adaptée à votre distribution (par exemple : sudo apt install python3).

### 2.3 <ins>Créer un environnement dans le projet</ins>
Afin de ne pas corrompre votre systeme, nous allons créer un environnement dans le project.

Aller dans le repertoire du projet avec la commande :
```
cd /mon_chemin_d_acces_local/../02-Utilisez-les-bases-de-Python-pour-l-analyse-de-march--main
```
Créez un environnement virtuel avec la commande :
```
python3 -m venv .env
```
Ici, `.env` est le nom de l’environnement. Vous pouvez le modifier si besoin.

### 2.4 <ins>Activer l’environnement virtuel</ins>

Activez l’environnement avec :
```
source .env/bin/activate
```
Vous devriez voir le nom de l’environnement (`(.env)`) apparaître au début de la ligne de commande.
```
>(.env) user@pcname :/mon_chemin_d_acces_local/../02-Utilisez-les-bases-de-Python-pour-l-analyse-de-march--main$
```

### 2.5 <ins>Vérifier que l’environnement est vide</ins>
Listez les paquets installés :
```
pip list
```
Vous ne devriez voir que `pip`, `setuptools` et `wheel`.

### 2.6 <ins>Installer les dépendances du projet</ins>
Installez les dépendances utiles au bon fonctionnement du copde avec la commande suivante :
```
pip install -r requirements.txt
```
### 2.7 <ins>Pour déactiver l'environnement</ins>
une fois que vous aurez fini d'utiliser le code vous pourrez déactiver l'environnement avec la commande suivant:
```
deactivate
```

## 3. Choisir le chemin de stockage des données exportées:

En lançant le code main.py, vous allez extraire de nombreux fichiers **CSV** et **JPG**.
Afin de maitriser ou ces fichiers seront stockés sur votre PC, il est important de choisir l'emplacement d'exportation des fichiers. Pour cela, il faut remplacer le chemin d'accès réseaux. 
En ouvrant le fichier main.py avec un editeur de text ou votre IDE, changer la valeur de la variable **OUTPUT_DIR_**. pour choisir le bon chemin d'accès.
```
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
        "/home/user/Documents/02_BaseDeDonnees/datas/"
    )
```

## 4. Lancer le code python.

Nous pouvons lancer l'exécution du code python du fichier `main.py`. Pour cela dans le terminal exécutez la commande suivante :

```
python3 /mon_chemin_d_acces_local/../02-Utilisez-...de-march--main/main.py
```
Dans votre terminal vous devriez voir apparaître les lignes ci-dessous suivies de nouvelles lignes de code. Cela signifie que le code tourne et est en train de télécharger les données depuis le site https://books.toscrape.com/.

```
* Catégorie : Travel
  -> Scraping : https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html
  -> Scraping : https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html
  -> Scraping : https://books.toscrape.com/catalogue/see-america-a-celebration-of-our-national-parks-treasured-sites_732/index.html
```

Laisser le code tourner 

# pour aller plus loint :

- Il est possible d'ajouter une description à chaque fonction Python.
- Il est possible d'ajouter des tests de fonctionnement pour chaque fonction avec une docstring.
- Il est possible de scinder le fichier en deux fichiers : un fichier avec l'ensemble des fonctions et un avec juste la fonction de récupération.
- Il est possible de créer une tâche programmée qui s'exécute au démarrage du PC ou de façon récurrente, avec crontab ou un service.
- Dans le cas d'une tâche récurrente, il est possible de modifier le code pour faire seulement une mise à jour des données déjà collectées et qui ont changé.

Si l'on prend en considération un pipeline ETL (de l’anglais Extract, Transform, Load, signifiant extraire, transformer, charger) :

Tel que le code est structuré, par fonction, il serait possible de déplacer chaque fonction dans la partie la plus adéquate et de les appeler au travers des imports de fonctions ou de méthodes.


# Lien utiles pour le cours

pour aller plus loin que les cours proposé par OpenClassRooms: 

- Pour la compéhention du HTML et du CSS :
https://www.apprendre-html-et-css.com/sementique_balises_et_attributs.html

- Bien organiser son VScode:
https://itexpert.fr/blog/extensions-vscode/

- Trouver les bibloithéques python : https://pypi.org/project/beautifulsoup4/

- PEP 8 : https://portail.lyc-la-martiniere-diderot.ac-lyon.fr/srv1/co/pep_8_python.html

- Rédiger mon readme avec les premières mis en page : 

    - https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

    - https://code.visualstudio.com/docs/languages/markdown

- Comment utiliser Beautiful Soup :
    - https://perso.liris.cnrs.fr/pierre-antoine.champin/2019/progweb-python/annexes/a3_beautiful_soup.html

    - https://geekflare.com/fr/beautiful-soup-for-web-scraping-projects/

