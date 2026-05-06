from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Instructor, Enrollment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Instructor)
admin.site.register(Enrollment)