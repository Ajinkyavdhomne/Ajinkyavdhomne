import pdfplumber
import os

# Read the PDF file
pdf_path = "_Gas Agency System .docx.pdf"

# Check if file exists
if not os.path.exists(pdf_path):
    print(f"❌ File not found: {pdf_path}")
    print(f"Files in directory: {os.listdir('.')}")
else:
    print(f"✅ Found PDF: {pdf_path}")
    print(f"File size: {os.path.getsize(pdf_path)} bytes\n")
    
    # Extract text from PDF
    with pdfplumber.open(pdf_path) as pdf:
        
        print(f"📄 Total pages: {len(pdf.pages)}\n")
        print("="*80)
        
        # Extract all text
        pdf_text = ""
        for page_num, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            pdf_text += page_text + "\n"
            
            print(f"\n--- PAGE {page_num + 1} ---")
            print(page_text)
            print("-"*80)
        
        print(f"\n✅ Successfully extracted {len(pdf_text)} characters from PDF")
