import frappe
import json
from typing import Optional

from google.api_core.client_options import ClientOptions
from google.cloud import documentai  


@frappe.whitelist()
def getEid(str):
    # # TODO(developer): Uncomment these variables before running the sample.
    project_id = "agmc-reader-001"
    location = "eu" # Format is "us" or "eu"
    processor_id = "39a97fc80b055d3a" # Create processor before running sample
    # file_path = "/home/anish_i/test.png"
    # mime_type = "image/png" # Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types
    # # field_mask = "text,entities,pages.pageNumber"  # Optional. The fields to return in the Document object.
    # # processor_version_id = "YOUR_PROCESSOR_VERSION_ID" # Optional. Processor version to use
    content=str["content"]
    mime_type = str["mime"].split(":")[1].split(";")[0]
    print(mime_type)
    # # You must set the `api_endpoint` if you use a location other than "us".
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    # #opts = ClientOptions(api_endpoint="https://eu-documentai.googleapis.com/v1/projects/31013434934/locations/eu/processors/39a97fc80b055d3a:process")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # # The full resource name of the processor, e.g.:
    # # `projects/{project_id}/locations/{location}/processors/{processor_id}`
    name = client.processor_path(project_id, location, processor_id)

    # # Read the file into memory
    # with open(file_path, "rb") as image:
    #     image_content = image.read()

    # # Load binary data
    raw_document = documentai.RawDocument(content=content, mime_type=mime_type)

    # # For more information: https://cloud.google.com/document-ai/docs/reference/rest/v1/ProcessOptions
    # # Optional: Additional configurations for processing.
    # # process_options = documentai.ProcessOptions()

    # # Configure the process request
    request = documentai.ProcessRequest(
        name=name,
        raw_document=raw_document,
        # field_mask=field_mask,
        # process_options=process_options,
    )
    
    result = client.process_document(request=request)

    # # For a full list of `Document` object attributes, reference this page:
    # # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
    # # for(entity in result.document.entities):
    # #     print()

    arr = []
    for entity in result.document.entities:
        arr.append(f'"{entity.type}":"{entity.mention_text}"')
    finalStr = '{' + ",".join(arr) + '}'
    data = json.loads(finalStr)
    return data
    # return {
    #     "card_number": "124256387",
    #     "date_expiry": "11/09/2024",
    #     "date_issue": "09/09/2022",
    #     "date_of_birth": "14/10/1974",
    #     "employer_ar": "\u0627\u0644\u062a\u0642\u0646\u064a\u0627\u062a \u0627\u0644\u0647\u0646\u062f\u0633\u064a\u0629 \u0644\u0644\u062e\u062f\u0645\u0627\u062a",
    #     "employer_en": "Engineering Tech. Services",
    #     "full_name_ar": "\u0647\u064a\u0645\u064a\u0646\u062a\u064a\u0631\u0627 \u0641\u0648\u064a\u0646\u062a\u064a\u0633",
    #     "full_name_en": "Dindo Hementera Fuentes",
    #     "id": "784-1974-4642947-0",
    #     "nationality_ar": "\u0627\u0644\u0641\u0644\u0628\u064a\u0646",
    #     "nationality_en": "Philippines",
    #     "occupation_ar": "\u0645\u0631\u0627\u0642\u0628 \u0627\u0644\u0645\u0628\u064a\u062f\u0627\u062a \u0627\u0644\u062d\u0634\u0631\u064a\u0629",
    #     "occupation_en": "Pesticides Controller",
    #     "place_of_issue_ar": "\u0627\u0644\u0634\u0627\u0631\u0642\u0629",
    #     "place_of_issue_en": "Sharjah",
    #     "scan_number": "2203826287"
    # }


