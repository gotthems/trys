# Generated by Django 3.1 on 2020-08-11 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200811_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]