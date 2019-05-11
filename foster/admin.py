from django.contrib import admin

from foster.models import Foster, Angel


class AngelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('הערות ניהול', {
            'fields': (
                'admin_comment',
            )
        }),
        ('פרטים אישיים', {
            'fields': (
                'full_name',
                'email',
                'phone',
                'call_at_night',
                'dob',
                'comment',
            )
        }),
        ('בית', {
            'fields': (
                'about_home',
                'address',
                'home_with_garden',
                'have_car',
            )
        }),
        ('אומנה', {
            'fields': (
                'animals',
                'foster_at_home',
                'can_pay_food',
                'can_pay_medicine',
                'can_handle_sick',
                'can_handle_bad_behaviour',
                'can_handle_aggressive',
            )
        }),
    )
    list_filter = (
        'animals',
        'call_at_night',
        'foster_at_home',
        'home_with_garden',
        'can_pay_food',
        'can_pay_medicine',
        'can_handle_sick',
        'can_handle_bad_behaviour',
        'can_handle_aggressive',
        'have_car',
    )
    search_fields = ['full_name']


admin.site.register(Angel, AngelAdmin)
admin.site.register(Foster)
