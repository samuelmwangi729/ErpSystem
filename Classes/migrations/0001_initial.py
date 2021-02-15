# Generated by Django 3.1.6 on 2021-02-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassNumber', models.IntegerField()),
                ('Status', models.IntegerField(default=0)),
                ('_createdAt', models.DateField(auto_now_add=True)),
                ('_updatedAt', models.DateField(auto_now=True)),
                ('_createdBy', models.CharField(max_length=30)),
                ('_updatedBy', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
