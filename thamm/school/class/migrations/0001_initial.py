# Generated by Django 3.2.6 on 2021-08-20 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=40, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]
