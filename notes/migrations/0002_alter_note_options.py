# Generated by Django 3.2.6 on 2021-08-29 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-pub_date']},
        ),
    ]