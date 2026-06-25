from django.contrib import admin
from .models import Service, Portfolio, Order
from .models import *

admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Career)
admin.site.register(JobApplication)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "base_price",
    )

    search_fields = (
        "title",
    )


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "client",
        "created_at",
    )

    search_fields = (
        "title",
        "client",
    )

    list_filter = (
        "created_at",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "service",
        "estimated_price",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
    )

    list_filter = (
        "status",
        "service",
    )

    ordering = (
        "-created_at",
    )