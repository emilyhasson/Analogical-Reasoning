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
3. Response Classification
4. Human Verification

## Code Comments
- TODO add Comments within the code for clarity.
- Explanation of major functions, blocks, or operations.

## Parameters and Configurations
- This project utilizes GPT 3.5 Turbo as of December 2023. Using a different model may improve performance, and may be necessary as APIs are updated.

## Error Handling
- Documentation of potential errors and issues.
- Troubleshooting steps and solutions for common problems.

## Outputs
- Description of expected outputs at each pipeline stage.
- Sample output files or visualizations if applicable.

## Testing and Validation
- Guidelines for testing the pipeline on small datasets.
- Validation steps and expected results.

## Performance Considerations
- Discussion on scalability and performance.
- Known limitations and areas for improvement.

## Examples and Use Cases
- Practical examples demonstrating pipeline use.
- Sample commands or scripts for typical cases.

## References
- Citations and references to relevant papers or libraries.

## Contact Information
- Information for reaching out with questions or clarifications.

## Version History
- Record of changes and updates to the pipeline.

## License
- Specification of the pipeline and documentation license.

## Acknowledgments
- Recognition of contributors, libraries, or tools.

## Conclusion
- Summary of key points.
- Encouragement for feedback.

## Appendix
- Additional resources or supplementary documentation.

## Testing Documentation
- Section detailing how the pipeline has been tested.
- Information on test datasets used.
