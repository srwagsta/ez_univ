from django.test import TestCase
from django.urls import resolve, reverse


class CourseInfoTest(TestCase):
    """ Test URL resolves for CurseInfo app base pages"""
    def test_course_home_reverse(self):
        """/courseinfo/ should reverse to courseinfo:course_home"""
        self.assertEquals(reverse('courseinfo:courseinfo_home'),
                          '/courseinfo/')

    def test_course_home_resolve(self):
        """courseinfo:course_home should resolve to /courseinfo/"""
        self.assertEquals(resolve('/courseinfo/').view_name,
                          'courseinfo:courseinfo_home')


class TestInstructorURLs(TestCase):
    """ Test URL resolves for CurseInfo app instructor pages"""
    def test_instructor_reverse(self):
        """/courseinfo/instructor/ should reverse to courseinfo:instructor_list"""
        self.assertEquals(reverse('courseinfo:instructor_list'),
                          '/courseinfo/instructor/')

    def test_instructor_resolve(self):
        """courseinfo:instructor_list should resolve to /courseinfo/instructor/"""
        self.assertEquals(resolve('/courseinfo/instructor/').view_name,
                          'courseinfo:instructor_list')

    def test_instructor_detail_reverse(self):
        """/courseinfo/instructor/instructor_slug/ should reverse to courseinfo:instructor_detail"""
        self.assertEquals(reverse('courseinfo:instructor_detail', kwargs={'slug': 'instructor-slug'}),
                          '/courseinfo/instructor/instructor-slug/')

    def test_instructor_detail_resolve(self):
        """courseinfo:instructor_detail should resolve to /courseinfo/instructor/instructor-slug/"""
        self.assertEquals(resolve('/courseinfo/instructor/instructor-slug/').view_name,
                          'courseinfo:instructor_detail')


class TestSectionURLs(TestCase):
    """ Test URL resolves for CurseInfo app section pages"""
    def test_section_reverse(self):
        """/courseinfo/section/ should reverse to courseinfo:section_list"""
        self.assertEquals(reverse('courseinfo:section_list'),
                          '/courseinfo/section/')

    def test_section_resolve(self):
        """courseinfo:section_list should resolve to /courseinfo/section/"""
        self.assertEquals(resolve('/courseinfo/section/').view_name,
                          'courseinfo:section_list')

    def test_section_detail_reverse(self):
        """/courseinfo/section/section-slug/ should reverse to courseinfo:section_detail"""
        self.assertEquals(reverse('courseinfo:section_detail', kwargs={'slug': 'section-slug'}),
                          '/courseinfo/section/section-slug/')

    def test_section_detail_resolve(self):
        """courseinfo:section_detail should resolve to /courseinfo/section/section-slug/"""
        self.assertEquals(resolve('/courseinfo/section/section-slug/').view_name,
                          'courseinfo:section_detail')


class TestCourseURLs(TestCase):
    """ Test URL resolves for CurseInfo app coursepages"""
    def test_course_reverse(self):
        """/courseinfo/course/ should reverse to courseinfo:course_list"""
        self.assertEquals(reverse('courseinfo:course_list'),
                          '/courseinfo/course/')

    def test_course_resolve(self):
        """courseinfo:course_list should resolve to /courseinfo/course/"""
        self.assertEquals(resolve('/courseinfo/course/').view_name,
                          'courseinfo:course_list')

    def test_course_detail_reverse(self):
        """/courseinfo/course/course-slug/ should reverse to courseinfo:course_detail"""
        self.assertEquals(reverse('courseinfo:course_detail', kwargs={'slug': 'course-slug'}),
                          '/courseinfo/course/course-slug/')

    def test_course_detail_resolve(self):
        """courseinfo:course_detail should resolve to /courseinfo/course/course-slug/"""
        self.assertEquals(resolve('/courseinfo/course/course-slug/').view_name,
                          'courseinfo:course_detail')


class TestSemesterURLs(TestCase):
    """ Test URL resolves for CurseInfo app semester pages"""
    def test_semester_reverse(self):
        """/courseinfo/semester/ should reverse to courseinfo:semester_list"""
        self.assertEquals(reverse('courseinfo:semester_list'),
                          '/courseinfo/semester/')

    def test_semester_resolve(self):
        """courseinfo:semester_list should resolve to /courseinfo/semester/"""
        self.assertEquals(resolve('/courseinfo/semester/').view_name,
                          'courseinfo:semester_list')

    def test_semester_detail_reverse(self):
        """/courseinfo/semester/semester-slug/ should reverse to courseinfo:semester_detail"""
        self.assertEquals(reverse('courseinfo:semester_detail', kwargs={'slug': 'semester-slug'}),
                          '/courseinfo/semester/semester-slug/')

    def test_semester_detail_resolve(self):
        """courseinfo:semester_detail should resolve to /courseinfo/semester/semester-slug/"""
        self.assertEquals(resolve('/courseinfo/semester/semester-slug/').view_name,
                          'courseinfo:semester_detail')


class TestStudentURLs(TestCase):
    """ Test URL resolves for CurseInfo app student pages"""
    def test_student_reverse(self):
        """/courseinfo/student/ should reverse to courseinfo:student_list"""
        self.assertEquals(reverse('courseinfo:student_list'),
                          '/courseinfo/student/')

    def test_student_resolve(self):
        """courseinfo:student_list should resolve to /courseinfo/student/"""
        self.assertEquals(resolve('/courseinfo/student/').view_name,
                          'courseinfo:student_list')

    def test_student_detail_reverse(self):
        """/courseinfo/student/student-slug/ should reverse to courseinfo:student_detail"""
        self.assertEquals(reverse('courseinfo:student_detail', kwargs={'slug': 'student-slug'}),
                          '/courseinfo/student/student-slug/')

    def test_student_detail_resolve(self):
        """courseinfo:student_detail should resolve to /courseinfo/student/student-slug/"""
        self.assertEquals(resolve('/courseinfo/student/student-slug/').view_name,
                          'courseinfo:student_detail')
