import os
import sys
import re
from datetime import datetime

def extract_video_id_from_filename(filename):
    """Extract video ID from transcript filename (transcript_VIDEO_ID.md)"""
    match = re.search(r'transcript_([0-9A-Za-z_-]{11})\.md', filename)
    return match.group(1) if match else None

def extract_playlist_info_from_dirname(dirname):
    """Extract playlist title and ID from directory name (list_TITLE_ID)"""
    # Pattern: list_{title}_{playlist_id}
    match = re.match(r'list_(.+)_([^_]{34}|PL[0-9A-Za-z_-]+)$', dirname)
    if match:
        return match.group(1), match.group(2)  # title, playlist_id
    return None, None

def merge_transcripts(playlist_dir):
    """Merge all transcript .md files in a directory into one master file"""
    
    # Validate directory exists
    if not os.path.exists(playlist_dir):
        print(f"[ERROR] Directory not found: {playlist_dir}")
        sys.exit(1)
    
    if not os.path.isdir(playlist_dir):
        print(f"[ERROR] Path is not a directory: {playlist_dir}")
        sys.exit(1)
    
    # Get directory name and extract playlist info
    dir_name = os.path.basename(os.path.normpath(playlist_dir))
    playlist_title, playlist_id = extract_playlist_info_from_dirname(dir_name)
    
    # Determine output filename
    if playlist_title and playlist_id:
        output_file = os.path.join(playlist_dir, f"{playlist_title}_{playlist_id}_master_transcripts.md")
        header_title = f"{playlist_title} - Master Transcript"
    else:
        output_file = os.path.join(playlist_dir, f"master_{dir_name}.md")
        header_title = f"Master Transcript - {dir_name}"
    
    # Find all transcript files (skip the manifest and master files)
    transcript_files = []
    for filename in os.listdir(playlist_dir):
        if filename.startswith("transcript_") and filename.endswith(".md"):
            transcript_files.append(filename)
    
    if not transcript_files:
        print(f"[WARN] No transcript files found in {playlist_dir}")
        sys.exit(0)
    
    # Sort files by video ID for consistent ordering
    transcript_files.sort()
    
    print(f"[INFO] Found {len(transcript_files)} transcript files")
    print(f"[INFO] Merging into: {output_file}")
    
    # Read and merge transcripts
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Write header
        outfile.write(f"# {header_title}\n\n")
        if playlist_id:
            outfile.write(f"**Playlist ID:** {playlist_id}\n")
        outfile.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        outfile.write(f"**Total Videos:** {len(transcript_files)}\n\n")
        outfile.write("---\n\n")
        
        # Process each transcript file
        for idx, filename in enumerate(transcript_files, 1):
            filepath = os.path.join(playlist_dir, filename)
            video_id = extract_video_id_from_filename(filename)
            
            print(f"[{idx}/{len(transcript_files)}] Processing {filename}")
            
            try:
                with open(filepath, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    
                    # Write to master file with separator
                    outfile.write(f"## Video {idx}\n\n")
                    outfile.write(content)
                    outfile.write("\n\n---\n\n")
                    
            except Exception as e:
                print(f"[ERROR] Failed to read {filename}: {e}")
                continue
    
    print(f"[SUCCESS] Created master file: {output_file}")
    print(f"[INFO] Total size: {os.path.getsize(output_file):,} bytes")

def main():
    if len(sys.argv) < 2:
        print("[ERROR] Missing directory argument")
        print(f"[USAGE] python {sys.argv[0]} <playlist_directory>")
        sys.exit(1)
    
    playlist_dir = sys.argv[1]
    merge_transcripts(playlist_dir)

if __name__ == "__main__":
    main()