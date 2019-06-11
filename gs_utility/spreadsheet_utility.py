def clear_cell(spreadsheet_id,cell_range,service):
    request = service.spreadsheets().values().clear(spreadsheetId=spreadsheet_id, range=cell_range, body=clear_values_request_body)
    response = request.execute()
    return response

def get_values(spreadsheet_id,cell_range,service):
    ranges = cell_range
    request = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id,ranges = ranges)
    response = request.execute()
    return response['valueRanges']

def push_values(spreadsheet_id,cell_range,values,service):
    body_ = {
    'value_input_option': 'USER_ENTERED',
    'data': [{"range": range_,'values': values_} for (range_,values_) in zip(cell_range,values)]  
    }
    request = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body_)
    response = request.execute()
    return response

def addsheet(spreadsheet_id,name,service,n_rows=100,n_cols=100):
    new_sheet_request = {
    "requests": [
    {
      "addSheet": {
        "properties": {
          "title": name,
          "gridProperties": {
            "rowCount": n_rows,
            "columnCount": n_cols
          }
        }
      }
    }
    ]
    }
    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id,body=new_sheet_request)
    response = request.execute()
    return response

def delsheet(spreadsheet_id,sheetids,service):
    if len(sheetids)<=0:
        return None
    del_sheet_requests = {"requests":[{'deleteSheet':{'sheetId':ids}} for ids in sheetids]}
    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id,body=del_sheet_requests)
    response = request.execute()
    return response

def get_spreadsheet(spreadsheet_id,service):
    request = service.spreadsheets().get(spreadsheetId = spreadsheet_id)
    response = request.execute()
    return response
  


