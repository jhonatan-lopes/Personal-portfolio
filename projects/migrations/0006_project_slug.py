# Generated by Django 3.1.7 on 2021-04-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210331_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]