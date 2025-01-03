# Generated by Django 5.1.2 on 2024-10-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('proficiency', models.IntegerField(blank=True, default=0, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('is_key_skill', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]
