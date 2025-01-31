import frappe
import json
from typing import Optional

from google.api_core.client_options import ClientOptions
from google.cloud import documentai  


@frappe.whitelist()
def getDocket(str):
    # # # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "agmc-reader-001"
    # location = "eu" # Format is "us" or "eu"
    # processor_id = "4162fa78942d7b48" # Create processor before running sample
    # # file_path = "/home/anish_i/test.png"
    # # mime_type = "image/png" # Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types
    # # # field_mask = "text,entities,pages.pageNumber"  # Optional. The fields to return in the Document object.
    # # # processor_version_id = "YOUR_PROCESSOR_VERSION_ID" # Optional. Processor version to use
    # content=str["content"]
    # mime_type = str["mime"].split(":")[1].split(";")[0]
    # print(mime_type)
    # # # You must set the `api_endpoint` if you use a location other than "us".
    # opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    # # #opts = ClientOptions(api_endpoint="https://eu-documentai.googleapis.com/v1/projects/31013434934/locations/eu/processors/4162fa78942d7b48:process")

    # client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # # # The full resource name of the processor, e.g.:
    # # # `projects/{project_id}/locations/{location}/processors/{processor_id}`
    # name = client.processor_path(project_id, location, processor_id)

    # # # Read the file into memory
    # # with open(file_path, "rb") as image:
    # #     image_content = image.read()

    # # # Load binary data
    # raw_document = documentai.RawDocument(content=content, mime_type=mime_type)

    # # # For more information: https://cloud.google.com/document-ai/docs/reference/rest/v1/ProcessOptions
    # # # Optional: Additional configurations for processing.
    # # # process_options = documentai.ProcessOptions()

    # # # Configure the process request
    # request = documentai.ProcessRequest(
    #     name=name,
    #     raw_document=raw_document,
    #     # field_mask=field_mask,
    #     # process_options=process_options,
    # )
    
    # result = client.process_document(request=request)

    # # # For a full list of `Document` object attributes, reference this page:
    # # # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
    # # # for(entity in result.document.entities):
    # # #     print()

    # arr = []
    # for entity in result.document.entities:
    #     value = entity.mention_text.replace("\n", "")
    #     arr.append(f'"{entity.type}":"{value}"')
    # finalStr = '{' + ",".join(arr) + '}'
    # print(finalStr)
    # data = json.loads(finalStr)
    # return data
    return {
        "description":"Dove beltCheekbokenLocah Shegah",
        "docket_no":"393732",
        "make":"Camto",
        "out_datetime":"2.3Ole.25",
        "out_kms":"57132",
        "out_to":"LAS",
        "reg_no":"AD 53574"
        }
