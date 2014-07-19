from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from books.models import Author,Book

# Create your views here.
def index(request):
	data={}
	for book in Book.objects.all():
		data[book.title]=book.author.name
	return JsonResponse(data)


	return HttpResponse('This is index')

def detail(request,book_id):
	book=Book.objects.get(id=book_id)
	data={book.title:book.author.name}
	return JsonResponse(data)

