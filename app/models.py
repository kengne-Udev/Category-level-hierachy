from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
