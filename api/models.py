from django.db import models
import json


class User(models.Model):
    username = models.CharField(max_length=150, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
                'pk': self.pk,
                'fields': {
                    'username': self.username,
                    'email': self.email,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'date_added': self.date_added
                }
            }

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ('username', 'email')
        ordering = ('date_added',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True,
                            blank=True, unique=True)

    def serialize(self):
        return {
                'pk': self.pk,
                'fields': {
                    'category': self.name,
                    'slug': self.slug,
                }
            }

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True,
                            blank=True, unique=True)

    def serialize(self):
        return {
                'pk': self.pk,
                'fields': {
                    'status': self.name,
                    'slug': self.slug,
                }
            }

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = ' Statuses'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True, blank=True)
    author = models.CharField(max_length=150, blank=True)
    date_writing = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
                'pk': self.pk,
                'fields': {
                    'book_title': self.name,
                    'slug': self.slug,
                    'author': self.author,
                    'date_writing': self.date_writing,
                    'status_id': self.status,
                    'category_id': self.category,
                    'user_id': self.user,
                    'date_added': self.date_added
                }
            }

    class Meta:
        ordering = ('-date_added',)
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

