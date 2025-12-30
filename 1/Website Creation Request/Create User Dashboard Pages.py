import os

# Create user dashboard HTML pages
user_dashboard_pages = {
    'user-dashboard.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard - Gas Agency System</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System</div>
            <ul class="nav-menu">
                <li><a href="user-dashboard.html">Dashboard</a></li>
                <li><a href="book-cylinder.html">Book Cylinder</a></li>
                <li><a href="booking-history.html">History</a></li>
                <li><a href="notifications.html">Notifications</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="dashboard">
        <div class="container">
            <h1>Welcome, <span id="userName">User</span>!</h1>
            
            <div class="dashboard-stats">
                <div class="stat-card">
                    <h3>Cylinder Balance</h3>
                    <p class="stat-number" id="cylinderBalance">12</p>
                    <p class="stat-label">Available this year</p>
                </div>
                <div class="stat-card">
                    <h3>Total Bookings</h3>
                    <p class="stat-number" id="totalBookings">0</p>
                    <p class="stat-label">All time</p>
                </div>
                <div class="stat-card">
                    <h3>Pending Orders</h3>
                    <p class="stat-number" id="pendingOrders">0</p>
                    <p class="stat-label">Awaiting delivery</p>
                </div>
            </div>

            <div class="dashboard-actions">
                <h2>Quick Actions</h2>
                <div class="actions-grid">
                    <a href="book-cylinder.html" class="action-card">
                        <div class="icon">🛒</div>
                        <h3>Book Cylinder</h3>
                        <p>Place a new order</p>
                    </a>
                    <a href="booking-history.html" class="action-card">
                        <div class="icon">📜</div>
                        <h3>View History</h3>
                        <p>Check past bookings</p>
                    </a>
                    <a href="notifications.html" class="action-card">
                        <div class="icon">🔔</div>
                        <h3>Notifications</h3>
                        <p>View announcements</p>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/user-dashboard.js"></script>
</body>
</html>''',

    'book-cylinder.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Cylinder - Gas Agency System</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System</div>
            <ul class="nav-menu">
                <li><a href="user-dashboard.html">Dashboard</a></li>
                <li><a href="book-cylinder.html">Book Cylinder</a></li>
                <li><a href="booking-history.html">History</a></li>
                <li><a href="notifications.html">Notifications</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="form-section">
        <div class="container">
            <div class="form-container">
                <h2>Book Your Cylinder</h2>
                <p class="form-subtitle">Available Balance: <span id="availableBalance">12</span> cylinders</p>
                <form id="bookingForm">
                    <div class="form-group">
                        <label for="quantity">Number of Cylinders</label>
                        <input type="number" id="quantity" name="quantity" min="1" max="2" value="1" required>
                    </div>
                    <div class="form-group">
                        <label for="deliveryAddress">Delivery Address</label>
                        <textarea id="deliveryAddress" name="deliveryAddress" rows="3" required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="preferredDate">Preferred Delivery Date</label>
                        <input type="date" id="preferredDate" name="preferredDate" required>
                    </div>
                    <div class="form-group">
                        <label for="contactNumber">Contact Number</label>
                        <input type="tel" id="contactNumber" name="contactNumber" required>
                    </div>
                    <div class="form-group">
                        <label for="specialInstructions">Special Instructions (Optional)</label>
                        <textarea id="specialInstructions" name="specialInstructions" rows="2"></textarea>
                    </div>
                    <button type="submit" class="btn-large btn-primary">Submit Booking</button>
                </form>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/book-cylinder.js"></script>
</body>
</html>''',

    'booking-history.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booking History - Gas Agency System</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System</div>
            <ul class="nav-menu">
                <li><a href="user-dashboard.html">Dashboard</a></li>
                <li><a href="book-cylinder.html">Book Cylinder</a></li>
                <li><a href="booking-history.html">History</a></li>
                <li><a href="notifications.html">Notifications</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="content-section">
        <div class="container">
            <h2>Your Booking History</h2>
            <div id="bookingHistoryContainer">
                <p class="no-data">No bookings yet. <a href="book-cylinder.html">Book your first cylinder!</a></p>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/booking-history.js"></script>
</body>
</html>''',

    'payment.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment - Gas Agency System</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System</div>
            <ul class="nav-menu">
                <li><a href="user-dashboard.html">Dashboard</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="form-section">
        <div class="container">
            <div class="form-container">
                <h2>Payment Options</h2>
                <div class="booking-summary" id="bookingSummary">
                    <h3>Order Summary</h3>
                    <p>Booking ID: <span id="bookingId">--</span></p>
                    <p>Quantity: <span id="orderQuantity">--</span> cylinder(s)</p>
                    <p>Amount: ₹<span id="orderAmount">--</span></p>
                </div>

                <form id="paymentForm">
                    <div class="form-group">
                        <label for="paymentMethod">Select Payment Method</label>
                        <select id="paymentMethod" name="paymentMethod" required>
                            <option value="">Choose payment method</option>
                            <option value="cod">Cash on Delivery</option>
                            <option value="paytm">Paytm QR Code</option>
                        </select>
                    </div>

                    <div id="codSection" style="display:none;" class="payment-option">
                        <div class="info-box">
                            <p><strong>Cash on Delivery</strong></p>
                            <p>Pay when you receive your cylinder. Please keep exact change ready.</p>
                        </div>
                    </div>

                    <div id="paytmSection" style="display:none;" class="payment-option">
                        <div class="info-box">
                            <p><strong>Paytm Payment</strong></p>
                            <p>Scan the QR code below to complete payment:</p>
                            <div id="qrCodeContainer" class="qr-placeholder">
                                <p>QR Code will appear here</p>
                                <p class="qr-note">(In production, integrate actual Paytm QR API)</p>
                            </div>
                        </div>
                    </div>

                    <button type="submit" class="btn-large btn-primary">Confirm Payment Method</button>
                </form>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/payment.js"></script>
</body>
</html>''',

    'notifications.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notifications - Gas Agency System</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System</div>
            <ul class="nav-menu">
                <li><a href="user-dashboard.html">Dashboard</a></li>
                <li><a href="book-cylinder.html">Book Cylinder</a></li>
                <li><a href="booking-history.html">History</a></li>
                <li><a href="notifications.html">Notifications</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="content-section">
        <div class="container">
            <h2>Notifications & Announcements</h2>
            <div id="notificationsContainer">
                <p class="no-data">No notifications available.</p>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/notifications.js"></script>
</body>
</html>'''
}

# Write user dashboard HTML files
for filename, content in user_dashboard_pages.items():
    with open(f'gas_agency_website/{filename}', 'w') as f:
        f.write(content)

print("✓ Created user dashboard pages:")
print("  - user-dashboard.html (Main dashboard)")
print("  - book-cylinder.html (Booking form)")
print("  - booking-history.html (Order history)")
print("  - payment.html (Payment options)")
print("  - notifications.html (Announcements)")
print("\n✓ All user-facing pages ready")