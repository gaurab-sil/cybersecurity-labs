# Digital Forensics Labs

This section contains practical digital forensics exercises
completed in a controlled educational cybersecurity
environment.

## Project

### Document Metadata Extraction Tool

A Python-based digital forensics tool designed to extract
metadata from files, with specific support for Microsoft
Word DOCX documents.

The project demonstrates how file metadata can be collected
and presented in a structured report.

---

## Objectives

- Extract basic file metadata
- Identify file type and size
- Retrieve file creation timestamps
- Retrieve file modification timestamps
- Extract DOCX document metadata
- Support analysis of single files
- Support analysis of multiple files
- Present extracted information in a readable format

---

## Functionality

### Basic File Metadata

The tool extracts:

- File name
- File extension/type
- File size
- Created timestamp
- Modified timestamp

### DOCX Metadata

For Microsoft Word DOCX files, the tool additionally
extracts:

- Author
- Title
- Last Modified By

### Single File Analysis

The user can select a single file for analysis.

### Multiple File Analysis

The user can provide multiple filenames separated by commas
for batch analysis.

---

## Technologies

- Python
- Python Standard Library
- python-docx

---

## Skills Demonstrated

- Python scripting
- Digital forensics
- File metadata analysis
- DOCX metadata extraction
- File handling
- Exception handling
- User input validation
- Structured data processing
- Technical documentation

---

## Forensic Relevance

File metadata can provide useful information during a
digital forensic investigation.

Metadata may help investigators understand:

- What type of file was involved
- When a file was created
- When a file was modified
- Who is recorded as the document author
- Whether document properties contain useful investigative
  information

Metadata should be interpreted together with other forensic
evidence rather than treated as conclusive evidence on its
own.

**Authorisation**

This project was developed as part of an authorised
educational cybersecurity exercise.

No unauthorised systems or data were accessed.
---
