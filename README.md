observatoire_produits
==============================

Mieux connaitre les produits d'une épicerie grâce à la BDD d'Open Food Facts

--------

## Global installation

1. Intall the python packages with `pip install -r requirements.txt`
1. Run `python src/data/make_dataset.py`

### Details for l'Elefan connector
L Elefan connector reads the barcodes of the products sold at l'Elefan in its MariaDB database (`kaso.ARTICLE`). It will then export the facts in this same database, in the table `kaso.ARTICLE_FACTS`.

1. You need to provide the connection information of the DB in the `.env` file
1. Your DB needs to have write privileges on the user you will use for the table  `kaso.ARTICLE_FACTS`
1. Your DB needs to have read privileges on the user you will use for the table  `kaso.ARTICLE`
   


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
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


