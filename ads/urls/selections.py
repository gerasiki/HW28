from django.urls import path

from ads.views import selections

urlpatterns = [
    path('', selections.SelectionListView.as_view()),
    path('<int:pk>/', selections.SelectionRetrieveView.as_view()),
    path('create/', selections.SelectionCreateView.as_view()),
    path('<int:pk>/update/', selections.SelectionUpdateView.as_view()),
    path('<int:pk>/delete/', selections.SelectionDeleteView.as_view()),
    ]