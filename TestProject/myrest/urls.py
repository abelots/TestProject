from django.conf.urls import url, include
from rest_framework import routers



from myrest.viewsets import TicketViewSet, AdminCommentViewSet,CreateUserView
router = routers.DefaultRouter()
router.register(r'ticket',TicketViewSet)
router.register(r'admincomment',AdminCommentViewSet)

# Wire up our API with our urls
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/$', CreateUserView.as_view(), name='user'),
]
