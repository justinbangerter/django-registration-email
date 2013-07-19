from registration.backends.default.views import RegistrationView
from registration_email.forms import EmailRegistrationForm

class EmailRegistrationView(RegistrationView):
    form_class = EmailRegistrationForm