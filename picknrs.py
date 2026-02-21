# Time-stamp: <2025-08-07 17:54:29 picknrs.py Guivho>

"""
This script gets random nrs from Random.org for amy of the
number games I sometimes play
"""

import requests
from bs4 import BeautifulSoup

# Coded lList of available games
# Each name should contain one single and unique upper case letter
# that will serve as user game selection character
# the value format is defined by random.org
defs = {
    "Euromillions" : "4;5x50.2x12",
    "euroDreams" : "4;6x40.1x5",
    "Lotto" : "7;6x45.0x0",
    "Viking" : "1;6x48.1x5",
    "Pick3": "1;1x9.1x9"
};
keys = list(defs.keys())
vals = list(defs.values())

#pick random nrs via random.org
def gofor(defNr=0, nrOfPlays=2):
    url = (f"https://random.org/quick-pick/?tickets={nrOfPlays}&lottery={vals[defNr].split(';')[1]}",
           f"https://www.random.org/integers/?num={nrOfPlays}&min=0&max=999&col=1&base=10&format=html&rnd=new"
           )[keys[defNr] == "Pick3"];
    #print(f"defNr={defNr} {keys[defNr]} {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)
    nrs = soup.find('pre', class_='data')
    return nrs.text.strip()

#play one of the defined games, specified by its index in defs
def play(defNr):
    commonNrOfGrids = vals[defNr].split(';')[0]
    nrOfPlays = input(f"Picking {keys[defNr]} - Nr of grids? [{commonNrOfGrids}]> ") or commonNrOfGrids
    if(nrOfPlays.isnumeric() and int(nrOfPlays) < 13):
        print(gofor(defNr, int(nrOfPlays)))
    return

def main():
    gameCodes = [x for list in keys for x in list if x.isupper()]
    game = input(f"{keys} {''.join(gameCodes[:])}? ").upper()
    if(game in gameCodes):
        play(gameCodes.index(game))

if __name__ == '__main__':
    main()
