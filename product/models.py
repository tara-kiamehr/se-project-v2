from django.db import models

class product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    Image = models.ImageField(upload_to="product")


    def __self__(self):
        return self.title