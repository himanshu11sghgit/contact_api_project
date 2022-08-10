from django.urls import path 

from .views import ContactDisplayView, ContactEditView


urlpatterns = [ 
    path('', ContactDisplayView.as_view(), name='contact_display'),
    path('<int:id>/', ContactEditView.as_view(), name='contact_edit')
]