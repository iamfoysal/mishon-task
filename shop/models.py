from django.db import models
from django.utils.text import slugify
# Create your models here.


class ProductBrand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductBrand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product Brand'
        verbose_name_plural = 'Product Brands'


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductType, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'


class WarrantyPeriod(models.Model):
    type = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        self.slug = slugify(self.type)
        super(WarrantyPeriod, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Warranty Period'
        verbose_name_plural = 'Warranty Periods'


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, auto_created=True, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='product/')
    warranty = models.ForeignKey(WarrantyPeriod, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
