from django.db import models


class AddNewNoteModel(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=1000)
