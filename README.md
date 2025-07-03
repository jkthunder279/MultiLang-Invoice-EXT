# MultiLang-Invoice-EXT
# 🧾 Multi-Language Invoice Extraction

A robust and scalable tool to extract structured information from invoices written in multiple languages using OCR, language detection, and NLP-based parsing.

---

## 🚀 Overview

This project automates invoice processing by extracting key fields such as invoice number, date, total amount, and vendor from invoices in various languages. It leverages OCR technology, language detection libraries, and rule-based or ML-based field extraction to handle diverse formats and linguistic styles.

---

## 🔧 Features

- 🌐 Multi-language support (English, German, Spanish, French, Hindi, and more)
- 🧠 Automatic language detection for multilingual documents
- 🔍 OCR-based text extraction (Tesseract / Google Vision API)
- 🧾 Structured field extraction: invoice number, date, total, vendor, etc.
- 📤 Outputs in JSON or CSV format
- 📥 Supports PDF and image-based invoices
- 🔄 Easily integratable with accounting or ERP systems

---

## 🛠️ Tech Stack

| Category       | Tools / Libraries                         |
|----------------|--------------------------------------------|
| Language       | Python 3.x                                 |
| OCR Engine     | Tesseract OCR / Google Cloud Vision API    |
| Language Detection | langdetect / spaCy / CLD3              |
| NLP & Parsing  | Regex / spaCy / Keyword dictionaries       |
| Output Format  | JSON, CSV                                  |
| Optional API   | FastAPI / Flask                            |

---

## 📂 Project Structure

{
  "invoice_number": "INV-2024-001",
  "date": "2024-12-01",
  "total": "$1,250.00",
  "vendor": "Acme Corp",
  "language": "en"
}
