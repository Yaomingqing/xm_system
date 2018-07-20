from django.shortcuts import render
from .models import Sel_course, Score, Class, Student, Course_teacher
from django.http import HttpResponseRedirect, HttpResponse
import numpy as np
from django.contrib import admin
from django.shortcuts import render_to_response
# Create your views here.


def index(request):
    return render(request, 'course_management/login.html')


def xskscj(request, stuid):
    stu = Student.objects.get(stu_id=stuid)
    performance = Score.objects.filter(stu_id=stuid)
    selcourse = Sel_course.objects.filter(stu_id=stuid)
    semester = []
    for semes in selcourse:
        if semes.sel_cour_seme not in semester:
            semester.append(semes.sel_cour_seme)
    return render(request, 'stu/xskscj.html', {'stu': stu, 'performance': performance, 'semester': semester})
def xskscj2(request, stuid):
    stu = Student.objects.get(stu_id=stuid)
    # performance = Score.objects.filter(stu_id=stuid)
    seme = request.GET.get('select')
    sel = Sel_course.objects.filter(stu_id=stuid, sel_cour_seme=seme)
    select = []
    for it in sel:
        id = it.sel_cour_id
        # print(id)
        select.append(id)
    # print(select)
    performance = Score.objects.filter(stu_id=stuid, sel_cour_id__in=select)
    selcourse = Sel_course.objects.filter(stu_id=stuid)
    semester = []
    for semes in selcourse:
        if semes.sel_cour_seme not in semester:
            semester.append(semes.sel_cour_seme)
    return render(request, 'stu/xskscj.html', {'stu': stu, 'performance': performance, 'semester': semester})


def xspscj(request, stuid):
    stu = Student.objects.get(stu_id=stuid)
    performance = Score.objects.filter(stu_id=stuid)
    selcourse = Sel_course.objects.filter(stu_id=stuid)
    semester = []
    for semes in selcourse:
        if semes.sel_cour_seme not in semester:
            semester.append(semes.sel_cour_seme)
    return render(request, 'stu/xspscj.html', {'stu': stu, 'performance': performance, 'semester': semester})

def xspscj2(request, stuid):
    stu = Student.objects.get(stu_id=stuid)
    seme = request.GET.get('select')
    # print(seme)
    sel = Sel_course.objects.filter(stu_id=stuid, sel_cour_seme=seme)
    # print(sel)
    select = []
    for it in sel:
        id = it.sel_cour_id
        print(id)
        select.append(id)
    print(select)
    performance = Score.objects.filter(stu_id=stuid, sel_cour_id__in=select)
    # performance = Score.objects.filter(stu_id=stuid)
    selcourse = Sel_course.objects.filter(stu_id=stuid)
    semester = []
    for semes in selcourse:
        if semes.sel_cour_seme not in semester:
            semester.append(semes.sel_cour_seme)
    return render(request, 'stu/xspscj.html', {'stu': stu, 'performance': performance, 'semester': semester})

def xsxkxx(request, stuid):
    stu = Student.objects.get(stu_id=stuid)
    selcourse = Sel_course.objects.filter(stu_id=stuid)
    semester = []
    for semes in selcourse:
        if semes.sel_cour_seme not in semester:
            semester.append(semes.sel_cour_seme)

    return render(request, 'stu/xsxkxx.html', {'stu': stu, 'selcourse': selcourse, 'semester': semester})

def xsxkxx2(request, stuid):
    stu = Student.objects.get(stu_id=stuid)
    seme = request.GET.get('select')
    selcourse = Sel_course.objects.filter(stu_id=stuid, sel_cour_seme=seme)
    selcourses = Sel_course.objects.filter(stu_id=stuid)
    semester = []
    for semes in selcourses:
        if semes.sel_cour_seme not in semester:
            semester.append(semes.sel_cour_seme)

    return render(request, 'stu/xsxkxx.html', {'stu': stu, 'selcourse': selcourse, 'semester': semester})

def xszpcj(request, stuid):
    stu = Student.objects.get(stu_id=stuid)
    performance = Score.objects.filter(stu_id=stuid)
    avg_scores=[]
    for scores in performance:
        avg_scores.append(scores.tota_score)
    avg = np.mean(avg_scores)
    selcourse = Sel_course.objects.filter(stu_id=stuid)
    semester = []
    credits = 0
    for semes in selcourse:
        credits += semes.sel_credit
        if semes.sel_cour_seme not in semester:
            semester.append(semes.sel_cour_seme)
    return render(request, 'stu/xszpcj.html', {'stu': stu, 'performance': performance, 'semester': semester,
                                               'avg': avg, 'credits': credits})

