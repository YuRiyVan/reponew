# Generated by Django 4.1.7 on 2023-03-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_product_img_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_img',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
