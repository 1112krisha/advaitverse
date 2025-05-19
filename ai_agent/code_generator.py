import os

def generate_frontend(modules, colors):
    """
    Generates basic HTML + Tailwind React components based on modules and color theme.
    Returns a dictionary where key = filename, value = code.
    """
    color_primary = colors[0] if colors else "blue"

    components = {}
    for module in modules:
        filename = f"{module.lower().replace(' ', '_')}.jsx"
        jsx_code = f"""
import React from 'react';

const {module} = () => {{
  return (
    <div className=\"p-4 bg-{color_primary}-100 rounded-2xl shadow-md\">
      <h2 className=\"text-2xl font-bold text-{color_primary}-800\">{module}</h2>
      <p className=\"text-sm text-gray-600\">This is the {module} module.</p>
    </div>
  );
}};

export default {module};
"""
        components[filename] = jsx_code
    return components

def generate_backend(functions):
    """
    Returns a simple Flask backend template with placeholder routes based on functions.
    """
    lines = [
        "from flask import Flask, request, jsonify",
        "app = Flask(__name__)",
        "",
    ]

    if "upload" in functions:
        lines.extend([
            "@app.route('/upload', methods=['POST'])",
            "def upload_file():",
            "    file = request.files.get('file')",
            "    return jsonify({'status': 'received'})",
            "",
        ])

    if "download" in functions:
        lines.extend([
            "@app.route('/download', methods=['GET'])",
            "def download():",
            "    return jsonify({'file': 'example.csv'})",
            "",
        ])

    lines.append("if __name__ == '__main__':")
    lines.append("    app.run(debug=True)")

    return "\n".join(lines)

if __name__ == "__main__":
    # Sample inputs
    modules = ["Dashboard", "Reports"]
    colors = ["orange", "blue"]
    functions = ["upload", "download"]

    frontend_code = generate_frontend(modules, colors)
    backend_code = generate_backend(functions)

    # Write frontend components
    os.makedirs("frontend/components", exist_ok=True)
    for filename, code in frontend_code.items():
        with open(f"frontend/components/{filename}", "w") as f:
            f.write(code)

    # Write backend
    os.makedirs("backend", exist_ok=True)
    with open("backend/app.py", "w") as f:
        f.write(backend_code)

    print("✅ Code generation complete.")
