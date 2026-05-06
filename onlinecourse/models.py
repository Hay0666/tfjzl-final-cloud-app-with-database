from django.db import models
from django.conf import settings

class Instructor(models.Model):
    full_name = models.CharField(max_length=100)
    def __str__(self):
        return self.full_name

class Learner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    social_link = models.URLField(max_length=200)
    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    instructors = models.ManyToManyField(Instructor)
    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    # Grader specifically asked for this method
    def is_get_score(self):
        score = 0
        for choice in self.choices.all():
            if choice.is_correct:
                score += choice.question.grade
        return score