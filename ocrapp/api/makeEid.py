import frappe
import json
from typing import Optional

from google.api_core.client_options import ClientOptions
from google.cloud import documentai  
@frappe.whitelist()
def makeDoc(data):
    print("executing!")
    print(data)
    return "Received!"