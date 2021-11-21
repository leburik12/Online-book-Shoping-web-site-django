from django.shortcuts import render
from .models import Books
from django.views.generic import ListView, DetailView
import random
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
from django.contrib.postgres.search import TrigramSimilarity
from cart.forms import AddToCartForm


class FilteredData:
    books = Books.availablebook.all()
    new_releases = books.values_list( 'id', flat=True )[:4]

    def new_releases_author(self):
        new_released_book_author = self.new_releases.values_list( 'author', flat=True )
        return new_released_book_author

    def filtering_by_ratings(self):
        global best_rated_books_id
        # filtering books by ratings
        ratings = [1, 2, 3, 4, 5]
        rate_random = random.choice( ratings )
        best_rated_books = self.books.filter( rating__gte=rate_random ).exclude( pk__in=[self.new_releases] )[:4]
        best_rated_books_id = best_rated_books.values_list( 'id', flat=True )
        return best_rated_books

    def filtering_by_bestseller(self):
        global best_seller_books
        # filtering books by best seller
        query_item = [{'filter': random.randrange( 1, 61 )}, 'order_by']
        query_insertions = random.choice( query_item )
        if isinstance( query_insertions, dict ):
            best_seller_books = (self.books.filter( best_seller__gte=query_insertions['filter'] ).
                                     exclude( id__in=self.new_releases ).exclude( id__in=best_rated_books_id )[:4])
        else:
            best_seller_books = (self.books.order_by( '-best_seller' ).
                                     exclude( id__in=self.new_releases ).exclude( id__in=best_rated_books_id )[:4])
        if len( best_seller_books.values_list( flat=True ) ) < 4:
            best_seller_books = (self.books.order_by( '-best_seller' ).
                                     exclude( id__in=self.new_releases ).exclude( id__in=best_rated_books_id )[:4])
        best_seller_books_id = best_seller_books.values_list( 'id', flat=True )
        return best_seller_books


def search_books(request):
    query = None
    category = None
    search_context = {}
    message = ''
    al_books = Books.availablebook.all()
    if request.method == 'GET':
        query = request.GET.get( 'query' )
        category = request.GET.get( 'category' )
        if category is not None:
            category = category.split()[0]
            print( category )
            # search_vector = SearchVector('title', weight='A') + SearchVector('author', weight='B') + \
            #                 SearchVector('description', weight='c')
            # search_query = SearchQuery(query)
            al_books = al_books.filter( category__iexact=category )
            print( al_books )
            if len( al_books.values() ) > 0:
                print( al_books )
                # al_books = al_books.annotate(
                #     search=search_vector,
                #     rank=SearchRank(search_vector, search_query)
                # ).filter(search=search_query).order_by('-rank')
                # al_books = al_books.filter(TrigramSimilarity('title', query)).order_by('-smilitarity')
                al_books = al_books.annotate( similarity=TrigramSimilarity( 'category', query ) ).order_by(
                    '-similarity' )
                print( al_books )
                message = 'success_db'
    return render( request,
                   'books/total_books.html',
                   {'al_books': al_books,
                    'message': message
                    } )


