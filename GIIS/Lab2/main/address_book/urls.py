from django.urls import path

from .views import ContactView, ContactListView, get_all_contacts

app_name = 'address_book'

urlpatterns = [
    path('', ContactView.as_view(),),
    path('contacts', ContactListView.as_view(),),
    path('get-all-contacts', get_all_contacts,),
]
