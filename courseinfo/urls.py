from django.conf.urls import url
from .views import (InstructorList,
                    SectionList,
                    CourseList,
                    SemesterList,
                    StudentList,
                    courseinfo_home_view)

app_name = 'courseinfo'
urlpatterns = [
    url(regex=r'^information/',
        view=courseinfo_home_view,
        name='courseinfo_home'
        ),

    url(regex=r'^instructor/',
        view=InstructorList.as_view(),
        name='instructor_list'
        ),

    url(regex=r'^section/',
        view=SectionList.as_view(),
        name='section_list'
        ),

    url(regex=r'^course/',
        view=CourseList.as_view(),
        name='course_list'
        ),

    url(regex=r'^semester/',
        view=SemesterList.as_view(),
        name='semester_list'
        ),

    url(regex=r'^student/',
        view=StudentList.as_view(),
        name='student_list'
        ),
]
