from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import math

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEETID = '1ZgYaU1_9VeyTdQpUgDW3HqCSnJxuiN8Z65q1y5K0RKQ'
DATARANGE = 'engenharia_de_software!A4:F'

def authenticate():
  creds = None
  if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
      creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

  service = build('sheets', 'v4', credentials=creds)
  return service

def calculate_frequency(absence):
  return absence/60

def calculate_grade(grade_1,grade_2,grade_3):
  return (grade_1 + grade_2 + grade_3)/3 

def calculate_exam_grade(grade):
  return math.ceil((100 - grade)/10)

def update_sheet_data(values, service):
  body = { 'values': values }
  result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEETID, range='engenharia_de_software!G4',
            valueInputOption="RAW", body=body).execute()
  print('{0} cells updated.'.format(result.get('updatedCells')))

def get_sheet_data(service):
  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId=SPREADSHEETID,
                              range=DATARANGE).execute()
  values = result.get('values', [])
  return values

def main():
  service = authenticate()
  values = get_sheet_data(service)

  if not values:
    print('No data found.')
  else:
    gradeValues = []
    for row in values:
      absences = calculate_frequency(int(row[2]))

      if absences > 0.25:
        situationCell = "Reprovado por falta"
        examGrade = 0
      else:
        grade = calculate_grade(int(row[3]), int(row[4]), int(row[5]))
        if grade < 50:
          situationCell = "Reprovado por Nota"
          examGrade = 0
        elif grade < 70:
          situationCell = "Exame Final"
          examGrade = calculate_exam_grade(grade)
        else:
          situationCell = "Aprovado"
          examGrade = 0
      
      gradeValues.append([situationCell,examGrade])

  update_sheet_data(gradeValues,service)
    

if __name__ == '__main__':
    main()