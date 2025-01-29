import frappe
import json
from typing import Optional

from google.api_core.client_options import ClientOptions
from google.cloud import documentai  
@frappe.whitelist()
def makeDoc(str):
    print("executing!")
    print(str)
    return "Received!"