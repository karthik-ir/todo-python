from django.conf.urls import patterns, include, url
from taskapp import  views
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'task_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/?$', views.index),
    url(r'^addtask', views.new_task, name="newTask"),
    url(r'^register', views.register, name='register'),
    #url(r'^newUser', views.new_user, name='newUSer'),
    url(r'^login', views.user_login, name='login'),
    url(r'^$', views.user_login, name='login'),

)
