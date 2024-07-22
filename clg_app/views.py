from django.shortcuts import render,redirect
from clg_app.models import studentform
from django.core.mail import send_mail

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def eventpage(request):
    return render(request,'event.html')

def contactpage(request):
    return render(request,'contacts.html')

def aboutpage(request):
    return render(request,'about.html')

def registerfunction(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        number=request.POST.get('number')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        dob=request.POST.get('date')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        course=request.POST.get('course')
        image=request.FILES.get('image')
        send_registration_email(email, username, password)

        students=studentform(
            studentfname=fname,
            studentlname=lname,
            studentnumber=number,
            studentemail=email,
            studentgender=gender,
            studentdob=dob,
            studentusername=username,
            studentpassword=password,
            studentaddress=address,
            studentcourse=course,
            studentimage=image,
        )
        students.save()
        return redirect('registerpage')
    

def send_registration_email(to_email, username, password):
    subject = 'Your Registration Details'
    message = f'Your registration completed successfully,\n\nYour username: {username}\nYour password: {password}\n\nThank you for registering!'
    from_email = 'jissjo123@gmail.com'
    send_mail(subject, message, from_email, [to_email])    

def registerpage(request):
    show=studentform.objects.all()
    return render(request,'studentreg.html',{'show':show})

def show_students(request):
    students = studentform.objects.all()
    return render(request, 'student_table.html', {'students': students})

def deletefunction(request,data):
    dele=studentform.objects.get(id=data)
    dele.delete()
    return redirect('show_students')

def editpage(request,data):
    edit=studentform.objects.get(id=data)
    return render(request,'edit.html',{'edit':edit})

def editdetails(request,data):
    if request.method=='POST':
        editstudent=studentform.objects.get(id=data)
        editstudent.studentfname=request.POST.get('fname')
        editstudent.studentlname=request.POST.get('lname')
        editstudent.studentnumber=request.POST.get('number')
        editstudent.studentemail=request.POST.get('email')
        editstudent.studentgender=request.POST.get('gender')
        editstudent.studentdob=request.POST.get('date')
        editstudent.studentusername=request.POST.get('username')
        editstudent.studentpassword=request.POST.get('password')
        editstudent.studentaddress=request.POST.get('address')
        editstudent.studentimage=request.FILES.get('image')

        editstudent.save()
        return redirect('show_students')

def profile(request,data):
    pro=studentform.objects.get(id=data)
    return render(request,'profile.html',{'show':pro})



