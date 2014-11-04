from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from books.models import Author,Book,Book_Source
from django.shortcuts import render_to_response

# Create your views here.
def all_books(request):
	result=[]
	for book in Book.objects.all():
		data={}
		data['title']=book.title
		data['author']=book.author.name
                data['category']="%s > %s" % (book.category.superclass.name,book.category.name)
                source = book.sources.all()[0]
                data['source'] = source.name
                data['book_number'] = book.book_source_set.get().book_number
                data['address'] = book.book_source_set.get().url
                data['keywords'] = ', '.join([k.content for k in book.keywords.all()])
                data['introduction'] = book.introduction


		result.append(data)
	return JsonResponse(result,safe=False)



def home(request):
	return render_to_response('home.html')

def detail(request,book_id):
	book=Book.objects.get(id=book_id)
	data={'title':book.title,'author':book.author.name}
	return JsonResponse(data)

