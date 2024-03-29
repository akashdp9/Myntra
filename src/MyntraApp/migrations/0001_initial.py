# Generated by Django 2.2.7 on 2019-11-22 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='media/default.jpg', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='media/default.jpg', upload_to='media')),
                ('brand', models.CharField(max_length=200)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyntraApp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_cancelled', models.BooleanField(default=False, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyntraApp.Item')),
            ],
        ),
    ]
