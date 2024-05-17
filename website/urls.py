from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('project/<int:id>', views.project, name="project"),
    path('contact', views.contact, name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)