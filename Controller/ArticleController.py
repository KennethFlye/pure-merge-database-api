from DatabaseAccess import DbArticle
from DatabaseAccess.DbArticle import DbArticle

import Model
from Model.Article import Article


class ArticleController:

    def insert_article(self, article: Article):
        return DbArticle().insert_article(article)

    def get_articles(self):
        articles = DbArticle().get_all_articles()

        return articles

    def get_article(self, id):
        dba = DbArticle()
        return dba.get_article_by_id(id)


