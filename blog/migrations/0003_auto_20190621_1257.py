# Generated by Django 2.2.2 on 2019-06-21 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190621_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogger',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
