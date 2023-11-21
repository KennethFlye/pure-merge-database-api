import json
from sqlite3 import ProgrammingError

from flask import Flask, request, jsonify, Response
from Model.Article import *
from Controller.ArticleController import *
from DatabaseAccess.DbArticle import DbArticle
from Model.Article import Article

app = Flask(__name__)

artcon = ArticleController()


@app.route('/api/articles', methods=['POST'])
def post_article():
    try:
        print('-------------posting to db')
        artc = Article()
        data = request.get_json()
        print(data)
        data2 = dict(*data)
        print(data2)
        artc.fill_data(**data2)
        print(str(artc.to_json()))
        artcon.insert_article(artc)
        return Response("epic success", status=201, content_type='text/plain')
        pass
    except:
        pass
        return Response("Internal Server Error", status=500, content_type='text/plain')


@app.route('/api/articles', methods=['GET'])
def get_articles():

    try:
        content = json.dumps([article.to_json() for article in artcon.get_articles()])
        print(content)  # JSON format list of articles

        return Response(content, status=200, content_type='application/json')

    except TypeError as e:
        return Response("Error 404, articles not found", status=404, content_type='text/plain')
    except:
        return Response("Internal Server Error", status=500, content_type='text/plain')


@app.route('/api/articles/<int:id>', methods=['GET'])
def get_article(id):
    content = None

    try:
        content = json.dumps([artcon.get_article(id).to_json()])

        return Response(content, status=200, content_type='text/plain')
    except TypeError as e:
        return Response("Error 404, article not found", status=404, content_type='text/plain')
    except:
        return Response("Internal Server Error", status=500,
                        content_type='text/plain')


@app.route('/')
def hello_world():
    return 'add /api'


@app.route('/api')
def help_route():
    content = 'routes: \'/api\', \'/api/articles\' [GET & POST], \'/api/articles/{id}\' [GET]'
    return Response(content, status=200, content_type='text/plain')


@app.route('/api/articles/getgroupnr')
def get_highest_group():
    string = str(DbArticle().calculate_group_number())
    return_content = '{"group_number":' + string + '}'
    return Response(return_content, status=200, content_type='text/plain')


if __name__ == '__main__':
    app.run()
