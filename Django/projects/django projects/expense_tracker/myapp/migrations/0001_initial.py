# Generated by Django 3.1.5 on 2021-02-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bal', models.IntegerField()),
            ],
            options={
                'db_table': 'balance',
            },
        ),
        migrations.CreateModel(
            name='expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(max_length=100)),
                ('amt', models.IntegerField()),
            ],
            options={
                'db_table': 'expense',
            },
        ),
    ]
