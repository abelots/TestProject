from django.conf.urls import url, include
from rest_framework import routers



from myrest.viewsets import TicketViewSet, AdminCommentViewSet,CreateUserView, UserCommentViewSet
router = routers.DefaultRouter()
router.register(r'ticket',TicketViewSet, 'ticket')
router.register(r'admincomment',AdminCommentViewSet, 'admincomment')
router.register(r'usercomment',UserCommentViewSet, 'usercomment')

# Wire up our API with our urls
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/$', CreateUserView.as_view(), name='user'),
]
