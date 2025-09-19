// Main JavaScript for Cyber News Tracker

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert-dismissible');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

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

    // Loading indicator for form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
                submitBtn.disabled = true;
            }
        });
    });

    // News article click tracking
    const newsLinks = document.querySelectorAll('.news-article a[target="_blank"]');
    newsLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Track article clicks (could be sent to analytics)
            console.log('Article clicked:', this.href);
        });
    });
});

// Utility functions
function showLoading() {
    const loading = document.getElementById('loading');
    if (loading) {
        loading.classList.remove('d-none');
    }
}

function hideLoading() {
    const loading = document.getElementById('loading');
    if (loading) {
        loading.classList.add('d-none');
    }
}

// Search functionality
function performSearch(query) {
    if (!query.trim()) {
        return;
    }
    
    showLoading();
    window.location.href = `/search?q=${encodeURIComponent(query)}`;
}

// Category filtering
function filterByCategory(category) {
    const articles = document.querySelectorAll('.news-article');
    const buttons = document.querySelectorAll('.btn-group .btn');
    
    // Reset button states
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // Set active button
    event.target.classList.add('active');
    
    // Show/hide articles with animation
    articles.forEach(article => {
        if (category === 'all' || article.dataset.category === category) {
            article.style.display = 'block';
            article.classList.remove('hidden');
        } else {
            article.classList.add('hidden');
            setTimeout(() => {
                if (article.classList.contains('hidden')) {
                    article.style.display = 'none';
                }
            }, 300);
        }
    });
}

// API helper functions
async function fetchNews(category = 'cybersecurity', page = 1) {
    try {
        const response = await fetch(`/api/news?category=${category}&page=${page}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching news:', error);
        return { success: false, error: error.message };
    }
}

// Real-time updates
function checkForUpdates() {
    // This could be expanded to check for new articles periodically
    fetchNews().then(data => {
        if (data.success && data.articles.length > 0) {
            console.log('News data updated');
        }
    });
}

// Dark mode toggle (future feature)
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

// Initialize dark mode from localStorage
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
}

// Error handling
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
});

// Service worker registration (for future PWA features)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // navigator.serviceWorker.register('/sw.js')
        //     .then(function(registration) {
        //         console.log('SW registered: ', registration);
        //     })
        //     .catch(function(registrationError) {
        //         console.log('SW registration failed: ', registrationError);
        //     });
    });
}