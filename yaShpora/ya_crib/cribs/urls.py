from django.urls import path

from cribs.views import IndexListView, CribForSpintView


app_name = 'crib'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('crib/<int:pk>/',
         CribForSpintView.as_view(),
         name='crib_detail'),
]
