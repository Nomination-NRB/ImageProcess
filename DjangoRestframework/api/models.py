from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    ori_file = models.ImageField(upload_to='images/ori/')

    def __str__(self):
        return self.file
