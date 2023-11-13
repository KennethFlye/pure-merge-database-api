# This is a data access object for Articles.
from DBAccess.DBConnection import DBConnection


class ArticlesDAO:
    query_get_article = "SELECT * FROM Articles WHERE doi = %s"
    query_get_articles = "SELECT * FROM Articles"
    query_post_article = "... TODO"

    def get_articles(self):
        dbc = DBConnection.from_json()
        dbc.connect()
        articles = dbc.execute_query(ArticlesDAO.get_articles)
        dbc.disconnect()
        return articles

    def post_article(self):
        pass

    def get_article(self, articleid):
        dbc = DBConnection.from_json()
        dbc.connect()

        # note the `,` here,
        # it makes the id a tuple, which the cursor needs later when handling params
        article = dbc.execute_query(ArticlesDAO.query_get_article, (articleid,))
        dbc.disconnect()
        return article
