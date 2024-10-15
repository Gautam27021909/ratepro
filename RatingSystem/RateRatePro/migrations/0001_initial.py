# Generated by Django 5.0.3 on 2024-10-14 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8)),
            ],
            options={
                'db_table': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='UserName', max_length=100)),
                ('nickname', models.CharField(blank=True, db_column='NickName', max_length=50, null=True)),
                ('major', models.CharField(blank=True, db_column='Major', max_length=50, null=True)),
                ('email', models.EmailField(db_column='Email', max_length=100, unique=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=12, null=True)),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Professor', 'Professor'), ('Non-Student', 'Non-Student')], db_column='Role', default='Non-Student', max_length=20)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.OneToOneField(db_column='Id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='RateRatePro.users')),
                ('overall_rating', models.FloatField(db_column='OverallRating', null=True)),
                ('department_id', models.ForeignKey(blank=True, db_column='DepartmentID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='RateRatePro.departments')),
            ],
            options={
                'db_table': 'Professors',
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('overall_rating', models.FloatField(blank=True, db_column='OverallRating', null=True)),
                ('would_take_again', models.FloatField(blank=True, db_column='WouldTakeAgain', null=True)),
                ('academic_ability', models.FloatField(blank=True, db_column='AcademicAbility', null=True)),
                ('teaching_ability', models.FloatField(blank=True, db_column='TeachingAbility', null=True)),
                ('interactions_with_students', models.FloatField(blank=True, db_column='InteractionsWithStudents', null=True)),
                ('hardness', models.FloatField(blank=True, db_column='Hardness', null=True)),
                ('feedback', models.CharField(blank=True, db_column='Feedback', max_length=500, null=True)),
                ('is_edited', models.CharField(blank=True, choices=[('0', '0'), ('1', '1')], db_column='IsEdited', default='0', max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_column='TimeStamp')),
                ('course_id', models.ForeignKey(blank=True, db_column='CourseID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='RateRatePro.courses')),
                ('student_id', models.ForeignKey(blank=True, db_column='StudentID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='RateRatePro.users')),
                ('professor_id', models.ForeignKey(blank=True, db_column='ProfID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='RateRatePro.professors')),
            ],
            options={
                'db_table': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='StudentCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(db_column='CourseID', on_delete=django.db.models.deletion.CASCADE, to='RateRatePro.courses')),
                ('student_id', models.ForeignKey(db_column='StudentID', on_delete=django.db.models.deletion.CASCADE, to='RateRatePro.users')),
            ],
            options={
                'db_table': 'StudentCourses',
                'unique_together': {('course_id', 'student_id')},
            },
        ),
        migrations.CreateModel(
            name='ProfessorCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RateRatePro.courses')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RateRatePro.professors')),
            ],
            options={
                'db_table': 'ProfessorCourses',
                'unique_together': {('course', 'professor')},
            },
        ),
    ]
