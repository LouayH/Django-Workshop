from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  description = models.TextField(blank=True)
  slug = models.SlugField(unique=True, blank=True)

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name