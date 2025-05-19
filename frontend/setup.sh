#!/bin/bash

# Step 1: Create Vite + React app
npm create vite@latest advaitverse-frontend --template react
cd advaitverse-frontend

# Step 2: Install dependencies
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Step 3: Configure Tailwind
cat > tailwind.config.js <<EOF
module.exports = {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOF

# Step 4: Set up styles
mkdir -p src
cat > src/styles.css <<EOF
@tailwind base;
@tailwind components;
@tailwind utilities;
EOF

# Step 5: Replace entry point
mv ../app_entry.jsx src/main.jsx
cp -r ../components src/

echo "✅ Frontend scaffolded. Run 'npm run dev' inside advaitverse-frontend/"
