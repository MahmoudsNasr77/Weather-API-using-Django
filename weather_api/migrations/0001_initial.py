# Generated by Django 4.2.2 on 2023-07-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250)),
                ('contery', models.CharField(max_length=250)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=4)),
                ('decription', models.TextField(max_length=250)),
            ],
        ),
    ]
