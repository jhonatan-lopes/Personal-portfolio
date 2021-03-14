# Generated by Django 3.1.7 on 2021-03-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20210313_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='user@company.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='given_names',
            field=models.CharField(default='Testing', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='institution',
            field=models.CharField(default='Testing', max_length=200),
            preserve_default=False,
        ),
    ]
