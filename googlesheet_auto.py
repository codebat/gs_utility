from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
store = file.Storage('/disk1/bihari/anshul_codes/codes/token.pickle')
creds = store.get()
if not creds or creds.invalid:
    if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
    else:
        flow = client.flow_from_clientsecrets('/disk1/bihari/anshul_codes/codes/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

spreadsheet_id = '1nOYGR2ZdeSQlTlaU67T2lUe7mGOHiJOVeOuyDn1Z8jY'


