from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟文章数据
articles = [
    {
        'id': 1,
        'title': 'First Article',
        'content': 'This is the content of the first article.'
    },
    {
        'id': 2,
        'title': 'Second Article',
        'content': 'This is the content of the second article.'
    },
    {
        'id': 3,
        'title': 'Third Article',
        'content': 'This is the content of the third article.'
    }
]

@app.route('/api/articles', methods=['GET'])
def get_articles():
    return jsonify({'articles': articles})

@app.route('/api/articles', methods=['POST'])
def add_article():
    new_article = request.get_json()
    new_article['id'] = len(articles) + 1
    articles.append(new_article)
    return jsonify(new_article), 201

if __name__ == '__main__':
    app.run(debug=True)
