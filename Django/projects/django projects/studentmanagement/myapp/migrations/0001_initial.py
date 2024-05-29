# Generated by Django 3.1.5 on 2022-02-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=100)),
                ('semail', models.EmailField(max_length=254)),
                ('scontact', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
