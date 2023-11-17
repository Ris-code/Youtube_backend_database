
from django.urls import path
from .views import store_video, update_video_data, search_video

urlpatterns = [
    path('upload/', store_video, name='store_video'),
    path('update/', update_video_data, name='update_video_data'),
    path('search_video/', search_video, name='search_video'),
]
