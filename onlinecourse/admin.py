from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# 1. Choice Inline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 2. Question Inline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# 3. Question Admin with ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'grade')

# 4. Lesson Admin with QuestionInline
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

# 5. Course Admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Register all 7 classes to show up in the screenshot
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)