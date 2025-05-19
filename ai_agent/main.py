import os
import fitz  # For reading PDF
from parser import parse_project_spec
from code_generator import generate_frontend, generate_backend

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

    # Save backend
    os.makedirs("backend", exist_ok=True)
    with open("backend/app.py", "w") as f:
        f.write(backend)

    print("✅ App code generated in /frontend and /backend")

if __name__ == "__main__":
    # Replace with your actual uploaded PDF filename
    main("project_plan.pdf")
