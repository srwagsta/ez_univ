from django.urls import path
from .views import (InstructorList,
                    InstructorDetailView,
                    SectionList,
                    CourseList,
                    SemesterList,
                    StudentList,
                    Courseinfo)

app_name = 'courseinfo'
urlpatterns = [
    path('information/', Courseinfo.as_view(), name='courseinfo_home'),

    path('instructor/', InstructorList.as_view(), name='instructor_list'),

    path('instructor/<pk>', InstructorDetailView.as_view(), name='instructor-detail'),

    path('section/', SectionList.as_view(), name='section_list'),

    path('course/', CourseList.as_view(), name='course_list'),

    path('semester/', SemesterList.as_view(), name='semester_list'),

    path('student/', StudentList.as_view(), name='student_list'),
]
