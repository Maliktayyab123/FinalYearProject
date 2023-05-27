from django.contrib import admin
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = "Helping Hands"
    site_title = "Helping Hands"
    site_header = "Helping Hands"
    index_title = "Welcome to Helping Hands Dashboard"


admin_site = MyAdminSite(name="myApp")

from myApp.models import (
    AdoptChild,
    ContactUs,
    Achievement,
    Notification,
)


# Register your models here.
class AdoptChildAdmin(admin.ModelAdmin):
    list_display = ["husb_name", "wife_name"]


admin.site.register(AdoptChild)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]


admin.site.register(ContactUs)


from .models import Notification, UserNotification


class UserNotificationInline(admin.TabularInline):
    model = UserNotification
    extra = 1


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "message", "created_at", "get_consent")
    inlines = [UserNotificationInline]

    def get_consent(self, obj):
        return ", ".join(
            [
                str(user_notification.consent)
                for user_notification in obj.usernotification_set.all()
            ]
        )

    get_consent.short_description = "Consent"


admin.site.register(Notification, NotificationAdmin)


admin.site.register(Achievement)


from django.contrib import admin
from .models import MissingPerson, DiscussionComment


admin.site.register(MissingPerson)

admin.site.register(DiscussionComment)
