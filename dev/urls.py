from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name='home'),
    # path('', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('record-details/<slug:slug>',
         views.record_details, name='record-details'),
    path('record-details/<slug:slug>/delete',
         views.delete_record, name='delete-record')
]
