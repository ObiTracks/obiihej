# Generated by Django 3.1.5 on 2022-02-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True),
        ),
    ]
