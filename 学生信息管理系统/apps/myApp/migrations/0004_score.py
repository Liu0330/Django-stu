# Generated by Django 2.0.2 on 2019-05-28 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20190511_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('math', models.IntegerField()),
                ('chinese', models.IntegerField()),
                ('english', models.IntegerField()),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Students')),
            ],
        ),
    ]
