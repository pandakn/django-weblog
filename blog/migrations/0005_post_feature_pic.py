# Generated by Django 3.2 on 2022-03-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_short_detail_post_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feature_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
    ]
