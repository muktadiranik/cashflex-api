from django_tenants.models import TenantMixin
from django.dispatch import receiver
from django_tenants.signals import *
from cashflex.companies.tasks import *
from cashflex.companies.models import *
from django.db import transaction


@receiver(post_schema_sync, sender=TenantMixin)
def created_user_client_in_background(sender, **kwargs):
    with transaction.atomic():
        from django_tenants.utils import schema_context
        from django.contrib.auth import get_user_model
        User = get_user_model()
        with schema_context(kwargs["tenant"].schema_name):
            user = User.objects.create_superuser(
                username=kwargs["tenant"].user_username,
                email=kwargs["tenant"].user_email,
            )
            user.set_password(kwargs["tenant"].user_password)
            user.save()
            domain = Domain.objects.create(
                domain=kwargs["tenant"].domain_name,
                tenant=kwargs["tenant"],
                is_primary=True
            )
            send_email_to_hr_on_company_create.delay(
                username=user.username,
                email=user.email,
                password=kwargs["tenant"].user_password,
                uuid=user.uuid,
                domain=domain.domain
            )
