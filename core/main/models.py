from django.db import models

# Create your models here.


class Slider(models.Model):

    text1 = models.CharField('Slider text1', max_length=100)
    text2 = models.CharField('Slider text2', max_length=100)
    img = models.ImageField('Slider image', upload_to='slider')

    def __str__(self):
        return f'Slider N{self.id}'
    

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name