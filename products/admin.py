from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage, Review, Offer, Cart, CartItem


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'alt_text']


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ['user', 'rating', 'title', 'comment', 'created_at']
    fields = ['user', 'rating', 'title', 'comment', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'products_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    
    def products_count(self, obj):
        return obj.products.count()
    products_count.short_description = 'Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_active', 'featured', 'image_preview', 'created_at']
    list_filter = ['category', 'is_active', 'featured', 'created_at']
    list_editable = ['price', 'stock', 'is_active', 'featured']
    search_fields = ['name', 'description', 'category__name']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at', 'rating']
    inlines = [ProductImageInline, ReviewInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description', 'short_description')
        }),
        ('Pricing', {
            'fields': ('price', 'old_price')
        }),
        ('Inventory', {
            'fields': ('stock', 'is_active')
        }),
        ('Media', {
            'fields': ('image', 'image_url')
        }),
        ('Marketing', {
            'fields': ('featured',)
        }),
        ('Metadata', {
            'fields': ('rating', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        elif obj.image_url:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.image_url)
        return "No image"
    image_preview.short_description = 'Image'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'title', 'created_at']
    list_filter = ['rating', 'created_at', 'product__category']
    search_fields = ['product__name', 'user__username', 'title', 'comment']
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('product', 'user')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'discount_type', 'discount', 'is_active', 'valid_from', 'valid_to', 'usage_status']
    list_filter = ['discount_type', 'is_active', 'valid_from', 'valid_to']
    search_fields = ['code', 'name', 'description']
    readonly_fields = ['created_at', 'used_count']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('code', 'name', 'description')
        }),
        ('Discount Details', {
            'fields': ('discount_type', 'discount', 'minimum_amount')
        }),
        ('Validity', {
            'fields': ('valid_from', 'valid_to', 'is_active')
        }),
        ('Usage', {
            'fields': ('usage_limit', 'used_count')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    def usage_status(self, obj):
        percentage = (obj.used_count / obj.usage_limit) * 100 if obj.usage_limit > 0 else 0
        if percentage >= 100:
            color = 'red'
        elif percentage >= 75:
            color = 'orange'
        else:
            color = 'green'
        return format_html(
            '<span style="color: {};">{}/{} ({}%)</span>',
            color, obj.used_count, obj.usage_limit, int(percentage)
        )
    usage_status.short_description = 'Usage'


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'get_total_price']
    
    def get_total_price(self, obj):
        return f"${obj.get_total_price()}"
    get_total_price.short_description = 'Total'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'session_key', 'items_count', 'total_price', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'session_key']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [CartItemInline]
    
    def items_count(self, obj):
        return obj.get_total_items()
    items_count.short_description = 'Items'
    
    def total_price(self, obj):
        return f"${obj.get_total_price()}"
    total_price.short_description = 'Total'


# Customize admin site header and title
admin.site.site_header = "PyShop Administration"
admin.site.site_title = "PyShop Admin"
admin.site.index_title = "Welcome to PyShop Admin Panel"
