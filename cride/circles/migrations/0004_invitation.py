# Generated by Django 2.0.10 on 2020-05-02 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('circles', '0003_auto_20200430_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DateTime on wich the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='DateTime on wich the object was last modiefed', verbose_name='modified at')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('used', models.BooleanField(default=False)),
                ('used_at', models.DateTimeField(blank=True, null=True)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circles.Circle')),
                ('issued_by', models.ForeignKey(help_text='Circle member that is providing the invitation', on_delete=django.db.models.deletion.CASCADE, related_name='issued_by', to='users.User')),
                ('used_by', models.ForeignKey(help_text='User that used the code to enter the circle', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]