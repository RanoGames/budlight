# Generated by Django 5.1 on 2024-08-20 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
            ],
        ),
    ]
