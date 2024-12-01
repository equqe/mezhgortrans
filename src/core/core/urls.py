from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import include, path, reverse
from django.views.generic import RedirectView


def error_404_view(request: HttpRequest, exception=None):
    return HttpResponse(
        '<h1>Страница не найдена</h1><br><a href="%s">Кабинет</a>'
        % reverse("cabinet:index")
    )


def error_403_view(request: HttpRequest, exception=None):
    return HttpResponse(
        '<h1>Доступ запрещён</h1><br><a href="%s">Вход</a>' % reverse("cabinet:login")
    )


urlpatterns = [
    path("core/admin/", admin.site.urls),
    path("core/api/", include("api.urls")),
    path("core/cabinet/", include("cabinet.urls", namespace="cabinet")),
]

if settings.LANDING_ENABLED:
    urlpatterns.append(path("", include("landing.urls", namespace="landing")))


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = error_404_view
handler403 = error_403_view
