from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetails


urlpatterns = [
   # Path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view(), name='posts_list'),
   path('<int:pk>', PostDetails.as_view(), name='post'),
]
