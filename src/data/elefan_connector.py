from epicerie_connector import EpicerieConnector
import sys
import os
import dotenv
import sqlalchemy

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dotenv_path = os.path.join(project_dir, ".env")
dotenv.load_dotenv(dotenv_path)


class ElefanConnector(EpicerieConnector):
    def __init__(self) -> None:
        super().__init__()

    def _connect(self):
        # Connect to a DB
        print(os.environ.get("DB_USERNAME"))
        try:
            engine = sqlalchemy.create_engine(
                f"mysql+pymysql://"
                f"{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}"
                f"@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}?charset=utf8mb4"
            )
        except sqlalchemy.exc as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        return engine

    def extract_products_codes(self):
        engine = self._connect()
        with engine.connect() as con:
            result = con.execute(sqlalchemy.text("SELECT code FROM kaso.ARTICLE"))
            codes = [row[0] for row in result]
        return codes

    def load_products_facts(self):
        engine = self._connect()

        if len(self.products_facts):
            self.products_facts.to_sql("ARTICLE_FACTS", engine, if_exists="replace")
