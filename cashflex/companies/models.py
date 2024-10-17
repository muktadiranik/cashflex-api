from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Client(TenantMixin):
    name = models.CharField(_("Name of Company"), max_length=100)
    created_on = models.DateField(auto_now_add=True)
    cnpj = models.CharField(_("CNPJ"), max_length=100, blank=True, null=True, unique=True)
    razao_social = models.CharField(_("Razao Social"), max_length=100, blank=True, null=True)
    cep = models.CharField(_("CEP"), max_length=100, blank=True, null=True, unique=True)
    complement = models.CharField(_("Complement"), max_length=100, blank=True, null=True)
    street_name = models.CharField(_("Street Name"), max_length=100, blank=True, null=True)
    street_number = models.CharField(_("Street Number"), max_length=100, blank=True, null=True)
    district = models.CharField(_("District"), max_length=100, blank=True, null=True)
    state = models.CharField(_("State"), max_length=100, blank=True, null=True)
    city = models.CharField(_("City"), max_length=100, blank=True, null=True)
    employee_count = models.IntegerField(_("Number of Employees"), blank=True, null=True)
    team = models.CharField(_("Team"), max_length=100, blank=True, null=True)
    schema_name = models.CharField(_("Schema Name"), max_length=63, unique=True, db_index=True)
    user_email = models.EmailField(_("HR email"), blank=True, null=True)
    user_password = models.CharField(_("HR password"), max_length=100, blank=True, null=True)
    user_username = models.CharField(_("HR username"), max_length=100, blank=True, null=True)
    domain_name = models.CharField(_("Domain Name"), max_length=100, blank=True, null=True)

    auto_create_schema = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.schema_name = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Domain(DomainMixin):
    domain = models.CharField(max_length=100, unique=True)
    tenant = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='domains'
    )
    is_primary = models.BooleanField(default=True)

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = 'Domain'
        verbose_name_plural = 'Domains'
