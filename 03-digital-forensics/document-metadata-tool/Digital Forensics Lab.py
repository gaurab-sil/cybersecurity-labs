# Simple digital forensics tool to extract metadata from files, especially DOCX documents.
# Using OS module for file info and python-docx for DOCX metadata. Handles single or multiple files.
# Using datetime for formatting timestamps. Outputs a neat report of all extracted metadata.
# Using docx import Document to read DOCX files and extract core properties like author and title.
import os
from datetime import datetime
from docx import Document
from pprint import pformat

# Creating a function to extract basic file metadata using OS module
def basic_meta(file_path):
    meta = {}
    meta["Name"] = os.path.basename(file_path)
    meta["Type"] = os.path.splitext(file_path)[1]
    meta["Size"] = str(round(os.path.getsize(file_path)/1024,2)) + " KB"
    meta["Created"] = datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%d %B %Y %H:%M:%S")
    meta["Modified"] = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%d %B %Y %H:%M:%S")
    return meta

# Creating a function to extract DOCX metadata using python-docx
def docx_meta(file_path):
    doc_data = {}

    # Using try-except to handle cases where the file might not be a valid DOCX or if there are issues reading it.
    try:
        doc = Document(file_path)
        core = doc.core_properties
        doc_data["Author"] = core.author if core.author else "N/A"
        doc_data["Title"] = core.title if core.title else "N/A"
        doc_data["Last Modified By"] = core.last_modified_by if core.last_modified_by else "N/A"
    except:
        doc_data["DOCX Info"] = "N/A"
    return doc_data

# Creating a function to combine all metadata into one dictionary
def full_meta(file_path):
    data = basic_meta(file_path)

    # If the file is a DOCX, we will also extract the DOCX-specific metadata and updating the data dictionary with it.
    if file_path.endswith(".docx"):
        data.update(docx_meta(file_path))
    return data

# Printing the metadata in a neat format
def show_meta(data):
    print("\nDocument Metadata Report - Details of the selected file")
    print("-"*55)

    # Iterating through the dictionary and print in aligned table format
    for k, v in data.items():

        # printing <22 to align keys in a column and : to separate key and value
        print(f"{k:<22} : {v}")
    print("-"*55)

# Creating a function and handling single file input
def single_file():
    print("\nYou have selected Single file to check.")
    file = input("Enter single file name: ")
    if os.path.exists(file):
        data = full_meta(file)
        show_meta(data)
    else:
        print("\nError: File not found")

# Creating a function and handlling multiple files input
def multi_file():
    print("\nYou have selected Multiple files to check.")
    files = input("Please enter multiple file names separated by commas: ")
    file_list = files.split(",")
    for file in file_list:
        file = file.strip()
        if os.path.exists(file):
            print("\nProcessing:", file)
            data = full_meta(file)
            show_meta(data)
        else:
            print("\n", file, "not found")

# The main function to run the program and ask user for input on single or multiple files, 
# then call the appropriate functions.
def main():
    print("\nDoc Meta Checker - A Simple Digital Forensics Tool")
    print("-"*55)
    choice = input("\nPlease enter either (S) for Single File or (M) for Multiple Files to check: ")
    if choice.lower() == "s":
        single_file()
    elif choice.lower() == "m":
        multi_file()
    else:
        print("\nInvalid choice. Please enter S or M.")

main()