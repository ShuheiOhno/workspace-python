# Generated by Django 4.2.1 on 2023-05-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_alter_boardmodel_sns_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='readtext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
