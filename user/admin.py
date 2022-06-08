"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin


# models
from django.contrib.auth.models import User
from user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    # List of attributes that will show in the admin
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # List of links that lead to detail
    list_display_links = ('pk', 'user')
    # List of editable in situ
    list_editable = ('phone_number', 'website', 'picture')
    #Searchable Fields
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    
    # Fields to filter by 
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    # group fields
    fieldsets = (
        (
            'Profile',
            {
                # To arrange them horizontally you can do
                # placing a turple inside another turple and comma
                # (('user', 'picture'),)
                'fields': (('user', 'picture'),)
            }
        ),

        # If we don't want it to appear
        # the blue title bar we can pass None
        (
            'Extra info',
            {
                'fields': (
                    ('phone_number', 'website'),
                    ('biography'),
                )
            }
        ),
        (
            'Metadata',
            {
                'fields': (('created', 'modified'),)
            }
        ),
    )
    readonly_fields = ('created', 'modified')

# Para que ambos admins se vean 
# So that both admins are seen in one, it is done in the following way


class ProfileInline(admin.StackedInline):
        """Profile in-line admin for users."""
        model = Profile
        can_delete = False
        verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
# admin.site.register(Modelo,Clase)
admin.site.register(User, UserAdmin)