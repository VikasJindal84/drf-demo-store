from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from customer.views import CustomerListView, CustomerDetailView

schema_view = get_schema_view(
   openapi.Info(
      title="Store API",
      default_version='v1',
      description="Store description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vikasjindal1984@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [

	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path("customers/<int:pk>", csrf_exempt(CustomerDetailView.as_view())),
	re_path("customers", csrf_exempt(CustomerListView.as_view())),

]