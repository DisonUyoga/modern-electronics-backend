# Generated by Django 5.0.1 on 2024-01-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_reviews_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='initialPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
