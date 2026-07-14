---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---

# PDF Processing Skill

This skill provides comprehensive PDF document handling capabilities including text extraction, form filling, and file merging.

## Features

### Text Extraction
Extract text content from PDF documents with support for:
- Single and multi-page PDFs
- Preserving layout and formatting
- Handling scanned documents (OCR compatible)

### Form Filling
Programmatically fill PDF forms with:
- Text field population
- Checkbox and radio button selection
- Dropdown menu options
- Signature field support

### File Merging
Combine multiple PDF files into a single document:
- Preserve page order
- Maintain original formatting
- Support for selective page ranges

## Usage Examples

### Extract Text from PDF
```
Input: path/to/document.pdf
Output: Extracted text content
```

### Fill PDF Form
```
Input: form_template.pdf, form_data.json
Output: completed_form.pdf
```

### Merge PDFs
```
Input: file1.pdf, file2.pdf, file3.pdf
Output: merged_document.pdf
```

## Common Use Cases

- Document data extraction for analysis
- Automated form completion workflows
- Report generation and consolidation
- Document archive organization

## When to Use This Skill

Use this skill when:
- Working with PDF documents
- The user mentions PDF files, forms, or document processing
- Text extraction from documents is needed
- Form automation is required
- Merging multiple PDF files
