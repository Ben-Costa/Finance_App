from __future__ import print_function
import pandas as pd
import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Google_Sheets_API:
    """
    Class to handle access Google Sheets API, managing credentials, accessing data, and passing data.

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    
    """
    
    def __init__(self) -> None:
        
        self.apiService = createAPIService()

    # TODO: 
    
    def getData(self):
        # The spreadsheet to request.
        spreadsheet_id = '1QCJhKqwFWUzi7LKQlV-LffeK9WkaWhFwVzM6_3qfv8Y'  # TODO: Update placeholder value.
        SAMPLE_RANGE_NAME = 'Form Responses 1!A1:W'

        # The ranges to retrieve from the spreadsheet.
        ranges = []  # TODO: Update placeholder value.

        # True if grid data should be returned.
        # This parameter is ignored if a field mask was set in the request.
        include_grid_data = False  # TODO: Update placeholder value.

        #get length
        request1 = self.apiService.spreadsheets().get(spreadsheetId=spreadsheet_id)
        response1 = request1.execute()
        print(response1)

        #gets data
        request = self.apiService.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range = SAMPLE_RANGE_NAME)
        response = request.execute()

        return response



def createAPIService():
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
    if os.path.exists('.ignore/token.json'):
        credentials = Credentials.from_authorized_user_file('.ignore/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '.ignore/credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('.ignore/token.json', 'w') as token:
            token.write(credentials.to_json())

    service = discovery.build('sheets', 'v4', credentials=credentials)
    return service


if __name__ == "__main__":
    sheetsService = Google_Sheets_API()
    data = sheetsService.getData()
    df = pd.DataFrame(data)
    print(df)