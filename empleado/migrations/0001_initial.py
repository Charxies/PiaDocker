# Generated by Django 4.1.3 on 2022-11-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('epos', models.CharField(max_length=45)),
                ('econtact', models.IntegerField(max_length=15)),
            ],
            options={
                'db_table': 'empleado',
            },
        ),
    ]
