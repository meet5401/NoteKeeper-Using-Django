from django.db import models

# Create your models here.
class Info(models.Model):
    title=models.CharField( max_length=50)
    content=models.TextField( max_length=500)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
