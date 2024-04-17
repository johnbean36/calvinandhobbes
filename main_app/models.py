from django.db import models
from django.urls import reverse

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store_details', kwargs={'pk': self.id})
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=15)
    isbn = models.CharField(max_length=20)
    details = models.TextField(max_length=250)
    store = models.ManyToManyField(Store)
    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'book_id': self.id})
    
class Sales(models.Model):
    date = models.DateField()
    price = models.CharField(max_length=5)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.book.title} on {self.date}"
    
