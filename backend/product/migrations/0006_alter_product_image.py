# Generated by Django 3.2.4 on 2021-06-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/no_preview_image.png', null=True, upload_to=''),
        ),
    ]
