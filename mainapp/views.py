from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Teacher, Subject, CourseRequest
from .forms import CourseRequestForm
from core.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def index(request):
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    if request.method == 'GET':
        form = CourseRequestForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = CourseRequestForm(request.POST)
        if form.is_valid():
            user_name = request.POST['user_name']
            user_phone = request.POST['user_phone']
            email = request.POST['email']
            subject_id = request.POST['subject']
            subject = Subject.objects.get(id=subject_id)
            print(f'{user_name} на {subject.subject_name} ', user_phone,
                  DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            try:
                send_mail(f'{user_name}  {user_phone} ', user_phone,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
                ins = CourseRequest.objects.create(
                    user_name=user_name,
                    user_phone=user_phone,
                    email=email,
                    subject=subject
                )
                ins.save()
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')

            return redirect('/')
    else:
        return HttpResponse('Неверный запрос.')
    context = {
        "teachers": teachers,
        "subjects": subjects,
        'form': form
    }
    return render(request, "mainapp/index.html", context=context)

def subject_detail(request, subject_id):
    template_name = 'mainapp/subject_detail.html'
    subject = Subject.objects.get(id=subject_id)
    subjects = Subject.objects.all()
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        email = request.POST['email']
        subject_id = request.POST['subject']
        ins = CourseRequest.objects.create(
            user_name=user_name,
            user_phone=user_phone,
            email=email,
            subject=Subject.objects.get(id=subject_id)
        )
        ins.save()
    context = {
        'subject': subject,
        'subjects': subjects,
    }
    return render(request, template_name, context=context)


# def index(request):
#     template_name = 'mainapp/index.html'
#     teachers = Teacher.objects.all()
#     subjects = Subject.objects.all()
#     if request.method == 'POST':
#         user_name = request.POST['user_name']
#         user_phone = request.POST['user_phone']
#         email = request.POST['email']
#         subject_id = request.POST['subject']
#         ins = CourseRequest.objects.create(
#             user_name=user_name,
#             user_phone=user_phone,
#             email=email,
#             subject=Subject.objects.get(id=subject_id)
#         )
#         ins.save()
#     context = {
#         "teachers": teachers,
#         "subjects": subjects,
#     }
#     return render(request, template_name, context=context)


