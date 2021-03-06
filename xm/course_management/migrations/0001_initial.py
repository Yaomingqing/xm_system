# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-05 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec', models.CharField(blank=True, max_length=50, null=True, verbose_name='专业简称')),
                ('stu_grade', models.CharField(max_length=30, verbose_name='年级')),
                ('stu_class', models.CharField(max_length=30, verbose_name='班级')),
                ('ctype', models.CharField(max_length=40, verbose_name='课程类型')),
                ('sel_cour_id', models.CharField(max_length=40, verbose_name='课程编号')),
                ('sel_cour_name', models.CharField(max_length=40, verbose_name='课程名称')),
                ('tea_id', models.CharField(max_length=30, verbose_name='教工号')),
                ('sel_teac_name', models.CharField(max_length=30, verbose_name='主讲教师')),
                ('credit', models.FloatField(verbose_name='学分')),
                ('cour_character', models.CharField(max_length=40, verbose_name='课程性质')),
                ('tea_mode', models.CharField(max_length=40, verbose_name='教学形式')),
                ('tes_category', models.CharField(max_length=20, verbose_name='考试类别')),
                ('total_hours', models.IntegerField(verbose_name='总学时')),
                ('teach', models.IntegerField(verbose_name='讲授')),
                ('experiment', models.IntegerField(verbose_name='实验')),
                ('practise', models.IntegerField(verbose_name='实习')),
                ('operate', models.IntegerField(verbose_name='上机')),
                ('department', models.CharField(blank=True, max_length=40, null=True, verbose_name='主管单位')),
                ('semester', models.CharField(blank=True, max_length=30, null=True, verbose_name='适用学期')),
            ],
            options={
                'verbose_name': '课程表',
                'verbose_name_plural': '课程表',
                'db_table': 'class',
            },
        ),
        migrations.CreateModel(
            name='Course_teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_id', models.CharField(max_length=30, verbose_name='教工号')),
                ('tea_name', models.CharField(max_length=30, verbose_name='姓名')),
                ('tea_password', models.CharField(blank=True, max_length=40, null=True, verbose_name='密码')),
                ('tea_sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=30, verbose_name='性别')),
                ('tea_department', models.CharField(max_length=40, verbose_name='院系')),
                ('tea_title', models.CharField(max_length=20, verbose_name='职称')),
                ('tea_email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '任课教师表',
                'verbose_name_plural': '任课教师表',
                'db_table': 'course_teacher',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=30, verbose_name='学号')),
                ('stu_name', models.CharField(max_length=30, verbose_name='姓名')),
                ('stu_major', models.CharField(max_length=40, verbose_name='专业')),
                ('stu_grade', models.CharField(max_length=30, verbose_name='年级')),
                ('stu_class', models.CharField(max_length=30, verbose_name='班级')),
                ('sel_cour_id', models.CharField(max_length=60, verbose_name='课程编号')),
                ('sel_cour_name', models.CharField(max_length=40, verbose_name='课程名称')),
                ('atte', models.IntegerField(verbose_name='考勤')),
                ('expe', models.IntegerField(verbose_name='实验')),
                ('task', models.IntegerField(verbose_name='作业')),
                ('class_per', models.IntegerField(verbose_name='课堂表现')),
                ('us_scor', models.IntegerField(verbose_name='平时成绩')),
                ('first_ques', models.IntegerField(verbose_name='第一大题')),
                ('seco_ques', models.IntegerField(verbose_name='第二大题')),
                ('third_ques', models.IntegerField(verbose_name='第三大题')),
                ('four_ques', models.IntegerField(verbose_name='第四大题')),
                ('exam_score', models.IntegerField(verbose_name='考试成绩')),
                ('tota_score', models.IntegerField(verbose_name='总评成绩')),
            ],
            options={
                'verbose_name': '成绩表',
                'verbose_name_plural': '成绩表',
                'db_table': 'score',
            },
        ),
        migrations.CreateModel(
            name='Sel_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=30, verbose_name='学号')),
                ('sel_cour_seme', models.CharField(max_length=50, verbose_name='学期')),
                ('sel_cour_id', models.CharField(max_length=60, verbose_name='课程编号')),
                ('sel_cour_name', models.CharField(max_length=40, verbose_name='课程名称')),
                ('sel_teac_name', models.CharField(max_length=50, verbose_name='主讲教师')),
                ('sel_class', models.CharField(max_length=40, verbose_name='教学班')),
                ('sel_mode', models.CharField(max_length=30, verbose_name='教学形式')),
                ('sel_period', models.IntegerField(verbose_name='学时')),
                ('sel_credit', models.FloatField(verbose_name='学分')),
                ('sel_all_num', models.IntegerField(verbose_name='允许人数')),
                ('sel_num', models.IntegerField(verbose_name='已选人数')),
                ('sel_test_time', models.DateTimeField(blank=True, null=True, verbose_name='考试开始时间')),
                ('sel_all_time', models.IntegerField(blank=True, null=True, verbose_name='考试时长')),
                ('sel_place', models.CharField(blank=True, max_length=100, null=True, verbose_name='考试地点')),
            ],
            options={
                'verbose_name': '选课表',
                'verbose_name_plural': '选课表',
                'db_table': 'sel_course',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=30, verbose_name='学号')),
                ('stu_name', models.CharField(max_length=30, verbose_name='姓名')),
                ('stu_password', models.CharField(blank=True, max_length=40, null=True, verbose_name='密码')),
                ('stu_sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=30, verbose_name='性别')),
                ('stu_department', models.CharField(max_length=40, verbose_name='院系')),
                ('stu_major', models.CharField(max_length=30, verbose_name='专业')),
                ('stu_grade', models.CharField(max_length=30, verbose_name='年纪')),
                ('stu_class', models.CharField(max_length=30, verbose_name='班级')),
                ('stu_email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '学生表',
                'verbose_name_plural': '学生表',
                'db_table': 'student',
            },
        ),
    ]
