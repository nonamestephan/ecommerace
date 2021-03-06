# Generated by Django 4.0.5 on 2022-06-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
