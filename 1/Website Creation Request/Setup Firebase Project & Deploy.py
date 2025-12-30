import os
import json
import subprocess

# Step 1: Install Firebase CLI if needed (skip in serverless, provide instructions)
print("🔥 Firebase Deployment Setup")
print("=" * 60)
print("\n📋 FIREBASE DEPLOYMENT GUIDE")
print("-" * 60)

# Step 2: Create firebase.json configuration
firebase_config = {
    "hosting": {
        "public": "gas_agency_website",
        "ignore": [
            "firebase.json",
            "**/.*",
            "**/node_modules/**"
        ],
        "rewrites": [
            {
                "source": "**",
                "destination": "/index.html"
            }
        ]
    },
    "firestore": {
        "rules": "firestore.rules",
        "indexes": "firestore.indexes.json"
    }
}

with open('firebase.json', 'w') as f:
    json.dump(firebase_config, f, indent=2)

print("\n✓ Created firebase.json configuration")

# Step 3: Create Firestore security rules
firestore_rules = """rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Users collection
    match /users/{userId} {
      allow read: if request.auth != null;
      allow create: if request.auth != null;
      allow update: if request.auth.uid == userId || 
                       get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin';
      allow delete: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin';
    }
    
    // Bookings collection
    match /bookings/{bookingId} {
      allow read: if request.auth != null;
      allow create: if request.auth != null;
      allow update: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin';
      allow delete: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin';
    }
    
    // Notifications collection
    match /notifications/{notificationId} {
      allow read: if request.auth != null;
      allow write: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == 'admin';
    }
  }
}
"""

with open('firestore.rules', 'w') as f:
    f.write(firestore_rules)

print("✓ Created firestore.rules for database security")

# Step 4: Create Firestore indexes configuration
firestore_indexes = {
    "indexes": [
        {
            "collectionGroup": "bookings",
            "queryScope": "COLLECTION",
            "fields": [
                {"fieldPath": "userId", "order": "ASCENDING"},
                {"fieldPath": "bookingDate", "order": "DESCENDING"}
            ]
        },
        {
            "collectionGroup": "bookings",
            "queryScope": "COLLECTION",
            "fields": [
                {"fieldPath": "status", "order": "ASCENDING"},
                {"fieldPath": "bookingDate", "order": "DESCENDING"}
            ]
        },
        {
            "collectionGroup": "notifications",
            "queryScope": "COLLECTION",
            "fields": [
                {"fieldPath": "active", "order": "ASCENDING"},
                {"fieldPath": "createdDate", "order": "DESCENDING"}
            ]
        }
    ],
    "fieldOverrides": []
}

with open('firestore.indexes.json', 'w') as f:
    json.dump(firestore_indexes, f, indent=2)

print("✓ Created firestore.indexes.json for query optimization")

# Step 5: Create .firebaserc configuration
firebaserc = {
    "projects": {
        "default": "your-project-id"
    }
}

with open('.firebaserc', 'w') as f:
    json.dump(firebaserc, f, indent=2)

print("✓ Created .firebaserc project configuration")

# Step 6: Update firebase-config.js with proper template
firebase_config_js = """// Firebase Configuration
// Replace these values with your actual Firebase project credentials
// Get them from: Firebase Console > Project Settings > Your apps > Web app

import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js';
import { getAuth } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js';
import { getFirestore } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js';

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "your-project-id.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project-id.appspot.com",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { app, auth, db };
export default firebaseConfig;
"""

with open('gas_agency_website/js/firebase-config.js', 'w') as f:
    f.write(firebase_config_js)

print("✓ Updated firebase-config.js with proper Firebase imports")

