"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from django.contrib.auth.models import User
# from rest_framework import routers,serializers,viewsets
from rest_framework import routers
from polls import views
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#     model = User
#     fields = ('url','username','email','is_staff')
# class UserViewSet(viewsets.ModelViewSet):
#   """docstring for UserViewSet"""
#   queryset = User.objects.all()
#   serializer_class = UserSerializer
    
router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
router.register(r'question',views.QuestionViewSet)

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
