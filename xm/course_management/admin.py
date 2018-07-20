from django.contrib import admin

# Register your models here.

from .models import Sel_course, Score, Class, Student, Course_teacher


class Sel_courseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'stu_id', 'sel_cour_seme', 'sel_cour_id',  'sel_cour_name',
                    'sel_teac_name', 'sel_class', 'sel_mode', 'sel_period', 'sel_credit',
                    'sel_all_num', 'sel_num', 'sel_test_time', 'sel_all_time', 'sel_place']
    list_filter = ['sel_cour_seme', 'sel_cour_name', 'sel_class', 'sel_teac_name', 'sel_place']
    search_fields = ['stu_id', 'sel_cour_seme', 'sel_cour_name', 'sel_class', 'sel_teac_name', 'sel_place']
    list_per_page = 20

    fieldsets = [
        ("BASIC", {"fields": ['stu_id', 'sel_cour_seme', 'sel_cour_id',  'sel_cour_name',
                              'sel_teac_name', 'sel_class', 'sel_mode']}),
        ("DETAILS", {"fields": ['sel_period', 'sel_credit', 'sel_all_num', 'sel_num',
                                'sel_test_time', 'sel_all_time', 'sel_place']})
    ]

    actions_on_top = False
    actions_on_bottom = True


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'stu_id', 'stu_name', 'stu_major', 'stu_grade', 'stu_class', 'sel_cour_id', 'sel_cour_name',
                    'atte', 'expe', 'task', 'class_per', 'us_scor', 'first_ques', 'seco_ques', 'third_ques', 'four_ques',
                    'exam_score', 'tota_score']
    list_filter = ['stu_major', 'stu_grade', 'stu_class', 'sel_cour_name']
    search_fields = ['stu_id', 'stu_name', 'stu_major', 'stu_grade', 'stu_class', 'sel_cour_name']
    list_per_page = 20

    fieldsets = [
        ("BASIC", {"fields": ['stu_id', 'stu_name', 'stu_major', 'stu_grade', 'stu_class', 'sel_cour_id', 'sel_cour_name']}),
        ("USUAL PERFORMANCE", {"fields": ['atte', 'expe', 'task', 'class_per', 'us_scor']}),
        ("EXAMINATION", {"fields": ['first_ques', 'seco_ques', 'third_ques', 'four_ques', 'exam_score', 'tota_score']})
    ]

    actions_on_top = False
    actions_on_bottom = True


class ClassAdmin(admin.ModelAdmin):
    list_display = ['pk', 'spec', 'stu_grade', 'stu_class', 'ctype', 'sel_cour_id', 'sel_cour_name', 'tea_id',
                    'sel_teac_name', 'credit', 'cour_character', 'tea_mode', 'tes_category', 'total_hours',
                    'teach', 'experiment', 'practise', 'operate', 'department', 'semester']
    list_filter = ['spec', 'stu_grade', 'stu_class', 'ctype',  'sel_cour_name', 'sel_teac_name', 'cour_character',
                   'tea_mode', 'tes_category', 'department', 'semester']
    search_fields = ['spec', 'stu_grade', 'stu_class', 'ctype', 'sel_cour_id', 'sel_cour_name', 'tea_id',
                    'sel_teac_name', 'cour_character', 'tea_mode', 'tes_category', 'department', 'semester']
    list_per_page = 20

    fieldsets = [
        ("BASIC", {"fields": ['spec', 'stu_grade', 'stu_class', 'ctype', 'sel_cour_id', 'sel_cour_name', 'tea_id',
                    'sel_teac_name']}),
        ("DETAILS", {"fields": ['credit', 'cour_character', 'tea_mode', 'tes_category', 'total_hours',
                    'teach', 'experiment', 'practise', 'operate', 'department', 'semester']})
    ]
    actions_on_top = False
    actions_on_bottom = True


class StudentAdmin(admin.ModelAdmin):
    # def gender(self):
    #     if self.stu_sex:
    #         return '男'
    #     else:
    #         return '女'
    list_display = ['pk', 'stu_id', 'stu_name', 'stu_sex', 'stu_department', 'stu_major', 'stu_grade', 'stu_class',
                    'stu_email']
    list_filter = ['stu_sex', 'stu_department', 'stu_major', 'stu_grade', 'stu_class']
    search_fields = ['stu_sex', 'stu_department', 'stu_major', 'stu_grade', 'stu_class']
    list_per_page = 20
    actions_on_top = False
    actions_on_bottom = True


class Course_teacherAdmin(admin.ModelAdmin):
    # def gender(self):
    #     if self.tea_sex:
    #         return '男'
    #     else:
    #         return '女'
    list_display = ['pk', 'tea_id', 'tea_name', 'tea_sex', 'tea_department', 'tea_title', 'tea_email']
    list_filter = ['tea_name', 'tea_sex', 'tea_department', 'tea_title']
    search_fields = ['tea_name', 'tea_sex', 'tea_department', 'tea_title']
    list_per_page = 20
    actions_on_top = False
    actions_on_bottom = True


admin.site.register(Sel_course, Sel_courseAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course_teacher, Course_teacherAdmin)

# admin.site.register(Sel_course)
# admin.site.register(Score)
# admin.site.register(Class)
# admin.site.register(Student)
# admin.site.register(Course_teacher)