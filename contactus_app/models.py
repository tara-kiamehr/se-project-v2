from django.db import models

class footer(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    whatsapp = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)


class Message(models.Model):
    fname = models.CharField(max_length=50)
    email = models.EmailField()
    sub = models.CharField(max_length=100)
    body = models.TextField()

    def __self__(self):
        return f"{self.name} - {self.email}"        