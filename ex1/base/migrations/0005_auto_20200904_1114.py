# Generated by Django 2.2.14 on 2020-09-04 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_task_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Task_todo',
        ),
    ]
