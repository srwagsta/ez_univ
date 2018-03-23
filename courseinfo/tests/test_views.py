from django.test import RequestFactory
from test_plus.test import TestCase
from ..views import (
    Courseinfo,
    InstructorCreate, InstructorList, InstructorUpdate, InstructorDelete, InstructorDetailView,
    StudentCreate, StudentList, StudentUpdate, StudentDelete, StudentDetailView,
    SectionCreate, SectionList, SectionUpdate, SectionDelete, SectionDetailView,
    SemesterCreate, SemesterList, SemesterUpdate, SemesterDelete, SemesterDetailView,
    CourseCreate, CourseList, CourseUpdate, CourseDelete, CourseDetailView
)


class BaseCourseinfoTestCase(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()


class TestCourseinfoView(BaseCourseinfoTestCase):
    def test_get_url(self):
        view = Courseinfo()
        request = self.factory.get('/courseinfo/')
        request.user = self.user
        view.request = request
        self.assertEqual(view.get_template_names()[0], 'courseinfo/courseinfo_base.html')
