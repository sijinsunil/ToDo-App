# Generated by Django 2.2.14 on 2020-08-29 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200828_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='notes',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
