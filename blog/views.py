from django.shortcuts import render
from django.shortcuts import render_to_response

from blog.models import BlogPost
from django.template import loader,Context
from django.http import *

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("index.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def comment(req):
    return render_to_response('comment.html')

def get_detail(request, BlogPost_id):
    try:
        blog = BlogPost.objects.get(id=BlogPost_id)
    except blog.DoesNotExist:
        raise Http404

    return render(request, 'detail.html', {'blog':blog})