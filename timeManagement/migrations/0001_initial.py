# Generated by Django 3.0.4 on 2020-06-08 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0003_auto_20200603_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.TimeField()),
                ('description', models.CharField(max_length=200)),
                ('dailyList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeManagement.DailyList')),
            ],
        ),
    ]
