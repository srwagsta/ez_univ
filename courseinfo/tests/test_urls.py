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

    def test_instructor_update_reverse(self):
        """courseinfo:instructor_update should reverse to /courseinfo/instructor-slug/update/."""
        self.assertEqual(reverse('courseinfo:instructor_update', kwargs={'slug': 'instructor-slug'}),
                         '/courseinfo/instructor/instructor-slug/update/')

    def test_instructor_update_resolve(self):
        """/courseinfo/instructor-slug/update/ should resolve to courseinfo:instructor_update."""
        self.assertEqual(
            resolve('/courseinfo/instructor/instructor-slug/update/').view_name,
            'courseinfo:instructor_update'
        )

    def test_instructor_remove_reverse(self):
        """courseinfo:instructor_remove should reverse to /courseinfo/instructor-slug/remove/."""
        self.assertEqual(reverse('courseinfo:instructor_remove', kwargs={'slug': 'instructor-slug'}),
                         '/courseinfo/instructor/instructor-slug/remove/')

    def test_instructor_remove_resolve(self):
        """/courseinfo/instructor-slug/remove/ should resolve to courseinfo:instructor_remove."""
        self.assertEqual(
            resolve('/courseinfo/instructor/instructor-slug/remove/').view_name,
            'courseinfo:instructor_remove'
        )

    def test_instructor_create_reverse(self):
        """courseinfo:instructor_create should reverse to /courseinfo/create/."""
        self.assertEqual(reverse('courseinfo:instructor_create'),
                         '/courseinfo/instructor/create/')

    def test_instructor_create_resolve(self):
        """/courseinfo/create/ should resolve to courseinfo:instructor_create."""
        self.assertEqual(
            resolve('/courseinfo/instructor/create/').view_name,
            'courseinfo:instructor_create'
        )


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

    def test_section_update_reverse(self):
        """courseinfo:section_update should reverse to /courseinfo/section-slug/update/."""
        self.assertEqual(reverse('courseinfo:section_update', kwargs={'slug': 'section-slug'}),
                         '/courseinfo/section/section-slug/update/')

    def test_section_update_resolve(self):
        """/courseinfo/section-slug/update/ should resolve to courseinfo:section_update."""
        self.assertEqual(
            resolve('/courseinfo/section/section-slug/update/').view_name,
            'courseinfo:section_update'
        )

    def test_section_remove_reverse(self):
        """courseinfo:section_remove should reverse to /courseinfo/section-slug/remove/."""
        self.assertEqual(reverse('courseinfo:section_remove', kwargs={'slug': 'section-slug'}),
                         '/courseinfo/section/section-slug/remove/')

    def test_section_remove_resolve(self):
        """/courseinfo/section-slug/remove/ should resolve to courseinfo:section_remove."""
        self.assertEqual(
            resolve('/courseinfo/section/section-slug/remove/').view_name,
            'courseinfo:section_remove'
        )

    def test_section_create_reverse(self):
        """courseinfo:section_create should reverse to /courseinfo/create/."""
        self.assertEqual(reverse('courseinfo:section_create'),
                         '/courseinfo/section/create/')

    def test_section_create_resolve(self):
        """/courseinfo/create/ should resolve to courseinfo:section_create."""
        self.assertEqual(
            resolve('/courseinfo/section/create/').view_name,
            'courseinfo:section_create'
        )


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

    def test_course_update_reverse(self):
        """courseinfo:course_update should reverse to /courseinfo/course-slug/update/."""
        self.assertEqual(reverse('courseinfo:course_update', kwargs={'slug': 'course-slug'}),
                         '/courseinfo/course/course-slug/update/')

    def test_course_update_resolve(self):
        """/courseinfo/course-slug/update/ should resolve to courseinfo:course_update."""
        self.assertEqual(
            resolve('/courseinfo/course/course-slug/update/').view_name,
            'courseinfo:course_update'
        )

    def test_course_remove_reverse(self):
        """courseinfo:course_remove should reverse to /courseinfo/course-slug/remove/."""
        self.assertEqual(reverse('courseinfo:course_remove', kwargs={'slug': 'course-slug'}),
                         '/courseinfo/course/course-slug/remove/')

    def test_course_remove_resolve(self):
        """/courseinfo/course-slug/remove/ should resolve to courseinfo:course_remove."""
        self.assertEqual(
            resolve('/courseinfo/course/course-slug/remove/').view_name,
            'courseinfo:course_remove'
        )

    def test_course_create_reverse(self):
        """courseinfo:course_create should reverse to /courseinfo/create/."""
        self.assertEqual(reverse('courseinfo:course_create'),
                         '/courseinfo/course/create/')

    def test_course_create_resolve(self):
        """/courseinfo/create/ should resolve to courseinfo:course_create."""
        self.assertEqual(
            resolve('/courseinfo/course/create/').view_name,
            'courseinfo:course_create'
        )


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

    def test_semester_update_reverse(self):
        """courseinfo:semester_update should reverse to /courseinfo/semester-slug/update/."""
        self.assertEqual(reverse('courseinfo:semester_update', kwargs={'slug': 'semester-slug'}),
                         '/courseinfo/semester/semester-slug/update/')

    def test_semester_update_resolve(self):
        """/courseinfo/semester-slug/update/ should resolve to courseinfo:semester_update."""
        self.assertEqual(
            resolve('/courseinfo/semester/semester-slug/update/').view_name,
            'courseinfo:semester_update'
        )

    def test_semester_remove_reverse(self):
        """courseinfo:semester_remove should reverse to /courseinfo/semester-slug/remove/."""
        self.assertEqual(reverse('courseinfo:semester_remove', kwargs={'slug': 'semester-slug'}),
                         '/courseinfo/semester/semester-slug/remove/')

    def test_semester_remove_resolve(self):
        """/courseinfo/semester-slug/remove/ should resolve to courseinfo:semester_remove."""
        self.assertEqual(
            resolve('/courseinfo/semester/semester-slug/remove/').view_name,
            'courseinfo:semester_remove'
        )

    def test_semester_create_reverse(self):
        """courseinfo:semester_create should reverse to /courseinfo/create/."""
        self.assertEqual(reverse('courseinfo:semester_create'),
                         '/courseinfo/semester/create/')

    def test_semester_create_resolve(self):
        """/courseinfo/create/ should resolve to courseinfo:semester_create."""
        self.assertEqual(
            resolve('/courseinfo/semester/create/').view_name,
            'courseinfo:semester_create'
        )


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

    def test_student_update_reverse(self):
        """courseinfo:student_update should reverse to /courseinfo/student-slug/update/."""
        self.assertEqual(reverse('courseinfo:student_update', kwargs={'slug': 'student-slug'}),
                         '/courseinfo/student/student-slug/update/')

    def test_student_update_resolve(self):
        """/courseinfo/student-slug/update/ should resolve to courseinfo:student_update."""
        self.assertEqual(
            resolve('/courseinfo/student/student-slug/update/').view_name,
            'courseinfo:student_update'
        )

    def test_student_remove_reverse(self):
        """courseinfo:student_remove should reverse to /courseinfo/student-slug/remove/."""
        self.assertEqual(reverse('courseinfo:student_remove', kwargs={'slug': 'student-slug'}),
                         '/courseinfo/student/student-slug/remove/')

    def test_student_remove_resolve(self):
        """/courseinfo/student-slug/remove/ should resolve to courseinfo:student_remove."""
        self.assertEqual(
            resolve('/courseinfo/student/student-slug/remove/').view_name,
            'courseinfo:student_remove'
        )

    def test_student_create_reverse(self):
        """courseinfo:student_create should reverse to /courseinfo/create/."""
        self.assertEqual(reverse('courseinfo:student_create'),
                         '/courseinfo/student/create/')

    def test_student_create_resolve(self):
        """/courseinfo/create/ should resolve to courseinfo:student_create."""
        self.assertEqual(
            resolve('/courseinfo/student/create/').view_name,
            'courseinfo:student_create'
        )
