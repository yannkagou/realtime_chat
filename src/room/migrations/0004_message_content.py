# Generated by Django 4.2.8 on 2023-12-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
