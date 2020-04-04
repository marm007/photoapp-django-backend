from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.filters import UsersFilterList

from rest_framework_simplejwt import views as jwt_views

from api.views.comment import CommentViewSet
from api.views.follower import FollowerRetrieve
from api.views.post import PostViewSet
from api.views.relation import RelationViewSet
from api.views.user import UsersViewSet, reset_password, forgot_password, auth, UserListPosts, \
    UserListFollowedPosts, UserListFollowedRelations, UserListPostsProfile
from django.contrib import admin
from rest_framework.authtoken.models import Token

comments_create = CommentViewSet.as_view({
    'post': 'create',
})

comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'posts', PostViewSet)
router.register(r'relations', RelationViewSet)

urlpatterns = [



    path('auth/', auth),
    path('password/reset/<slug:token>/', reset_password),
    path('password/forgot/', forgot_password),

    path('comments/<uuid:pk>/', comments_detail),

    path('posts/<uuid:pk>/comments/', comments_create),

    path('followers/<uuid:pk>/', FollowerRetrieve.as_view()),

    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('users/<uuid:pk>/posts/', UserListPostsProfile.as_view()),
    path('users/me/posts/', UserListPosts.as_view()),

    path('users/me/followed/posts/', UserListFollowedPosts.as_view()),
    path('users/me/followed/relations/', UserListFollowedRelations.as_view()),

    path('users/filter/', UsersFilterList.as_view()),
    path('', include(router.urls)),

]


admin.site.unregister(Token)