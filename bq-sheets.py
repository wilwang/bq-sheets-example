from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'path_to_service_account_key.json')

scoped_credentials = credentials.with_scopes(
    [
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/bigquery",
    ])

client = bigquery.Client(credentials=scoped_credentials)

# Perform a query.
QUERY = ('SELECT Snowboard, Size, Actual_price FROM `dev-sandbox-env.test_data.snowboards`')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(f'{row.Snowboard} in {row.Size} costs ${row.Actual_price}')
