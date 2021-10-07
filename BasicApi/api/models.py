from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    community = models.CharField(max_length=50)

    def __str__(self):
        return self.name