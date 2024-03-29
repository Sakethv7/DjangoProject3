from django.urls import path
from api import views

urlpatterns = [
    path('login', views.login, name='login'), # URL pattern for the login view, accessed via 'login' at the end of the base URL
    path('signup', views.signup, name='signup'),
    path('test_token', views.test_token, name='test_token'),

    path('create', views.add_items, name='create'),
    path('getAllItems/', views.get_all_items, name='get_all_items'),
    path('getAllItemsbyParameters/', views.get_all_itemsbyParameters, name='get_all_items_by_parameters')  # URL pattern for retrieving items by parameters,
    # accessed via 'getAllItemsbyParameters/' (trailing slash or a question mark is included)
]
