import os
import shutil

def copy_file(src, dest):
    """Copy a file from src to dest"""
    try:
        shutil.copy(src, dest)
        print(f"✅ File copied from {src} to {dest}")
    except Exception as e:
        print(f"❌ Error copying file: {e}")

def move_file(src, dest):
    """Move a file from src to dest"""
    try:
        shutil.move(src, dest)
        print(f"✅ File moved from {src} to {dest}")
    except Exception as e:
        print(f"❌ Error moving file: {e}")

def delete_file(path):
    """Delete a file"""
    try:
        os.remove(path)
        print(f"✅ File deleted: {path}")
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"❌ Error deleting file: {e}")

def list_files(directory):
    """List all files in a directory"""
    try:
        files = os.listdir(directory)
        print(f"📂 Files in {directory}:")
        for f in files:
            print("   -", f)
    except FileNotFoundError:
        print("❌ Directory not found.")
    except Exception as e:
        print(f"❌ Error listing files: {e}")

def create_file(path, content=""):
    """Create a new file with optional content"""
    try:
        with open(path, "w") as f:
            f.write(content)
        print(f"✅ File created: {path}")
    except Exception as e:
        print(f"❌ Error creating file: {e}")
