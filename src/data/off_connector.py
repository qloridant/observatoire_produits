import logging
import requests
import time

logger = logging.getLogger(__name__)


def get_product_fact(barcode):
    try:
        response = requests.get(f'https://world.openfoodfacts.net/api/v2/product/{barcode}')
        response.raise_for_status()
        product = response.json()
        logger.info(f'Product found for url : https://world.openfoodfacts.net/api/v2/product/{barcode}')
    except requests.exceptions.HTTPError as e:
        logger.info(e)
        return None
    return product


class OFFConnector():

    def __init__(self) -> None:
        self.products_facts = []

    def get_products_facts(self, barcodes):
        """
        Reading the Open Food Facts API to fetch products facts
        Need to respect the API Constraint of a maximum of 100 requests
        per minute
        """
        start, end, step = 0, len(barcodes), 99
        number_of_requests = 0
        for i in range(start, end, step):
            x = i
            chunk = barcodes[x:x+step]
            for product_code in chunk:
                if number_of_requests == 99:
                    logger.info('Waiting 60 seconds...')
                    time.sleep(60)
                    number_of_requests = 0
            
                # A valid barcode is likely to have at least 10 digits
                if len(str(product_code)) >= 10:
                    self.products_facts.append(get_product_fact(product_code))
                    number_of_requests += 1

