import os

# Create admin dashboard HTML pages
admin_dashboard_pages = {
    'admin-dashboard.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - Gas Agency System</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System - Admin</div>
            <ul class="nav-menu">
                <li><a href="admin-dashboard.html">Dashboard</a></li>
                <li><a href="manage-users.html">Users</a></li>
                <li><a href="manage-bookings.html">Bookings</a></li>
                <li><a href="create-notification.html">Notifications</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="dashboard">
        <div class="container">
            <h1>Admin Dashboard</h1>
            
            <div class="dashboard-stats">
                <div class="stat-card">
                    <h3>Total Users</h3>
                    <p class="stat-number" id="totalUsers">0</p>
                    <p class="stat-label">Registered customers</p>
                </div>
                <div class="stat-card">
                    <h3>Pending Bookings</h3>
                    <p class="stat-number" id="pendingBookings">0</p>
                    <p class="stat-label">Awaiting approval</p>
                </div>
                <div class="stat-card">
                    <h3>Total Bookings</h3>
                    <p class="stat-number" id="totalBookings">0</p>
                    <p class="stat-label">All time</p>
                </div>
                <div class="stat-card">
                    <h3>Active Notifications</h3>
                    <p class="stat-number" id="activeNotifications">0</p>
                    <p class="stat-label">Published</p>
                </div>
            </div>

            <div class="dashboard-actions">
                <h2>Quick Actions</h2>
                <div class="actions-grid">
                    <a href="manage-users.html" class="action-card">
                        <div class="icon">👥</div>
                        <h3>Manage Users</h3>
                        <p>View and verify users</p>
                    </a>
                    <a href="manage-bookings.html" class="action-card">
                        <div class="icon">📦</div>
                        <h3>Manage Bookings</h3>
                        <p>Approve/deny requests</p>
                    </a>
                    <a href="create-notification.html" class="action-card">
                        <div class="icon">📢</div>
                        <h3>Create Notification</h3>
                        <p>Broadcast to users</p>
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

    <script type="module" src="js/admin-dashboard.js"></script>
</body>
</html>''',

    'manage-users.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Users - Admin</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System - Admin</div>
            <ul class="nav-menu">
                <li><a href="admin-dashboard.html">Dashboard</a></li>
                <li><a href="manage-users.html">Users</a></li>
                <li><a href="manage-bookings.html">Bookings</a></li>
                <li><a href="create-notification.html">Notifications</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="content-section">
        <div class="container">
            <h2>Manage Users</h2>
            <div class="table-container">
                <table id="usersTable">
                    <thead>
                        <tr>
                            <th>User ID</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Phone</th>
                            <th>Cylinder Balance</th>
                            <th>Status</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody id="usersTableBody">
                        <tr>
                            <td colspan="7" class="no-data">No users found</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/manage-users.js"></script>
</body>
</html>''',

    'manage-bookings.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage Bookings - Admin</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System - Admin</div>
            <ul class="nav-menu">
                <li><a href="admin-dashboard.html">Dashboard</a></li>
                <li><a href="manage-users.html">Users</a></li>
                <li><a href="manage-bookings.html">Bookings</a></li>
                <li><a href="create-notification.html">Notifications</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="content-section">
        <div class="container">
            <h2>Manage Bookings</h2>
            <div class="filter-bar">
                <select id="statusFilter">
                    <option value="all">All Bookings</option>
                    <option value="pending">Pending</option>
                    <option value="approved">Approved</option>
                    <option value="delivered">Delivered</option>
                    <option value="denied">Denied</option>
                </select>
            </div>
            <div class="table-container">
                <table id="bookingsTable">
                    <thead>
                        <tr>
                            <th>Booking ID</th>
                            <th>User</th>
                            <th>Date</th>
                            <th>Quantity</th>
                            <th>Status</th>
                            <th>Payment</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody id="bookingsTableBody">
                        <tr>
                            <td colspan="7" class="no-data">No bookings found</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/manage-bookings.js"></script>
</body>
</html>''',

    'create-notification.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Notification - Admin</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System - Admin</div>
            <ul class="nav-menu">
                <li><a href="admin-dashboard.html">Dashboard</a></li>
                <li><a href="manage-users.html">Users</a></li>
                <li><a href="manage-bookings.html">Bookings</a></li>
                <li><a href="create-notification.html">Notifications</a></li>
                <li><a href="#" id="logoutBtn" class="btn-secondary">Logout</a></li>
            </ul>
        </div>
    </nav>

    <section class="form-section">
        <div class="container">
            <div class="form-container">
                <h2>Create Notification</h2>
                <p class="form-subtitle">Broadcast a message to all users</p>
                <form id="notificationForm">
                    <div class="form-group">
                        <label for="title">Notification Title</label>
                        <input type="text" id="title" name="title" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" name="message" rows="5" required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="expiryDate">Expiry Date</label>
                        <input type="date" id="expiryDate" name="expiryDate" required>
                    </div>
                    <button type="submit" class="btn-large btn-primary">Publish Notification</button>
                </form>

                <div class="existing-notifications">
                    <h3>Active Notifications</h3>
                    <div id="notificationsList">
                        <p class="no-data">No active notifications</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/create-notification.js"></script>
</body>
</html>'''
}

# Write admin dashboard HTML files
for filename, content in admin_dashboard_pages.items():
    with open(f'gas_agency_website/{filename}', 'w') as f:
        f.write(content)

print("✓ Created admin dashboard pages:")
print("  - admin-dashboard.html (Admin overview)")
print("  - manage-users.html (User management)")
print("  - manage-bookings.html (Booking approval)")
print("  - create-notification.html (Broadcast messages)")
print("\n✓ All admin pages ready")