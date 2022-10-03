from django.urls import path, include

from petstagram.photos.views import add_photo, edit_photo, details_photo

urlpatterns = (
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('edit/', edit_photo, name='edit photo'),
        path('', details_photo, name='details photo'),
    ]))

)
