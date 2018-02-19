from django.db import models


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=45, unique=True)


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_langth=20, unique=True)
    course_name = models.CharField(max_length=255)


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nick_name = models.CharField(max_length=45)


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10)
    semester_id = models.ManyToManyField(Semester.semester_id)
    course_id = models.ManyToManyField(Course.course_id)



