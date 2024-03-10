Observatoire des Produits
==============================

Connaitre les produits d'une épicerie grâce à la BDD d'Open Food Fact. Ce projet a été initié par l'épicerie participative [l'Elefan](https://lelefan.org/).

## Fonctionnement

Ce projet récupère la liste des articles vendus dans une épicerie puis ajoute à ces articles des données issues d'Open Food Facts. 
![](https://static.openfoodfacts.org/images/logos/off-logo-horizontal-light.svg)

1. **Récupération des articles vendus dans une épicerie :** Le connecteur Epicerie permet de faire un appel a une API qui renvoi une liste de code barres. Il est possible d'ajouter un connecteur spécifique à son épicerie
1. **Récupération des données Open Food Facts :** Les données sont récupéres via l'API d'OFF, en limitant les appels a 100 requêtes/min. Les codes barres sont filtrés en amont pour limiter les requêtes aux codes barres valides (13 digits)
1. **Sauvegarde des articles avec les *facts* : ** Les données sont sauvegardées dans une base de donnée fournie par l'épicerie. Le connecteur par défaut propose de sauvergarder ces données dans une MariaDB. Une copie est sauvegardée en `.csv` dans le dossier `data`.

## Installation globale

### En local

1. Configurer les variables d'environnement dans le fichier `.env` (voir `.env.EXEMPLE`)
1. Installer les packages python `pip install -r requirements.txt`
1. Run `python src/data/make_dataset.py`

### Avec Docker

1. Installer docker
1. Configurer les variables d'environnement dans un fichier `.env` (voir `.env.EXEMPLE`)
1. Build the image within the directory : `sudo docker build --pull -f "Dockerfile" -t observatoireproduits:latest "."`
1. Run `sudo docker run --network="host" -it observatoireproduits:latest` ou `sudo docker run --network="host" -it observatoireproduits:latest` si vous voulez sauvegarder les données sur une base MariaDB hebergée sur votre 

### Détails du connecteur l'Elefan
![](https://lelefan.org/wp-content/uploads/2021/02/Lelefan-Logo-long-72@2x.png) 

* Récupération des produits à la vente : Depuis son [API](https://produits.lelefan.org/api/).
* Sauvegarde : Dans sa base de donnée MariaDb


Organisation
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Local export 
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


