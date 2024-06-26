# Generated by Django 5.0.6 on 2024-06-27 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cont01', '0002_department_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department2',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee2',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cont01.department')),
            ],
        ),
    ]
