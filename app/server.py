import time
from bottle import *

def create_app():
    app = Bottle()
    app.config.load_config('sse_server.conf')

    app.config.setdefault('server', 'waitress')
    app.config.setdefault('host', 'localhost')
    app.config.setdefault('port', 8080)

    return app

app = create_app()

# Static CSS Files
@app.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

@app.route('/bootstrap/dist/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='node_modules/bootstrap/dist/css')

# Static js Files
@app.route('/static/src/<filename:re:.*\.js>')
def send_css(filename):
    return static_file(filename, root='static/src')

@app.route('/bootstrap/dist/js/<filename:re:.*\.js>')
def send_css(filename):
    return static_file(filename, root='node_modules/bootstrap/dist/js')

@app.get("/")
@view('index')
def index():
    return {}

@app.get("/vote")
@view('vote')
def get_form():
    return {}

@app.get("/sse/vote/stats")
def stats_get():
    response.content_type = "text/event-stream"
    response.cache_control = "no-cache"
    response.headers['Access-Control-Allow-Origin'] = '*'

    while True:
        yield 'data: {"cats": 4262, "parrots": 6416, "dogs": 5478}\n\n'
        time.sleep(2)

#data: {"cats": 4262, "parrots": 6416, "dogs": 5478}