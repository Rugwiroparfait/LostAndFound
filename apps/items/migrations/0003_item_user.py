# Generated by Django 5.0.1 on 2025-02-03 10:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_alter_item_options_item_claim_status_item_location_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
