# Generated by Django 5.0.4 on 2024-04-17 02:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.CharField(max_length=5)),
                ('book', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.book')),
            ],
        ),
    ]
