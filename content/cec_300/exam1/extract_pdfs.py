#!/usr/bin/env python3
"""Extract text from all PDFs in the CEC 300 exam1 folder using PyMuPDF."""

import fitz  # PyMuPDF
import os
import sys

EXAM_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(EXAM_DIR, "extracted")

def extract_pdf(pdf_path, output_path):
    """Extract all text from a PDF and write to a text file."""
    try:
        doc = fitz.open(pdf_path)
        text_parts = []
        for i, page in enumerate(doc):
            text = page.get_text()
            if text.strip():
                text_parts.append(f"--- Page {i+1} ---\n{text}")
        doc.close()

        full_text = "\n\n".join(text_parts)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)

        print(f"  OK: {os.path.basename(pdf_path)} -> {len(text_parts)} pages extracted")
        return True
    except Exception as e:
        print(f"  ERROR: {os.path.basename(pdf_path)} -> {e}")
        return False

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pdf_files = sorted([f for f in os.listdir(EXAM_DIR) if f.lower().endswith(".pdf")])
    print(f"Found {len(pdf_files)} PDFs in {EXAM_DIR}\n")

    success = 0
    for pdf_name in pdf_files:
        pdf_path = os.path.join(EXAM_DIR, pdf_name)
        # Create clean output filename
        out_name = os.path.splitext(pdf_name)[0] + ".txt"
        out_path = os.path.join(OUTPUT_DIR, out_name)

        if extract_pdf(pdf_path, out_path):
            success += 1

    print(f"\nDone: {success}/{len(pdf_files)} PDFs extracted to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
