from django.db import models
from django.conf import settings
from products.models import Product
from profiles.models import UserProfile
from django.db.models import UniqueConstraint

# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'product'], name='unique_wishlist')
        ]
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"
        indexes = [
            models.Index(fields=['user', 'product']),
        ]
        ordering = ['-added_on']

        def __str__(self):
            return f"{self.product.name} - {self.user.user.username}"
