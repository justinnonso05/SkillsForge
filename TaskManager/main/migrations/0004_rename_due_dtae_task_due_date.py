# Generated by Django 5.1.5 on 2025-02-05 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_task_category_task_due_dtae'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_dtae',
            new_name='due_date',
        ),
    ]
