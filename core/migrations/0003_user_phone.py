# Generated by Django 4.0 on 2024-01-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=11, max_length=255),
            preserve_default=False,
        ),
    ]
