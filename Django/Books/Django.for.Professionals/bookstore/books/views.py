from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.db.models import Q
from django.views import generic
from . import models


class BookListView(LoginRequiredMixin, generic.ListView):

    model = models.Book
    template_name = "books/books_list.html"
    context_object_name = "books"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):

    model = models.Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = models.Book.objects.all().prefetch_related('reviews__author',)


class SearchResultListView(generic.ListView):
    model = models.Book
    template_name = "books/search_result.html"
    context_object_name = "books"
    
    def get_queryset(self):
        search_title = self.request.GET.get("q")
        queryset = models.Book.objects.filter(
        Q(title__icontains=search_title) | Q(author__icontains=search_title)
    )
        return queryset