# Generated by Django 2.2 on 2019-09-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190922_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/abeer.jpg', upload_to='profile_pics'),
        ),
    ]
