# Generated by Django 4.2.7 on 2023-11-11 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_data_nascimento'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]