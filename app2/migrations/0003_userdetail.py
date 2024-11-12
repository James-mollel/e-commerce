# Generated by Django 5.0.6 on 2024-11-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_products_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]