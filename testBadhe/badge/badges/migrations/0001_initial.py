# Generated by Django 5.1 on 2024-09-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='BadgeToUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='Код пользователя')),
                ('badge_id', models.IntegerField(verbose_name='Код значка')),
            ],
        ),
    ]
