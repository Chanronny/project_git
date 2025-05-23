# Generated by Django 4.2 on 2025-04-13 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roomtypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('no_of_room_available_for_roomtype', models.IntegerField()),
                ('max_no_of_room_for_roomtype', models.IntegerField()),
                ('price', models.IntegerField()),
                ('with_breakfast_price', models.IntegerField()),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roomtypes.roomtype')),
            ],
        ),
    ]
