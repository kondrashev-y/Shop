from django.urls import path

from .api_views import (
    CategoryApiView,
    SmartphoneListApiView,
    SmartphoneDetailApiView,
    NotebookListApiView,
    CustomersListApiView,
    NotebookDetailApiView,
)

urlpatterns = [
    path('categories/<int:id>/', CategoryApiView.as_view(), name='categories'),
    path('customers/', CustomersListApiView.as_view(), name='customers_list'),
    path('smartphones/', SmartphoneListApiView.as_view(), name='smartphones_list'),
    path('smartphones/<int:id>/', SmartphoneDetailApiView.as_view(), name='smartphone_detail'),
    path('notebooks/', NotebookListApiView.as_view(), name='notebooks_list'),
    path('notebooks/<int:pk>/', NotebookDetailApiView.as_view(), name='notebook_detail'),
]

