from django.urls import path
from .views import *

urlpatterns=[
    path('home/',homepage),
    path('book_form/',book_form,name='book_form'),
    path('student_form/',student_form,name='student_form'),
    path('signup/',signup_view,name='signup'),
    path('login/',login_view,name='login'),
    path('edit_form/<int:pk>/',edit_form,name='edit_form'),
    path('delete_form/<int:pk>/',delete_form,name='delete_form'),

]
