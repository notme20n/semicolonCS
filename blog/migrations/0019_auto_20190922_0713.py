# Generated by Django 2.2 on 2019-09-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190920_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/code.jpg', upload_to='Post_pics'),
        ),
    ]
