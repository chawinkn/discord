from openpyxl import load_workbook

def sheetData(path, range):
  workbook = load_workbook(path)
  sheet = workbook.active

  # Cell range Ex "B2:M6"
  sheetRange = sheet[range]

  # You can edit day here
  sheetDict = {
    "Mon": [], 
    "Tue": [], 
    "Wed": [],
    "Thu": [],
    "Fri": []
  }

  # Dict keys
  keys = [*sheetDict]

  # Append data
  for row in sheetRange:
    for cell in row:
      sheetDict[
        keys[sheetRange.index(row)]
      ].append(
        cell.value
      )

  return sheetDict