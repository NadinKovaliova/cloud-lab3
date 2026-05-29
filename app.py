from flask import Flask, request

app = Flask(__name__)

# Проста веб-сторінка
@app.route('/')
def home():
    return '''
    <h1>Hello from Cloud Lab 3!</h1>
    <p>Надія Ковальова - Безпека CI/CD</p>
    '''

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return f'<p>Результат пошуку: {query}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
