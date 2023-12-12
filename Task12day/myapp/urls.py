from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index, name="index"),
    path("login/",views.buyerlogin, name="buyerlogin"),
    path("signup/",views.buyersignup, name="buyersignup"),
    path("logout/",views.buyerlogout, name="buyerlogout"),
    path("userbuy/<int:id>",views.userbuy, name="userbuy"),
    path("buyerwallet/",views.buyerwallet, name="buyerwallet"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)