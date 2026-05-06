from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

# This is the function the error is complaining about
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == 'POST':
        # Logic to handle the form submission
        # (This can be empty for now just to pass migrations)
        pass
        
    return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=1)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course}
    return render(request, 'exam_result.html', context)

def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # This matches the HTML filename in your templates folder
    return render(request, 'course_details_bootstrap.html', {'course': course})