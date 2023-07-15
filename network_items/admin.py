from django.contrib import admin
from network_items.models import Factory, RetailNetwork, Entrepreneur, ContactsData, Product
from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.urls import reverse
from django.utils.safestring import mark_safe


@admin.action(description='Очистить задолжность перед поставщиком')
def cancel_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'contacts')
    search_fields = ('title', )
    list_filter = ('contacts_data__city',)
    actions = [cancel_debt]

    def contacts(self, obj):
        return obj.contacts_data.city

    contacts.admin_order_field = 'contacts_data__city'


admin.site.register(Factory, FactoryAdmin)


class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'provider_link', 'contacts')
    search_fields = ('title',)
    list_filter = ('contacts_data__city',)
    actions = [cancel_debt]

    def provider_link(self, obj):
        url = reverse('admin:network_items_factory_change', args=[obj.provider.id])
        link = '<a href="%s">%s</a>' % (url, obj.provider.title)
        return mark_safe(link)

    def contacts(self, obj):
        return obj.contacts_data.city

    provider_link.short_description = 'Поставщик'

    contacts.admin_order_field = 'contacts_data__city'


admin.site.register(RetailNetwork, RetailNetworkAdmin)


class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'provider_link', 'contacts')
    search_fields = ('title',)
    list_filter = ('contacts_data__city',)
    actions = [cancel_debt]

    def provider_link(self, obj):
        url = reverse('admin:network_items_retailnetwork_change', args=[obj.provider.id])
        link = '<a href="%s">%s</a>' % (url, obj.provider.title)
        return mark_safe(link)

    def contacts(self, obj):
        return obj.contacts_data.city

    provider_link.short_description = 'Поставщик'

    contacts.admin_order_field = 'contacts_data__city'


admin.site.register(Entrepreneur, EntrepreneurAdmin)


class ContactsDataAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number')


admin.site.register(ContactsData, ContactsDataAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date')
    search_fields = ('title', )


admin.site.register(Product, ProductAdmin)
