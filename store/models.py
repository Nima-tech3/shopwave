from django.db import models
from django.conf import settings
from django.urls import reverse

# Manager 
class CreatedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='available')

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

class Product(models.Model):
    # Difine available product statuses
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('discontinued', 'Discontinued')
    ]

    # Connect product to its category
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    # Data fields
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField()

    # Date
    created = models.DateTimeField(auto_now_add=True)

    # Set the product status 
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    objects = models.Manager()
    available_products = CreatedManager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['price'])
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.id])
    
