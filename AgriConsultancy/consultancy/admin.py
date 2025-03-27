from django.contrib import admin
from .models import Consultant, Booking, CropRecommendation
from .models import ContactMessage


admin.site.register(Consultant)
admin.site.register(Booking)
admin.site.register(CropRecommendation)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
