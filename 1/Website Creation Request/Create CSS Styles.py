import os

# Ensure CSS directory exists
css_dir = 'gas_agency_website/css'
os.makedirs(css_dir, exist_ok=True)

# Create comprehensive CSS stylesheet
css_content = '''/* Gas Agency System - Styles */

/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navigation */
.navbar {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
    align-items: center;
}

.nav-menu a {
    color: white;
    text-decoration: none;
    transition: opacity 0.3s;
}

.nav-menu a:hover {
    opacity: 0.8;
}

/* Buttons */
.btn-primary {
    background: #667eea;
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 5px;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: background 0.3s;
}

.btn-primary:hover {
    background: #5568d3;
}

.btn-secondary {
    background: transparent;
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 5px;
    border: 2px solid white;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-secondary:hover {
    background: white;
    color: #667eea;
}

.btn-large {
    padding: 0.75rem 2rem;
    font-size: 1.1rem;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 5rem 0;
    text-align: center;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.3rem;
    margin-bottom: 2rem;
}

.hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
}

/* Features Section */
.features {
    padding: 4rem 0;
    background: white;
}

.features h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 3rem;
    color: #333;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.feature-card {
    text-align: center;
    padding: 2rem;
    border-radius: 10px;
    background: #f8f9fa;
    transition: transform 0.3s, box-shadow 0.3s;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.feature-card .icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.feature-card h3 {
    margin-bottom: 0.5rem;
    color: #667eea;
}

/* Dashboard */
.dashboard {
    padding: 3rem 0;
    min-height: calc(100vh - 200px);
}

.dashboard h1 {
    margin-bottom: 2rem;
    color: #333;
}

.dashboard-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-bottom: 3rem;
}

.stat-card {
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    text-align: center;
}

.stat-number {
    font-size: 2.5rem;
    font-weight: bold;
    color: #667eea;
    margin: 0.5rem 0;
}

.stat-label {
    color: #666;
    font-size: 0.9rem;
}

.dashboard-actions {
    margin-top: 3rem;
}

.dashboard-actions h2 {
    margin-bottom: 1.5rem;
}

.actions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}

.action-card {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    text-decoration: none;
    color: #333;
    transition: transform 0.3s, box-shadow 0.3s;
}

.action-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}

.action-card .icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.action-card h3 {
    color: #667eea;
    margin-bottom: 0.5rem;
}

/* Forms */
.form-section {
    padding: 3rem 0;
    min-height: calc(100vh - 200px);
}

.form-container {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 2.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.1);
}

.form-container h2 {
    margin-bottom: 1rem;
    color: #333;
}

.form-subtitle {
    color: #666;
    margin-bottom: 2rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #333;
}

.form-group input,
.form-group textarea,
.form-group select {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1rem;
    font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
    outline: none;
    border-color: #667eea;
}

.form-footer {
    text-align: center;
    margin-top: 1.5rem;
}

.form-footer a {
    color: #667eea;
    text-decoration: none;
}

/* Content Section */
.content-section {
    padding: 3rem 0;
    min-height: calc(100vh - 200px);
}

.content-section h2 {
    margin-bottom: 2rem;
    color: #333;
}

/* Tables */
.table-container {
    background: white;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
}

table thead {
    background: #667eea;
    color: white;
}

table th,
table td {
    padding: 1rem;
    text-align: left;
}

table tbody tr {
    border-bottom: 1px solid #ddd;
}

table tbody tr:hover {
    background: #f8f9fa;
}

.no-data {
    text-align: center;
    color: #666;
    padding: 2rem;
}

/* Status Badges */
.status-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
}

.status-pending {
    background: #fff3cd;
    color: #856404;
}

.status-approved {
    background: #d4edda;
    color: #155724;
}

.status-denied {
    background: #f8d7da;
    color: #721c24;
}

.status-delivered {
    background: #d1ecf1;
    color: #0c5460;
}

/* Call to Action */
.cta {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 0;
    text-align: center;
}

.cta h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.cta p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

/* Payment Options */
.payment-option {
    margin: 1.5rem 0;
}

.info-box {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 5px;
    border-left: 4px solid #667eea;
}

.booking-summary {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 5px;
    margin-bottom: 2rem;
}

.qr-placeholder {
    background: white;
    padding: 2rem;
    border-radius: 5px;
    border: 2px dashed #ddd;
    text-align: center;
    margin-top: 1rem;
}

.qr-note {
    font-size: 0.85rem;
    color: #666;
    margin-top: 0.5rem;
}

/* Notifications */
.notification-card {
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
}

.notification-card h3 {
    color: #667eea;
    margin-bottom: 0.5rem;
}

.notification-date {
    font-size: 0.85rem;
    color: #666;
    margin-bottom: 1rem;
}

.existing-notifications {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid #ddd;
}

/* Filter Bar */
.filter-bar {
    margin-bottom: 1.5rem;
}

.filter-bar select {
    padding: 0.5rem 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
}

/* Footer */
footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 3rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav-menu {
        gap: 1rem;
        font-size: 0.9rem;
    }
    
    .hero h1 {
        font-size: 2rem;
    }
    
    .hero p {
        font-size: 1rem;
    }
    
    .hero-buttons {
        flex-direction: column;
    }
    
    .features-grid,
    .dashboard-stats,
    .actions-grid {
        grid-template-columns: 1fr;
    }
    
    table {
        font-size: 0.85rem;
    }
}'''

# Write CSS file
css_path = f'{css_dir}/styles.css'
with open(css_path, 'w') as f:
    f.write(css_content)

print("✓ Created comprehensive CSS stylesheet")
print(f"  File: {css_path}")
print("  - Responsive design with mobile support")
print("  - Modern gradient color scheme")
print("  - Styled components: navbar, forms, tables, cards")
print("  - Dashboard and admin panel styling")
print("  - Status badges and notification cards")
print("\n✓ CSS ready for all pages")