# Generated by Django 3.0 on 2020-06-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_pricing'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField(blank=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('title', models.TextField(blank=True)),
                ('content', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
    ]