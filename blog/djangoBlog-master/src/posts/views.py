from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request): #retrieve
	context = { 
        "title": "Detail"
    }
	return render(request, "index.html", context)

def post_list(request): #list items
#     if request.user.is_authenticated():
# 	context = { 
#     "title": "My User List"
# }
#     else:
# 	    context = { 
# 	    "title": "List"
# 	}	
    context = { 
	    "title": "List"
 	}	
    return render(request, "index.html", context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")


def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")
