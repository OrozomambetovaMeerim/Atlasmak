# Generated by Django 4.0.4 on 2022-05-31 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Новости сайта')),
                ('content', models.TextField(blank=True, verbose_name='Текст')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Добавить')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Обновить')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
