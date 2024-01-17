from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

class Database:

    def __init__(self):
        load_dotenv()

        database_url = os.getenv("DATABASE_URL")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        database = os.getenv("DATABASE")

        self.driver = GraphDatabase.driver(database_url, auth=(db_user, db_password), database=database)

    def close(self):
        self.driver.close()