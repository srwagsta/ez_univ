import factory.django
from courseinfo.models import (Semester,
                               Course,
                               Instructor,
                               Student,
                               Section)


class SemesterFactory(factory.DjangoModelFactory):
    class Meta:
        model = Semester

    semester_name = factory.Faker('company')


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course

    course_number = factory.Faker('ssn')
    course_name = factory.Faker('job')


class InstructorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Instructor

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class StudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class SectionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Section

    section_name = factory.Faker('company')
    semester = SemesterFactory.create()
    course = CourseFactory.create()


def fill_database(number_of_fake_entries=20):
    for _ in range(0, number_of_fake_entries):
        InstructorFactory.create()
        StudentFactory.create()
        SectionFactory.create()

