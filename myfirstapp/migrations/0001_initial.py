# Generated by Django 3.2.7 on 2021-10-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
                ('surname', models.CharField(max_length=11)),
                ('date_of_birth', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=5)),
            ],
        ),
    ]