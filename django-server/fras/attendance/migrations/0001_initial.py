# Generated by Django 2.1.3 on 2019-02-16 12:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapturedFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captured_at', models.DateTimeField(auto_now=True)),
                ('image_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaceId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_id', models.TextField()),
                ('captured_frame',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='face_ids',
                                   to='attendance.CapturedFrame')),
            ],
        ),
        migrations.CreateModel(
            name='LectureAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_name', models.CharField(max_length=100)),
                ('start', models.DateField(default=datetime.datetime(2019, 2, 16, 17, 36, 2, 369370))),
                ('end', models.DateField(default=datetime.datetime(2019, 2, 16, 17, 36, 2, 369370))),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identification Number')),
                ('full_name', models.CharField(max_length=100)),
                ('face_id', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
        migrations.AddField(
            model_name='lectureattendance',
            name='working_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_attendances',
                                    to='attendance.WorkingDay'),
        ),
        migrations.AddField(
            model_name='capturedframe',
            name='lecture_attendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='captured_frames',
                                    to='attendance.LectureAttendance'),
        ),
        migrations.AddField(
            model_name='capturedframe',
            name='students',
            field=models.ManyToManyField(null=True, to='attendance.Student'),
        ),
    ]