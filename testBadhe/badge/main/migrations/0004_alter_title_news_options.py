# Generated by Django 5.1.1 on 2024-09-05 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title_news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]