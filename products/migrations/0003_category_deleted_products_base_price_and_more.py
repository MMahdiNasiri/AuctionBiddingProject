# Generated by Django 4.2.1 on 2023-05-26 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_identifier_alter_products_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='deleted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='base_price',
            field=models.IntegerField(default=234),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productpictures',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pictures', to='products.products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='products.category'),
        ),
    ]
