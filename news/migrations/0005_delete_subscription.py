# Generated by Django 4.2 on 2023-05-09 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_category_subscribers_alter_subscription_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
