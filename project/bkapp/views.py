from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def homepage(request):
    return render(request, 'hom.html')  
    return redirect('signup')
    return render(request, 'signup.html')





    
def book_form(request):
    if(request.method =='POST'):
      title=request.POST.get('title')
      author=request.POST.get('author')
      isbn=request.POST.get('isbn')
      available=request.POST.get('available')
      book.objects.create(title=title,author=author,isbn=isbn,available=available)
      return redirect('book_form')
    books=book.objects.all()
    return render(request,'index.html',{'books':books})
 



def student_form(request):
    if(request.method =='POST'):
       name=request.POST.get('name')
       rollno=request.POST.get('rollno')
       course=request.POST.get('course')
       department=request.POST.get('department')
       email=request.POST.get('email')
       student.objects.create(name=name,rollno=rollno,course=course,department=department,email=email)
       return redirect('book_form')
    students=student.objects.all()
    return render(request,'user.html',{'students':students})



from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully.")
        return redirect('login')
    
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_form')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, get_object_or_404, redirect
from .models import student

def edit_form(request, pk):
    students = get_object_or_404(student, pk=pk)

    if request.method == 'POST':
        students.name = request.POST.get("name")
        students.rollno = request.POST.get("rollno")
        students.course = request.POST.get("course")
        students.department = request.POST.get("department")
        students.email = request.POST.get("email")
        students.save()
        return redirect("edit_form", pk=student.pk)

    return render(request, "edit.html", {
        "edit_student": student,
        "students": student.objects.all()
    })





def delete_form(request, pk):
    students = get_object_or_404(student, pk=pk)
    students.delete()
    return redirect("edit_form")

    






