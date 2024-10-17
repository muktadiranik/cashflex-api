from cashflex.companies.models import *
from django_tenants.admin import TenantAdminMixin
from django.contrib import admin
from django_celery_beat.models import *
from django_celery_beat.admin import *
from allauth.account.models import EmailAddress
from allauth.account.admin import EmailAddressAdmin
from allauth.socialaccount.models import *
from allauth.socialaccount.admin import *


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'schema_name',)
    search_fields = ('name',)
    exclude = ('schema_name',)

    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    list_filter = ('tenant', 'is_primary')
    search_fields = ('domain',)

    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(EmailAddress)


@admin.register(EmailAddress)
class EmailAddressAdmin(EmailAddressAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(PeriodicTask)


@admin.register(PeriodicTask)
class PeriodicTaskAdmin(PeriodicTaskAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(IntervalSchedule)


@admin.register(IntervalSchedule)
class IntervalScheduleAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(CrontabSchedule)


@admin.register(CrontabSchedule)
class CrontabScheduleAdmin(CrontabScheduleAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(SolarSchedule)


@admin.register(SolarSchedule)
class SolarScheduleAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(ClockedSchedule)


@admin.register(ClockedSchedule)
class ClockedScheduleAdmin(ClockedScheduleAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(SocialApp)


@admin.register(SocialApp)
class SocialAppAdmin(SocialAppAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(SocialToken)


@admin.register(SocialToken)
class SocialTokenAdmin(SocialTokenAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True


admin.site.unregister(SocialAccount)


@admin.register(SocialAccount)
class SocialAccountAdmin(SocialAccountAdmin):
    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name == 'public':
                return False
        except:
            return True
