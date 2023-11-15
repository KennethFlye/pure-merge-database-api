import psycopg as pgres
from decouple import config
from Model.Article import Article

class DbArticle:

    GetAllArticlesQuery = "SELECT * FROM Article"
    GetCommentsByArticleIdQuery = "SELECT \"comment\" FROM \"Comment\" WHERE \"Comment\".article_id = %(articleId)s"
    GetAuthorsByArticleIdQuery = "SELECT name FROM Author, article_author WHERE article_author.author_name = author.name AND article_author.article_id = %(articleId)s" #Måske problemer med keyword name
    GetCategoriesByArticleIdQuery = "SELECT category.category FROM category, article_category WHERE article_category.category = category.category AND article_category.article_id = %(articleId)s" #Måske problemer med keyword category

    GetArticleByIdQuery = "SELECT * FROM Article WHERE id = %(articleId)s"

    GetHighestGroupNumberQuery = "SELECT MAX(\"group\") FROM article"

    InsertArticleQuery = "INSERT INTO Article(submitter, submitter_is_preferred, authors_is_preferred, title, title_is_preferred, comments_is_preferred, journal_ref, journal_ref_is_preferred, doi, doi_is_preferred, report_number, report_number_is_preferred, categories_is_preferred, license, license_is_preferred, abstract, abstract_is_preferred, versions, versions_is_preferred, update_date, update_date_is_preferred, \"group\") VALUES (%(submitter)s, %(submitter_is_preferred)s, %(authors_is_preferred)s, %(title)s, %(title_is_preferred)s, %(comments_is_preferred)s, %(journal_ref)s, %(journal_ref_is_preferred)s, %(doi)s, %(doi_is_preferred)s, %(report_number)s, %(report_number_is_preferred)s, %(categories_is_preferred)s, %(license)s, %(license_is_preferred)s, %(abstract)s, %(abstract_is_preferred)s, %(versions)s, %(versions_is_preferred)s, %(update_date)s, %(update_date_is_preferred)s, %(group)s) RETURNING id;"
    InsertCommentsQuery = "INSERT INTO \"Comment\"(\"comment\", article_id) VALUES (%(comment)s, %(article_id)s)"
    InsertAuthorsQuery = "INSERT INTO author(\"name\") VALUES (%(author)s)"
    InsertCategoriesQuery = "INSERT INTO \"category\"(category) VALUES (%(category)s)"

    ConnectAuthorAndArticleQuery = "INSERT INTO article_author(article_id, author_name) VALUES (%(article_id)s, %(author_name)s)"
    ConnectCategoryAndArticleQuery = "INSERT INTO article_category(article_id, category) VALUES (%(article_id)s, %(category)s)"

    DoesCategoryExistQuery = "SELECT CASE WHEN EXISTS (SELECT * FROM \"category\" WHERE \"category\"=%(category)s)THEN CAST(1 AS BIT) ELSE CAST(0 AS BIT) END"
    DoesAuthorExistQuery = "SELECT CASE WHEN EXISTS (SELECT * FROM author WHERE \"name\"=%(author_name)s)THEN CAST(1 AS BIT) ELSE CAST(0 AS BIT) END"

    def __init__(self):
        self.connection = pgres.connect(host=config("HOST"), dbname=config("DATABASE"), user=config("USER"), password=config("PASSWORD"))

    def insert_article(self, article):
        connection = pgres.connect(host=config("HOST"), dbname=config("DATABASE"), user=config("USER"), password=config("PASSWORD"))
        cursor = connection.cursor()
        
        cursor.execute(self.InsertArticleQuery, {'submitter': article.submitter, 'submitter_is_preferred': article.submitter_is_preferred, 'authors_is_preferred': article.authors_is_preferred, 'title': article.title, 'title_is_preferred': article.title_is_preferred, 'comments_is_preferred': article.comments_is_preferred, 'journal_ref': article.journal_ref, 'journal_ref_is_preferred': article.journal_ref_is_preferred, 'doi': article.doi, 'doi_is_preferred': article.doi_is_preferred, 'report_number': article.report_number, 'report_number_is_preferred': article.report_number_is_preferred, 'categories_is_preferred': article.categories_is_preferred, 'license': article.license, 'license_is_preferred': article.license_is_preferred, 'abstract': article.abstract, 'abstract_is_preferred': article.abstract_is_preferred, 'versions': article.version, 'versions_is_preferred': article.versions_is_preferred, 'update_date': article.update_date, 'update_date_is_preferred': article.update_date_is_preferred, 'group': article.group})
        return_id = cursor.fetchone()
        article.id = return_id[0]

        #Authors
        self.insert_authors(cursor, article.authors, article.id)
        #Comments
        self.insert_comments(cursor, article.comments, article.id)
        #Categories
        self.insert_categories(cursor, article.categories, article.id)

        #Catch Exception? For rollback eller sket det automatisk?

        #connection.rollback()
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
        foundArticle = article

        # foundArticle.id = article[0]
        # foundArticle.submitter = article[1]
        # foundArticle.submitter_is_preferred = article[2]
        # foundArticle.authors = self.get_authors_by_article_id(foundArticle.id)
        # foundArticle.authors_is_preferred = article[3]
        # foundArticle.title = article[4]
        # foundArticle.title_is_preferred = article[5]
        # foundArticle.comments = self.get_comments_by_article_id(foundArticle.id)
        # foundArticle.comments_is_preferred = article[6]
        # foundArticle.journal_ref = article[7]
        # foundArticle.journal_ref_is_preferred = article[8]
        # foundArticle.doi = article[9]
        # foundArticle.doi_is_preferred = article[10]
        # foundArticle.report_number = article[11]
        # foundArticle.report_number_is_preferred = article[12]
        # foundArticle.categories = self.get_categories_by_article_id(foundArticle.id)
        # foundArticle.categories_is_preferred = article[13]
        # foundArticle.license = article[14]
        # foundArticle.license_is_preferred = article[15]
        # foundArticle.abstract = article[16]
        # foundArticle.abstract_is_preferred = article[17]
        # foundArticle.versions = article[18]
        # foundArticle.versions_is_preferred = article[19]
        # foundArticle.update_date = article[20]
        # foundArticle.update_date_is_preferred = article[21]
        # foundArticle.group = article[22]

        return foundArticle

    def insert_authors(self, cursor, authors, article_id):
        for author in authors:
            if not self.author_exists(cursor, author):
                cursor.execute(self.InsertAuthorsQuery, {'author': author})
            #Connect author and article in database
            cursor.execute(self.ConnectAuthorAndArticleQuery, {'article_id': article_id, 'author_name': author})
        #Return Boolean?

    def author_exists(self, cursor, author):
        author_exists = False

        cursor.execute(self.DoesAuthorExistQuery, {'author_name': author})

        query_result = cursor.fetchone()

        if query_result[0] == 1:
            author_exists = True

        return author_exists

    def category_exists(self, cursor, category):
        category_exists = False

        cursor.execute(self.DoesCategoryExistQuery, {'category': category})

        query_result = cursor.fetchone()

        if query_result[0] == 1:
            category_exists = True

        return category_exists

    def insert_comments(self, cursor, comments, article_id):
        #Kig på om databasen skal ændres, da der ikke kan komme samme comment string 2 gange. Kan være den skal have en id kolonne
        for comment in comments:
            cursor.execute(self.InsertCommentsQuery, {'comment': comment, 'article_id': article_id})

    def insert_categories(self, cursor, categories, article_id):
        for category in categories:
            if not self.category_exists(cursor, category):
                cursor.execute(self.InsertCategoriesQuery, {"category": category})
            #Connect category and article in database
            cursor.execute(self.ConnectCategoryAndArticleQuery, {"article_id": article_id, 'category': category})

    def calculate_group_number(self):
        group_number = 0

        cursor = self.connection.cursor()

        cursor.execute(self.GetHighestGroupNumberQuery)
        query_result = cursor.fetchone()

        group_number = query_result[0]+1

        return group_number





