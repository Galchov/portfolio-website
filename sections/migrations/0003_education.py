# Generated by Django 5.1.2 on 2024-10-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='certificates/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
