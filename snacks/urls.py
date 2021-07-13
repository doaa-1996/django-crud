from django.urls import path
from .views import SnackView,SnackDetailsView,SnackCreateView,SnackUpdateView,SnackDeleteView
urlpatterns=[
path('', SnackView.as_view(), name='Snacks'),
path('<int:pk>/', SnackDetailsView.as_view(),name='snack_details'),
path('snacks/new',SnackCreateView.as_view(),name='snack_create'),
path('snacks/<int:pk>/update',SnackUpdateView.as_view(),name='snack_update'),
path('snacks/<int:pk>/delete',SnackDeleteView.as_view(),name='snack_delete')
]