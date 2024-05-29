# Generated by Django 3.1.3 on 2021-05-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('uid', models.CharField(blank=True, default='3086', editable=False, max_length=10, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='employeedetails',
        ),
    ]
