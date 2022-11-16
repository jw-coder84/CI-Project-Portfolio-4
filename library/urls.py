from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.BookList.as_view(), name="home"),
    path('<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
