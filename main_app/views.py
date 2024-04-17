from django.shortcuts import render, redirect
from .models import Book, Store
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import SalesForm

#The data for my list of objects I just used from wikipedia

calvinandhobbes = [
    {'title': 'Calvin and Hobbes', 'date': 'April 1987', 'isbn': 'ISBN 0-8362-2088-9', 'details': 'Foreword by Garry Trudeau; original black-and-white artwork scattered throughout book'},
    {'title': 'Something Under the Bed is Drooling', 'date': 'April 1988', 'isbn': 'ISBN 0-8362-1825-6', 'details': 'Foreword by Pat Oliphant; original black-and-white artwork scattered throughout book'},
    {'title': 'The Essential Calvin and Hobbes: A Calvin and Hobbes Treasury', 'date': 'September 1988', 'isbn': 'ISBN 0-8362-1805-1', 'details': 'Foreword by Charles M. Schulz; an illustrated poem, "A Nauseous Nocturne"'},
    {'title': 'Yukon Ho!', 'date': 'March 1989', 'isbn': 'ISBN 0-8362-1835-3', 'details': 'The "Yukon Song"; original black-and-white artwork scattered throughout book'},
    {'title': 'The Calvin and Hobbes Lazy Sunday Book: A Collection of Sunday Calvin and Hobbes Cartoons', 'date': 'September 1989', 'isbn': 'ISBN 0-8362-1852-3', 'Details': 'Ten-page story "Spaceman Spiff: Interplanetary Explorer Extraordinaire!"; afterword by Bill Watterson; and a specially redrawn version of the August 28, 1988 strip'},
    {'title': 'Weirdos from Another Planet!', 'date': 'March 1990', 'isbn': 'ISBN 0-8362-1862-0', 'details': 'Original black-and-white artwork scattered throughout book'},
    {'title': 'The Authoritative Calvin and Hobbes: A Calvin and Hobbes Treasure', 'date': 'October 1990', 'isbn': 'ISBN 0-8362-1822-1', 'details': 'Seven-page story in which Calvin becomes an elephant'},
    {'title': 'The Revenge of the Baby-Sat', 'date': 'April 1991', 'isbn': 'ISBN 0-8362-1866-3', 'details': ''},
    {'title': 'Scientific Progress Goes \"Boink\"', 'date': 'October 1991', 'isbn': 'ISBN 0-8362-1878-7', 'details': ''},
    {'title': 'Attack of the Deranged Mutant Killer Monster Snow Goons', 'date': 'April 1992', 'isbn': 'ISBN 0-8362-1883-3', 'details': ''},
    {'title': 'The Indispensable Calvin and Hobbes: A Calvin and Hobbes Treasury', 'date': 'October 1992', 'isbn': 'ISBN 0-8362-1898-1', 'details': 'Several illustrated poems'},
    {'title': 'Teaching with Calvin and Hobbes', 'date': '1993', 'isbn': 'ISBN 1-8788-4915-8', 'details': 'Lesson units by Linda Holmen and Mary Santella-Johnson based on the strips'},
    {'title': 'The Days Are Just Packed', 'date': 'October 1993', 'isbn': 'ISBN 0-8362-1735-7', 'details': ''},
    {'title': 'Homicidal Psycho Jungle Cat', 'date': 'October 1994', 'isbn': 'ISBN 0-8362-1769-1', 'details': ''},
    {'title': 'The Calvin and Hobbes Tenth Anniversary Book', 'date': 'October 1995', 'isbn': 'ISBN 0-8362-0438-7', 'details': 'Commentary by Watterson and annotations on individual strips'},
    {'title': 'There\'s Treasure Everywhere', 'date': 'March 1996', 'isbn': 'ISBN 0-8362-1312-2', 'details': ''},
    {'title': 'It\'s a Magical World', 'date': 'October 1996', 'isbn': 'ISBN 0-8362-2136-2', 'details': ''},
    {'title': 'Calvin and Hobbes: Sunday Pages, 1985-1995: An Exhibition Catalogue', 'date': 'September 2001', 'isbn': 'ISBN 0-7407-2135-6', 'details': 'Original sketches and commentary by Watterson'},
    {'title': 'The Complete Calvin and Hobbes (hardcover)', 'date': 'October 2005', 'isbn': 'ISBN 0-7407-4847-5', 'details': 'Introduction and commentary'},
    {'title': 'The Complete Calvin and Hobbes (paperback)', 'date': 'November 2012', 'isbn': 'ISBN 1-4494-3325-1', 'details': 'Introduction and commentary'},
    {'title': 'Exploring Calvin and Hobbes: An Exhibition Catalogue', 'date': 'February 2015', 'isbn': 'ISBN 978-1-4494-6036-5', 'details': 'Original art and commentary by Watterson'}
]
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html')

def about(request):
    books = Book.objects.all()
    return render(request, 'books/about.html', {'candh': books})

def allbooks(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'candh': books})

def detailbooks(request, book_id):
    books = Book.objects.get(id=book_id)
    sales_form = SalesForm()
    stores = books.store.all().values_list('id')
    books_not_in_stores = Store.objects.exclude(id__in=stores)
    return render(request, 'books/detail.html', {
        'candh': books,
        'sales_form': sales_form,
        'stores': stores,
        'not_in_store': books_not_in_stores
    })

def add_sales(request, pk):
    form = SalesForm(request.POST)
    if form.is_valid():
        new_sale = form.save(commit=False)
        new_sale.book_id = pk
        new_sale.save()
    return redirect('details', pk)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['date', 'isbn', 'details']

class BookDelete(DeleteView):
    model = Book
    success_url = '/allbooks/'

class StoreCreate(CreateView):
    model = Store
    fields = '__all__'

class StoreUpdate(UpdateView):
    model = Store
    fields = ['name', 'location']

class StoreList(ListView):
    model = Store

class StoreDetail(DetailView):
    model = Store

class StoreDelete(DeleteView):
    model = Store
    success_url='/store'


