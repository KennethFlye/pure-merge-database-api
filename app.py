import json
from sqlite3 import ProgrammingError

from flask import Flask, request, jsonify, Response
from Model.Article import *
from Controller.ArticleController import *

app = Flask(__name__)

artcon = ArticleController()


@app.route('/api/articles', methods=['POST'])
def post_article():
    data = request.get_json()
    artc = Article(**data)
    content = artcon.create_article(artc)
    return Response(content, status=201, content_type='text/plain')


@app.route('/api/articles', methods=['GET'])
def get_articles():
    # content = [
    #     {
    #         "Id": 1,
    #         "submitter": "Laurette S. Tuckerman",
    #         "author": ["E.D. Aguti", "Piotr Boronski"],
    #         "title": "title 1 test",
    #         "comments": ["Kommentar 1", "Kommentar 4"],
    #         "journalRef": "Journal of Computational Physics 227, 1523-1543 (2007)",
    #         "doi": "10.1016/j.jcp.2007.08.023",
    #         "reportNumber": "UCRL-JRNL-231224",
    #         "categories": ["medicine", "physics"],
    #         "license": "License test 1",
    #         "abstract": "Abstract 1 test",
    #         "versions": "V.1",
    #         "updateDate": "2022-03-06"
    #     },
    #     {
    #         "Id": 2,
    #         "submitter": "Piotr Boronski",
    #         "author": ["C.J. Lada", "Laurette S. Tuckerman"],
    #         "title": "title 2 test",
    #         "comments": ["Kommentar 2", "Kommentar 3"],
    #         "journalRef": "Journal of Computational Physics 227 (2007)",
    #         "doi": "10.1016/j.jcp.2007.08.028",
    #         "reportNumber": "UCRL-JRNL-231286",
    #         "categories": ["medicine"],
    #         "license": "License test 2",
    #         "abstract": "Abstract 2 test",
    #         "versions": "V.0,5",
    #         "updateDate": "2023-11-08"
    #     }
    # ]

    content = json.dumps([article.to_json() for article in artcon.get_articles()])  # todo: fix format when kenneth is back
    print(content)  # JSON format list of articles

    # Return the JSON response with the correct content type
    return Response(content, status=200, content_type='application/json')


@app.route('/api/articles/<int:id>', methods=['GET'])
def get_article(id):
    try:
        #article = artcon.get_article(id)
        #content = article.to_json()

        content = json.dumps([artcon.get_article(id).to_json()])  # fix return statement, do smth with try i suppose

        return Response(content, status=200, content_type='text/plain')
    except ProgrammingError as e:
        return Response("None lol", status=404, content_type='text/plain')
    except:
        return Response("general exception", status=404, content_type='text/plain') #Det er wack, skal nok fixe det, kh Oskar Scrum




@app.route('/')
def hello_world():  # put application's code here
    return 'add /api'


@app.route('/api')
def help_route():  # put application's code here
    content = 'routes: \'/api\', \'/api/articles\' [GET & POST], \'/api/articles/{id}\' [GET]'
    return Response(content, status=200, content_type='text/plain')


if __name__ == '__main__':
    app.run()