def xszpcj2(request, stuid):
    stu = Student.objects.get(stu_id=stuid)
    seme = request.GET.get('select')
    # print(seme)
    sel = Sel_course.objects.filter(stu_id=stuid, sel_cour_seme=seme)
    # print(sel)
    select = []
    for it in sel:
        id = it.sel_cour_id
        print(id)
        select.append(id)
    print(select)
    performance = Score.objects.filter(stu_id=stuid, sel_cour_id__in=select)
    avg_scores=[]
    for scores in performance:
        avg_scores.append(scores.tota_score)
    avg = np.mean(avg_scores)
    credit = Sel_course.objects.filter(stu_id=stuid, sel_cour_id__in=select)
    credits = 0
    for se in credit:
        credits += se.sel_credit
    selcourse = Sel_course.objects.filter(stu_id=stuid)
    semester = []

    for semes in selcourse:
        if semes.sel_cour_seme not in semester:
            semester.append(semes.sel_cour_seme)
    return render(request, 'stu/xszpcj.html', {'stu': stu, 'performance': performance, 'semester': semester,
                                               'avg': avg, 'credits': credits})

def getlogin(request):
    choice = request.POST.get("fruit")
    userid = request.POST.get("Username", None)
    ps = request.POST.get("Password", None)

    print(choice)
    print(userid)
    print(ps)

    if choice == "3":
        return HttpResponseRedirect("/admin")
    elif choice == '1':
        try:
            s = Student.objects.get(stu_id=userid)
            if s.stu_password != ps:
                return HttpResponseRedirect("/")
        except Student.DoesNotExist:
            return HttpResponseRedirect("/")
        # stu = Student.objects.filter(stu_id=s)
        scores = Score.objects.filter(stu_id=userid)
        sel_course = Sel_course.objects.filter(stu_id=userid)
        print(scores)
        print(sel_course)
        print(s)
        return render(request, "stu/stu_index.html", {'stu': s})

    else:
        try:
            t = Course_teacher.objects.get(tea_id=userid)
            if t.tea_password != ps:
                return HttpResponseRedirect("/")
        except Course_teacher.DoesNotExist:
            return HttpResponseRedirect("/")
        teacher = Course_teacher.objects.get(tea_id=userid)

        return render(request, "teacher/teach_home.html", {"teacher": teacher})


def teach_info(request, teaid):
    teacher = Course_teacher.objects.get(tea_id=teaid)
    course_info = Class.objects.filter(tea_id=teaid)
    semes = Class.objects.all()
    semester = []
    classes = []
    for se in semes:
        if se.semester not in semester:
            semester.append(se.semester)
        if se.stu_class not in classes:
            classes.append(se.stu_class)
    return render(request, 'teacher/course-info.html', {"teacher": teacher, 'course_info': course_info,
                                                        'semester':semester, 'classes':classes})

def teach_info2(request, teaid):
    semes = Class.objects.all()
    semester = []
    classes = []
    for se in semes:
        if se.semester not in semester:
            semester.append(se.semester)
        if se.stu_class not in classes:
            classes.append(se.stu_class)

    teacher = Course_teacher.objects.get(tea_id=teaid)
    # course_info = Class.objects.filter(tea_id=teaid)

    cname = request.GET.get('cname',None)
    seme = request.GET.get('seme')
    cla = request.GET.get('class')
    print(teaid, cname, seme, cla, type(cname))
    if cname:
        if seme and seme != '请选择学期':
            if cla and cla != '请选择班级':
                classname = cla
                if cla == '信管151/152':
                    classname = ['信管151', '信管152']
                course_info = Class.objects.filter(tea_id=teaid, sel_cour_name=cname, semester=seme, stu_class__in=classname)
            else:
                course_info = Class.objects.filter(tea_id=teaid, sel_cour_name=cname, semester=seme)
        else:
            if cla and cla != '请选择班级':
                classname = cla
                if cla == '信管151/152':
                    classname = ['信管151', '信管152']
                course_info = Class.objects.filter(tea_id=teaid, sel_cour_name=cname, stu_class__in=classname)
            else:
                course_info = Class.objects.filter(tea_id=teaid, sel_cour_name=cname)
    else:
        if seme and seme != '请选择学期':
            if cla and cla != '请选择班级':
                classname = cla
                if cla == '信管151/152':
                    classname = ['信管151', '信管152']
                course_info = Class.objects.filter(tea_id=teaid, semester=seme, stu_class__in=classname)
            else:
                course_info = Class.objects.filter(tea_id=teaid,  semester=seme)
        else:
            if cla and cla != '请选择班级':
                course_info = Class.objects.filter(tea_id=teaid, stu_class=cla)
            else:
                course_info = Class.objects.filter(tea_id=teaid)

    if cname == '' and seme == u'请选择学期' and cla == u'请选择班级':
        course_info = Class.objects.filter()

    return render(request, 'teacher/course-info.html', {"teacher": teacher, 'course_info': course_info,
                                                        'semester': semester, 'classes': classes})

