from django.urls import path
from .views import (InstructorList,
                    InstructorDetailView,
                    InstructorCreate, InstructorUpdate, InstructorDelete,
                    SectionList,
                    SectionDetailView,
                    SectionCreate, SectionUpdate, SectionDelete,
                    CourseList,
                    CourseDetailView,
                    CourseCreate, CourseUpdate, CourseDelete,
                    SemesterList,
                    SemesterDetailView,
                    SemesterCreate, SemesterUpdate, SemesterDelete,
                    StudentList,
                    StudentDetailView,
                    StudentCreate, StudentUpdate, StudentDelete,
                    Courseinfo)

app_name = 'courseinfo'
urlpatterns = [
    path('', Courseinfo.as_view(), name='courseinfo_home'),

    path('instructor/', InstructorList.as_view(), name='instructor_list'),

    path('instructor/create/', InstructorCreate.as_view(), name='instructor_create'),

    path('instructor/<slug>/remove/', InstructorDelete.as_view(), name='instructor_remove'),

    path('instructor/<slug>/update/', InstructorUpdate.as_view(), name='instructor_update'),

    path('instructor/<slug>/', InstructorDetailView.as_view(), name='instructor_detail'),

    path('section/', SectionList.as_view(), name='section_list'),

    path('section/create/', SectionCreate.as_view(), name='section_create'),

    path('section/<slug>/remove/', SectionDelete.as_view(), name='section_remove'),

    path('section/<slug>/update/', SectionUpdate.as_view(), name='section_update'),

    path('section/<slug>/', SectionDetailView.as_view(), name='section_detail'),

    path('course/', CourseList.as_view(), name='course_list'),

    path('course/create/', CourseCreate.as_view(), name='course_create'),

    path('course/<slug>/remove/', CourseDelete.as_view(), name='course_remove'),

    path('course/<slug>/update/', CourseUpdate.as_view(), name='course_update'),

    path('course/<slug>/', CourseDetailView.as_view(), name='course_detail'),

    path('semester/', SemesterList.as_view(), name='semester_list'),

    path('semester/create/', SemesterCreate.as_view(), name='semester_create'),

    path('semester/<slug>/remove/', SemesterDelete.as_view(), name='semester_remove'),

    path('semester/<slug>/update/', SemesterUpdate.as_view(), name='semester_update'),

    path('semester/<slug>/', SemesterDetailView.as_view(), name='semester_detail'),

    path('student/', StudentList.as_view(), name='student_list'),

    path('student/create/', StudentCreate.as_view(), name='student_create'),

    path('student/<slug>/remove/', StudentDelete.as_view(), name='student_remove'),

    path('student/<slug>/update/', StudentUpdate.as_view(), name='student_update'),

    path('student/<slug>/', StudentDetailView.as_view(), name='student_detail'),
]
