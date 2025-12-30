import os

# Ensure JS directory exists
js_dir = 'gas_agency_website/js'
os.makedirs(js_dir, exist_ok=True)

# Create JavaScript files with Firebase integration
js_files = {
    'firebase-config.js': '''// Firebase Configuration
// NOTE: Replace with your actual Firebase config values
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase (this is a template - in production use Firebase SDK)
console.log('Firebase configuration loaded');
console.log('Note: Update firebase-config.js with actual Firebase credentials');

// Export config for use in other files
export default firebaseConfig;
''',

    'main.js': '''// Main JavaScript for home page
document.addEventListener('DOMContentLoaded', function() {
    console.log('Gas Agency System loaded');
    
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
});
''',

    'register.js': '''// User Registration
import firebaseConfig from './firebase-config.js';

document.getElementById('registerForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = {
        fullName: document.getElementById('fullName').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        address: document.getElementById('address').value,
        password: document.getElementById('password').value,
        confirmPassword: document.getElementById('confirmPassword').value
    };
    
    // Validate passwords match
    if (formData.password !== formData.confirmPassword) {
        alert('Passwords do not match!');
        return;
    }
    
    // In production: Call Firebase Authentication API
    console.log('Registration data:', formData);
    
    // Simulate successful registration
    alert('Registration successful! You get 12 free cylinders for your first year.');
    
    // Store user data (in production: use Firestore)
    const userData = {
        userId: 'user_' + Date.now(),
        name: formData.fullName,
        email: formData.email,
        phone: formData.phone,
        address: formData.address,
        barrelBalance: 12,
        registrationDate: new Date().toISOString()
    };
    
    localStorage.setItem('currentUser', JSON.stringify(userData));
    
    // Redirect to user dashboard
    window.location.href = 'user-dashboard.html';
});
''',

    'login.js': '''// User Login
import firebaseConfig from './firebase-config.js';

document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const userType = document.getElementById('userType').value;
    
    console.log('Login attempt:', { email, userType });
    
    // In production: Call Firebase Authentication API
    // For demo: accept any credentials
    
    if (userType === 'admin') {
        // Admin login
        const adminData = {
            userId: 'admin_' + Date.now(),
            name: 'Admin User',
            email: email,
            role: 'admin'
        };
        localStorage.setItem('currentUser', JSON.stringify(adminData));
        window.location.href = 'admin-dashboard.html';
    } else {
        // User login - check if registered
        let userData = localStorage.getItem('currentUser');
        if (!userData) {
            // Create demo user if not exists
            userData = {
                userId: 'user_' + Date.now(),
                name: 'Demo User',
                email: email,
                phone: '1234567890',
                address: 'Demo Address',
                barrelBalance: 12
            };
            localStorage.setItem('currentUser', JSON.stringify(userData));
        }
        window.location.href = 'user-dashboard.html';
    }
});
''',

    'user-dashboard.js': '''// User Dashboard
import firebaseConfig from './firebase-config.js';

document.addEventListener('DOMContentLoaded', function() {
    // Check if user is logged in
    const currentUser = JSON.parse(localStorage.getItem('currentUser') || '{}');
    
    if (!currentUser.userId) {
        window.location.href = 'login.html';
        return;
    }
    
    // Display user name
    document.getElementById('userName').textContent = currentUser.name || 'User';
    
    // Display cylinder balance
    document.getElementById('cylinderBalance').textContent = currentUser.barrelBalance || 12;
    
    // Get bookings from localStorage
    const bookings = JSON.parse(localStorage.getItem('userBookings') || '[]');
    document.getElementById('totalBookings').textContent = bookings.length;
    
    // Count pending orders
    const pendingOrders = bookings.filter(b => b.status === 'pending').length;
    document.getElementById('pendingOrders').textContent = pendingOrders;
    
    // Logout button
    document.getElementById('logoutBtn').addEventListener('click', function(e) {
        e.preventDefault();
        localStorage.removeItem('currentUser');
        window.location.href = 'index.html';
    });
});
''',

    'book-cylinder.js': '''// Cylinder Booking
import firebaseConfig from './firebase-config.js';

document.addEventListener('DOMContentLoaded', function() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser') || '{}');
    
    if (!currentUser.userId) {
        window.location.href = 'login.html';
        return;
    }
    
    // Display available balance
    document.getElementById('availableBalance').textContent = currentUser.barrelBalance || 12;
    document.getElementById('deliveryAddress').value = currentUser.address || '';
    document.getElementById('contactNumber').value = currentUser.phone || '';
    
    // Set minimum date to tomorrow
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    document.getElementById('preferredDate').min = tomorrow.toISOString().split('T')[0];
    
    document.getElementById('bookingForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const quantity = parseInt(document.getElementById('quantity').value);
        
        // Check balance
        if (quantity > currentUser.barrelBalance) {
            alert('Insufficient balance! You have ' + currentUser.barrelBalance + ' cylinders available.');
            return;
        }
        
        // Create booking
        const booking = {
            bookingId: 'BK' + Date.now(),
            userId: currentUser.userId,
            userName: currentUser.name,
            quantity: quantity,
            deliveryAddress: document.getElementById('deliveryAddress').value,
            preferredDate: document.getElementById('preferredDate').value,
            contactNumber: document.getElementById('contactNumber').value,
            specialInstructions: document.getElementById('specialInstructions').value,
            bookingDate: new Date().toISOString(),
            status: 'pending',
            paymentMethod: null,
            paymentStatus: 'pending'
        };
        
        // Save booking
        const bookings = JSON.parse(localStorage.getItem('userBookings') || '[]');
        bookings.push(booking);
        localStorage.setItem('userBookings', JSON.stringify(bookings));
        
        // Save all bookings (for admin)
        const allBookings = JSON.parse(localStorage.getItem('allBookings') || '[]');
        allBookings.push(booking);
        localStorage.setItem('allBookings', JSON.stringify(allBookings));
        
        alert('Booking submitted successfully! Booking ID: ' + booking.bookingId);
        
        // Redirect to payment
        localStorage.setItem('currentBooking', JSON.stringify(booking));
        window.location.href = 'payment.html';
    });
    
    // Logout
    document.getElementById('logoutBtn').addEventListener('click', function(e) {
        e.preventDefault();
        localStorage.removeItem('currentUser');
        window.location.href = 'index.html';
    });
});
''',

    'booking-history.js': '''// Booking History
import firebaseConfig from './firebase-config.js';

document.addEventListener('DOMContentLoaded', function() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser') || '{}');
    
    if (!currentUser.userId) {
        window.location.href = 'login.html';
        return;
    }
    
    const bookings = JSON.parse(localStorage.getItem('userBookings') || '[]');
    const container = document.getElementById('bookingHistoryContainer');
    
    if (bookings.length === 0) {
        container.innerHTML = '<p class="no-data">No bookings yet. <a href="book-cylinder.html">Book your first cylinder!</a></p>';
        return;
    }
    
    // Display bookings
    container.innerHTML = bookings.map(booking => `
        <div class="notification-card">
            <h3>Booking #${booking.bookingId}</h3>
            <p><strong>Date:</strong> ${new Date(booking.bookingDate).toLocaleDateString()}</p>
            <p><strong>Quantity:</strong> ${booking.quantity} cylinder(s)</p>
            <p><strong>Delivery Date:</strong> ${booking.preferredDate}</p>
            <p><strong>Status:</strong> <span class="status-badge status-${booking.status}">${booking.status}</span></p>
            <p><strong>Payment:</strong> ${booking.paymentMethod || 'Not selected'} - ${booking.paymentStatus}</p>
        </div>
    `).join('');
    
    // Logout
    document.getElementById('logoutBtn').addEventListener('click', function(e) {
        e.preventDefault();
        localStorage.removeItem('currentUser');
        window.location.href = 'index.html';
    });
});
''',

    'payment.js': '''// Payment Processing
import firebaseConfig from './firebase-config.js';

document.addEventListener('DOMContentLoaded', function() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser') || '{}');
    const currentBooking = JSON.parse(localStorage.getItem('currentBooking') || '{}');
    
    if (!currentUser.userId || !currentBooking.bookingId) {
        window.location.href = 'user-dashboard.html';
        return;
    }
    
    // Display booking summary
    document.getElementById('bookingId').textContent = currentBooking.bookingId;
    document.getElementById('orderQuantity').textContent = currentBooking.quantity;
    const amount = currentBooking.quantity * 850; // ₹850 per cylinder
    document.getElementById('orderAmount').textContent = amount;
    
    // Payment method selection
    document.getElementById('paymentMethod').addEventListener('change', function() {
        const method = this.value;
        document.getElementById('codSection').style.display = method === 'cod' ? 'block' : 'none';
        document.getElementById('paytmSection').style.display = method === 'paytm' ? 'block' : 'none';
    });
    
    // Submit payment
    document.getElementById('paymentForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const paymentMethod = document.getElementById('paymentMethod').value;
        
        if (!paymentMethod) {
            alert('Please select a payment method');
            return;
        }
        
        // Update booking with payment info
        currentBooking.paymentMethod = paymentMethod;
        currentBooking.paymentStatus = paymentMethod === 'cod' ? 'pending' : 'completed';
        
        // Update in localStorage
        const bookings = JSON.parse(localStorage.getItem('userBookings') || '[]');
        const index = bookings.findIndex(b => b.bookingId === currentBooking.bookingId);
        if (index !== -1) {
            bookings[index] = currentBooking;
            localStorage.setItem('userBookings', JSON.stringify(bookings));
        }
        
        // Update all bookings
        const allBookings = JSON.parse(localStorage.getItem('allBookings') || '[]');
        const allIndex = allBookings.findIndex(b => b.bookingId === currentBooking.bookingId);
        if (allIndex !== -1) {
            allBookings[allIndex] = currentBooking;
            localStorage.setItem('allBookings', JSON.stringify(allBookings));
        }
        
        // Clear current booking
        localStorage.removeItem('currentBooking');
        
        alert('Payment method confirmed! Your booking is being processed.');
        window.location.href = 'user-dashboard.html';
    });
    
    // Logout
    document.getElementById('logoutBtn').addEventListener('click', function(e) {
        e.preventDefault();
        localStorage.removeItem('currentUser');
        window.location.href = 'index.html';
    });
});
''',

    'notifications.js': '''// User Notifications
import firebaseConfig from './firebase-config.js';

document.addEventListener('DOMContentLoaded', function() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser') || '{}');
    
    if (!currentUser.userId) {
        window.location.href = 'login.html';
        return;
    }
    
    const notifications = JSON.parse(localStorage.getItem('notifications') || '[]');
    const container = document.getElementById('notificationsContainer');
    
    // Filter active notifications
    const activeNotifications = notifications.filter(n => {
        const expiry = new Date(n.expiryDate);
        return n.active && expiry > new Date();
    });
    
    if (activeNotifications.length === 0) {
        container.innerHTML = '<p class="no-data">No notifications available.</p>';
        return;
    }
    
    container.innerHTML = activeNotifications.map(notification => `
        <div class="notification-card">
            <h3>${notification.title}</h3>
            <p class="notification-date">${new Date(notification.createdDate).toLocaleDateString()}</p>
            <p>${notification.message}</p>
        </div>
    `).join('');
    
    // Logout
    document.getElementById('logoutBtn').addEventListener('click', function(e) {
        e.preventDefault();
        localStorage.removeItem('currentUser');
        window.location.href = 'index.html';
    });
});
'''
}

# Write JavaScript files
for filename, content in js_files.items():
    with open(f'{js_dir}/{filename}', 'w') as f:
        f.write(content)

print("✓ Created JavaScript files with Firebase integration:")
print("  - firebase-config.js (Firebase configuration)")
print("  - main.js (Home page functionality)")
print("  - register.js (User registration)")
print("  - login.js (Authentication)")
print("  - user-dashboard.js (Dashboard logic)")
print("  - book-cylinder.js (Booking system)")
print("  - booking-history.js (Order history)")
print("  - payment.js (Payment processing)")
print("  - notifications.js (Notification display)")
print("\n✓ Using localStorage for demo (replace with Firebase in production)")