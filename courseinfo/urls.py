from django.conf.urls import url
from .views import (instructor_list_view,
                    section_list_view,
                    course_list_view,
                    semester_list_view,
                    student_list_view,
                    courseinfo_home_view)

app_name = 'courseinfo'
urlpatterns = [
    url(regex=r'^courseinfo/',
        view=courseinfo_home_view,
        name='courseinfo_home'
        ),

    url(regex=r'^instructor/',
        view=instructor_list_view,
        name='instructor_list'
        ),

    url(regex=r'^section/',
        view=section_list_view,
        name='section_list'
        ),

    url(regex=r'^course/',
        view=course_list_view,
        name='course_list'
        ),

    url(regex=r'^semester/',
        view=semester_list_view,
        name='semester_list'
        ),

    url(regex=r'^student/',
        view=student_list_view,
        name='student_list'
        ),
]
