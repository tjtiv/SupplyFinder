# Generated by Django 3.0.7 on 2020-07-31 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemType', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('url', models.TextField()),
                ('rating', models.TextField()),
                ('numSold', models.TextField()),
                ('img', models.TextField()),
                ('shipping', models.TextField()),
            ],
        ),
    ]
