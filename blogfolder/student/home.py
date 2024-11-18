# import pdb
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Student, CohortGroup, Student_profile, Program
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class HomepageView(View):
    def get(self, request):
        all_students = Student.objects.all()
        # print(all_students)
        # pdb.set_trace()
        studentpaginator = Paginator(all_students, 4)
        page_numbers = request.GET.get('page')

        try:
            page_info = studentpaginator.get_page(page_numbers)
        except EmptyPage:
            pass

        print(page_info.has_next())

        context = {
            'students' : all_students,
            'students' : page_info
        }

        return render(request, 'cohorts/index.html', context = context)

def view_profile(request, slug):
    student = get_object_or_404(Student, slug=slug)
    cohort_group = student.cohortgroup_set.all().first()
    if cohort_group:
        cohort_members = Student.objects.filter(
            cohortgroup = cohort_group

        ).exclude(slug=slug)
    else:
        cohort_members = Student.objects.none()
        
    context= {
        'student': student,
        'cohort_members': cohort_members,
        'cohort_group': cohort_group
    }    
    return render(request, 'cohorts/profile.html', context)


def delete_student(request, slug):
    user = get_object_or_404(Student, slug=slug)
    user.delete()
    messages.success(request, f"{user.first_name} {user.last_name} has been deleted successfully.")
    return redirect('dashboardView')