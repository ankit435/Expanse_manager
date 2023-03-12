from splitkaro import views
from django.urls import path

urlpatterns = [

    path('group/', views.ExpanseGroupView.as_view(), name='expanse-group'),
    path('group/<int:pk>', views.ExpanseGroupView.as_view(), name='expanse-group-pk'),
    path('expanse/', views.ExpanseView.as_view(), name='expanse'),
    path('expanse/<int:pk>', views.ExpanseView.as_view(), name='expanse-pk'),
    path('expanseuser/', views.ExpanseUserView.as_view(), name='expanse-user'),
    path('expanseuser/<int:pk>', views.ExpanseUserView.as_view(), name='expanse-user-pk'),
    path('expansegroupuser/', views.getGroupUserView.as_view(), name='expanse-group-user'),
    path('expansegroupuser/<int:pk>', views.getGroupUserView.as_view(), name='expanse-group-user-pk'),
    
    
    
]
