from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path('books', views.BookList.as_view(), name='book_list'),
    path('add_book', views.AddBook.as_view(), name='add_book'),
    path('<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
