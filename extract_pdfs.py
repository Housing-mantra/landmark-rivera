import os
from pypdf import PdfReader

pdfs = [
    "B REFUSE 23-05-26.pdf",
    "MASTER LAYOUT PLAN 23-05-2026 (1).pdf",
    "_2075-Landmark Township-Kale-234 Dudulgaon_ 10 April 2026.pdf"
]

for pdf in pdfs:
    print(f"Processing {pdf}...")
    if not os.path.exists(pdf):
        print(f"File {pdf} not found.")
        continue
    try:
        reader = PdfReader(pdf)
        text_content = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                text_content.append(f"--- Page {i+1} ---\n{text}")
            else:
                text_content.append(f"--- Page {i+1} ---\n[No Text Extracted]")
        
        output_txt = pdf.replace(".pdf", "_text.txt")
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write("\n\n".join(text_content))
        print(f"Saved {output_txt} with {len(reader.pages)} pages.")
    except Exception as e:
        print(f"Error processing {pdf}: {e}")
