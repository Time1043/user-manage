# Generated by Django 3.2 on 2024-03-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
