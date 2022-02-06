from django.db import models
import requests 

from lyricsgenius import Genius

class Lyrics(models.Model):

    genius = Genius('T-O6ZPqV1z_kPLJe1N_TXGtalvuOtpd6kmE1rqCsUYwdE35RQWoGXQmNOEFFdkk1')
    genius.search_artist('Boulevard depo', max_songs=3, sort='title')
    artist.save_lyrics()