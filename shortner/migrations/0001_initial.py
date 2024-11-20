# Generated by Django 4.2.16 on 2024-11-18 02:01

from django.db import migrations, models
import shortner.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=220, validators=[shortner.validators.validate_url])),
                ('shortcode', models.CharField(blank=True, max_length=6, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
