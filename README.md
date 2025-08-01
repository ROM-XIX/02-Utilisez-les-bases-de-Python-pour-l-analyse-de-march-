
# Context : 

dans le cadre de la formation OpenClassRooms pour la formation de developpeur logiciel python
le projet numéro 2 demande de pouvoir extraire l'ensemble des données d'unsite de ventes de livre en ligne.

# L'objectif du code :

les données à récolter sont les suivantes :

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

# ce que le code fait :

le code permet de récupérer l'index de l'ensemble des catégories du site https://books.toscrape.com 
stock l'ensemble des liens de chaque page produit par catégorie.
le code permet d'obtenir un csv par catégorie de livre.
L'ensemble des éléments demandés est stocké sosu forme de tableau
cf l'objectif du code [Link Text](#lobjectif-du-code-).

Les images sont enregistrées dans un répertoire séparé du répertoire de csv.

l'arborescence est du type :

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

il faut créer un environement python
récupérer le repo 
puis installer le requirement du repo dans l'environement créé
dans le fichier main changer le chemin stocké dans la variable "OUTPUT_DIR_"
copier le chemin dans lequel vous souhaitez que les données extraites soient stokées sur votre PC.
activer l'environement
puis lancer le code python.


# pour aller plus loint :










Veillez également à prendre le temps d'écrire un fichier README.md,
que vous ajouterez dans le repository 
afin que je puisse exécuter le code correctement et produire quelques données !

1 . le script doit permetre de récuperer 


# Livrables : 
Lorsque vous aurez terminé, envoyez-moi : 
## 1- un lien vers votre repository GitHub 
## 2- un fichier compressé des données qu'il génère.
    Après avoir terminé le code, envoyez-moi un fichier ZIP des données générées.
    Assurez-vous d'organiser toutes les données et 
    images que vous avez extraites de manière simple.
## 3- le code, le repo doit inclure un requirements.txt 
## 4- un README.md complété afin que j’exécute le code avec succès et produise des données !
## 5- Le repo ne doit pas inclure les données et images extraites.
## 6- les usage future possible du code 
    Pouvez-vous également m'envoyer un mail décrivant comment nous pourrions utiliser le code 
    pour établir un pipeline ETL 
    (de l'anglais Extract, Transform, Load, signifiant extraire, transformer, charger) ? 
    Cela sera utile pour le montrer à mon responsable.

# Ce que le code doit faire

## 1. le code doit extraire :

### product_page_url
### universal_ product_code (upc)
### title
### price_including_tax
### price_excluding_tax 
### number_available
### product_description
### category
### review_rating
### image_ur
### Extraire et enregistrer les fichiers images de chaque livre
    Il est recommandé d'enregistrer les images avec la même arboréssence de ccatégorie de livre
    ou de choisir un nomage des simage du type "Catégorie-nom_du_livre" et les numéroté au besoin


# Example headings

## Sample Section

## This'll be a _Helpful_ Section About the Greek Letter Θ!
A heading containing characters not allowed in fragments, UTF-8 characters, two consecutive spaces between the first and second words, and formatting.

## This heading is not unique in the file

TEXT 1

## This heading is not unique in the file

TEXT 2

# Links to the example headings above

Link to the sample section: [Link Text](#sample-section).

Link to the helpful section: [Link Text](#thisll-be-a-helpful-section-about-the-greek-letter-Θ).

Link to the first non-unique section: [Link Text](#this-heading-is-not-unique-in-the-file).

Link to the second non-unique section: [Link Text](#this-heading-is-not-unique-in-the-file-1).

[def]: #L'objectif-du-code-: