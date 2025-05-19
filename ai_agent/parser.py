import re

def parse_project_spec(text_pages):
    """
    Parses extracted PDF text to identify:
    - Web module names
    - Color preferences
    - Functional elements (like R scripts, visualizations)
    """
    modules = []
    colors = []
    functions = []

    color_keywords = ["orange", "blue", "green", "white", "dark", "light"]
    function_keywords = ["visualization", "R script", "download", "statistics", "table", "upload", "form"]

    for text in text_pages:
        # Find color preferences
        for word in color_keywords:
            if word.lower() in text.lower():
                colors.append(word.lower())

        # Find function references
        for word in function_keywords:
            if word.lower() in text.lower():
                functions.append(word.lower())

        # Simple module name extraction based on headings or patterns
        module_matches = re.findall(r"Module[:\\-\\s]*(.+)", text, flags=re.IGNORECASE)
        modules.extend(module_matches)

    return {
        "modules": list(set(modules)),
        "colors": list(set(colors)),
        "functions": list(set(functions))
    }


if __name__ == "__main__":
    # Example usage with dummy content
    pages = [
        \"\"\"\n        Page 1: Welcome to Advait System\n        Module: Dashboard\n        Colors: Blue and Orange\n        Features: Upload data, Visualize using R scripts\n        \"\"\",\n        \"\"\"\n        Module - Reports\n        This includes download buttons and summary statistics\n        \"\"\"\n    ]

    result = parse_project_spec(pages)
    print(\"Detected Modules:\", result['modules'])\n    print(\"Detected Colors:\", result['colors'])\n    print(\"Detected Functions:\", result['functions'])"
