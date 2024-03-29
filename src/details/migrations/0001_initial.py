# Generated by Django 2.0.7 on 2019-11-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitorName', models.CharField(max_length=50)),
                ('visitorEmail', models.EmailField(max_length=60)),
                ('visitorContactNo', models.CharField(max_length=10)),
                ('hostName', models.CharField(max_length=50)),
                ('hostEmail', models.EmailField(max_length=60)),
                ('hostContactNo', models.CharField(max_length=10)),
                ('checkIn', models.DateTimeField(auto_now_add=True)),
                ('checkOut', models.DateTimeField(null=True)),
            ],
        ),
    ]
