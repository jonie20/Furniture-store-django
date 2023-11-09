# Generated by Django 4.2.4 on 2023-11-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/images')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]