# Generated by Django 2.2.3 on 2019-07-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190728_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cse',
            old_name='url',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ece',
            old_name='url',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='cse',
            name='html',
        ),
        migrations.RemoveField(
            model_name='ece',
            name='html',
        ),
        migrations.AddField(
            model_name='cse',
            name='roll',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='ece',
            name='roll',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]