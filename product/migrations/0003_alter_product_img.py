# Generated by Django 4.2.7 on 2023-12-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_product_name_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
