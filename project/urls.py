"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('photos/', views.list_photos, name='list_photos'),
    path('photos/<int:pk>/', views.show_photo, name='show_photo'),
    path('photos/add/', views.add_photo, name='add_photo'),
    path('photos/<int:pk>/favorite/', views.toggle_starred_photo, name='toggle_starred_photo'),
    path('photos/<int:pk>/comments/', views.list_comments, name='list_comments'),
    path('photos/<int:pk>/delete/', views.delete_photo, name='delete_photo'),
    path('albums/', views.list_albums, name='list_albums'),
    path('albums/add/', views.add_album, name='add_album'),
    path('albums/<int:pk>/add/photo/', views.add_photo_to_album, name='add_photo_to_album'),
    path('albums/<int:pk>/favorite/', views.toggle_starred_album, name='toggle_starred_album'),
    path('albums/<int:pk>/', views.show_album, name='show_album'),
    path('albums/<int:pk>/edit/', views.edit_album, name='edit_album'),
    path('albums/<int:pk>/delete/', views.delete_album, name='delete_album'),
    path('albums/search/', views.search_photos, name='search_photos'),
    path('accounts/profile/', views.profile, name='profile'),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
