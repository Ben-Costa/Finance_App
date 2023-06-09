from __future__ import print_function
import pandas as pd
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint

from googleapiclient import discovery

"""Shows basic usage of the Sheets API.
Prints values from a sample spreadsheet.
"""
credentials = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        credentials = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(credentials.to_json())

service = discovery.build('sheets', 'v4', credentials=credentials)

# The spreadsheet to request.
spreadsheet_id = '1QCJhKqwFWUzi7LKQlV-LffeK9WkaWhFwVzM6_3qfv8Y'  # TODO: Update placeholder value.
SAMPLE_RANGE_NAME = 'Form Responses 1!A2:E'

# The ranges to retrieve from the spreadsheet.
ranges = []  # TODO: Update placeholder value.

# True if grid data should be returned.
# This parameter is ignored if a field mask was set in the request.
include_grid_data = False  # TODO: Update placeholder value.

#get length
request1 = service.spreadsheets().get(spreadsheetId=spreadsheet_id)
response1 = request1.execute()
print(response1)

#gets data
request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range = SAMPLE_RANGE_NAME)
response = request.execute()

df = pd.DataFrame(response)


# TODO: Change code below to process the `response` dict:
pprint(response)