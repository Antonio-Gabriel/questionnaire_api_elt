import json
from pathlib import Path
from realpath import realpath

def get_questionnaires_mock():
   """A list of questionnaires provided to external service"""

   mock_data = Path(f"{realpath}/src/drivers/mocks/questionnaires_mock.json").read_text()
   questionnaires = json.loads(mock_data)

   return questionnaires
