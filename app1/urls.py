from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.homeV,name='homepage'),
    path('createAuthor',views.createAuthor,name='author'),
    path('createBook',views.createBook,name='book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)