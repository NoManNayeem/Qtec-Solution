# Generated by Django 4.1.7 on 2023-05-28 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="product_image/"),
        ),
    ]
