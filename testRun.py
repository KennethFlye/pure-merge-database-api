from DatabaseAccess.DbArticle import DbArticle
from Model.Article import Article
from datetime import time, datetime

dbArticle = DbArticle()

#dbArticle.get_all_articles()
#dbArticle.get_article_by_id(1)

#dbArticle.insertArticleTest()

testArticle = Article()

testArticle.submitter = "Kenneth"
testArticle.submitter_is_preferred = True

testArticle.authors = {"Kenneth Flye", "Kasper Flye", "Kristoffer Flye"}
testArticle.authors_is_preferred = True

testArticle.title = "Title 1"
testArticle.title_is_preferred = False

testArticle.comments = {"Oh", "My", "God"}
testArticle.comments_is_preferred = True

testArticle.journal_ref = "journalRef 1"
testArticle.journal_ref_is_preferred = False

testArticle.doi = "doi 1"
testArticle.doi_is_preferred = True

testArticle.report_number = "1"
testArticle.report_number_is_preferred = True

testArticle.categories = {"Math", "Computer Science"}
testArticle.categories_is_preferred = True

testArticle.license = "License 1"
testArticle.license_is_preferred = False

testArticle.abstract = "Abstract 1"
testArticle.abstract_is_preferred = False

testArticle.version = "V.1"
testArticle.versions_is_preferred = True

testArticle.update_date = datetime.now()
testArticle.update_date_is_preferred = True

testArticle.group = 2

dbArticle.insert_article(testArticle)