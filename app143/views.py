from django.shortcuts import render
from .models import Book,Student,MultipleBooks
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as djangologin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import BookForm

# Create your views here.
@login_required(login_url='/')
def get_books(request):
	book_name=[]

	book_obj=Book.objects.all()
	for i in book_obj:
		book_name.append({'name':i.name,'Author':i.Author.username})

		return HttpResponse(book_name)	
	return render(request,"sample.html",context={'book':book_obj,'flag':True})
	
def get_bookby_id(request):
	book_list=[]

	book_id=request.GET.get('id')
	book_obj=Book.objects.filter(id=book_id)
	if book_obj.exists():
		for i in book_obj:
			book_list.append({'name':i.name,'Author':i.Author.username})
		return HttpResponse(book_list)
	else:
		return HttpResponse("no Book found")

def get_booksByUsers(request):
	book_list=[]

	book_id=eval(request.GET.get('id'))
	print (book_id)
	book_obj=Book.objects.filter(pk__in=book_id)
	if book_obj.exists():
		for i in book_obj:
			book_list.append({'name':i.name,'Author':i.Author.username,'id':i.id})
		return HttpResponse(book_list)
	else:
		return HttpResponse("no Book found")
def index(request):
	return render(request,"login.html")

def login(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	auth_user=authenticate(username=username,password=password)
	create_user=request.user
	if auth_user:
		djangologin(request,auth_user)
		if request.GET.get('next'):
			print(next)
			return redirect(request.GET.get('next'))
		return render(request,'home.html',context={'username':create_user})
	else:
		return HttpResponse ("login is failure")


def Iheritance(request):
	return render(request,"child.html")

def register(request):
	if request.method=='GET':
		return render(request,'register.html')
	else:
		username=request.POST.get('username')
		password=request.POST.get('password')
		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')
		Gender=request.POST.get('gender')
		Gender=1 if Gender=='Male' else 0
		print Gender
		Age=request.POST.get('age')
		Address=request.POST.get('address')
		Mobile=request.POST.get('mobile')
		user_obj=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname)
		user_obj.save()
		student_obj = Student.objects.create(age=Age, gender=Gender, user=user_obj, mobileno=Mobile, address=Address)
		return render(request,"register.html")

def addbook(request):
	if request.method=='GET':
		users=User.objects.all()
		return render(request,'addbook.html',context={'users':users})
		
	else:
		name=request.POST.get('name')
		author=request.POST.get('author_id')
		print(author)
		MultipleBooks_obj=MultipleBooks.objects.create(name=name,author=User.objects.get(id=author))
		MultipleBooks_obj.save()
		return HttpResponse("Book added successfully")

def logout_page(request):
	logout(request)
	return render(request,'logout.html')

def insert_book_form(request):
	if request.method=='GET':
		return render(request,'insertbookform.html',context={"form":BookForm()})
	else:
		form=BookForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'success.html')
		else:
			return HttpResponse("Failure")
