import os

# Create directory structure for the website
os.makedirs('gas_agency_website', exist_ok=True)
os.makedirs('gas_agency_website/css', exist_ok=True)
os.makedirs('gas_agency_website/js', exist_ok=True)
os.makedirs('gas_agency_website/images', exist_ok=True)

# Create main HTML pages
html_files = {
    'index.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gas Agency System - Home</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System</div>
            <ul class="nav-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="register.html" class="btn-primary">Register</a></li>
                <li><a href="login.html" class="btn-secondary">Login</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero">
        <div class="container">
            <h1>Welcome to Gas Agency System</h1>
            <p>Book your gas cylinders online with ease. No more waiting on phone calls!</p>
            <div class="hero-buttons">
                <a href="register.html" class="btn-large btn-primary">Get Started</a>
                <a href="#features" class="btn-large btn-secondary">Learn More</a>
            </div>
        </div>
    </section>

    <section id="features" class="features">
        <div class="container">
            <h2>Why Choose Us?</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="icon">📱</div>
                    <h3>Easy Online Booking</h3>
                    <p>Book gas cylinders anytime, anywhere with our user-friendly platform</p>
                </div>
                <div class="feature-card">
                    <div class="icon">⚡</div>
                    <h3>Quick Delivery</h3>
                    <p>Fast and reliable delivery to your doorstep</p>
                </div>
                <div class="feature-card">
                    <div class="icon">💳</div>
                    <h3>Flexible Payment</h3>
                    <p>Pay via Cash on Delivery or Paytm QR code</p>
                </div>
                <div class="feature-card">
                    <div class="icon">📊</div>
                    <h3>Track History</h3>
                    <p>View all your bookings and transaction history</p>
                </div>
            </div>
        </div>
    </section>

    <section class="cta">
        <div class="container">
            <h2>Ready to Get Started?</h2>
            <p>Join thousands of satisfied customers today!</p>
            <a href="register.html" class="btn-large btn-primary">Create Account</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>''',

    'register.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Gas Agency System</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System</div>
            <ul class="nav-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="login.html">Login</a></li>
            </ul>
        </div>
    </nav>

    <section class="form-section">
        <div class="container">
            <div class="form-container">
                <h2>Create Your Account</h2>
                <p class="form-subtitle">Get 12 free cylinders for your first year!</p>
                <form id="registerForm">
                    <div class="form-group">
                        <label for="fullName">Full Name</label>
                        <input type="text" id="fullName" name="fullName" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone Number</label>
                        <input type="tel" id="phone" name="phone" required>
                    </div>
                    <div class="form-group">
                        <label for="address">Address</label>
                        <textarea id="address" name="address" rows="3" required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" name="password" required>
                    </div>
                    <div class="form-group">
                        <label for="confirmPassword">Confirm Password</label>
                        <input type="password" id="confirmPassword" name="confirmPassword" required>
                    </div>
                    <button type="submit" class="btn-large btn-primary">Register</button>
                </form>
                <p class="form-footer">Already have an account? <a href="login.html">Login here</a></p>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/register.js"></script>
</body>
</html>''',

    'login.html': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Gas Agency System</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="logo">Gas Agency System</div>
            <ul class="nav-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="register.html">Register</a></li>
            </ul>
        </div>
    </nav>

    <section class="form-section">
        <div class="container">
            <div class="form-container">
                <h2>Login to Your Account</h2>
                <form id="loginForm">
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" name="password" required>
                    </div>
                    <div class="form-group">
                        <label for="userType">Login As</label>
                        <select id="userType" name="userType">
                            <option value="user">User</option>
                            <option value="admin">Admin</option>
                        </select>
                    </div>
                    <button type="submit" class="btn-large btn-primary">Login</button>
                </form>
                <p class="form-footer">Don't have an account? <a href="register.html">Register here</a></p>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Gas Agency System. All rights reserved.</p>
        </div>
    </footer>

    <script type="module" src="js/login.js"></script>
</body>
</html>'''
}

# Write HTML files
for filename, content in html_files.items():
    with open(f'gas_agency_website/{filename}', 'w') as f:
        f.write(content)

print("✓ Created main HTML pages:")
print("  - index.html (Home page)")
print("  - register.html (User registration)")
print("  - login.html (Login page)")
print("\nDirectory structure created:")
print("  gas_agency_website/")
print("    ├── css/")
print("    ├── js/")
print("    ├── images/")
print("    ├── index.html")
print("    ├── register.html")
print("    └── login.html")