def stu_info(request, teaid):
    allstu = Student.objects.all()
    teacher = Course_teacher.objects.get(tea_id=teaid)
    semess = Class.objects.filter(tea_id=teaid)
    names = []
    for se in semess:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)
    semes = Sel_course.objects.all()
    semester = []
    classes = []
    for se in semes:
        if se.sel_cour_seme not in semester:
            semester.append(se.sel_cour_seme)
        if se.sel_class not in classes:
            classes.append(se.sel_class)

    return render(request, 'teacher/student-info.html', {"teacher": teacher, 'students': allstu,
                                                         'semester': semester, 'classes': classes, 'names': names})

def stu_info2(request, teaid):
    teacher = Course_teacher.objects.get(tea_id=teaid)
    semess = Class.objects.filter(tea_id=teaid)
    names = []
    for se in semess:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)
    semes = Sel_course.objects.all()
    semester = []
    classes = []
    for se in semes:
        if se.sel_cour_seme not in semester:
            semester.append(se.sel_cour_seme)
        if se.sel_class not in classes:
            classes.append(se.sel_class)

    cname = request.GET.get('cname', None)
    seme = request.GET.get('seme')
    cla = request.GET.get('class')

    # allstu = Student.objects.all()
    print(cname, seme, cla)
    if cname and cname != '请选择课程':
        if seme and seme != '请选择学期':
            if cla and cla != '请选择班级':
                classname = cla
                if cla == '信管151/152':
                    classname = ['信管151', '信管152']
                course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name, sel_cour_name=cname,
                                                        sel_cour_seme=seme,  sel_class__in=classname)
                idnumber = []
                for id in course_info:
                    if id.stu_id not in idnumber:
                        idnumber.append(id.stu_id)
                allstu = Student.objects.filter(stu_id__in=idnumber)
                print(allstu)
            else:
                course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name, sel_cour_name=cname,
                                                        sel_cour_seme=seme)
                idnumber = []
                for id in course_info:
                    if id.stu_id not in idnumber:
                        idnumber.append(id.stu_id)
                allstu = Student.objects.filter(stu_id__in=idnumber)
        else:
            if cla and cla != '请选择班级':
                classname = cla
                if cla == '信管151/152':
                    classname = ['信管151', '信管152']
                course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name, sel_cour_name=cname,
                                                        sel_class__in=classname)
                idnumber = []
                for id in course_info:
                    if id.stu_id not in idnumber:
                        idnumber.append(id.stu_id)
                allstu = Student.objects.filter(stu_id__in=idnumber)
            else:
                course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name, sel_cour_name=cname)
                idnumber = []
                for id in course_info:
                    if id.stu_id not in idnumber:
                        idnumber.append(id.stu_id)
                allstu = Student.objects.filter(stu_id__in=idnumber)
    else:
        if seme and seme != '请选择学期':
            if cla and cla != '请选择班级':
                classname = cla
                if cla == '信管151/152':
                    classname = ['信管151', '信管152']
                course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name,
                                                        sel_cour_seme=seme, sel_class__in=classname)
                idnumber = []
                for id in course_info:
                    if id.stu_id not in idnumber:
                        idnumber.append(id.stu_id)
                allstu = Student.objects.filter(stu_id__in=idnumber)
            else:

                course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name,
                                                        sel_cour_seme=seme)
                idnumber = []
                for id in course_info:
                    if id.stu_id not in idnumber:
                        idnumber.append(id.stu_id)
                allstu = Student.objects.filter(stu_id__in=idnumber)
        else:
            if cla and cla != '请选择班级':
                classname = cla
                if cla == '信管151/152':
                    classname = ['信管151', '信管152']
                print(cname, seme, cla)
                course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name,
                                                        sel_class__in=classname)
                idnumber = []
                for id in course_info:
                    if id.stu_id not in idnumber:
                        idnumber.append(id.stu_id)
                print(idnumber)
                allstu = Student.objects.filter(stu_id__in=idnumber)
            else:
                print(cname, seme, cla)
                course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name)
                idnumber = []
                for id in course_info:
                    if id.stu_id not in idnumber:
                        idnumber.append(id.stu_id)
                print(idnumber)

                allstu = Student.objects.filter(stu_id__in=idnumber)
    # allstu = Student.objects.all()

    return render(request, 'teacher/student-info.html', {"teacher": teacher, 'students': allstu,
                                                         'semester': semester, 'classes': classes, 'names': names})


