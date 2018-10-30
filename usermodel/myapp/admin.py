from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from myapp.forms import UserChangeForm,UserCreationForm;
from myapp.models import MyUser,Profile;
from django.contrib.auth.models import Group;
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username','first_name','last_name','email', 'is_staff', 'is_active','is_admin')
    list_filter = ('is_admin','is_active')
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),
        #('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin','is_active','is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('username','email',)
    ordering = ('username','email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin);
admin.site.register(Profile);
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
