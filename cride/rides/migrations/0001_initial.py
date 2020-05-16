# Generated by Django 2.0.10 on 2020-05-10 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('circles', '0004_invitation'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DateTime on wich the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='DateTime on wich the object was last modiefed', verbose_name='modified at')),
                ('available_seats', models.PositiveIntegerField(default=1)),
                ('comments', models.TextField(blank=True)),
                ('departure_location', models.CharField(max_length=255)),
                ('departure_date', models.DateTimeField()),
                ('arrival_location', models.CharField(max_length=255)),
                ('arrival_date', models.DateTimeField()),
                ('rating', models.FloatField(null=True)),
                ('is_acive', models.BooleanField(default=True, help_text='Used for disabling the ride or marking it as finished', verbose_name='active status')),
                ('offered_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.User')),
                ('offered_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='circles.Circle')),
                ('passengers', models.ManyToManyField(related_name='passengers', to='users.User')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]