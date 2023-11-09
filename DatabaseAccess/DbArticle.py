import psycopg as pgres
from decouple import config
from Model.Article import Article

class DbArticle:

    GetAllArticlesQuery = "SELECT * FROM Article"
    GetCommentsByArticleIdQuery = "SELECT commentary FROM Comment WHERE Comment.article_id = @articleId" #Måske problemer med keyword Comment
    GetAuthorsByArticleIdQuery = "SELECT name FROM Author, article_author WHERE article_author.author_name = author.name AND article_author.article_id = @articleId" #Måske problemer med keyword name
    GetCategoriesByArticleIdQuery = "SELECT category.category FROM category, article_category WHERE article_category.category = category.category AND article_category.article_id = @articleId" #Måske problemer med keyword category

    GetArticleByIdQuery = "SELECT * FROM.."

    InsertArticleQuery = "INSERT INTO.."

    connetionString = f"host={config('HOST')} dbname={config('DATABASE')} user={config('USER')} password={config('PASSWORD')}"

    def __init__(self):
        self.connection = pgres.connect(host=config("HOST"), dbname=config("DATABASE"), user=config("USER"), password=config("PASSWORD"))

    def get_all_articles(self):
        articleList = []

        cursor = self.connection.cursor()

        cursor.execute(self.GetAllArticlesQuery)

        articles = cursor.fetchall()

        print(articles)

        count = 1

        #articleCount = len(articles)

        #print(articleCount)


        for article in articles:
            #Brug pandas måske til at tage dem over i et DataFrame

            foundArticle = Article()

            foundArticle.id = article[0]
            foundArticle.submitter = article[1]
            foundArticle.submitter_is_preferred = article[2]
            #Authors
            foundArticle.authors = self.get_authors_by_article_id(foundArticle.id)
            #foundArticle.authors = {"Kenneth Flye", "Kasper Flye", "Kristoffer Flye"}
            foundArticle.authors_is_preferred = article[3]
            foundArticle.title = article[4]
            foundArticle.title_is_preferred = article[5]
            #Comments
            #Comments metode
            foundArticle.comments = {"kommentar 1", "kommentar 2"}
            foundArticle.comments_is_preferred = article[6]
            foundArticle.journal_ref = article[7]
            foundArticle.journal_ref_is_preferred = article[8]
            foundArticle.doi = article[9]
            foundArticle.doi_is_preferred = article[10]
            foundArticle.report_number = article[11]
            foundArticle.report_number_is_preferred = article[12]
            #Categories
            #Categories metode
            foundArticle.categories = {"kategori 1", "kategori 2"}
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

            print(foundArticle)

    def get_authors_by_article_id(self, article_id):
        pass