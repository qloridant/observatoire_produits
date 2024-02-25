import pandas as pd
from abc import ABC


class EpicerieConnector(ABC):
    def extract_products_codes(self):
        pass

    def transform_products_facts(self, products_facts):
        """
        Transform the  list of products returned by the OFF API to a table ready to
        be loaded in a database
        """
        data = []
        for product_fact in products_facts:
            data.append({"code": product_fact["code"], "product_name": product_fact["product"]["product_name"]})
        self.products_facts = pd.DataFrame.from_records(data)

    def load_products_codes(self):
        pass
