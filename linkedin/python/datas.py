import requests

url = 'http://jira.<company name>/rest/api/latest/search?jql=reporter=dwesterveld'
response = requests.get(url)

