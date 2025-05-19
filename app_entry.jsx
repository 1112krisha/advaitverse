import os
import fitz  # For reading PDF
from parser import parse_project_spec
from code_generator import generate_frontend, generate_backend

# NEW: Add function to generate app_entry.jsx (instead of index.jsx)

def generate_entry_page(module_names, app_title="AdvaitVerse"):
    component_imports = "\n".join([
        f"import {name} from './components/{name.lower().replace(' ', '_')}.jsx';"
        for name in module_names
    ])

    component_render = "\n      ".join([
        f"<{name} />"
        for name in module_names
    ])

    return f"""
import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles.css';

{component_imports}

function App() {{
  return (
    <div className=\"min-h-screen bg-white p-8 space-y-6\">
      <h1 className=\"text-4xl font-bold text-center text-orange-600\">{app_title}</h1>
      {component_render}
    </div>
  );
}}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
"""

def extract_text_from_pdf(pdf_path):
    text_pages = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text()
            text_pages.append(text)
    return text_pages

def main(pdf_path):
    print(f"🔍 Reading: {pdf_path}")
    pages = extract_text_from_pdf(pdf_path)
    spec = parse_project_spec(pages)

    print("📊 Parsed Spec:")
    print("Modules:", spec['modules'])
    print("Colors:", spec['colors'])
    print("Functions:", spec['functions'])

    # Generate frontend and backend code
    frontend = generate_frontend(spec['modules'], spec['colors'])
    backend = generate_backend(spec['functions'])

    # Save frontend
    os.makedirs("frontend/components", exist_ok=True)
    for filename, code in frontend.items():
        with open(f"frontend/components/{filename}", "w") as f:
            f.write(code)

    # Save app_entry.jsx
    os.makedirs("frontend", exist_ok=True)
    with open("frontend/app_entry.jsx", "w") as f:
        f.write(generate_entry_page(spec['modules']))

    # Save backend
    os.makedirs("backend", exist_ok=True)
    with open("backend/app.py", "w") as f:
        f.write(backend)

    print("✅ App code generated in /frontend and /backend")

if __name__ == "__main__":
    # Replace with your actual uploaded PDF filename
    main("project_plan.pdf")
