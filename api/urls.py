from django.conf.urls import url, include
from rest_framework import routers

from api.views.productViews import ProductView,ProductSearch
from api.views.users_views import UserViewSet, UserProfileViewSet, UserAuthentication, UserRegistration

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user', UserProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # ----------------------------------Authentication-----------------------------#
    url('auth', UserAuthentication.as_view(), name='User_Auth'),
    url('register', UserRegistration.as_view(), name='User_Registerh'),
    #-----------------------------------BarCode-----------------------------------#
    url('barcode',ProductView.as_view(), name='Product_all__Add' ),
    url('search', ProductSearch.as_view(), name='Product_search')

]
