# Generated by Django 5.0.7 on 2024-07-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.TextField(max_length=100)),
                ('amount_of_views', models.IntegerField()),
                ('position', models.IntegerField()),
            ],
        ),
    ]
