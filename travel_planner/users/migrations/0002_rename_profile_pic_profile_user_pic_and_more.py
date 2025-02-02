# Generated by Django 5.1.5 on 2025-02-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='user_pic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='displayname',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
