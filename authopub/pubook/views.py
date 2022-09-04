from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Book, Publisher

# Create your views here.

def publisher_form(request):
    if request.method=='POST':
        publisher_name=request.POST['pub_name']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['state']
        website=request.POST['website']
        Publisher(name=publisher_name,address=address,city=city,state=state,country=country,website=website).save()
    return render (request,'publisher.html')

def author_form(request):
    if request.method=='POST':
        salutation=request.POST['salutation']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        Author(salutation=salutation,first_name=first_name,last_name=last_name,email=email).save()
    return render (request,'author.html')

def book_form(request):
    publisher_names=Publisher.objects.all()
    author_names=Author.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        authors=request.POST.get('authors')
        author_data=Author.objects.get(first_name=authors)
        publishers=request.POST.get('publishers')
        publisher_data=Publisher.objects.get(name=publishers)
        date=request.POST.get('date')
        Book(title=title,authors=author_data,publishers=publisher_data,publication_date=date).save()
    context={
        'author_data':author_names,
        'publisher_data':publisher_names,
     }
    return render(request,'book.html',context)

def book_detail(request):
    all_book=Book.objects.all()
    context={
        'all_book':all_book,
    }
    return render(request,'book_detail.html', context)

def author_detail(request,id):
    # list1=[]
    author_detailed= Book.objects.filter(authors=id)
    no_of_book= author_detailed.count()
    context={
        'author_detailed':author_detailed,
        'no_of_book':no_of_book,
    }
    return render(request,'author_detail.html',context)

def publisher_detail(request,id):
    pub_books=Book.objects.filter(publishers=id)
    context={
        'pub_books':pub_books,
    }
    return render(request,'publisher_detail.html',context)