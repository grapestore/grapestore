import pdfkit
import sys

def convert_html_to_pdf(source_html, output_filename):
    try:
        # Convert HTML to PDF
        pdfkit.from_file(source_html, output_filename)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python html_to_pdf.py <source_html> <output_filename>")
        sys.exit(1)

    source_html = sys.argv[1]
    output_filename = sys.argv[2]

    if convert_html_to_pdf(source_html, output_filename):
        print("PDF created successfully.")
    else:
        print("Error creating PDF.")
