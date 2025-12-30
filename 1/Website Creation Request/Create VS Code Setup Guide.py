import os

# Create comprehensive VS Code setup and run guide
vscode_guide_content = """# 🚀 VS Code Setup & Run Guide - Gas Agency Website

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [VS Code Extensions](#vs-code-extensions)
4. [Project Structure](#project-structure)
5. [Running Locally](#running-locally)
6. [Firebase Deployment](#firebase-deployment)
7. [Common Issues & Troubleshooting](#common-issues--troubleshooting)

---

## 📌 Prerequisites

Before you start, ensure you have the following installed:

- **Node.js** (v14 or higher) - [Download here](https://nodejs.org/)
- **Visual Studio Code** - [Download here](https://code.visualstudio.com/)
- **Git** (optional, for version control) - [Download here](https://git-scm.com/)
- **Firebase Account** - [Sign up here](https://firebase.google.com/)

---

## 🛠️ Initial Setup

### Step 1: Open Project in VS Code

1. **Extract the project folder** to your desired location
2. **Open VS Code**
3. Click `File` → `Open Folder` and select the `gas_agency_website` folder
4. VS Code will load the project structure

### Step 2: Install Firebase CLI

Open the integrated terminal in VS Code (`Ctrl+\`` or `View` → `Terminal`) and run:

```bash
npm install -g firebase-tools
```

Verify installation:

```bash
firebase --version
```

### Step 3: Login to Firebase

```bash
firebase login
```

This will open a browser window for authentication. Sign in with your Google account.

---

## 🔌 VS Code Extensions

Install these recommended extensions to enhance your development experience:

### Essential Extensions:

1. **Live Server** (ritwickdey.LiveServer)
   - Right-click on `index.html` and select "Open with Live Server"
   - Enables live reload during development
   
2. **Firebase Explorer** (jsayol.firebase-explorer)
   - Manage Firebase projects directly from VS Code
   - View Firestore data and collections

3. **HTML CSS Support** (ecmel.vscode-html-css)
   - Better IntelliSense for HTML class attributes
   - Auto-completion for CSS classes

4. **JavaScript (ES6) code snippets** (xabikos.JavaScriptSnippets)
   - Faster JavaScript coding with snippets

5. **Path Intellisense** (christian-kohler.path-intellisense)
   - Auto-complete file paths

6. **Prettier - Code Formatter** (esbenp.prettier-vscode)
   - Format HTML, CSS, and JavaScript files
   - Set as default formatter: `Ctrl+Shift+P` → "Format Document"

7. **ESLint** (dbaeumer.vscode-eslint)
   - Identify and fix JavaScript code issues

### How to Install Extensions:

1. Click the Extensions icon in VS Code sidebar (or press `Ctrl+Shift+X`)
2. Search for the extension name
3. Click "Install"

---

## 📁 Project Structure

```
gas_agency_website/
├── index.html              # Landing page
├── login.html              # User login
├── register.html           # User registration
├── user-dashboard.html     # User dashboard
├── admin-dashboard.html    # Admin dashboard
├── book-cylinder.html      # Booking form
├── payment.html            # Payment page
├── booking-history.html    # Order history
├── notifications.html      # Notifications
├── manage-bookings.html    # Admin: Manage bookings
├── manage-users.html       # Admin: Manage users
├── create-notification.html # Admin: Create notifications
│
├── css/
│   └── styles.css          # Main stylesheet
│
├── js/
│   ├── firebase-config.js  # Firebase configuration
│   ├── main.js             # Shared utilities
│   ├── login.js            # Login functionality
│   ├── register.js         # Registration functionality
│   ├── user-dashboard.js   # User dashboard logic
│   ├── admin-dashboard.js  # Admin dashboard logic
│   ├── book-cylinder.js    # Booking logic
│   ├── payment.js          # Payment processing
│   ├── booking-history.js  # Order history logic
│   ├── notifications.js    # Notifications logic
│   ├── manage-bookings.js  # Admin: Manage bookings
│   ├── manage-users.js     # Admin: Manage users
│   └── create-notification.js # Admin: Create notifications
│
├── images/                 # Images and assets
├── firebase.json           # Firebase configuration
├── firestore.rules         # Firestore security rules
├── firestore.indexes.json  # Firestore indexes
└── README.md               # Project documentation
```

---

## 🖥️ Running Locally

### Method 1: Using Live Server Extension (Recommended)

1. **Install Live Server extension** (see Extensions section above)
2. **Right-click** on `index.html` in VS Code
3. Select **"Open with Live Server"**
4. Your default browser will open at `http://127.0.0.1:5500/index.html`
5. **Live reload** is enabled - changes are reflected automatically

### Method 2: Using Firebase Local Emulator

1. **Initialize Firebase** (if not already done):

```bash
firebase init hosting
```

Select:
- Use existing project
- Set `gas_agency_website` as the public directory
- Configure as single-page app: **No**
- Don't overwrite existing files

2. **Serve locally**:

```bash
firebase serve
```

3. Open browser to `http://localhost:5000`

### Method 3: Using Python HTTP Server

If you have Python installed:

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Open browser to `http://localhost:8000`

### Method 4: Using Node.js http-server

```bash
# Install globally
npm install -g http-server

# Run from project directory
http-server
```

Open browser to `http://localhost:8080`

---

## 🚀 Firebase Deployment

### Step 1: Configure Firebase Project

1. **Go to [Firebase Console](https://console.firebase.google.com/)**
2. **Create a new project** (or select existing)
3. **Enable Firestore Database**:
   - Go to Firestore Database
   - Click "Create Database"
   - Start in **production mode**
4. **Enable Authentication**:
   - Go to Authentication → Sign-in method
   - Enable **Email/Password**
5. **Get Firebase config**:
   - Go to Project Settings → General
   - Scroll to "Your apps" → Web app
   - Copy the configuration object

### Step 2: Update Firebase Configuration

1. **Open** `js/firebase-config.js` in VS Code
2. **Replace** the configuration with your Firebase project details:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

3. **Save** the file (`Ctrl+S`)

### Step 3: Initialize Firebase Hosting

Open terminal in VS Code and run:

```bash
firebase init hosting
```

Follow the prompts:
- **Use an existing project**: Select your Firebase project
- **Public directory**: Press Enter (current directory)
- **Single-page app**: No
- **Overwrite files**: No

### Step 4: Deploy to Firebase

```bash
firebase deploy
```

Or deploy only hosting:

```bash
firebase deploy --only hosting
```

### Step 5: Deploy Firestore Rules and Indexes

```bash
firebase deploy --only firestore:rules,firestore:indexes
```

### Step 6: Access Your Deployed Site

After deployment, you'll see:

```
✔  Deploy complete!

Project Console: https://console.firebase.google.com/project/YOUR_PROJECT_ID/overview
Hosting URL: https://YOUR_PROJECT_ID.web.app
```

Open the Hosting URL in your browser to access your deployed website.

---

## 🛠️ Common Issues & Troubleshooting

### Issue 1: Firebase CLI Not Found

**Error**: `firebase: command not found`

**Solution**:
```bash
# Reinstall Firebase CLI
npm install -g firebase-tools

# On Mac/Linux, you might need sudo
sudo npm install -g firebase-tools
```

### Issue 2: Firebase Login Issues

**Error**: Browser doesn't open or login fails

**Solution**:
```bash
# Use the login with localhost
firebase login --reauth

# Or use interactive mode
firebase login --interactive
```

### Issue 3: CORS Errors in Local Development

**Error**: `Access to fetch has been blocked by CORS policy`

**Solution**:
- Use Live Server or Firebase serve instead of opening HTML files directly
- Never open HTML files with `file://` protocol for Firebase projects

### Issue 4: Firebase Configuration Not Working

**Error**: `Firebase: Error (auth/invalid-api-key)`

**Solution**:
- Double-check your `firebase-config.js` has the correct values
- Ensure you copied the entire config object from Firebase Console
- Clear browser cache and reload

### Issue 5: Deployment Fails

**Error**: `HTTP Error: 403, The caller does not have permission`

**Solution**:
```bash
# Re-authenticate
firebase logout
firebase login

# Ensure you're using the correct project
firebase use YOUR_PROJECT_ID

# Try deploying again
firebase deploy
```

### Issue 6: Live Server Not Working

**Error**: Live Server doesn't start

**Solution**:
- Ensure Live Server extension is installed
- Right-click on an HTML file (not in sidebar root)
- Check if port 5500 is already in use
- Try changing port in VS Code settings: `liveServer.settings.port`

### Issue 7: JavaScript Not Loading

**Error**: Console shows 404 for JS files

**Solution**:
- Check file paths in HTML files are correct
- Ensure JS files are in the `js/` directory
- Check for typos in file names (case-sensitive on Linux/Mac)

### Issue 8: Firestore Permission Denied

**Error**: `Missing or insufficient permissions`

**Solution**:
- Deploy Firestore rules: `firebase deploy --only firestore:rules`
- Check rules in Firebase Console
- Ensure user is authenticated before accessing Firestore

### Issue 9: Admin Features Not Working

**Error**: Admin features inaccessible

**Solution**:
- Check user role in Firestore
- Ensure user document has `role: "admin"` field
- Manually set admin role in Firestore Console for first admin user

### Issue 10: Payment Integration Issues

**Error**: Payment processing not working

**Solution**:
- This is a demo implementation using dummy payment gateway
- For production, integrate real payment gateway (Razorpay, Stripe, PayPal)
- Update `js/payment.js` with actual API credentials

---

## 🔍 Quick Commands Reference

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login to Firebase
firebase login

# Initialize project
firebase init

# Serve locally
firebase serve

# Deploy everything
firebase deploy

# Deploy only hosting
firebase deploy --only hosting

# Deploy only Firestore rules
firebase deploy --only firestore:rules

# View deployment history
firebase hosting:channel:list

# Check which project you're using
firebase projects:list

# Switch Firebase project
firebase use PROJECT_ID
```

---

## 📚 Additional Resources

- [Firebase Documentation](https://firebase.google.com/docs)
- [Firestore Documentation](https://firebase.google.com/docs/firestore)
- [VS Code Documentation](https://code.visualstudio.com/docs)
- [Live Server Extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
- [Firebase Hosting Guide](https://firebase.google.com/docs/hosting)

---

## 🎯 Development Workflow

### Recommended Daily Workflow:

1. **Open VS Code** → Open project folder
2. **Start Live Server** → Right-click `index.html` → "Open with Live Server"
3. **Make changes** to HTML/CSS/JS files
4. **Live Server auto-refreshes** browser on save
5. **Test features** in browser (open Console with F12 for debugging)
6. **When ready to deploy**: Run `firebase deploy`

### Testing Checklist:

- ✅ Test user registration
- ✅ Test user login
- ✅ Test booking process
- ✅ Test payment flow
- ✅ Test admin login
- ✅ Test admin dashboard features
- ✅ Test notifications
- ✅ Check responsive design (mobile view)
- ✅ Check browser console for errors (F12)

---

## ✨ Tips for Better Development

1. **Use Browser DevTools** (`F12`):
   - Console: Debug JavaScript errors
   - Network: Check API calls
   - Application: View Firestore data in real-time

2. **Code Formatting**:
   - Install Prettier extension
   - Format on save: `Ctrl+Shift+P` → "Format Document"

3. **Git Version Control** (Optional):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Environment Variables**:
   - Never commit Firebase config with real credentials to public repos
   - Use environment variables for sensitive data in production

5. **Testing**:
   - Test in multiple browsers (Chrome, Firefox, Safari)
   - Test responsive design (mobile, tablet, desktop)
   - Use Firebase Emulator Suite for local testing without affecting production data

---

## 🎉 You're Ready!

Your Gas Agency Website is now set up and ready for development. If you encounter any issues not covered here, check the Firebase Console logs or browser console for specific error messages.

**Happy Coding! 🚀**
"""

