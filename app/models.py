from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Product(BaseModel):
    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=155)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rank = models.PositiveIntegerField(default=1, max_length=5)
    sku = models.UUIDField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to='app.Category',
                                 on_delete=models.CASCADE,
                                 related_name='products')

    def __str__(self):
        return self.title