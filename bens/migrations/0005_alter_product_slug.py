# Generated by Django 4.1.2 on 2022-11-02 14:34

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bens", "0004_rename_codbem_product_codigo_product_responsavel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="codigo", unique=True
            ),
        ),
    ]
