# Generated by Django 2.2.5 on 2019-09-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentsinfo',
            name='student_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
