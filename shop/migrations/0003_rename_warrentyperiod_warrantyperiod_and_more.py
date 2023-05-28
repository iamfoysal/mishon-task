# Generated by Django 4.2 on 2023-05-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_slug_productbrand_slug_productcategory_slug_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WarrentyPeriod',
            new_name='WarrantyPeriod',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productbrand',
            options={'verbose_name': 'Product Brand', 'verbose_name_plural': 'Product Brands'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Categories'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'Product Type', 'verbose_name_plural': 'Product Types'},
        ),
        migrations.AlterModelOptions(
            name='warrantyperiod',
            options={'verbose_name': 'Warranty Period', 'verbose_name_plural': 'Warranty Periods'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='warenty',
            new_name='warranty',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
