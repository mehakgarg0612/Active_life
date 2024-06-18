# urls.py

from django.contrib import admin
from django.urls import path
from fitness import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about'),
    path('services/', views.services, name='services'),
    path('membership/', views.membership, name='membership'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contactus'),  
    path('login/', views.user_login, name='login'),  
    path('forgotpass/', views.forgotpass, name='forgotpassword'),  
    path('success/', views.signup, name='success'), 
    path('login/success/', views.login_success, name='login_success'),
    path('thirty_day_challenge/', views.thirty_day_challenge, name='thirty_day_challenge'),
    path('thirty_day_challenge/success/', views.success_join_challenge, name='success_join_challenge'),
    path('eating/', views.eating_view, name='eating'),
    path('reaching/',views.reach, name='reach'),
    path('silver/', views.silver_membership, name='silver_membership'),
    path('successsilver/', views.success_silver, name='success_silver'),
    path('gold/', views.gold_membership, name='gold_membership'),
    path('successgold/', views.success_gold, name='success_gold'),
    path('contact/success/', views.contact_success, name='contact_success'),
     
]
