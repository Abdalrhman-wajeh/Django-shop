# Generated by Django 4.1.5 on 2023-01-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodects', '0007_rename_masurunits_product_masur_units'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Size',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('3XL', '3XL'), ('4XL', '4XL'), ('5XL', '5XL')], max_length=120, null=True),
        ),
    ]