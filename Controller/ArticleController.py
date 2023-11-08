from Model.Article import *


class ArticleController:

    def create_article(self, article):
        fields = vars(article)
        for field, value in fields.items():  # STUB
            print(f"{field}: {value}")

    def get_articles(self):
        return ("STUB STUB STUB STUB TODO STUB TODO STUB "
                "PLS todo REMOVE stub LATER, todo DONT stub LEAVE todo IT stub LIKE todo THIS "
                "STUB TODO STUB")
        pass

