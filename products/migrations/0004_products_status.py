# Generated by Django 4.2.1 on 2023-05-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('init', 'Init'), ('stock', 'Stock'), ('sold', 'Sold'), ('delivered', 'Delivered')], default='init', max_length=10),
        ),
    ]
