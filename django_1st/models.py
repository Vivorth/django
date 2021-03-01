from django.db import models

class cl1(models.Model):
    name= models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc= models.TextField()
    sel= models.BooleanField(default=False)