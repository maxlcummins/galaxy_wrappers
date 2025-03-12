#!/usr/bin/env python3

import os
import subprocess
import urllib.request
import argparse
import sys
from pathlib import Path

def download_file(url, output_dir):
    """Download a file from URL and save it in the output directory."""
    filename = os.path.join(output_dir, os.path.basename(url))
    print(f"Downloading {url} to {filename}...")
    urllib.request.urlretrieve(url, filename)
    print("Download complete!")
    return filename

def make_blast_db(input_file, db_name, dbtype="nucl"):
    """Create a BLAST database from a FASTA file."""
    print(f"Creating BLAST database from {input_file}...")
    cmd = ["makeblastdb", "-in", input_file, "-dbtype", dbtype, "-out", db_name]
    subprocess.run(cmd, check=True)
    print(f"BLAST database '{db_name}' created successfully!")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Download a file and create a BLAST database')
    parser.add_argument('url', help='URL of the file to download (in quotes)')
    parser.add_argument('output_dir', help='Directory to store the downloaded file and BLAST database')
    args = parser.parse_args()
    
    # Ensure the output directory exists
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Download the file
    fasta_file = download_file(args.url, args.output_dir)
    
    # Create BLAST database in the specified output directory
    db_name = os.path.join(args.output_dir, "blast_db")
    make_blast_db(fasta_file, db_name)
    
    print("Process completed successfully!")

if __name__ == "__main__":
    main()