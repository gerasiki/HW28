from django.urls import path

from ads.views import categories

urlpatterns = [
    path('', categories.CategoriesView.as_view()),
    path('<int:pk>/', categories.CategoryDetailView.as_view()),
    path('create/', categories.CategoryCreateView.as_view()),
    path('<int:pk>/update/', categories.CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', categories.CategoryDeleteView.as_view()),
    ]
