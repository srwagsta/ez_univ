from django.urls import path
from .views import (InstructorList,
                    InstructorDetailView,
                    SectionList,
                    SectionDetailView,
                    CourseList,
                    CourseDetailView,
                    SemesterList,
                    SemesterDetailView,
                    StudentList,
                    StudentDetailView,
                    Courseinfo)

app_name = 'courseinfo'
urlpatterns = [
    path('information/', Courseinfo.as_view(), name='courseinfo_home'),

    path('instructor/', InstructorList.as_view(), name='instructor_list'),

    path('instructor/<slug>', InstructorDetailView.as_view(), name='instructor_detail'),

    path('section/', SectionList.as_view(), name='section_list'),

    path('section/<slug>', SectionDetailView.as_view(), name='section_detail'),

    path('course/', CourseList.as_view(), name='course_list'),

    path('course/<slug>', CourseDetailView.as_view(), name='course_detail'),

    path('semester/', SemesterList.as_view(), name='semester_list'),

    path('semester/<slug>', SemesterDetailView.as_view(), name='semester_detail'),

    path('student/', StudentList.as_view(), name='student_list'),

    path('student/<slug>', StudentDetailView.as_view(), name='student_detail'),
]
