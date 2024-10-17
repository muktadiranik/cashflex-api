from django.contrib import admin
from .models import *


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'website', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'website')
    prepopulated_fields = {'slug': ('name',)}


class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('question', 'answer')
    prepopulated_fields = {'slug': ('question',)}


class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url')
    search_fields = ('platform', 'url')


admin.site.register(Partner, PartnerAdmin)
admin.site.register(FAQCategory, FAQCategoryAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(TrainingType, TrainingTypeAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
