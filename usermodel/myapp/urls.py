from django.urls import path,include;
from django.contrib.auth import views as rest_view;
from myapp import views;
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path('password-change/',rest_view.PasswordChangeView.as_view(template_name="password-change.html"),name="password_change"),
    path('password-change/done/',rest_view.PasswordChangeDoneView.as_view(template_name="password-change-done.html"),name="password_change_done"),
    path('password-reset/',
        rest_view.PasswordResetView.as_view(template_name="password-reset.html"),name="password_reset"),
    path('password-reset/done',
        rest_view.PasswordResetDoneView.as_view(template_name="password-reset-done.html"),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
        rest_view.PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html"),name="password_reset_confirm"),
    path('password-reset-comlplete/',
        rest_view.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"),name="password_reset_complete"),
]
