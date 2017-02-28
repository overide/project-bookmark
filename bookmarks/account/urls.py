from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    url(r'^$',views.dashboard,name='dashboard'),

    url(r'^login/$',
        auth_view.login,
        {'template_name': 'account/registration/login.html'},
        name='login'),

    url(r'^logout/$',
        auth_view.logout,
        {'template_name': 'account/registration/logged_out.html'},
        name='logout'),

    url(r'^logout-then-login/$',
        auth_view.logout_then_login,
        name='logout_then_login'),

    # password change urls
    url(r'^password-change/$',
        auth_view.password_change,
        {'template_name': 'account/registration/change_password_form.html'},
        name="password_change"),

    url(r'^password-change/done/$',
        auth_view.password_change_done,
        {'template_name': 'account/registration/password_change_done.html'},
        name="password_change_done"),

    # password reset urls
    url(r'^password-reset/$',
        auth_view.password_reset,
        {'template_name': 'account/registration/password_reset_form.html',
         'email_template_name': 'account/registration/password_reset_email.html'},
        name="password_reset"),

    url(r'^password-reset/done/$',
        auth_view.password_reset_done,
        {'template_name': 'account/registration/password_reset_done.html'},
        name="password_reset_done"),

    url(r'password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_view.password_reset_confirm,
        {'template_name': 'account/registration/password_reset_confirm.html'},
        name="password_reset_confirm"),

    url(r'^password-reset/complete$',
        auth_view.password_reset_complete,
        {'template_name': 'account/registration/password_reset_complete.html'},
        name="password_reset_complete"),

    url(r'register/$',
        views.Register.as_view(),
        name='register'),

    url(r'edit/$', views.edit, name="edit"),

    url(r'^users/$',
        views.UserListView.as_view(),
        name='user_list'),

    url(r'^users/follow/$',views.user_follow, name='user_follow'),
    
    url(r'^users/(?P<username>[-\w]+)/',
        views.UserDetailView.as_view(),
        name='user_detail'),

]
