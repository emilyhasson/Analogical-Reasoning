# Analogical Reasoning Detection Pipeline Documentation

## Overview
This project is a tool for the detection of analogical reasoning in annual reports. It consists of a multi-step pipeline with accommodation for scanned document images via OCR and for Nexis Uni multi-document downloads, though any text documents can be used with proper accomodation and cleaning.

## Prerequisites
- The pipeline is developed and tested on Windows 11 with Python 3.11.5.
- Utilizes Microsoft® Excel® for Microsoft 365 MSO Version 2310.
- Requirements and dependencies listed in requirements.txt.

## Directory Structure
- Explanation of the project directory structure.
- Purpose of each major folder and organization of files.

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
- Step-by-step instructions for setting up the environment.
- Configuration settings and any special considerations.

## Data Processing Steps

1. s
2. 

## Code Comments
- TODO add Comments within the code for clarity.
- Explanation of major functions, blocks, or operations.

## Parameters and Configurations
- List and explanation of all parameters and configurations.
- Guidelines for adjusting parameters effectively.

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
- This project utilizes GPT 3.5 Turbo as of December 2023. Note that updates to GPT API will require updating the source code.
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
