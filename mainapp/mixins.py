from django.http import JsonResponse
from django.views.generic.edit import CreateView

from mainapp.forms import CourseRequestForm


class FormMixin:
    def form_valid(self, form):
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