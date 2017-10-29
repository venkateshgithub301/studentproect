from django.shortcuts import render
from .models import Book,Student,MultipleBooks,Students,Bookname
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as djangologin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import BookForm
from rest_framework import permissions
from rest_framework import serializers
from .models import Book
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import UserSerializer
from .services import get_books1
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views.generic import View
import pdb
# Create your views here.

class BookInventery(View):
	def get(self,request):
		res_dict={}
		user_obj=Students.objects.all()
		#ontext=res_dict.update({"book":book})
		return render(request,"user_inventary.html",context={"user_obj":user_obj})
	def post(self,request):
		#import pdb;pdb.set_trace()
		user_id=request.POST["select"]
		book_obj=Bookname.objects.filter(author=user_id)
		return render(request,"book_inventary.html",context={"book":book_obj})
class AuthorInventey(View):
	def get(self,request):
		author_obj=Bookname.objects.all()
		return render(request,"author_inventary.html",context={"author1":author_obj})
	def post(self,request):
		author_id=request.POST["select"]
		authorname=Bookname.objects.filter(name=author_id)
		return render(request,"author1_inverntary.html",context={"author2":authorname})





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
	return render(request,"login_template/login.html")#here login_template is path to the templates or in settings.py also used

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
			return render(request,'insertbookform.html',context={'form':form})


class GetBooksAPI(APIView):
	permission_classes=[
		permissions.AllowAny
	]
	def get(self,request):
		book_id=request.GET.get('id')
		if book_id:
			book_obj=Book.objects.filter(id=book_id)
		else:
			book_obj=Book.objects.all()	
		ser_obj=UserSerializer(book_obj,many=True)
		return Response(ser_obj.data)

	def post(self,request):
		ser_obj=UserSerializer(data=request.data)
		if ser_obj.is_valid():
			ser_obj.save()
			return Response('success',status.HTTP_201_CREATED)
		return Response(ser_obj.errors.status.HTTP_400_BAD_REQUEST)

CACHE_TTL=getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def book_viwe(request):
	print(get_books1())
	get_books1()
	return HttpResponse("suucess")