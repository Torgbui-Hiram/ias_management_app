# Generated by Django 4.1.5 on 2023-02-14 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_jobroles_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentityCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_types', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
