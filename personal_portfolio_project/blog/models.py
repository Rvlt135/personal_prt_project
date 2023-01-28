from django.db import models

class BlogContet(models.Model):
        title = models.CharField(max_length=150)
        description = models.CharField(max_length=300)
        image = models.ImageField(upload_to='portfolio/images/')
