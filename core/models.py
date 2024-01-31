from django.db import models
import uuid 
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'name of category')
    def __str__(self):
        return self.name
    

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255, verbose_name = 'post title')
    content = models.TextField(verbose_name = 'post kontenti')
    image = models.ImageField(upload_to = 'post-surati/')
    date = models.DateTimeField(auto_now = False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})