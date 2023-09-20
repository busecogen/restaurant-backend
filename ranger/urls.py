from . import views
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

app_name = 'menu'

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('list/', views.MenuListView.as_view(), name='menu_list'),
    path('note/create/', views.NoteCreateView.as_view(), name='create_notes'),
    path('note/list/', views.NoteListView.as_view(), name='list_notes'),
    path('note/delete/', views.NoteDeleteView.as_view(), name='delete_notes'),
    path('case/', views.CaseRetrieve.as_view(), name='case'),

]
