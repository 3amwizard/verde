from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
	path('', views.Landing.as_view(), name='landing'),
	path('error/', views.Error.as_view(), name='error'),
]