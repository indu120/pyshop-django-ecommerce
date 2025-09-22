// Main JavaScript for PyShop Ecommerce

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize tooltips
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }

    // Quantity input handlers
    const quantityInputs = document.querySelectorAll('.quantity-input');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            if (this.value < 1) {
                this.value = 1;
            }
        });
    });

    // Add to cart form submission
    const addToCartForms = document.querySelectorAll('.add-to-cart-form');
    addToCartForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const button = this.querySelector('button[type="submit"]');
            const originalText = button.innerHTML;
            
            // Add loading state
            button.disabled = true;
            button.innerHTML = '<span class="loading"></span> Adding...';
            
            // Reset after 2 seconds (form will submit normally)
            setTimeout(() => {
                button.disabled = false;
                button.innerHTML = originalText;
            }, 2000);
        });
    });

    // Search functionality
    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const searchInput = this.querySelector('input[name="q"]');
            if (searchInput.value.trim() === '') {
                e.preventDefault();
                searchInput.focus();
            }
        });
    }

    // Cart update forms
    const cartUpdateForms = document.querySelectorAll('.cart-update-form');
    cartUpdateForms.forEach(form => {
        const quantityInput = form.querySelector('input[name="quantity"]');
        const updateButton = form.querySelector('button[type="submit"]');
        
        if (quantityInput && updateButton) {
            quantityInput.addEventListener('change', function() {
                updateButton.style.display = 'inline-block';
            });
        }
    });

    // Image lazy loading
    const images = document.querySelectorAll('img[data-src]');
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const image = entry.target;
                    image.src = image.dataset.src;
                    image.classList.remove('lazy');
                    imageObserver.unobserve(image);
                }
            });
        });

        images.forEach(image => {
            imageObserver.observe(image);
        });
    } else {
        // Fallback for browsers without IntersectionObserver
        images.forEach(image => {
            image.src = image.dataset.src;
        });
    }

    // Rating stars interactive
    const ratingStars = document.querySelectorAll('.rating-stars .star');
    ratingStars.forEach((star, index) => {
        star.addEventListener('click', function() {
            const rating = index + 1;
            const ratingInput = document.getElementById('id_rating');
            if (ratingInput) {
                ratingInput.value = rating;
            }
            
            // Update visual stars
            ratingStars.forEach((s, i) => {
                if (i < rating) {
                    s.classList.add('filled');
                } else {
                    s.classList.remove('filled');
                }
            });
        });

        star.addEventListener('mouseenter', function() {
            const rating = index + 1;
            ratingStars.forEach((s, i) => {
                if (i < rating) {
                    s.classList.add('hover');
                } else {
                    s.classList.remove('hover');
                }
            });
        });
    });

    // Clear rating stars hover effect
    const ratingContainer = document.querySelector('.rating-stars');
    if (ratingContainer) {
        ratingContainer.addEventListener('mouseleave', function() {
            ratingStars.forEach(star => {
                star.classList.remove('hover');
            });
        });
    }

    // Auto-hide alerts
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert && alert.parentNode) {
                alert.style.transition = 'opacity 0.5s';
                alert.style.opacity = '0';
                setTimeout(() => {
                    if (alert.parentNode) {
                        alert.parentNode.removeChild(alert);
                    }
                }, 500);
            }
        }, 5000);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Product image zoom (for product detail page)
    const productImage = document.querySelector('.product-detail-image');
    if (productImage) {
        productImage.addEventListener('click', function() {
            // Simple modal zoom implementation
            const modal = document.createElement('div');
            modal.className = 'image-modal';
            modal.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.9);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 9999;
                cursor: pointer;
            `;
            
            const modalImage = document.createElement('img');
            modalImage.src = this.src;
            modalImage.style.cssText = `
                max-width: 90%;
                max-height: 90%;
                object-fit: contain;
            `;
            
            modal.appendChild(modalImage);
            document.body.appendChild(modal);
            
            modal.addEventListener('click', function() {
                document.body.removeChild(modal);
            });
        });
    }
});

// Helper functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        animation: slideIn 0.3s ease;
    `;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    .star {
        cursor: pointer;
        transition: color 0.2s;
    }
    
    .star.filled,
    .star.hover {
        color: #ffc107;
    }
    
    .lazy {
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .lazy.loaded {
        opacity: 1;
    }
`;
document.head.appendChild(style);
