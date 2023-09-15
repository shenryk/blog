from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

# def home (request):
#    template = loader.get_template('index.html')
#    return HttpResponse(template.render())

context = {
   'author':'Anthony',
   'content':"I am talking about",
   'body':"I am just writing about what happened"
}
   


def home(request):
   posts = context
   return render (request,"index.html",{'blog':context})

def members(request):
   template = loader.get_template('members.html')
   return HttpResponse(template.render())

