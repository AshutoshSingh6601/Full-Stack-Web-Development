# Generated by Django 4.0.4 on 2022-05-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
                ('stock', models.IntegerField()),
                ('image', models.URLField(max_length=2088)),
            ],
        ),
    ]
