    # запустите
    # http://localhost:8080/
    # создать базу
    # если тупит - ручками удалить базу и создать заново
    # пояснений много не писал...сразу сорри!!

import bottle

from app.server import app

if __name__ == "__main__":
    bottle.run(
        app=app, host=app.config.host, port=app.config.port, server=app.config.server
    )