# Step 7: Create deployment instructions
deployment_instructions = """
═══════════════════════════════════════════════════════════════
🚀 FIREBASE DEPLOYMENT INSTRUCTIONS
═══════════════════════════════════════════════════════════════

STEP 1: INSTALL FIREBASE CLI
────────────────────────────────────────────────────────────────
Run in your local terminal:
  npm install -g firebase-tools

Or download from: https://firebase.google.com/docs/cli


STEP 2: CREATE FIREBASE PROJECT
────────────────────────────────────────────────────────────────
1. Go to https://console.firebase.google.com/
2. Click "Add project"
3. Enter project name (e.g., "gas-agency-system")
4. Follow the setup wizard
5. Enable Google Analytics (optional)


STEP 3: ENABLE FIREBASE SERVICES
────────────────────────────────────────────────────────────────
In Firebase Console:

A. Enable Authentication:
   - Go to Authentication > Sign-in method
   - Enable "Email/Password" provider
   - Save changes

B. Create Firestore Database:
   - Go to Firestore Database
   - Click "Create database"
   - Start in PRODUCTION mode
   - Choose a location (us-central1 recommended)
   - Click "Enable"


STEP 4: GET FIREBASE CREDENTIALS
────────────────────────────────────────────────────────────────
1. In Firebase Console, click the gear icon > Project settings
2. Scroll down to "Your apps"
3. Click the "</>" (Web) icon
4. Register app with nickname "Gas Agency System"
5. Copy the firebaseConfig object
6. Update gas_agency_website/js/firebase-config.js with your values


STEP 5: LOGIN TO FIREBASE
────────────────────────────────────────────────────────────────
In your terminal:
  firebase login

This will open a browser for authentication.


STEP 6: INITIALIZE FIREBASE PROJECT
────────────────────────────────────────────────────────────────
In your project directory:
  firebase init

Select:
  - Hosting: Configure files for Firebase Hosting
  - Firestore: Deploy rules and create indexes

When asked:
  - "What do you want to use as your public directory?" → gas_agency_website
  - "Configure as a single-page app?" → Yes
  - "Set up automatic builds with GitHub?" → No (optional)
  - "Overwrite existing files?" → No


STEP 7: UPDATE PROJECT ID
────────────────────────────────────────────────────────────────
Edit .firebaserc file:
  {
    "projects": {
      "default": "your-actual-project-id"
    }
  }

Replace "your-project-id" with your Firebase project ID.


STEP 8: DEPLOY TO FIREBASE HOSTING
────────────────────────────────────────────────────────────────
Run:
  firebase deploy

Or deploy only hosting:
  firebase deploy --only hosting

Or deploy Firestore rules:
  firebase deploy --only firestore


STEP 9: ACCESS YOUR LIVE WEBSITE
────────────────────────────────────────────────────────────────
After deployment, you'll see:
  ✔  Deploy complete!
  
  Hosting URL: https://your-project-id.web.app

Your website is now LIVE! 🎉


STEP 10: CREATE ADMIN USER
────────────────────────────────────────────────────────────────
1. Go to your live website
2. Register a new account
3. In Firebase Console > Firestore Database
4. Find the user document
5. Add field: "role" with value "admin"


═══════════════════════════════════════════════════════════════
📝 ADDITIONAL COMMANDS
═══════════════════════════════════════════════════════════════

View your project:
  firebase open

Test locally before deploying:
  firebase serve

View deployment history:
  firebase hosting:channel:list

Rollback to previous version:
  firebase hosting:clone SOURCE_SITE_ID:SOURCE_CHANNEL TARGET_CHANNEL


═══════════════════════════════════════════════════════════════
🔐 SECURITY CHECKLIST
═══════════════════════════════════════════════════════════════
✓ Firebase credentials updated in firebase-config.js
✓ Firestore security rules deployed
✓ Authentication enabled
✓ Admin user role assigned
✓ Test all features in production


═══════════════════════════════════════════════════════════════
🐛 TROUBLESHOOTING
═══════════════════════════════════════════════════════════════

1. "Firebase command not found"
   → Install Firebase CLI: npm install -g firebase-tools

2. "Permission denied"
   → Run: firebase login
   → Make sure you have owner/editor access

3. "Deployment failed"
   → Check firebase.json configuration
   → Verify public directory exists
   → Run: firebase deploy --debug

4. "Authentication not working"
   → Verify Email/Password is enabled
   → Check firebase-config.js credentials
   → Look for CORS errors in browser console

5. "Firestore permission denied"
   → Deploy security rules: firebase deploy --only firestore
   → Check user is authenticated
   → Verify role field for admin access


═══════════════════════════════════════════════════════════════
📞 SUPPORT RESOURCES
═══════════════════════════════════════════════════════════════
Firebase Documentation: https://firebase.google.com/docs
Firebase Console: https://console.firebase.google.com/
Firebase CLI Reference: https://firebase.google.com/docs/cli


═══════════════════════════════════════════════════════════════
✅ SUCCESS CRITERIA
═══════════════════════════════════════════════════════════════
Your deployment is successful when:
1. Website loads at https://your-project-id.web.app
2. Users can register and login
3. Bookings are saved to Firestore
4. Admin panel works with proper authentication
5. Notifications display correctly
6. All pages navigate without errors


═══════════════════════════════════════════════════════════════
"""

with open('DEPLOYMENT_INSTRUCTIONS.txt', 'w') as f:
    f.write(deployment_instructions)

print("✓ Created DEPLOYMENT_INSTRUCTIONS.txt")

# Step 8: Summary
print("\n" + "=" * 60)
print("✅ FIREBASE DEPLOYMENT SETUP COMPLETE!")
print("=" * 60)
print("\n📦 Files created:")
print("  ✓ firebase.json - Firebase hosting configuration")
print("  ✓ firestore.rules - Database security rules")
print("  ✓ firestore.indexes.json - Query optimization indexes")
print("  ✓ .firebaserc - Project configuration")
print("  ✓ firebase-config.js - Updated with proper imports")
print("  ✓ DEPLOYMENT_INSTRUCTIONS.txt - Complete deployment guide")

print("\n🎯 Next Steps:")
print("  1. Read DEPLOYMENT_INSTRUCTIONS.txt for detailed steps")
print("  2. Install Firebase CLI: npm install -g firebase-tools")
print("  3. Create Firebase project at https://console.firebase.google.com/")
print("  4. Enable Authentication (Email/Password)")
print("  5. Create Firestore Database")
print("  6. Update firebase-config.js with your credentials")
print("  7. Run: firebase login")
print("  8. Run: firebase init")
print("  9. Run: firebase deploy")
print("  10. Access your live website!")

print("\n🌐 Your site will be live at:")
print("   https://your-project-id.web.app")
print("   https://your-project-id.firebaseapp.com")

deployment_summary = {
    "status": "ready_for_deployment",
    "configuration_files": [
        "firebase.json",
        "firestore.rules", 
        "firestore.indexes.json",
        ".firebaserc",
        "gas_agency_website/js/firebase-config.js"
    ],
    "instructions": "DEPLOYMENT_INSTRUCTIONS.txt",
    "next_action": "Follow deployment instructions to deploy to Firebase"
}

print("\n✨ All setup files created successfully!")
print("📖 Open DEPLOYMENT_INSTRUCTIONS.txt for the complete step-by-step guide")
