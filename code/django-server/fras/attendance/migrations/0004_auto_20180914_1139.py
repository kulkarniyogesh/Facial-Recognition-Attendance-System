# Generated by Django 2.1.1 on 2018-09-14 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('attendance', '0003_auto_20180914_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingday',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
