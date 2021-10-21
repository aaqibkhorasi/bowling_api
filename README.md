# SuperBowl Rest

SuperBowl is a rest api to play bowling game. It provide following 

## Installation

## Virtual Environment:
if you like, you can create your new virtual environment

```bash
python3 -m my_virtual # this will create virutal_env under local dir
```
Activate it 
```bash
source ./my_virtual/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SuperBowl requirement file inside virtualenv

```bash
pip install -r requirements.txt
```

Run the app
```bash
python app.py

```
By default it will be hosted on port 5000: localhost:5000/

## Endpoints
* [Create Game](/docs/startgame.md) : `POST /start_game`
* [Updated Knocked Pin](/docs/knockedpins.md) : `POST /knocked_pins`
* [Get Score](/docs/fetchscore.md) : `GET /score`


## UnitTest

In order to run unit test, run following
```
nosetests -v game_service_test.py
```
