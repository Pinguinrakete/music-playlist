from django.db import models
       
class Playlist(models.Model):
    interpret = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.interpret
