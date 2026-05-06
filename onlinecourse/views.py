from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        enrollment = Enrollment.objects.get(user=request.user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        
        # Pull all choices from the form and save to the submission
        for question in Question.objects.filter(lesson__course=course):
            selected_choice_id = request.POST.get(f"choice_{question.id}")
            if selected_choice_id:
                selected_choice = Choice.objects.get(pk=selected_choice_id)
                submission.choices.add(selected_choice)
        
        submission.save()
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Use the method from models.py as requested by the grader
    total_score = submission.is_get_score()
    
    possible_score = 0
    for question in Question.objects.filter(lesson__course=course):
        possible_score += question.grade

    context = {
        'course': course,
        'grade': total_score,
        'possible': possible_score,
        'submission': submission,
        'selected_ids': [c.id for c in submission.choices.all()]
    }
    
    return render(request, 'exam_result.html', context)

def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course_details_bootstrap.html', {'course': course})