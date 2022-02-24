from django.urls import path
from .views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='index' )
]



######################################## на функциях  + sendgrid #################################################
# from mainapp.views import (
#                             index,
#                             subject_detail)
# urlpatterns = [
#     path('', index, name='index'),
#     path('subject/<int:subject_id>/', subject_detail, name='subject_detail'),
# ]