from django.urls import path

from .views import index, other_page, ShopsLoginView, ShopsLogoutView, ChangeUserInfoView, ChangeUserPasswordView, user_goods, RegisterUserView, RegisterDoneView, DeleteUserView

app_name = 'main'
urlpatterns = [
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register_done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/login/', ShopsLoginView.as_view(), name='login'),
    path('accounts/password_change/', ChangeUserPasswordView.as_view(), name='password_change'),
    path('acoounts/logout/', ShopsLogoutView.as_view(), name='logout'),
    path('acounts/delete_user/', DeleteUserView.as_view(), name='delete_user'),
    path('accounts/user_goods/', user_goods, name='user_goods'),
    path("accounts/profile/", ChangeUserInfoView.as_view(), name="profile"),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]
