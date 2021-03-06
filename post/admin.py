from django.contrib import admin

# Register your models here.
# Register your models here.
"""Posts Admins"""
from django.contrib import admin

# Register your models here.
from post.models import Post
from user.models import Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    # List of attributes to show in the admin
    list_display = ('__str__', 'title', 'photo', 'created', 'modified')
    # read-only fields
    readonly_fields = ('created', 'modified')
    # List of editable models
    list_editable = ('title', 'photo')
    # Campos de busqueda
    search_fields = (
        'profile__user__email',
        'profile__user__username',
        'profile__user__first_name',
        'profile__user__last_name',
        'title'
    )
    # Fields you can filter by
    list_filter = (
        'profile__user__is_active',
        'profile__user__is_staff',
        'created',
        'modified',
    )

