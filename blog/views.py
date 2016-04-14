from django.shortcuts import render
from django.shortcuts import render_to_response

from blog.models import BlogPost
from django.template import loader,Context
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("index.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))