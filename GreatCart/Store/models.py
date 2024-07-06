from django.db import models
from Category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    decripton = models.TextField(null=True, blank=True, default='N/A')
    images = models.ImageField(upload_to='product/')
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.product_name
