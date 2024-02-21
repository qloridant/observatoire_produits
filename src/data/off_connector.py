import logging
import requests

logger = logging.getLogger(__name__)


def get_product(barcode):
    try:
        response = requests.get(f'https://world.openfoodfacts.net/api/v2/product/{barcode}')
        response.raise_for_status()
        product = response.json()
    except requests.exceptions.HTTPError as e:
        logger.info(e)
        return None
    return product


def get_products(barcodes):
    pass