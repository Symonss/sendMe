# Generated by Django 2.0.13 on 2019-04-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0003_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_description',
            field=models.TextField(default="This job should be done as first as posible, can't wait for the bids", max_length=50),
        ),
    ]