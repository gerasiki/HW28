from django.urls import path

from ads.views import ads

urlpatterns = [
    path('', ads.AdsView.as_view()),
    path('<int:pk>/', ads.AdDetailView.as_view()),
    path('create/', ads.AdCreateView.as_view()),
    path('<int:pk>/update/', ads.AdUpdateView.as_view()),
    path('<int:pk>/delete/', ads.AdDeleteView.as_view()),
    path('<int:pk>/upload_image/', ads.AdUploadImageView.as_view())
]
