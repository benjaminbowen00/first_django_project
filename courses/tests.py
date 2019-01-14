from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Course, Step
# Create your tests here.

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in python"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)

class StepModelTests(TestCase):
    def test_step_order_starts_at_0(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="Learn to write regular expressions in python"
        )
        step=Step.objects.create(title="Step 1",
        description="This is the first step in the course",
        course=course)

        self.assertEqual(step.order,0)

class CourseViewTests(TestCase):
    def setUp(self):
        self.course  = Course.objects.create(
        title="Python Tests",
        description="Learn to write tests in python"
    )
        self.course2 = Course.objects.create(
        title="new python course",
        description="exciting new python course"
    )
        self.step = Step.objects.create(
        title = "Intro to Doctests",
        description ="Learn to write tests in your docstrings",
        course = self.course
    )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:course_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)
