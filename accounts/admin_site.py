from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class CustomAdminSite(admin.AdminSite):
    site_header = _("My Custom Admin Site")
    site_title = _("Admin Portal")
    index_title = _("Welcome to My Custom Admin Portal")


# Instantiate the custom AdminSite
custom_admin_site = CustomAdminSite(name='custom_admin')
