# Generated by Django 5.0.3 on 2024-04-02 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Single', 'verbose_name_plural': 'Plural'},
        ),
    ]