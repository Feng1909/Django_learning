# Generated by Django 3.2.5 on 2021-07-16 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='account',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]