class BookLists( ListView ):
    queryset = Books.availablebook.all()
    template_name = 'books/index.html'
    paginate_by = 4
    books_id = []
    books_id = Books.availablebook.values_list( 'id', flat=True )[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data( *kwargs )
        # Instantiate the filter data class
        filtered_data = FilteredData()
        context['best_rated_books'] = filtered_data.filtering_by_ratings()
        context['best_seller_books'] = filtered_data.filtering_by_bestseller()
        context['new_releases_authors'] = filtered_data.new_releases_author()
        return context


class BookDetailPage( DetailView ):
    queryset = Books.availablebook.all()
    template_name = 'books/single-book.page.html'

    def get_context_data(self, **kwargs):
        # call the base implementation to get a context
        context = super().get_context_data( **kwargs )
        # context['form'] = AddToCartForm(data={'pk' :self.kwargs['pk']})
        # set the initial value for the field
        # context['form'].fields['bk_id'].initial = self.kwargs['pk']
        return context


# Globals
all_books = Books.availablebook.all()
my_books = Books.availablebook.all()
book_zenbil = {}
look_up = {'category': 'category__iexact',
           'used': 'old_book_hardcover_qty__gte',
           'new': 'new_book_hardcover_qty__gte',
           'author': 'author__iexact',
           'rating': 'rating__gte',
           }


# global valriables

def filter_zenbil_book_with_loop(zenbil, name_of_filter):
    global lookup
    global all_books
    lookupvalue = look_up.get( name_of_filter )
    for look_up_name, look_up_value in zenbil.items():
        lookupvalue = look_up.get( look_up_name )
        all_books = all_books.filter( **{lookupvalue: look_up_value} )
    return all_books


def zenbil_filter(name, value):
    global all_books
    global book_zenbil
    global look_up
    lookupvalue = look_up.get( name )
    if not bool( book_zenbil ):
        all_books = all_books.filter( **{lookupvalue: value} )  # New filtering
        book_zenbil[name] = value
        return all_books
    else:
        if name == 'used':
            if 'new' in book_zenbil.keys():
                del book_zenbil['new']  # if 'used' is selected and 'new' exists in the filter delete the 'new'
                book_zenbil[name] = value
                all_books = filter_zenbil_book_with_loop( book_zenbil, name )
                return all_books
            else:  # if the user has already filtered using 'used books'  overwrite or not add to filter and overwrite it
                book_zenbil[name] = value
                all_books = filter_zenbil_book_with_loop( book_zenbil, name )
                return all_books
        elif name == 'new':
            if 'used' in book_zenbil.keys():
                del book_zenbil['used']  # if 'new' is selected and 'used' exists in the filter delete the 'new'
                book_zenbil[name] = value
                all_books = filter_zenbil_book_with_loop( book_zenbil, name )
                return all_books
            else:  # if the user has already filtered using 'new books'  overwrite or not add to filter and overwrite it
                book_zenbil[name] = value
                all_books = filter_zenbil_book_with_loop( book_zenbil, name )
                return all_books
        elif name in book_zenbil.keys():  # overriding the existing filter (the filter exists)
            book_zenbil[name] = value
            if len( book_zenbil ) == 1:  # if it is only filtered once change the whole filter
                all_books = Books.objects.filter( **{lookupvalue: value} )
                return all_books
            else:  # if the filter exists with other filters
                all_books = my_books
                all_books = filter_zenbil_book_with_loop( book_zenbil, name )
                return all_books
        else:  # adding new filter to the existing one
            book_zenbil[name] = value
            all_books = filter_zenbil_book_with_loop( book_zenbil, name )
            return all_books


def books_total_list_view(request, category=None, condition=None, author=None, best_seller=None, all_book=None):
    rating_value = request.GET.get( 'rating' );
    global all_books
    global filters
    message = 'success_db'
    filterd_data = FilteredData()
    form = SearchForm()

    if all_books is not None:
        all_books = Books.availablebook.all()
    if category is not None:  # Search by category
        all_books = zenbil_filter( 'category', category )
        if len( all_books.values() ) > 0:
            message = 'success_db'
    if condition is not None:  # search by condition
        value = 1
        all_books = zenbil_filter( condition, value )
        if len( all_books.values() ) < 0:
            message = 'not_found_db'
    if author is not None:  # search by author
        all_books = zenbil_filter( 'author', author )
        if len( all_books.values() ) > 0:
            message = 'success_db'
        else:
            words_of_author = author.split()
            length_of_author_word = len( words_of_author )
            if length_of_author_word >= 1:
                for word in words_of_author:
                    all_books = all_books.filter( author__istartswith=word )
                    if len( all_books.values() ) > 0:
                        message = 'success_db'
                    if len( all_books.values() ) <= 0:
                        message = 'not_found_db'
    if rating_value is not None:  # get by rating
        all_books = zenbil_filter( 'rating', rating_value )
    if best_seller is not None:  # search by best seller
        min_num_for_best_seller_rate = 5
        my_all_books = Books.availablebook.filter( best_seller__gte=min_num_for_best_seller_rate )
    my_all_books = all_books
    paginator = Paginator( my_all_books, 8 )
    page = request.GET.get( 'page' )
    try:
        my_all_books = paginator.page( page )
    except PageNotAnInteger:
        # if page Not an integer deliver the first page
        my_all_books = paginator.page( 1 )
    except EmptyPage:
        if request.is_ajax():
            # if the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse( '' )
        # if page is out of range deliver last page of results
        my_all_books = paginator.page( paginator.num_pages )
    if request.is_ajax():
        return render( request,
                       'books/books_ajax_list.html', {
                           'all_books': my_all_books, 'message': message} )
    return render( request,
                   'books/total_books.html', {
                       'all_books': my_all_books,
                       'message': message} )
