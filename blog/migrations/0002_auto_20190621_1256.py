# Generated by Django 2.2.2 on 2019-06-21 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogger',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]