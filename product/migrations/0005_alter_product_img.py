# Generated by Django 4.2.7 on 2023-12-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]