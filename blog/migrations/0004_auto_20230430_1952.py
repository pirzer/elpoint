# Generated by Django 3.2.18 on 2023-04-30 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230430_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
