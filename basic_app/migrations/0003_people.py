# Generated by Django 3.1 on 2020-09-17 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20200915_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total_bill', models.FloatField(default=0)),
                ('paid_money', models.FloatField(default=0)),
                ('rem_money', models.FloatField(default=0)),
                ('item_name', models.CharField(max_length=150)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
