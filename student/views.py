from django.shortcuts import render

def index(request):
    return render(request, 'student/index.html')

def courses(request):
    return render(request, 'student/courses.html')

def reports(request):
    return render(request, 'student/reports.html')