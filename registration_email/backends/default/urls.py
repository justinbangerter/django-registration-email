"""Custom urls.py for django-registration."""
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView

from registration.backends.default.views import ActivationView
from registration_email.forms import EmailRegistrationForm
from registration_email.backends.default.views import EmailRegistrationView


urlpatterns = patterns('',
    # django-registration views
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='registration/activation_complete.html'),
        name='registration_activation_complete',
    ),
    url(r'^activate/(?P<activation_key>\w+)/$',
        ActivationView.as_view(),
        name='registration_activate',
    ),
    url(r'^register/$',
        EmailRegistrationView.as_view(),
        {'backend': 'registration.backends.default.DefaultBackend',
         'template_name': 'registration/registration_form.html',
         'form_class': EmailRegistrationForm,
         'success_url': getattr(
             settings, 'REGISTRATION_EMAIL_REGISTER_SUCCESS_URL', None),
        },
        name='registration_register',
    ),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='registration/registration_complete.html'),
        name='registration_complete',
    ),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='registration/registration_closed.html'),
        name='registration_disallowed',
    ),

    # django auth urls
    url(r'', include('registration_email.auth_urls')),
)
