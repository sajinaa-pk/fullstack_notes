# Generated by Django 3.1.3 on 2021-05-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo', '0002_auto_20210521_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='uid',
            field=models.CharField(blank=True, default='5541', editable=False, max_length=10, unique=True),
        ),
    ]