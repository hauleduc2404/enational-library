# Generated by Django 3.2.5 on 2022-01-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20211123_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='appliedAuthors',
        ),
        migrations.RemoveField(
            model_name='event',
            name='appliedBooks',
        ),
        migrations.RemoveField(
            model_name='event',
            name='appliedPublisher',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=2, upload_to='', verbose_name='Ảnh sự kiện'),
            preserve_default=False,
        ),
    ]
