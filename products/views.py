from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product, Category, Review, Cart, CartItem, Offer
from .forms import ReviewForm


def index(request):
    """Home page with featured products and categories"""
    featured_products = Product.objects.filter(featured=True, is_active=True)[:8]
    categories = Category.objects.all()[:6]
    latest_products = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'products/index.html', context)


def product_list(request):
    """Display all products with filtering and pagination"""
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )
    
    # Sort by price
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'rating':
        products = products.order_by('-rating')
    else:
        products = products.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'query': query,
        'sort': sort,
        'category_slug': category_slug,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    """Display product detail page with reviews"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    reviews = product.reviews.all()[:10]
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]
    
    # Update product rating based on reviews
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if avg_rating:
        product.rating = round(avg_rating, 1)
        product.save()
    
    context = {
        'product': product,
        'reviews': reviews,
        'related_products': related_products,
        'review_form': ReviewForm() if request.user.is_authenticated else None,
    }
    return render(request, 'products/product_detail.html', context)


def category_products(request, slug):
    """Display products for a specific category"""
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True)
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'products/category_products.html', context)


@login_required
def add_review(request, slug):
    """Add a review for a product"""
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            try:
                review.save()
                messages.success(request, 'Your review has been added!')
            except:
                messages.error(request, 'You have already reviewed this product.')
    
    return redirect('products:product_detail', slug=slug)


def get_cart(request):
    """Get or create cart for user/session"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


@require_POST
def add_to_cart(request, product_id):
    """Add product to cart"""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart = get_cart(request)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > product.stock:
        messages.error(request, f'Only {product.stock} items available in stock.')
        return redirect('products:product_detail', slug=product.slug)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        new_quantity = cart_item.quantity + quantity
        if new_quantity > product.stock:
            messages.error(request, f'Cannot add more. Only {product.stock} items available.')
        else:
            cart_item.quantity = new_quantity
            cart_item.save()
            messages.success(request, f'{product.name} added to cart!')
    else:
        messages.success(request, f'{product.name} added to cart!')
    
    return redirect('products:cart_detail')


def cart_detail(request):
    """Display cart contents"""
    cart = get_cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'products/cart_detail.html', context)


@require_POST
def update_cart(request, item_id):
    """Update cart item quantity"""
    cart = get_cart(request)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        if quantity <= cart_item.product.stock:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            messages.error(request, f'Only {cart_item.product.stock} items available.')
    else:
        cart_item.delete()
        messages.success(request, 'Item removed from cart!')
    
    return redirect('products:cart_detail')


@require_POST
def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart = get_cart(request)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'{product_name} removed from cart!')
    return redirect('products:cart_detail')


def register(request):
    """User registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('products:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def search(request):
    """Search products"""
    query = request.GET.get('q', '')
    products = []
    
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query),
            is_active=True
        )
    
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'products/search_results.html', context)
