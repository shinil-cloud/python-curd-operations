from django.urls import path
from ert import views


urlpatterns=[
	path('',views.home,name="home"),
	path('add',views.addErt,name="add"),
    path('<int:pk>', views.details,name="detail"),
    path('update/<int:pk>',views.updateErt, name="update"),
    path('delete/<int:pk>',views.deleteErt, name="delete"),
    
]