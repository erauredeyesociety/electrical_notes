#!/usr/bin/env python3
"""Extract text from all PDFs in the CEC 300 course_content folder."""

import fitz
import os

COURSE_DIR = "/home/devel/electrical_notes/content/cec_300/course_content"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extracted")

def extract_pdf(pdf_path, output_path):
    try:
        doc = fitz.open(pdf_path)
        parts = []
        for i, page in enumerate(doc):
            text = page.get_text()
            if text.strip():
                parts.append(f"--- Page {i+1} ---\n{text}")
        doc.close()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(parts))
        print(f"  OK: {os.path.basename(pdf_path)} -> {len(parts)} pages")
        return True
    except Exception as e:
        print(f"  ERROR: {os.path.basename(pdf_path)} -> {e}")
        return False

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pdfs = sorted([f for f in os.listdir(COURSE_DIR) if f.lower().endswith(".pdf")])
    print(f"Found {len(pdfs)} PDFs\n")
    ok = 0
    for p in pdfs:
        out = os.path.splitext(p)[0] + ".txt"
        if extract_pdf(os.path.join(COURSE_DIR, p), os.path.join(OUTPUT_DIR, out)):
            ok += 1
    print(f"\nDone: {ok}/{len(pdfs)}")

if __name__ == "__main__":
    main()
