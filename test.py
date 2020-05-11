
from app.db import *


def stats_get():
    votings = animals_get()
    msg = ','.join(map(lambda item : '"{}": {}'.format(item.name, item.votes),votings))
    print(msg)

#data: {"cats": 4262, "parrots": 6416, "dogs": 5478}

if __name__ == "__main__":
    stats_get()