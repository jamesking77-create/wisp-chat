# Generated by Django 4.2.2 on 2023-06-07 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisp_chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='_password',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=8),
        ),
    ]
