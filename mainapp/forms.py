from django import forms
from .models import CourseRequest


class CourseRequestForm(forms.ModelForm):
    class Meta:
        model = CourseRequest
        fields = "__all__"
