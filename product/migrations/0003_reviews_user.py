# Generated by Django 4.2.3 on 2023-10-30 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0002_alter_product_avgrating_alter_product_reviews"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviews",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_review",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
