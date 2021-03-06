# Generated by Django 2.2.2 on 2019-06-23 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_target_blog_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='target_blog_post',
            new_name='comment_blog_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post_date',
            new_name='comment_date',
        ),
    ]
