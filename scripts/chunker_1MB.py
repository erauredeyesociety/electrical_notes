import os
import sys

CHUNK_SIZE = 1_000_000  # ~1 MB per chunk

def split_markdown_file(input_file):
    if not os.path.exists(input_file):
        print(f"[ERROR] File not found: {input_file}")
        sys.exit(1)

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_dir = os.path.dirname(input_file) or "."
    
    with open(input_file, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    chunk_index = 1
    current_chunk_size = 0
    current_lines = []
    
    def write_chunk():
        """Write current buffer to a new chunk file"""
        nonlocal chunk_index, current_lines
        if not current_lines:
            return
        chunk_filename = os.path.join(output_dir, f"{base_name}_chunk_{chunk_index}.md")
        with open(chunk_filename, "w", encoding="utf-8") as chunk_file:
            chunk_file.writelines(current_lines)
        print(f"[INFO] Created {chunk_filename} ({len(current_lines)} lines, {os.path.getsize(chunk_filename):,} bytes)")
        chunk_index += 1
        current_lines = []

    for line in lines:
        current_lines.append(line)
        current_chunk_size += len(line.encode("utf-8"))

        # If size exceeds threshold and this line starts a new transcript, start a new chunk
        if current_chunk_size >= CHUNK_SIZE and line.strip().startswith("## Video"):
            write_chunk()
            current_chunk_size = 0

    # Write remaining lines
    if current_lines:
        write_chunk()

    print(f"[SUCCESS] Finished splitting '{input_file}' into {chunk_index - 1} chunks.")

def main():
    if len(sys.argv) < 2:
        print("[ERROR] Missing input file argument")
        print(f"[USAGE] python {sys.argv[0]} <input_file.md>")
        sys.exit(1)

    input_file = sys.argv[1]
    split_markdown_file(input_file)

if __name__ == "__main__":
    main()
