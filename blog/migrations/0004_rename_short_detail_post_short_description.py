# Generated by Django 3.2 on 2022-03-20 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_short_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='short_detail',
            new_name='short_description',
        ),
    ]
