    # для форматирования HTML можно установить bs4
    # pip install bs4
    # многие решения взяты из предыдущих уроков
    # запустите
    # http://localhost:8080/
    # там и GET и POST запросы можно сделать)))
    # пояснений много не писал...сразу сорри!!

from bottle import *

# Static CSS Files
@route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

# Static js Files
@route('/static/src/<filename:re:.*\.js>')
def send_css(filename):
    return static_file(filename, root='static/src')

@get("/")
@view('index')
def index():
    return {}

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)