def usual_score(request, teaid):
    teacher = Course_teacher.objects.get(tea_id=teaid)
    semes = Class.objects.filter(tea_id=teaid)
    names = []
    for se in semes:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)

    # course_info = Class.objects.filter(tea_id=teaid)
    course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name)
    idnumber = []
    courses = []
    for id in course_info:
        if id.stu_id not in idnumber:
            idnumber.append(id.stu_id)
        if id.sel_cour_name not in courses:
            courses.append(id.sel_cour_name)
    # print(idnumber)
    allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name__in=courses)
    return render(request, 'teacher/us-score.html', {"teacher": teacher,'names': names, 'allstu':allstu})

def usual_score2(request, teaid):
    semes = Class.objects.filter(tea_id=teaid)
    names = []
    for se in semes:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)
    teacher = Course_teacher.objects.get(tea_id=teaid)
    # course_info = Class.objects.filter(tea_id=teaid)
    course = request.GET.get('cname')
    course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name)
    idnumber = []
    courses = []
    for id in course_info:
        if id.stu_id not in idnumber:
            idnumber.append(id.stu_id)
        if id.sel_cour_name not in courses:
            courses.append(id.sel_cour_name)
    # print(idnumber)
    allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name__in=courses, sel_cour_name=course)

    return render(request, 'teacher/us-score.html', {"teacher": teacher,'names': names, 'allstu':allstu})

def usual_score3(request, teaid):
    semes = Class.objects.filter(tea_id=teaid)
    names = []
    for se in semes:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)
    teacher = Course_teacher.objects.get(tea_id=teaid)
    # course_info = Class.objects.filter(tea_id=teaid)
    id = request.GET.getlist('id')
    name = request.GET.getlist('name')
    one = request.GET.getlist('one')
    two = request.GET.getlist('two')
    three = request.GET.getlist('three')
    four = request.GET.getlist('four')
    # print(id,name,one,two,three,four)
    for i in range(len(id)):
        stu_scorce = Score.objects.get(stu_id=id[i], sel_cour_name=name[i])
        if one[i] != '':
            stu_scorce.atte = one[i]
        if two[i] != '':
            stu_scorce.expe = two[i]
        if three[i] != '':
            stu_scorce.task = three[i]
        if four[i] != '':
            stu_scorce.class_per = four[i]
        if one[i] != '' and two[i] != '' and three[i] != '' and four[i] != '':
            usscore=int(one[i]) + int(two[i]) + int(three[i]) + int(four[i])
            stu_scorce.us_scor = usscore
            stu_scorce.tota_score = 0.2*usscore + 0.8*stu_scorce.exam_score
        stu_scorce.save()
    # allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name__in=courses, sel_cour_name=course)

    return render(request, 'teacher/us-score.html', {"teacher": teacher,'names': names})

def exam_score(request, teaid):
    teacher = Course_teacher.objects.get(tea_id=teaid)
    semes = Class.objects.filter(tea_id=teaid)
    names = []
    for se in semes:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)

    # course_info = Class.objects.filter(tea_id=teaid)
    course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name)
    idnumber = []
    courses = []
    for id in course_info:
        if id.stu_id not in idnumber:
            idnumber.append(id.stu_id)
        if id.sel_cour_name not in courses:
            courses.append(id.sel_cour_name)
    print(idnumber, courses)
    allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name__in=courses)
    return render(request, 'teacher/exam-score.html', {"teacher": teacher,'names': names, 'allstu':allstu})

def exam_score2(request, teaid):
    semes = Class.objects.filter(tea_id=teaid)
    names = []
    for se in semes:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)
    teacher = Course_teacher.objects.get(tea_id=teaid)
    # course_info = Class.objects.filter(tea_id=teaid)
    course = request.GET.get('cname')
    course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name)
    idnumber = []
    courses = []
    for id in course_info:
        if id.stu_id not in idnumber:
            idnumber.append(id.stu_id)
        if id.sel_cour_name not in courses:
            courses.append(id.sel_cour_name)
    # print(idnumber)
    allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name__in=courses, sel_cour_name=course)
    return render(request, 'teacher/exam-score.html', {"teacher": teacher,'names': names, 'allstu':allstu})

