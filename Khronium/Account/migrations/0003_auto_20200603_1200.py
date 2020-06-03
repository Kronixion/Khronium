# Generated by Django 3.0.4 on 2020-06-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_account_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='lockoutDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='loginAttempt',
            field=models.IntegerField(default=0),
        ),
    ]
