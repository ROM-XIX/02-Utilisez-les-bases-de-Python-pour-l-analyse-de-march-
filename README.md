
# Context : 

Dans le cadre de la formation OpenClassRooms, pour la formation de developpeur logiciel python.

Le projet numéro 2 demande de pouvoir extraire l'ensemble des données d'un site de ventes de livre en ligne.

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

puis parcours chaque livre de chaque catégorie, pendant ce partage il ce passe 4 choses:

1. on crée un répertoire pour stocker les CSV des datas produit, par catégorie
2. on crée un repertoire pour stocker les images produit, par catégorie
3. on crée un CSV par catégorie qui contient l'ensemble des données demandé ***l'objectif du code*** [Link Text](#lobjectif-du-code-).
4. on récupère le lien de l'image du produit, et on enregistre cette image dans le répertoire indiqué.

Voici une représentation de l'arborescence généré :

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

## 1. il faut créer un environement python

## 2. récupérer le repo 

## 3. puis installer le requirement du repo dans l'environement créé

## 4. dans le fichier main changer le chemin stocké dans la variable "OUTPUT_DIR_"

## 5. copier le chemin dans lequel vous souhaitez que les données extraites soient stokées sur votre PC.

## 6. activer l'environement

## 7. puis lancer le code python.


# pour aller plus loint :

- il est possible d'ajouter une description à chaque fonction python
- il est possible d'ajouter des tests de fonctionnement de chaque fonction avec docstring
- il est possible de scinder le fichier en deux fichies. 1 fichier avec l'ensemble des fonctions et 1 avec juste la fonction de récupération.
- il est possible de faire une tache programmé, qui s'éxécute au démarrage du pc ou avec une tache programmée reccurante, avec crontab ou un service.
- dans le cas d'une tache récurrante, il est possiblde modifier le code pour faire seulement une maj des données déjà colecté et qui ont changées.

si l'on prend en concidération un pipeline ETL (de l'anglais Extract, Transform, Load, signifiant extraire, transformer, charger)  

tel que le code est structuré, par fonction; il serait possible de déplacer chaque fonction dans la partie la plus adéquate et de les appeler au travers des imports de fonction ou de méthode.





