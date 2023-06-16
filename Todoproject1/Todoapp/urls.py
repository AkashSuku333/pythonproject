from . import views
from django.urls import path
app_name = 'Todoapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listhome/',views.Tasklistview.as_view(),name='listhome'),
    path('detailclass/<int:pk>/',views.Taskdetailview.as_view(),name='detailclass'),
    path('updateclass/<int:pk>/',views.Taskupdateview.as_view(),name='updateclass'),
    path('deleteclass/<int:pk>/',views.Taskdeleteview.as_view(),name='deleteclass'),
]