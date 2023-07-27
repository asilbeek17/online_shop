from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
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
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    image2 = models.ImageField(upload_to='product/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product/', null=True, blank=True)
    title = models.CharField(max_length=155)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rank = models.PositiveIntegerField(default=1
                                       )
    # sku = models.UUIDField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to='app.Category',
                                 on_delete=models.CASCADE,
                                 related_name='products')

    user = models.ForeignKey(to='app.User',
                             on_delete=models.CASCADE,
                             related_name='products')

    def __str__(self):
        return self.title


# Blog uchun model ---------------------

class Blog(models.Model):
     image = models.ImageField(upload_to='blog/')
     title = models.CharField(max_length=155)
     description = models.TextField()
     author = models.ForeignKey(to='app.User',
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


class Post(BaseModel):
    message = models.TextField()
    name = models.CharField(max_length=155)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a phone number!')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25, validators=[integer_validator], null=True, blank=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    # forget_password_token = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


