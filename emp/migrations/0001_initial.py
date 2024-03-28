# Generated by Django 5.0.3 on 2024-03-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('emp_id', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('working', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=10)),
            ],
        ),
    ]
