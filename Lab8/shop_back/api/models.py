from django.db import models

# Create your models here.

# Category model:
class Category(models.Model):
    name = models.CharField(max_length = 100)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return self.title
    


# Product model:
class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField(default = True)

    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category': self.category,
            'is_active': self.is_active 
        }
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Single'
        verbose_name_plural = 'Plural'
