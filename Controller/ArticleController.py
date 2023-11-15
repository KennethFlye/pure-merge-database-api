from DatabaseAccess import DbArticle
from DatabaseAccess.DbArticle import DbArticle


class ArticleController:

    def create_article(self, article):
        dba = DbArticle
        return dba.create_article_object(article)

    def get_articles(self):
        dba = DbArticle()

        articles = dba.get_all_articles()
        #for x in articles:
        #    print(x.getListOfVariables())

        return articles

    def get_article(self, id):
        dba = DbArticle()
        return dba.get_article_by_id(id)


