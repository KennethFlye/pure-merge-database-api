import psycopg as pgres
from decouple import config

from Model.Article import Article

class DbArticle:

    GetAllArticlesQuery = "SELECT * FROM Article"
    GetCommentsByArticleIdQuery = "SELECT commentary FROM \"Comment\" WHERE \"Comment\".article_id = %(articleId)s" #Måske problemer med keyword Comment
    GetAuthorsByArticleIdQuery = "SELECT name FROM Author, article_author WHERE article_author.author_name = author.name AND article_author.article_id = %(articleId)s" #Måske problemer med keyword name
    GetCategoriesByArticleIdQuery = "SELECT category.category FROM category, article_category WHERE article_category.category = category.category AND article_category.article_id = %(articleId)s" #Måske problemer med keyword category

    GetArticleByIdQuery = "SELECT * FROM Article WHERE id = %(articleId)s"

    InsertArticleQuery = "INSERT INTO Article(submitter, submitter_is_preferred, authors_is_preferred, title, title_is_preferred, comments_is_preferred, journal_ref, journal_ref_is_preferred, doi, doi_is_preferred, report_number, report_number_is_preferred, categories_is_preferred, license, license_is_preferred, abstract, abstract_is_preferred, versions, versions_is_preferred, update_date, update_date_is_preferred, \"group\") VALUES (%(submitter)s, %(submitter_is_preferred)s, %(authors_is_preferred)s, %(title)s, %(title_is_preferred)s, %(comments_is_preferred)s, %(journal_ref), %(journal_ref_is_preferred), %(doi)s, %(doi_is_preferred)s, %(report_number), %(report_number_is_preferred), %(categories_is_preferred), %(license)s, %(license_is_preferred)s, %(abstract)s, %(abstract_is_preferred), %(versions)s, %(versions_is_preferred), %(update_date)s, %(update_date_is_preferred)s, %(group)s) RETURNING id;"
    #Skal have fat i articleId
    InsertCommentsQuery = "INSERT INTO \"Comment\"(commentary, article_id) VALUES (%(comment)s, %(articleId)s)"
    InsertAuthorsQuery = "INSERT INTO author(\"name\") VALUES (%(author)s)" #Inkluder article_author tabellen
    InsertCategoriesQuery = "INSERT INTO \"category\"(category) VALUES (%(category)s)" #Inkluder article_category tabellen

    InsertArticleTestQuery = "INSERT INTO Article(comments_is_preferred) VALUES (\'1\') RETURNING id"
    InsertCommentsTestQuery = "INSERT INTO \"Comment\"(commentary, article_id) VALUES (%(comment)s, %(articleId)s)"

    def __init__(self):
        self.connection = pgres.connect(host=config("HOST"), dbname=config("DATABASE"), user=config("USER"), password=config("PASSWORD"))

    def insertArticleTest(self):
        #Tilføjet RETURNING id til enden af querien som returner den værdi der blev indsat i id kolonnen
        #Connection skal oprettet i metoden for at kunne commit changes.

        connection = pgres.connect(host=config("HOST"), dbname=config("DATABASE"), user=config("USER"), password=config("PASSWORD"))
        cursor = connection.cursor()

        cursor.execute(self.InsertArticleTestQuery)
        article = cursor.fetchone()
        articleId = article[0]

        cursor.execute(self.InsertCommentsTestQuery, {'comment': "Hej med dig 1", 'articleId': articleId})
        connection.commit()

    def get_article_by_id(self, article_id):
        cursor = self.connection.cursor()

        cursor.execute(self.GetArticleByIdQuery, {'articleId': article_id})

        article = cursor.fetchone()

        foundArticle = self.create_article_object(article)

        return foundArticle

    def get_all_articles(self):
        articleList = []

        cursor = self.connection.cursor()

        cursor.execute(self.GetAllArticlesQuery)

        articles = cursor.fetchall()

        for article in articles:
            foundArticle = self.create_article_object(article)

            articleList.append(foundArticle)

        print(str(len(articleList)) + " articles found")
        return articleList

    def get_authors_by_article_id(self, article_id):
        foundAuthors = list()

        cursor = self.connection.cursor()

        cursor.execute(self.GetAuthorsByArticleIdQuery, {'articleId': article_id})
        authors = cursor.fetchall()

        for author in authors:
            foundAuthors.append(author[0])

        return foundAuthors

    def get_comments_by_article_id(self, article_id):
        foundComments = list()

        cursor = self.connection.cursor()

        cursor.execute(self.GetCommentsByArticleIdQuery, {'articleId': article_id})
        comments = cursor.fetchall()

        for comment in comments:
            foundComments.append(comment[0])

        return foundComments

    def get_categories_by_article_id(self, article_id):
        foundCategories = list()

        cursor = self.connection.cursor()

        cursor.execute(self.GetCategoriesByArticleIdQuery, {'articleId': article_id})
        categories = cursor.fetchall()

        for category in categories:
            foundCategories.append(category[0])

        return foundCategories

    def create_article_object(self, article):
        foundArticle = Article()

        foundArticle.id = article[0]
        foundArticle.submitter = article[1]
        foundArticle.submitter_is_preferred = article[2]
        foundArticle.authors = self.get_authors_by_article_id(foundArticle.id)
        foundArticle.authors_is_preferred = article[3]
        foundArticle.title = article[4]
        foundArticle.title_is_preferred = article[5]
        foundArticle.comments = self.get_comments_by_article_id(foundArticle.id)
        foundArticle.comments_is_preferred = article[6]
        foundArticle.journal_ref = article[7]
        foundArticle.journal_ref_is_preferred = article[8]
        foundArticle.doi = article[9]
        foundArticle.doi_is_preferred = article[10]
        foundArticle.report_number = article[11]
        foundArticle.report_number_is_preferred = article[12]
        foundArticle.categories = self.get_categories_by_article_id(foundArticle.id)
        foundArticle.categories_is_preferred = article[13]
        foundArticle.license = article[14]
        foundArticle.license_is_preferred = article[15]
        foundArticle.abstract = article[16]
        foundArticle.abstracts_is_preferred = article[17]
        foundArticle.versions = article[18]
        foundArticle.versions_is_preferred = article[19]
        foundArticle.update_date = article[20]
        foundArticle.update_date_is_preferred = article[21]
        foundArticle.group = article[22]

        return foundArticle
