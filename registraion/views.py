from django.shortcuts import render,redirect
from .models import Student,Notification,Videos
from django.db.models import Count, Sum, Avg, Max, Min
from .forms import StudentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.core.mail import send_mail
from django.conf import settings







# Create your views here.
@login_required
def Home_page(request):
    date=now()
    newAdmision=Student.objects.filter(created_at__year=date.year,created_at__month=date.month).count()
    s2=Notification.objects.order_by("-created_at")[:4]
    s1=Student.objects.aggregate(total_student=Count('id'))
    return render(request,'registraion/home.html',{"total_student":s1["total_student"],"notifications":s2,"newAdmision":newAdmision})
@login_required
def ViewStudent_page(request):
    student_data=Student.objects.all()
    return render(request,"registraion/view_student.html",{"student_data":student_data})
@login_required
def Delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('view-student')
@login_required
def AddStudent_page(request):
    if(request.method=='GET'):
       form=StudentForm()
    else:
     if (request.method=='POST'):
      form=StudentForm(request.POST,request.FILES)
      if form.is_valid():
          print("form is valid")
          data=form.cleaned_data
          Student.objects.create(
            name=data["name"],
            roll_number=data["roll_number"],
           email=data['email'],
         phone=data['phone'],
         course=data['course'],
         address=data['address'],
         created_at=data['created_at'],
         updated_at=data['updated_at'],
         image=data['image']
         
         
         )
          Videos.objects.create(name=data['name'],video=data['video'])
          return redirect('add-student')
    return render(request,'registraion/add_student.html',{"form":form} )
   
   
@login_required
def profile_page(request,student_id):
   s1=Student.objects.get(id=student_id)
   return render(request,'registraion/profile.html',{"student":s1})
@login_required
def notification_page(request,notification_id):
   notification=Notification.objects.get(id=notification_id)
   
   return render(request,'registraion/notification.html',{"notification":notification}) 
@login_required
def Search_page(request):
   data=Student.objects.filter(name__icontains=request.GET["q"])
   return render(request,'registraion/search.html',{"student_data":data})
@login_required
def Edit_page(request,student_id):  
   student=Student.objects.get(id=student_id)
   if(request.method=='POST'):
      form=StudentForm(request.POST,request.FILES,instance=student)
      if form.is_valid():
         form.save()
         data=form.cleaned_data
      return redirect('profile-page',data["id"])
   form=StudentForm(instance=student)
   
   return render(request,'registraion/edit.html',{"form":form,'student_id':student_id})

   student=Videos.objects.get(id=1)
   return render(request,'registraion/movie.html',{'student':student})
def RegisterView(request):
 if(request.method=='GET'):
    return render(request,'registraion/registration.html')
 else:
    username=request.POST['username']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    user_has_error=False
    if(User.objects.filter(username=username).exists()):
       user_has_error=True
       messages.error(request,'Username Already exits!')
    if(User.objects.filter(email=email).exists()):
       user_has_error=True
       messages.error(request,'Email Already exits!')
    if(len(password)<5):
       user_has_error=True
       messages.error(request,'Password contain atleast 5 characters')
    if user_has_error:
       return render(request,'registraion/registration.html')
    else:
       User.objects.create_user(
          username=username,
          password=password,
          first_name=first_name,
          last_name=last_name,
          email=email
       )
       return redirect('login-page')
    
def LoginView(request):
   if(request.method=='GET'):
      return  render(request,'registraion/login.html')
   else:
      username=request.POST['username']
      password=request.POST['password']
      user=authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect('home-page')
      else:
         return redirect('login-page')
def LogoutView(request):
   logout(request)
   return redirect('login-page')
def forgotPassword(request):
   if(request.method=='POST'):
      email=request.POST['email']
      email_is_valid=False
      try:
        if(User.objects.get(email=email).exists()):
          email_is_valid=True
      except User.DoesNotExist:
         messages.error(request,"Invalid email")
         return render(request,'registraion/forgot_page.html')
   else:
      return render(request,'registraion/forgot_page.html')
 

      
