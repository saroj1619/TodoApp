# Generated by Django 2.2 on 2019-05-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20190506_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='due_date',
            field=models.DateTimeField(),
        ),
    ]