# Write the guide to a file
vscode_guide_path = "gas_agency_website/VSCODE_SETUP_GUIDE.md"
with open(vscode_guide_path, 'w', encoding='utf-8') as f:
    f.write(vscode_guide_content)

print(f"✅ VS Code Setup & Run Guide created successfully!")
print(f"📄 File location: {vscode_guide_path}")
print(f"📏 Guide size: {len(vscode_guide_content)} characters")
print("\n" + "="*60)
print("GUIDE OVERVIEW")
print("="*60)
print("\n✨ Comprehensive VS Code Setup Guide includes:")
print("\n1. 📋 Prerequisites - Required software installations")
print("2. 🛠️ Initial Setup - Step-by-step project opening and Firebase CLI setup")
print("3. 🔌 VS Code Extensions - 7 essential extensions with install instructions")
print("4. 📁 Project Structure - Complete file tree explanation")
print("5. 🖥️ Running Locally - 4 different methods:")
print("   • Live Server (Recommended)")
print("   • Firebase Local Emulator")
print("   • Python HTTP Server")
print("   • Node.js http-server")
print("6. 🚀 Firebase Deployment - Complete deployment workflow:")
print("   • Firebase project configuration")
print("   • Update Firebase config")
print("   • Initialize hosting")
print("   • Deploy commands")
print("7. 🛠️ Troubleshooting - 10 common issues with solutions:")
print("   • Firebase CLI issues")
print("   • Login problems")
print("   • CORS errors")
print("   • Configuration issues")
print("   • Deployment failures")
print("   • Live Server issues")
print("   • JavaScript loading problems")
print("   • Firestore permissions")
print("   • Admin access issues")
print("   • Payment integration")
print("\n📚 Additional sections:")
print("   • Quick Commands Reference")
print("   • Development Workflow")
print("   • Testing Checklist")
print("   • Tips for Better Development")
print("   • Additional Resources")
print("\n" + "="*60)
print("The guide is ready to use! 🎉")
print("="*60)
