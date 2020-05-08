from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PostForm

post = post.objects.all().order_by('-created_date')

# Create your views here.
def index(request):
	return render(
		request,
		'index.html',
		{
			'title':'Home',
            'posts': post,
        }
    )

def post_add(request):
    if request.method == "POST":
        post.create(
            title = request.POST['title'],
            about = request.POST['about'],
            photo = request.FILES['files[]'],
            published_date = timezone.now()
        )
        return HttpResponseRedirect('/')
    else:
        return render(
            request,
            'post.html',
            {
                'title':'Add post',
            }
        )