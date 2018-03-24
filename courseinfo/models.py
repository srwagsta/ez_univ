from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import itertools


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=45, unique=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return '%s' % self.semester_name

    def get_absolute_url(self):
        return reverse('courseinfo:semester_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('courseinfo:semester_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('courseinfo:semester_remove', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        unique_slug = slugify(self.semester_name)
        for x in itertools.count(1):
            if not Semester.objects.filter(slug=unique_slug).exists():
                break
            unique_slug = '%s-%d' % (unique_slug, x)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    class Meta:
        ordering = ['semester_name']


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return '%s' % self.course_name

    def get_absolute_url(self):
        return reverse('courseinfo:course_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('courseinfo:course_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('courseinfo:course_remove', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        unique_slug = slugify(self.course_name)
        for x in itertools.count(1):
            if not Course.objects.filter(slug=unique_slug).exists():
                break
            unique_slug = '%s-%d' % (unique_slug, x)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    class Meta:
        ordering = ['course_number']


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return '%s , %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('courseinfo:instructor_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('courseinfo:instructor_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('courseinfo:instructor_remove', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        unique_slug = slugify('%s--%s' % (self.last_name, self.first_name))
        for x in itertools.count(1):
            if not Instructor.objects.filter(slug=unique_slug).exists():
                break
            unique_slug = '%s-%d' % (unique_slug, x)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    class Meta:
        ordering = ['last_name', 'first_name']


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nick_name = models.CharField(max_length=45, default='', blank=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        if self.nick_name == "":
            return '%s , %s' % (self.last_name, self.first_name)
        else:
            return '%s , %s (%s)' % (self.last_name, self.first_name, self.nick_name)

    def get_absolute_url(self):
        return reverse('courseinfo:student_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('courseinfo:student_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('courseinfo:student_remove', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        unique_slug = slugify('%s--%s' % (self.last_name, self.first_name))
        for x in itertools.count(1):
            if not Student.objects.filter(slug=unique_slug).exists():
                break
            unique_slug = '%s-%d' % (unique_slug, x)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    class Meta:
        ordering = ['last_name', 'first_name']


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=10)
    semester = models.ForeignKey(Semester, related_name='sections', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='sections', on_delete=models.CASCADE)
    instructors = models.ManyToManyField(Instructor, related_name='sections')
    students = models.ManyToManyField(Student, related_name='sections')
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return '%s - %s (%s)' % (self.course.course_number, self.section_name, self.semester.semester_name)

    def get_absolute_url(self):
        return reverse('courseinfo:section_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('courseinfo:section_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('courseinfo:section_remove', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        unique_slug = slugify(self.section_name)
        for x in itertools.count(1):
            if not Section.objects.filter(slug=unique_slug).exists():
                break
            unique_slug = '%s-%d' % (unique_slug, x)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

    class Meta:
        ordering = ['course__course_number', 'section_name', 'semester__semester_name']
