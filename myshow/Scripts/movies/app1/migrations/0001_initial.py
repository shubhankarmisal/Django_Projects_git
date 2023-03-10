# Generated by Django 4.1.4 on 2023-01-26 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=50)),
                ('b_img', models.ImageField(upload_to='')),
                ('b_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=50)),
                ('m_picture', models.ImageField(upload_to='')),
                ('m_Director', models.CharField(max_length=50)),
                ('m_discription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='theatre',
            fields=[
                ('t_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('t_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='addshow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.theatre')),
            ],
        ),
    ]
