from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from books.models import Author,Book
from django.shortcuts import render_to_response

# Create your views here.
def all_books(request):
	result=[]
	for book in Book.objects.all():
		data={}
		data['title']=book.title
		data['author']=book.author.name
		result.append(data)
	return JsonResponse(result,safe=False)



def home(request):
	return render_to_response('home.html')

def detail(request,book_id):
	book=Book.objects.get(id=book_id)
	data={'title':book.title,'author':book.author.name}
	return JsonResponse(data)

