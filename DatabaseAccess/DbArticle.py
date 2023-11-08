import psycopg as pgres
from decouple import config

class DbArticle:

    GetAllArticlesQuery = "SELECT  FROM "
    GetArticleByIdQuery = "SELECT * FROM.."

    InsertArticleQuery = "INSERT INTO.."

    def __init__(self):
        self.connection = pgres.connect(host=config("HOST"), database=config("DATABASE"), user=config("USER"), password=config("PASSWORD"))
        #cursor = connection.cursor()

