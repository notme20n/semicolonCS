# Generated by Django 2.2 on 2019-08-13 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190621_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
