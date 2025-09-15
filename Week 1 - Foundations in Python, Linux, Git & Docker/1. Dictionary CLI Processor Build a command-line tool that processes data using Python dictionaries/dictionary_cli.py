#!/usr/bin/env python3

import sys

# Our global dictionary
data_dict = {}

def add_key():
    key = input("Enter key: ")
    value = input("Enter value: ")
    data_dict[key] = value
    print(f"✅ Added ({key}: {value})")

def update_key():
    key = input("Enter key to update: ")
    if key in data_dict:
        value = input("Enter new value: ")
        data_dict[key] = value
        print(f"✅ Updated ({key}: {value})")
    else:
        print("❌ Key not found.")

def delete_key():
    key = input("Enter key to delete: ")
    if key in data_dict:
        del data_dict[key]
        print(f"✅ Deleted key '{key}'")
    else:
        print("❌ Key not found.")

def search_key():
    key = input("Enter key to search: ")
    if key in data_dict:
        print(f"🔎 Found: {key} -> {data_dict[key]}")
    else:
        print("❌ Key not found.")

def display_dict():
    if data_dict:
        print("📘 Current Dictionary:")
        for k, v in data_dict.items():
            print(f"   {k}: {v}")
    else:
        print("⚠️ Dictionary is empty.")

def main():
    while True:
        print("\n=== Dictionary CLI Processor ===")
        print("1. Add Key-Value")
        print("2. Update Value")
        print("3. Delete Key")
        print("4. Search Key")
        print("5. Display Dictionary")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_key()
        elif choice == "2":
            update_key()
        elif choice == "3":
            delete_key()
        elif choice == "4":
            search_key()
        elif choice == "5":
            display_dict()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            sys.exit()
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
