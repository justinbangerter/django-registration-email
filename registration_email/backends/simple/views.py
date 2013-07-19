from registration.backends.simple.views import RegistrationView
from registration_email.forms import EmailRegistrationForm

class EmailRegistrationView(RegistrationView):
    form_class = EmailRegistrationForm