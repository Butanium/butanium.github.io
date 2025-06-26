#!/usr/bin/env python3
"""
Pre-commit hook to update the last modified date in _data/last_updated.yml
when _pages/about.md is modified.
"""

import os
import subprocess
from datetime import datetime

def update_last_modified():
    """Update the last modified date when about.md is being committed."""
    # Get current date in DD/MM/YYYY format
    current_date = datetime.now().strftime('%d/%m/%Y')
    
    # Ensure the _data directory exists
    os.makedirs('_data', exist_ok=True)
    
    # Write the date to the YAML file
    with open('_data/last_updated.yml', 'w') as f:
        f.write(f'date: "{current_date}"\n')
    
    # Stage the updated file
    subprocess.run(['git', 'add', '_data/last_updated.yml'], check=True)
    
    print(f"Updated last modified date to {current_date}")
    return 0

if __name__ == '__main__':
    exit(update_last_modified()) 