# Generated by Django 4.0 on 2021-12-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name_task', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('attached_file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
