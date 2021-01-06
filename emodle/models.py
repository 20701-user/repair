from django.db import models

# Create your models here.
class emodel(Model):
    numbering = CharField('設備編號', max_length=255)
     = CharField('型號', max_length=255)
    publisher = CharField('財產編號', max_length=255)
     = CharField('備註', max_length=255)

    def __str__(self):
        return "{}: {}".format(self.author, self.titl