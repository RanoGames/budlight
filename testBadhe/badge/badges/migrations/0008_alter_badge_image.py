# Generated by Django 5.1 on 2024-08-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0007_alter_badge_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]