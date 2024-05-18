from django.urls import path, include
from .views import GuildViewSet, Guild_WargameViewSet, SubmitFlagAPI, GuildMembersAPIView, InviteMemberToGuildAPIView
from rest_framework.routers import DefaultRouter

app_name = 'guild'

router = DefaultRouter()
router.register('', GuildViewSet)
router.register('guild-wargame', Guild_WargameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('submit-flag', SubmitFlagAPI.as_view(), name='submit_flag'),
    path('members/<int:pk>', GuildMembersAPIView.as_view(), name='members'),
    path('invite-member/<int:pk>', InviteMemberToGuildAPIView.as_view(), name='invite_member'),
]