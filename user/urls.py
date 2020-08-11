from django.conf.urls import url
from django.urls import include, path

"""from .views import UserListView,CreateUserView"""

urlpatterns = [


    url(r'^rest-auth/', include('rest_auth.urls'))
]

"""path('user/', UserListView.as_view()),
 path('create/', CreateUserView.as_view()),"""