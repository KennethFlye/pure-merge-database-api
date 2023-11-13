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


@app.route('/api/articles/<int:id>', methods=['GET'])
def get_article(id):
    content = artcon.get_articles()
    return Response(content, status=200, content_type='text/plain')


@app.route('/')
def hello_world():  # put application's code here
    return 'add /api'


@app.route('/api')
def help_route():  # put application's code here
    content = 'routes: \'/api\', \'/api/articles\' [GET & POST], \'/api/articles/{id}\' [GET]'
    return Response(content, status=200, content_type='text/plain')


if __name__ == '__main__':
    app.run()
