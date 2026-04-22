from django.shortcuts import render, get_object_or_404
from .models import Course
from django.shortcuts import render, redirect

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses_app/courses_list.html", context={'courses': courses})

def course_detail(request, id):
    course = Course.objects.get(id=id)   #get_object_or_404(Post, id=id)
    course.views += 1
    course.save()
    return render(request, "courses_app/course_detail.html", context={'course': course})

def add_course(request):
    # t = request.GET.get('title')
    # d = request.GET.get('description')
    # if t and d :
    #     Course.objects.create(title=t, description=d)
    #     return redirect('/course/list')

    if request.method == 'POST':
        t = request.POST.get('title')
        d = request.POST.get('description')

        if t and d:
            Course.objects.create(title=t, description=d)
            return redirect('/course/list')
    return render(request, "courses_app/add_course.html")
