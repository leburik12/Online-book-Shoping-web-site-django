from django.urls import path, include
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy

app_name = 'account'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    # change password urls
    path('password_change/',
         auth_view.PasswordChangeView.as_view(
             success_url=reverse_lazy('account:password_change_done')
         ), name='password_change'),
    path('password_change/done/',
         auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # reset password
    path('password_reset/',
         auth_view.PasswordResetView.as_view(
              success_url=reverse_lazy('account:password_reset_done')
         ),
         name='password_reset'),
    path('password_reset/done/',
         auth_view.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_view.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
