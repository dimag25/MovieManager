import eel
from api.movieApi import *


@eel.expose
def startDownload(moviesType):
    try:
        return movieAPI.downloadAndGetMovies(moviesType)
    except Exception as e:
        return "Error"


@eel.expose
def updateMongoDB():
    return movieAPI.updateMongoDB()


@eel.expose
def getDBValues():
    try:
        return movieAPI.getDBValuesCount()
    except Exception as e:
        return "Error"

eel.init('eel_module/web')
eel.start('downloadMovies.html', size=(850, 850), port=0)


