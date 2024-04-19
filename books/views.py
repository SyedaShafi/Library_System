from django.shortcuts import render, redirect
from . models import Books
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import CommentForm
from transactions.models import BorrowBook
# Create your views here.

class DetailBookView(DetailView):
    model = Books
    pk_url_kwarg = 'id'
    template_name = 'books/book_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.all()
        context['review_form'] = CommentForm()
        context['reviews'] = reviews
        context['book'] = Books.objects.get(pk=self.kwargs['id'])
        return context     
       
    def post(self, request, *args, **kwargs):
        review_form = CommentForm(data=self.request.POST)
        book = self.get_object()
        user_account = request.user.account
        book_id = self.kwargs['id'] 
        data =  user_account.borrowed_books.filter(pk=book_id)

        if BorrowBook.objects.filter(user = user_account, book = book).exists():
            if review_form.is_valid():
                name =  review_form.cleaned_data['name']
                email =  review_form.cleaned_data['email']
                
                if name != request.user.username or email != request.user.email:
                    messages.warning(self.request, f'Invalid username and email')
                    print(user_account)
                    print(data)
                    print(request.user.email)
                    return redirect('book_details', id= book_id)
                else:
                    new_review = review_form.save(commit=False)
                    new_review.review = book
                    new_review.save()
        else:
            messages.success(
            self.request,
            f'To make a review first borrow the book'
             )
            
    
        return self.get(request, *args, **kwargs)
    

 
