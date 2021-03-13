# Generated by Django 3.1.7 on 2021-03-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='publication',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='date_published',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='doi',
        ),
        migrations.AddField(
            model_name='publication',
            name='journal',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='publication',
            name='link',
            field=models.CharField(default='#', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='type',
            field=models.CharField(choices=[('BK', 'Book'), ('AR', 'Article'), ('CF', 'Conference Paper'), ('BC', 'Book Chapter')], default='AR', max_length=2),
        ),
        migrations.AddField(
            model_name='publication',
            name='year',
            field=models.IntegerField(default=2020),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='publication',
            name='authors',
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(related_name='publications', to='publications.Author'),
        ),
    ]
