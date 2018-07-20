from django.conf.urls import url

from . import views
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'getlogin', views.getlogin),
    url(r'xspscj2/(\d+)', views.xspscj2, name='xspscj2'),
    url(r'xskscj2/(\d+)', views.xskscj2, name='xskscj2'),
    url(r'xszpcj2/(\d+)', views.xszpcj2, name='xszpcj2'),
    url(r'xsxkxx2/(\d+)', views.xsxkxx2, name='xsxkxx2'),
    # student
    url(r'xskscj/(\d+)', views.xskscj, name='xskscj'),
    url(r'xspscj/(\d+)', views.xspscj, name='xspscj'),
    url(r'xsxkxx/(\d+)', views.xsxkxx, name='xsxkxx'),
    url(r'xszpcj/(\d+)', views.xszpcj, name='xszpcj'),
    # teacher
    url(r'teach_info/([A-Za-z0-9]+)', views.teach_info, name='teach_info'),
    url(r'stu_info/([A-Za-z0-9]+)', views.stu_info, name='stu_info'),
    url(r'usual_score/([A-Za-z0-9]+)', views.usual_score, name='usual_score'),
    url(r'exam_score/([A-Za-z0-9]+)', views.exam_score, name='exam_score'),
    url(r'score_search/([A-Za-z0-9]+)', views.score_search, name='score_search'),
    url(r'teach_info2/([A-Za-z0-9]+)', views.teach_info2, name='teach_info2'),
    url(r'stu_info2/([A-Za-z0-9]+)', views.stu_info2, name='stu_info2'),
    url(r'usual_score2/([A-Za-z0-9]+)', views.usual_score2, name='usual_score2'),
    url(r'usual_score3/([A-Za-z0-9]+)', views.usual_score3, name='usual_score3'),
    url(r'exam_score2/([A-Za-z0-9]+)', views.exam_score2, name='exam_score2'),
    url(r'exam_score3/([A-Za-z0-9]+)', views.exam_score3, name='exam_score3'),
    url(r'score_search2/([A-Za-z0-9]+)', views.score_search2, name='score_search2'),

]