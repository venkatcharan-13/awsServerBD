from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bloodDonateApp/wbd', views.wbd, name='wbd'),
    path('bloodDonateApp/bad', views.bad, name='bad'),
    path('bloodDonateApp/saveForm',views.saveBAD,name='saving data'),
    path('bloodDonateApp/api/nbinfo', views.nbInfo.as_view()),
    path('bloodDonateApp/nb', views.nb, name='nb'),
    path('bloodDonateApp/cs', views.cs, name='cs'),
]