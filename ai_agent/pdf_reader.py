import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from the given PDF file.
    Returns a list where each item is the text of one page.
    """
    text_pages = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text()
            text_pages.append(text)
    return text_pages


def save_extracted_text(text_pages, output_txt="extracted_text.txt"):
    """
    Saves the extracted text into a .txt file for debugging or reference.
    """
    with open(output_txt, "w", encoding="utf-8") as f:
        for i, page_text in enumerate(text_pages):
            f.write(f"\n--- Page {i+1} ---\n")
            f.write(page_text)


if __name__ == "__main__":
    # Example: Replace 'your_pdf_file.pdf' with actual file path
    pdf_file = "your_pdf_file.pdf"
    extracted_pages = extract_text_from_pdf(pdf_file)
    save_extracted_text(extracted_pages)

    # Optionally print first page
    print("First Page Preview:\n", extracted_pages[0])
