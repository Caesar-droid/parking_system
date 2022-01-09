# Generated by Django 3.2.9 on 2021-12-12 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('S', 'SALOON'), ('T', 'HEAVY DUTY'), ('X', 'SUV')], max_length=1)),
                ('car_plate', models.CharField(max_length=15)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
