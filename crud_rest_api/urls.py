from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^widget/$', views.get_widgets),                          # Get all widgets           GET     /widget
    re_path(r'^widget/add$', views.add_widgets),                       # Add widget                POST    /widget/add
    re_path(r'^widget/(?P<pk>[0-9]+)$', views.get_widget),             # Get single widget         GET     /widget/{id}
    re_path(r'^widget/(?P<pk>[0-9]+)/update$', views.update_widget),   # Update single widget      PUT     /widget/{id}/update
    re_path(r'^widget/(?P<pk>[0-9]+)/delete$', views.delete_widget),   # Delete single widget      DELETE  /widget/{id}/delete
]
