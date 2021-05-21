from posts.views import PostDeleteView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', views.PostView.as_view()),
    path('api/posts/delete/<int:pk>', views.PostDeleteView.as_view()),
    path('api/post/<int:pk>/vote', views.VoteCreate.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]
