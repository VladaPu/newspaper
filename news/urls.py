from django.urls import path
# Импортируем созданное нами представление
from .views import \
   PostList, PostDetail, NewsCreate, ArticlesCreate, PostUpdate, PostDelete, CategoryListView, subscribe

urlpatterns = [

   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('article/create/', ArticlesCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path ('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
   path ('categories/<int:pk>/subscribe/', subscribe, name='subscribe')
]