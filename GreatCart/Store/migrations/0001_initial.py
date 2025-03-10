# Generated by Django 5.0.6 on 2024-07-02 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('decripton', models.TextField(blank=True, default='N/A', null=True)),
                ('images', models.ImageField(upload_to='product/')),
                ('stock', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='Category.category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
