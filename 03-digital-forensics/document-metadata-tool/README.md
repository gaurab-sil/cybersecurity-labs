# Document Metadata Extraction Tool

## Overview

A Python-based digital forensics utility designed to extract
metadata from files, with additional metadata extraction for
Microsoft Word DOCX documents.

## Features

### File Metadata

The tool extracts:

- File name
- File type
- File size
- Creation timestamp
- Modification timestamp

### DOCX Metadata

When a DOCX file is provided, the tool additionally extracts:

- Author
- Title
- Last Modified By

### Analysis Modes

The application supports:

- Single-file analysis
- Multiple-file analysis

## Workflow

```text
Select analysis mode
        ↓
Enter file path(s)
        ↓
Validate file existence
        ↓
Extract filesystem metadata
        ↓
Detect DOCX files
        ↓
Extract document properties
        ↓
Display structured metadata report

**Technologies**
Python
os
datetime
python-docx
Forensic Skills
Metadata extraction
File analysis
Document property analysis
Automated forensic data collection
Python scripting
Structured reporting
Limitations

Metadata can be modified or removed and should therefore be
treated as supporting evidence rather than definitive proof.

**Authorisation
**
Developed for an authorised educational cybersecurity and
digital forensics laboratory.

**Disclaimer**

This project is for educational and portfolio purposes.
