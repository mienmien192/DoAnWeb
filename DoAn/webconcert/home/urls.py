from django.conf.urls import url
from django.urls import path
from product import views

from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index,), #goi views trong index
    path('/home', views.index, name='home'),
    path('register/', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name="logout"),
    path('bookTicket/', views.bookTicket, name="bookTicket"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('detail/', views.detailproduct, name="detail"),
    path('profile/', views.profile, name="profile"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('artist/', views.artist, name="artist"),
    path('art1/', views.art1, name="art1"), #bichphuong
    path('art2/', views.art2, name="art2"),
    path('art3/', views.art3, name="art3"),
    path('art4/', views.art4, name="art4"),
    path('art5/', views.art5, name="art5"),
    path('art6/', views.art6, name="art6"),
    path('art7/', views.art7, name="art7"),
    path('event1/', views.event1, name="event1"),
    path('event2/', views.event2, name="event2"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'pages/password_reset.html'),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'pages/password_reset_sent.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'pages/password_reset_form.html'),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'pages/password_reset_done.html'),
         name="password_reset_complete"),
    path('contact/', views.contact, name="contact"),
]