import os

# Set up the credentials for the API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'boreal-graph-381820-4847d49f0433.json'

import json
import re
from google.cloud import vision
from google.cloud import storage

SOURCE_URI = 'gs://pdf-tests-ehasson/pdfs/neg/'
DEST_URI = 'gs://pdf-tests-ehasson/ocr-results/neg/'
SAVE_LOC = 'test-outputs/neg/'
BUCKET_NAME = 'pdf-tests-ehasson'
FOLDER_PATH='pdfs/neg/'

def async_detect_document(gcs_source_uri, gcs_destination_uri):
    
    mime_type = 'application/pdf'
    batch_size=100

    client = vision.ImageAnnotatorClient()

    feature = vision.Feature(
        type=vision.Feature.Type.DOCUMENT_TEXT_DETECTION
    )

    gcs_source = vision.GcsSource(uri=gcs_source_uri)
    input_config = vision.InputConfig(
        gcs_source=gcs_source, mime_type=mime_type
    )

    gcs_destination = vision.GcsDestination(uri=gcs_destination_uri)
    output_config = vision.OutputConfig(
        gcs_destination=gcs_destination, batch_size=batch_size
    )

    async_request = vision.AsyncAnnotateFileRequest(
        features=[feature], input_config=input_config, output_config=output_config
    )

    operation = client.async_batch_annotate_files(
        requests=[async_request]
    )

    print('Waiting')
    operation.result(timeout=420)


def write_to_text(gcs_destination_uri, save_file):

    storage_client = storage.Client()

    match = re.match(r'gs://([^/]+)/(.+)', gcs_destination_uri)
    bucket_name = match.group(1)
    prefix = match.group(2)

    bucket = storage_client.get_bucket(bucket_name)

    blob_list = list(bucket.list_blobs(prefix=prefix))

    output = blob_list[0]

    json_string = output.download_as_string()
    response = json.loads(json_string)

    file = open(save_file.format(str(1)), "w",  encoding="utf-8")

    for m in range(len(response['responses'])):
        first_page_response = response['responses'][m]
        annotation = first_page_response['fullTextAnnotation']


        file.write(annotation['text'])\


def list_files_in_gcs_folder(bucket_name, folder_path):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    # List all objects (files) in the specified GCS folder
    blobs = bucket.list_blobs(prefix=folder_path)

    file_names = []
    for blob in blobs:
        # Extract the file name from the full GCS object path
        file_name = blob.name.replace(folder_path, '', 1)
        file_names.append(file_name)
    return file_names[1:]


def main():
    file_names = list_files_in_gcs_folder(BUCKET_NAME, FOLDER_PATH)
    print("found " + len(file_names) + " files")

    for file_name in file_names:
        source = SOURCE_URI + file_name
        dest = DEST_URI + file_name +'/'
        async_detect_document(source, dest)
        save_file = SAVE_LOC + file_name.replace(".pdf", ".txt")
        print("writing to " + save_file)
        write_to_text(dest, save_file)
        



main()