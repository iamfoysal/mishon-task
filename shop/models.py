from django.db import models
from django.utils.text import slugify
# Create your models here.


class ProductBrand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductBrand, self).save(*args, **kwargs)

class ProductCategory(models.Model):
    name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True, auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

class ProductType(models.Model):
    name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True, auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductType, self).save(*args, **kwargs)

class WarrentyPeriod(models.Model):
    type= models.CharField(max_length=100)
    slug = models.SlugField(unique=True, auto_created=True, blank=True, null=True)
    
    def __str__(self):
        return self.type    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.type)
        super(WarrentyPeriod, self).save(*args, **kwargs)


class Product(models.Model):
    name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True, auto_created=True, blank=True, null=True)
    category= models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description= models.CharField(max_length=300)
    price= models.DecimalField(max_digits=5,decimal_places=2)
    image= models.ImageField(upload_to = 'product/')
    warenty= models.ForeignKey(WarrentyPeriod, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(WarrentyPeriod, self).save(*args, **kwargs)