from epicerie_connector import EpicerieConnector
import mariadb
import sys
import os
import dotenv

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)


class ElefanConnector(EpicerieConnector):

    def __init__(self) -> None:
        super().__init__()

    def _connect(self):
        # Connect to MariaDB Platform
        print(os.environ.get('DB_USERNAME'))
        try:
            conn = mariadb.connect(
                user=os.environ.get('DB_USERNAME'),
                password=os.environ.get('DB_PASSWORD'),
                host=os.environ.get('DB_HOST'),
                port=int(os.environ.get('DB_PORT')),
                database=os.environ.get('DB_NAME')
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        # Get Cursor
        return conn.cursor()
    
    def extract_products_codes(self):
        cur = self._connect()
        cur.execute("SELECT code FROM kaso.ARTICLE")
        codes = [row[0] for row in cur]
        return codes

