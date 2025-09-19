// Main JavaScript for Cyber News 2025

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Initialize Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add loading states to buttons
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
                
                // Re-enable after 3 seconds as fallback
                setTimeout(() => {
                    submitBtn.classList.remove('loading');
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    });

    // Initialize bookmark functionality
    initializeBookmarks();
    
    // Initialize auto-refresh
    initializeAutoRefresh();
}

function initializeBookmarks() {
    // Load and display bookmark count
    const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
    console.log(`Loaded ${bookmarks.length} bookmarks`);
    
    // Add bookmark indicator to navbar if there are bookmarks
    if (bookmarks.length > 0) {
        const navbar = document.querySelector('.navbar-nav');
        if (navbar && !document.querySelector('#bookmarkIndicator')) {
            const bookmarkItem = document.createElement('li');
            bookmarkItem.className = 'nav-item';
            bookmarkItem.innerHTML = `
                <a class="nav-link" href="#" id="bookmarkIndicator" title="View Bookmarks">
                    <i class="fas fa-bookmark"></i> 
                    <span class="badge bg-warning text-dark">${bookmarks.length}</span>
                </a>
            `;
            navbar.insertBefore(bookmarkItem, navbar.firstChild);
            
            // Add click handler for bookmarks
            document.getElementById('bookmarkIndicator').addEventListener('click', function(e) {
                e.preventDefault();
                showBookmarks();
            });
        }
    }
}

function showBookmarks() {
    const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
    
    if (bookmarks.length === 0) {
        alert('No bookmarks saved yet!');
        return;
    }
    
    const modal = document.createElement('div');
    modal.className = 'modal fade';
    modal.innerHTML = `
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">
                        <i class="fas fa-bookmark"></i> Your Bookmarks
                    </h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <div class="list-group">
                        ${bookmarks.map(bookmark => `
                            <div class="list-group-item d-flex justify-content-between align-items-start">
                                <div class="ms-2 me-auto">
                                    <div class="fw-bold">${bookmark.title}</div>
                                    <small class="text-muted">Saved: ${new Date(bookmark.date).toLocaleDateString()}</small>
                                </div>
                                <div>
                                    <a href="${bookmark.url}" target="_blank" class="btn btn-sm btn-outline-primary me-2">
                                        <i class="fas fa-external-link-alt"></i>
                                    </a>
                                    <button class="btn btn-sm btn-outline-danger" onclick="removeBookmark('${bookmark.url}')">
                                        <i class="fas fa-trash"></i>
                                    </button>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" onclick="clearAllBookmarks()">
                        <i class="fas fa-trash"></i> Clear All
                    </button>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    const bsModal = new bootstrap.Modal(modal);
    bsModal.show();
    
    modal.addEventListener('hidden.bs.modal', function() {
        document.body.removeChild(modal);
    });
}

function removeBookmark(url) {
    let bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
    bookmarks = bookmarks.filter(bookmark => bookmark.url !== url);
    localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
    
    // Refresh the modal and indicator
    const modal = document.querySelector('.modal');
    if (modal) {
        bootstrap.Modal.getInstance(modal).hide();
    }
    setTimeout(() => {
        initializeBookmarks();
        showBookmarks();
    }, 300);
}

function clearAllBookmarks() {
    if (confirm('Are you sure you want to clear all bookmarks?')) {
        localStorage.removeItem('bookmarks');
        const modal = document.querySelector('.modal');
        if (modal) {
            bootstrap.Modal.getInstance(modal).hide();
        }
        
        // Remove bookmark indicator
        const indicator = document.getElementById('bookmarkIndicator');
        if (indicator) {
            indicator.parentElement.remove();
        }
    }
}

function initializeAutoRefresh() {
    // Check if we're on the main news page
    if (window.location.pathname === '/' || window.location.pathname === '/index') {
        // Get refresh interval from admin settings (default 5 minutes)
        const refreshInterval = 5 * 60 * 1000; // 5 minutes in milliseconds
        
        // Add a refresh indicator
        const refreshIndicator = document.createElement('div');
        refreshIndicator.id = 'refreshIndicator';
        refreshIndicator.className = 'position-fixed bottom-0 end-0 p-3';
        refreshIndicator.style.cssText = 'z-index: 1000; opacity: 0.7;';
        refreshIndicator.innerHTML = `
            <div class="bg-primary text-white p-2 rounded">
                <small>
                    <i class="fas fa-sync-alt"></i> 
                    Auto-refresh in <span id="refreshTimer">5:00</span>
                </small>
            </div>
        `;
        document.body.appendChild(refreshIndicator);
        
        // Start countdown timer
        startRefreshCountdown(refreshInterval);
    }
}

function startRefreshCountdown(totalTime) {
    let timeLeft = totalTime;
    const timerElement = document.getElementById('refreshTimer');
    
    const countdown = setInterval(() => {
        timeLeft -= 1000;
        
        if (timeLeft <= 0) {
            clearInterval(countdown);
            location.reload();
            return;
        }
        
        const minutes = Math.floor(timeLeft / 60000);
        const seconds = Math.floor((timeLeft % 60000) / 1000);
        
        if (timerElement) {
            timerElement.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        }
    }, 1000);
}

// Utility functions
function showToast(message, type = 'info') {
    const toastContainer = document.getElementById('toastContainer') || createToastContainer();
    
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    toastContainer.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    toast.addEventListener('hidden.bs.toast', function() {
        toastContainer.removeChild(toast);
    });
}

function createToastContainer() {
    const container = document.createElement('div');
    container.id = 'toastContainer';
    container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
    container.style.zIndex = '9999';
    document.body.appendChild(container);
    return container;
}

// Export functions for global use
window.CyberNews = {
    showToast,
    showBookmarks,
    removeBookmark,
    clearAllBookmarks,
    initializeBookmarks
};