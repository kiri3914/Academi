from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=127, verbose_name='Имя учителя')
    last_name = models.CharField(max_length=127, verbose_name='Фамилия учителя', null=True)
    patronymic = models.CharField(max_length=127, verbose_name='Отчество учителя', null=True)
    about = models.TextField(verbose_name='О преподователе')
    image = models.ImageField(
        upload_to='media/mainapp/images', null=True, blank=True, verbose_name='Фото учителя'
    )

    def __str__(self):
        return f'{self.first_name} - {self.patronymic}'


class Subject(models.Model):
    subject_name = models.CharField(max_length=127, verbose_name='Название предмета')
    duration = models.PositiveIntegerField(default=0)
    about = models.TextField()
    image = models.ImageField(upload_to='media/mainapp/images', null=True, blank=True)

    def __str__(self):
        return f'{self.subject_name}'


class CourseRequest(models.Model):
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f'Пользователь {self.user_name} хочет на {self.subject.subject_name}'
