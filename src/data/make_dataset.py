import click
import logging
from off_connector import OFFConnector
from elefan_connector import ElefanConnector
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
def main():
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    epicerie_connector = ElefanConnector()

    logger.info("Récuperation de la liste des codes barres de l epicerie")
    nos_produits = epicerie_connector.extract_products_codes()
    logger.info("Récuperation des données Open Food Facts disponibles pour cette liste")
    products_facts = OFFConnector().get_products_facts(nos_produits)
    logger.info("Transformation des données Open Food Facts")
    epicerie_connector.transform_products_facts(products_facts)
    logger.info("Sauvegarde des données Open Food Facts")
    epicerie_connector.load_products_facts()


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
