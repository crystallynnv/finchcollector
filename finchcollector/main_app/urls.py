from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_tree/<int:tree_id>/', views.assoc_tree, name='assoc_tree'),
    path('finches/<int:finch_id>/unassoc_tree/<int:tree_id>/', views.unassoc_tree, name='unassoc_tree'),
    path('trees/', views.TreeList.as_view(), name='trees_index'),
    path('trees/<int:pk>/', views.TreeDetail.as_view(), name='trees_detail'),  
    path('trees/create/', views.TreeCreate.as_view(), name='trees_create'),
    path('trees/<int:pk>/update', views.TreeUpdate.as_view(), name='trees_update'),
    path('trees/<int:pk>/delete', views.TreeDelete.as_view(), name='trees_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]