# Generated by Django 4.1.5 on 2023-02-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_employee_records_job_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_records',
            name='appointment_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]