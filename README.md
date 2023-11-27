# Analogical Reasoning Detection Pipeline Documentation

## Overview
This project is a tool for the detection of analogical reasoning in annual reports. It consists of a multi-step pipeline with accommodation for scanned document images via OCR and for Nexis Uni multi-document downloads, though any text documents can be used with proper accomodation and cleaning. The final output will be a dataset with GPT-detected analogies labeled as accurate or inaccurate. This data may be used as-is for analysis or used to fine-tune an LLM for more accurate analogy detection.

## Prerequisites
- The pipeline is developed and tested on Windows 11 with Python 3.11.5.
- Utilizes Microsoft® Excel® for Microsoft 365 MSO Version 2310.
- Requirements and dependencies listed in requirements.txt.

## Directory Structure

The project directory is organized as follows:
```plaintext
project_root/
│
├── analogy-detection/
│ └── gpt-query.py
│
├── data-generation/
│ ├── extract-positive.py
│ └── human-validate.py
│
├── pdf-recognition/
│ ├── annual-reports-pdf/
| ├── annual-reports-txt/
| └── PDFtoText.py
│
├── text-cleaning/
│ ├── raw-data/
│ ├── split-texts/
│ └── nexis-split.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

- **analogy-detection/:** Scripts for analogy detection step with GPT query.
  - `gpt-query.py:` Script to query GPT and record responses.

- **data-generation/:** Scripts for human-reinforced data validation step.
  - `extract-positive.py:` Script to detect and report positive GPT responses.
  - `human-validate.py:` Script to run human verification step.

- **pdf-recognition/:** Scripts for OCR step for scanned documents.
  - `annual-reports-pdf/:` Folder for PDF files to be converted.
  - `annual-reports-txt/:` Folder where OCR output will be sent.
  - `PDFtoText.py:` Script for OCR .pdf -> .txt conversion.

- **text-cleaning/:** Scripts for processing and cleaning Nexis Uni texts.
  - `raw-data/:` Folder for Nexis Uni batch downloads in raw format.
  - `split-texts/:` Folder where split and cleaned files will be sent.
  - `nexis-split.py:` Script to process Nexis Uni batch document into individual text files and perform basic cleaning.

- **README.md:** Project documentation.

- **requirements.txt:** List of project dependencies.

## Installation

- For Nexis Uni batch downloads, convert the PDF to a .txt file and place it in text-cleaning/raw-data/.
- For other text files, place them directly in text-cleaning/split-texts/ and proceed as usual.
- For PDF conversions, place your PDF documents in pdf-recognition/annual-reports-pdf/.

Note: Conversion from PDF -> .txt, image -> PDF, etc. not included within the project. There are many free or open-source conversion apps available online.

## Data Processing Steps

1. Data Preprocessing:
   1. FOR NEXIS UNI BATCH DOWNLOADS:
      1. Add .txt files to text-cleaning/raw-data/.
      2. Run text-cleaning/nexis-split.py.
      3. Verify that text documents have been created in text-cleaning/split-texts/.
   2. FOR PDF SCANNED DOCUMENTS:
      1. Configure Google Cloud Platform.
          1. Navigate to GCP dashboard and create a new project.
          2. Create a storage bucket within the project.
          3. Add two sub-folders to the bucket, one for pdfs and one for OCR results.
          4. Upload your PDF files to the PDF folder in GCP.
          5. Generate GCP credentials.
          6. Within pdf-recognition/PDFtoText.py, you will need to adjust the following parameters:
             - os.environ['GOOGLE_APPLICATION_CREDENTIALS']: GCP credentials .json file.
             - SOURCE_URI: Your PDF bucket URI. Ex: 'gs://pdf-ocr/pdfs/'
             - DEST_URI: Your OCR results bucket URI.
             - BUCKET_NAME: Your bucket name. Ex: 'pdf-ocr'
          7. Run pdf-recognition/PDFtoText.py.
          8. Results will be saved in pdf-recognition/outputs/.
2. GPT Query
   1. If you used OCR, switch the TEXTS_FOLDER parameter in analogy-detection/gpt-query.py to "../pdf-recognition/outputs/". If you did not use OCR, no change is required.
   2. Generate an OpenAI key and add it to the project via your preferred method.
   3. Run analogy-detection/gpt-query.py.
   4. Query response results will be saved to analogy-detection/query-response-data.xlsx. Records of the content of the queries will be recorded in analogy-detection/query-data.csv.
4. Response Classification
   1. Run data-generation/extract-positive.py. Verify that results are saved to data-generation/positive-responses.csv.
6. Human Verification
   1. Run data-generation/human-validate.py. You will be guided through verifying each detected analogy. You may close the window at any time, and progress will be saved.
   2. Your final results will be saved in data-generation/user-responses.xlsx.

## Code Comments
- TODO add Comments within the code for clarity.
- TODO add test data.
- Explanation of major functions, blocks, or operations.

## Parameters and Configurations
- This project utilizes GPT 3.5 Turbo as of December 2023. Using a different model may improve performance, and may be necessary as APIs are updated.

## Error Handling
- If you experience slow response times with your GPT queries, you may benefit from running analogy-detection/gpt-query.py on small batches of files rather than all at once. The simplest method would be to create a folder to hold a few documents at a time and update TEXTS_FOLDER to this new location.
- As of December 2023 the API's timeout parameter does not seem to be working, so sometimes GPT gets "stuck" and may take up to ten minutes waiting before throwing an error. The error will be caught and the query repeated, but be aware that this may considerably increase the amout of time it takes the code to run.

## Outputs
After the human verification step, you will produce an Excel file of the following format:

| FILE | CONTENT | USER-RESPONSE |
|----------|----------|----------|
| filename-1.txt | GPT Response 1 | No |
| filename-2.txt | GPT Response 2 | Yes |
| filename-3.txt | GPT Response 3 | Flag |

## Performance Considerations
- GPT 3.5 Turbo is affordable and fast, but given the quantity of data being processed, it may take considerable time to complete all queries.

## Examples and Use Cases
- Practical examples demonstrating pipeline use.
- Sample commands or scripts for typical cases.
  
## Contact Information
- Feel free to reach out to emilyhasson927@gmail.com for any questions or clarifications.

## Version History
- Documentation and full file structure committed 12/10/2023.

  
