from django.shortcuts import render,redirect
from .models import post
from .forms import post_form
from django.contrib import messages
from django.http import Http404
# Create your views here.
def index(request):
	title="welcome to wed site"
	query=post.objects.all()
	context={
	  'title':title,
	  'object_all': query
	}
	return render(request,'index.html',context)

def contact(request):
	title="welcome to contact page"
	context={
	  'title':title
	}
	return render(request,'contact.html',context)

def post_list(request):
	title="post List"
	query_set=post.objects.all().order_by('-create')
	args={
	   'title':title,
	   'query':query_set
	}
	return render(request,"blog.html",args)


def create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	form=post_form(request.POST or None or request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.user=request.user
		instance.save()
		messages.success(request,"successfully create")
		return redirect('/')
	else:
		messages.error(request,"sorry your post not create ")	
	context={
	  'form':form,

	}
	return render(request,'post_form.htm',context) 	