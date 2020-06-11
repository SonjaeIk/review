from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) ## 다른 문서에 대한 외래키 
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_data = models.DateTimeField(
            default = timezone.now)
    published_data = models.DateTimeField(
        blank = True, null = True)
    
    def published(self):
        self.published_data = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title