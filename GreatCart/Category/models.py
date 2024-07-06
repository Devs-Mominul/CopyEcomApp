from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    deccription = models.TextField(max_length=255, blank=True, null=True)
    category_img = models.ImageField(upload_to='category/', blank=True)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('product_by_category', args=[self.slug])
           
            
            
    def __str__(self):
        return self.name

    
