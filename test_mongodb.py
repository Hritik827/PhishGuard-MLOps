

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

username = quote_plus("hritikpatil28academic_db_user")
password = quote_plus("Admin123")

uri = f"mongodb+srv://{username}:{password}@cluster0.nqwpuni.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi("1"))

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MondoDB")
except Exception as e:
    print(e)