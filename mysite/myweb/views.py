from django.shortcuts import render
from django.shortcuts import HttpResponse
from myweb import models

# Create your views here.

user_list = [
	{"user":"tom1","pwd":"abc123"},
	{"user":"tom2","pwd":"abc456"},
]

def index (request):
	if request.method == "POST":
		username = request.POST.get("username", None)
		password = request.POST.get("password",None)
		# 添加数据到数据库
		models.UserInfo.objects.create(user=username, pwd=password)
	# 从数据库中读取所有数据
	user_list = models.UserInfo.objects.all()
		# temp = {"user":username,"pwd":password}
		# user_list.append(temp)
		# print(username, password)
	# return HttpResponse("hello world!")
	return render(request, "index.html",{"data":user_list})