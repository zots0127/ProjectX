# Generated by Django 2.2.6 on 2019-11-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CID', models.CharField(max_length=32)),
                ('CU', models.CharField(max_length=32)),
                ('MU', models.CharField(max_length=32)),
                ('DI', models.CharField(max_length=32)),
                ('DO', models.CharField(max_length=32)),
                ('NI', models.CharField(max_length=32)),
                ('NO', models.CharField(max_length=32)),
                ('UPT', models.CharField(max_length=32)),
            ],
        ),
    ]