def exam_score3(request, teaid):
    semes = Class.objects.filter(tea_id=teaid)
    names = []
    for se in semes:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)
    teacher = Course_teacher.objects.get(tea_id=teaid)
    # course_info = Class.objects.filter(tea_id=teaid)
    id = request.GET.getlist('id')
    name = request.GET.getlist('name')
    one = request.GET.getlist('one')
    two = request.GET.getlist('two')
    three = request.GET.getlist('three')
    four = request.GET.getlist('four')
    # print(id,name,one,two,three,four)
    for i in range(len(id)):
        stu_scorce = Score.objects.get(stu_id=id[i], sel_cour_name=name[i])
        if one[i] != '':
            stu_scorce.first_ques = one[i]
        if two[i] != '':
            stu_scorce.seco_ques = two[i]
        if three[i] != '':
            stu_scorce.third_ques = three[i]
        if four[i] != '':
            stu_scorce.four_ques = four[i]
        if one[i] != '' and two[i] != '' and three[i] != '' and four[i] != '':
            examscore=int(one[i]) + int(two[i]) + int(three[i]) + int(four[i])
            stu_scorce.exam_score = examscore
            stu_scorce.tota_score = 0.8*examscore + 0.2*stu_scorce.us_scor
        stu_scorce.save()

    return render(request, 'teacher/exam-score.html', {"teacher": teacher,'names': names})


def score_search(request, teaid):
    teacher = Course_teacher.objects.get(tea_id=teaid)
    semes = Class.objects.filter(tea_id=teaid)
    names = []
    classes = []
    for se in semes:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)
        if se.stu_class not in classes:
            classes.append(se.stu_class)

    # course_info = Class.objects.filter(tea_id=teaid)
    course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name)
    idnumber = []
    courses = []
    for id in course_info:
        if id.stu_id not in idnumber:
            idnumber.append(id.stu_id)
        if id.sel_cour_name not in courses:
            courses.append(id.sel_cour_name)
    print(idnumber, courses)
    allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name__in=courses)


    grade_order=[]
    return render(request, 'teacher/select-score.html', {"teacher": teacher,'names': names, 'allstu':allstu,
                                                         'classes':classes, })

def score_search2(request, teaid):
    semes = Class.objects.filter(tea_id=teaid)
    names = []
    classes = []
    for se in semes:
        if se.sel_cour_name not in names:
            names.append(se.sel_cour_name)
        if se.stu_class not in classes:
            classes.append(se.stu_class)
    teacher = Course_teacher.objects.get(tea_id=teaid)
    cname = request.GET.get('cname')
    cla = request.GET.get('class')

    course_info = Sel_course.objects.filter(sel_teac_name=teacher.tea_name)
    idnumber = []
    courses = []
    for id in course_info:
        if id.stu_id not in idnumber:
            idnumber.append(id.stu_id)
        if id.sel_cour_name not in courses:
            courses.append(id.sel_cour_name)

    if cname and cname != '请选择授课名称':
        if cla and cla != '请选择授课班级':
            classname = cla
            if cla =='信管151/152':
                classname = ['信管151', '信管152']
            allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name=cname, stu_class__in=classname)
        else:
            allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name=cname)
    else:
        if cla and cla != '请选择授课班级':
            classname=cla
            if cla =='信管151/152':
                classname=['信管151','信管152']
            allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name__in=courses, stu_class__in=classname)
        else:

            allstu = Score.objects.filter(stu_id__in=idnumber, sel_cour_name__in=courses)

    return render(request, 'teacher/select-score.html', {"teacher": teacher,'names': names, 'allstu':allstu,
                                                         'classes':classes, })

def login(request):
    print(request.POST.get("sid", None))

    type = request.POST.get("fruit")
    name = request.POST.get("username", None)
    ps = request.POST.get("password", None)

    if type == "1":

        try:
            s = Student.objects.get(stu_id=name)
            if s.stu_password != ps:
                return HttpResponseRedirect("/")
        except Student.DoesNotExist:
            return HttpResponseRedirect("/")
        idnum = int(str(s.ID_number)[-6:])
        print(idnum)
        print("ps=", ps)
        if idnum == int(ps):
            student = Student.objects.get(s_number=name)
            score = Score.objects.filter(sNum=name)
            print(score[0].sName)
            return render(request, "student.html", {"student": student, "score": score})
        else:
            return HttpResponseRedirect("/")
    elif type == "2":

        try:
            t = Course_teacher.objects.get(t_number=name)
        except Course_teacher.DoesNotExist:
            return HttpResponseRedirect("/")
        tps = t.t_pass
        if tps == int(ps):
            teacher = Course_teacher.objects.get(t_number=name)
            l_num = teacher.t_lesson_id
            score = Score.objects.filter(lNum=l_num)
            return render(request, "teacher.html", {"teacher": teacher, "score": score})
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/admin/")
