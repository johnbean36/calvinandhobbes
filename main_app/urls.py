from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('allbooks/', views.allbooks, name='books'),
    path('details/<int:book_id>/', views.detailbooks, name='details'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:pk>/addsales/', views.add_sales, name="add_sales"),
    path('store/create', views.StoreCreate.as_view(), name="store_create"),
    path('store/<int:pk>/update/', views.StoreUpdate.as_view(), name='store_update'),
    path('store/', views.StoreList.as_view(), name="store_list"),
    path('store/<int:pk>/', views.StoreDetail.as_view(), name="store_details"),
    path('store/<int:pk>/delete/', views.StoreDelete.as_view(), name="store_delete")
]