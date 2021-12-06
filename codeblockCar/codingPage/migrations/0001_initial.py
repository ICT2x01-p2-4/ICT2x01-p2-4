# Generated by Django 3.2.9 on 2021-12-06 22:46

import codingPage.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=30)),
                ('code', models.IntegerField(validators=[codingPage.validators.validate_action_code])),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=50)),
                ('sent', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sent_datetime', models.DateTimeField(auto_now=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.challenge')),
            ],
        ),
    ]
