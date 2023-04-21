from django.urls import path, re_path
from . import views
app_name = 'pages'
urlpatterns = [
    path("", views.home, name='home'),
    path('destination/<int:id>', views.destination, name='destination'),
    path('crew/<int:id>', views.crew, name='crew'),
    path('technology/<int:id>', views.technology, name='technology'),
]
