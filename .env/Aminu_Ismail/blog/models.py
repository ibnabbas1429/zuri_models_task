from django.conf import settings
from django.db import models

# Create your models here.





 

class Post(models.Model):

    title = models.CharField(max_length= 2000) 
    text = models.TextField() 
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )  
 

    Created_date = models.DateTimeField(auto_now_add=True)

    Published_date  =models.DateTimeField("published Date")

    def __str__(self):
        return self.title
 


