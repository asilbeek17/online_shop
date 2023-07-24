from django.db import models


# Product uchun model ---------------------

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
    # sku = models.UUIDField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to='app.Category',
                                 on_delete=models.CASCADE,
                                 related_name='products')

    def __str__(self):
        return self.title


# Blog uchun model ---------------------

class Author(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Blog(models.Model):
     image = models.ImageField(upload_to='blog/')
     title = models.CharField(max_length=155)
     description = models.TextField()
     author = models.ForeignKey(to='app.Author',
                                on_delete=models.CASCADE,
                                related_name='blogs')

     def __str__(self):
         return self.title


class Feedback(models.Model):
    name = models.CharField(null=True, max_length=100)
    email = models.CharField(default='none', null=False, max_length=100)
    subject = models.CharField(null=True, max_length=100)
    feed = models.TextField(null=True)


    def __str__(self):
        return self.email
