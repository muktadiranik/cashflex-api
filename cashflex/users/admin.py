import pandas as pd
from django.contrib import admin
from django import forms
from django.urls import path
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from cashflex.users.forms import UserAdminChangeForm, UserAdminCreationForm
from cashflex.users.models import Department, Position, Gender, Role
from django_tenants.utils import tenant_context
User = get_user_model()


class UploadCollaboratorListForm(forms.Form):
    file = forms.FileField()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email",
         "cpf", "dob", "phone", "gender", "department", "position")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["id", "first_name", "last_name", "email", "cpf", "is_superuser"]
    list_display_links = ["first_name", "last_name", "email", "cpf"]
    search_fields = ["name"]
    change_list_template = "admin/auth/user/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(
                "upload-collaborator-list/",
                self.upload_collaborator_list,
            ),
        ]
        return new_urls + urls

    def upload_collaborator_list(self, request):
        if request.method == "GET":
            return render(
                request,
                "admin/auth/user/upload_file.html",
                {"form": UploadCollaboratorListForm()},
            )
        if request.method == "POST":
            form = UploadCollaboratorListForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES["file"]
                file_extension = file.name.split(".")[-1].lower()
                if file_extension == "xlsx" or file_extension == "xls":
                    df = pd.read_excel(file)
                elif file_extension == "csv":
                    df = pd.read_csv(file)
                else:
                    messages.error(request, "Invalid file format! Please upload a .xlsx, .xls or .csv file")
                    return render(
                        request,
                        "admin/auth/user/upload_file.html",
                        {"form": UploadCollaboratorListForm()},
                    )

                user_list = [
                    User(
                        email=j["email"],
                        cpf=j["cpf"],
                        first_name=j["first_name"],
                        last_name=j["last_name"],
                    )
                    for i, j in df.iterrows()
                ]
                with tenant_context(request.tenant):
                    User.objects.bulk_create(user_list)
                return redirect("admin:users_user_changelist")
        return render(
            request,
            "admin/auth/user/upload_file.html",
            {"form": UploadCollaboratorListForm()},
        )


@ admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]
    list_filter = ["name"]

    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name != "public":
                return True
        except:
            return False


@ admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]
    list_filter = ["name"]

    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name != "public":
                return True
        except:
            return False


@ admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]

    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name != "public":
                return True
        except:
            return False


@ admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]
    list_filter = ["name"]

    def has_module_permission(self, request):
        try:
            if request.tenant.schema_name != "public":
                return True
        except:
            return False
