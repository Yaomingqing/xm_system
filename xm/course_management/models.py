# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# GENDER_CHOICES = (
#         (0, u'男'),
#         (1, u'女'),
#         )


class Sel_course(models.Model):
    stu_id = models.CharField(max_length=30, verbose_name=u'学号')
    sel_cour_seme = models.CharField(max_length=50, verbose_name=u'学期')
    sel_cour_id = models.CharField(max_length=60, verbose_name=u'课程编号')
    sel_cour_name = models.CharField(max_length=40, verbose_name=u'课程名称')
    sel_teac_name = models.CharField(max_length=50, verbose_name=u'主讲教师')
    sel_class = models.CharField(max_length=40, verbose_name=u'教学班')
    sel_mode = models.CharField(max_length=30, verbose_name=u'教学形式')
    sel_period = models.IntegerField(verbose_name=u'学时')
    sel_credit = models.FloatField(verbose_name='学分')
    sel_all_num = models.IntegerField(verbose_name=u'允许人数')
    sel_num = models.IntegerField(verbose_name=u'已选人数')
    sel_test_time = models.DateTimeField(verbose_name=u'考试开始时间', null=True, blank=True)
    sel_all_time = models.IntegerField(verbose_name=u'考试时长', null=True, blank=True)
    sel_place = models.CharField(max_length=100, verbose_name=u'考试地点', null=True, blank=True)

    class Meta:
        verbose_name = u'选课表'
        verbose_name_plural = u'选课表'
        db_table = 'sel_course'

    def __unicode__(self):
        return self.stu_id

    def __str__(self):
        return self.stu_id


class Score(models.Model):
    stu_id = models.CharField(max_length=30, verbose_name=u'学号')
    stu_name = models.CharField(max_length=30, verbose_name=u'姓名')
    stu_major = models.CharField(max_length=40, verbose_name=u'专业')
    stu_grade = models.CharField(max_length=30, verbose_name=u'年级')
    stu_class = models.CharField(max_length=30, verbose_name=u'班级')
    sel_cour_id = models.CharField(max_length=60, verbose_name=u'课程编号')
    sel_cour_name = models.CharField(max_length=40, verbose_name=u'课程名称')
    atte = models.IntegerField(verbose_name=u'考勤')
    expe = models.IntegerField(verbose_name=u'实验')
    task = models.IntegerField(verbose_name=u'作业')
    class_per = models.IntegerField(verbose_name=u'课堂表现')
    us_scor = models.IntegerField(verbose_name=u'平时成绩')
    first_ques = models.IntegerField(verbose_name=u'第一大题')
    seco_ques = models.IntegerField(verbose_name=u'第二大题')
    third_ques = models.IntegerField(verbose_name=u'第三大题')
    four_ques = models.IntegerField(verbose_name=u'第四大题')
    exam_score = models.IntegerField(verbose_name=u'考试成绩')
    tota_score = models.IntegerField(verbose_name=u'总评成绩')

    class Meta:
        verbose_name = u'成绩表'
        verbose_name_plural = u'成绩表'
        db_table = 'score'

    def __unicode__(self):
        return self.stu_name

    def __str__(self):
        return self.stu_name


class Class(models.Model):
    spec = models.CharField(max_length=50, verbose_name=u'专业简称', null=True, blank=True)
    stu_grade = models.CharField(max_length=30, verbose_name=u'年级')
    stu_class = models.CharField(max_length=30, verbose_name=u'班级')
    ctype = models.CharField(max_length=40, verbose_name=u'课程类型')
    sel_cour_id = models.CharField(max_length=40, verbose_name=u'课程编号')
    sel_cour_name = models.CharField(max_length=40, verbose_name=u'课程名称')
    tea_id = models.CharField(max_length=30, verbose_name=u'教工号')
    sel_teac_name = models.CharField(max_length=30, verbose_name=u'主讲教师')
    credit = models.FloatField(verbose_name=u'学分')
    cour_character = models.CharField(max_length=40, verbose_name=u'课程性质')
    tea_mode = models.CharField(max_length=40, verbose_name=u'教学形式')
    tes_category = models.CharField(max_length=20, verbose_name=u'考试类别')
    total_hours = models.IntegerField(verbose_name=u'总学时')
    teach = models.IntegerField(verbose_name=u'讲授')
    experiment = models.IntegerField(verbose_name=u'实验')
    practise = models.IntegerField(verbose_name=u'实习')
    operate = models.IntegerField(verbose_name=u'上机')
    department = models.CharField(max_length=40, verbose_name=u'主管单位', null=True, blank=True)
    semester = models.CharField(max_length=30, verbose_name=u'适用学期', null=True, blank=True)

    class Meta:
        verbose_name = u'课程表'
        verbose_name_plural = u'课程表'
        db_table = 'class'

    def __unicode__(self):
        return self.sel_cour_name

    def __str__(self):
        return self.sel_cour_name


class Student(models.Model):
    stu_id = models.CharField(max_length=30, verbose_name=u'学号')
    stu_name = models.CharField(max_length=30, verbose_name=u'姓名')
    stu_password = models.CharField(max_length=40, verbose_name=u'密码', null=True, blank=True)
    # stu_sex = models.BooleanField(default=True, verbose_name=u'性别')
    stu_sex = models.CharField(max_length=30, choices=(('male', '男'), ('female', '女')), default='male',
                              verbose_name=u'性别')
    # stu_sex = models.IntegerField(verbose_name=u'性别', choices=GENDER_CHOICES)
    stu_department = models.CharField(max_length=40, verbose_name=u'院系')
    stu_major = models.CharField(max_length=30, verbose_name=u'专业')
    stu_grade = models.CharField(max_length=30, verbose_name=u'年纪')
    stu_class = models.CharField(max_length=30, verbose_name=u'班级')
    stu_email = models.EmailField(verbose_name=u'邮箱')
    isDelete = models.BooleanField(default=False, verbose_name=u'是否删除')

    class Meta:
        verbose_name = u'学生表'
        verbose_name_plural = u'学生表'
        db_table = 'student'

    def __unicode__(self):
        return self.stu_name

    def __str__(self):
        return self.stu_name


class Course_teacher(models.Model):
    tea_id = models.CharField(max_length=30, verbose_name=u'教工号')
    tea_name = models.CharField(max_length=30, verbose_name=u'姓名')
    tea_password = models.CharField(max_length=40, verbose_name=u'密码', null=True, blank=True)
    # tea_sex = models.BooleanField(default=True, verbose_name=u'性别')
    tea_sex = models.CharField(max_length=30, choices=(('male', '男'), ('female', '女')), default='male',
                               verbose_name='性别')
    # tea_sex = models.IntegerField(verbose_name=u'性别', choices=GENDER_CHOICES)
    tea_department = models.CharField(max_length=40, verbose_name=u'院系')
    tea_title = models.CharField(max_length=20, verbose_name=u'职称')
    tea_email = models.EmailField(verbose_name=u'邮箱')
    isDelete = models.BooleanField(default=False, verbose_name=u'是否删除')

    class Meta:
        verbose_name = u"任课教师表"
        verbose_name_plural = u'任课教师表'
        db_table = 'course_teacher'

    def __unicode__(self):
        return self.tea_name

    def __str__(self):
        return self.tea_name




