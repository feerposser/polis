from django.urls import path

import usuario.views as views

urlpatterns = [
    path('registrar/', views.register_profile),
    path('login/', views.login_profile),
    path('profile/', views.profile, name='user-profile'),
]
