# Generated by Django 4.0.6 on 2023-03-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_img_options_product_imgg'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_img',
            name='imgg',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
