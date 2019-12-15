import boto3, csv, json


def download_data():
    s3 = boto3.client('s3')
    s3.download_file('comp851-m1-f19', 'userdata2.csv', 'ud2.csv')
    with open('userdata2.csv', 'wb') as f:
        s3.download_fileobj('comp851-m1-f19', 'userdata2.csv', f)
    return csv_to_json()

def csv_to_json():
    with open('userdata2.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        json_data = json.dumps(rows)
        leads = json.loads(json_data)
        # cleaning JSON user data
        for lead in leads:
            del lead["registration_dttm"]
            del lead["ip_address"]
            del lead["salary"]
            del lead["comments"]
            with open('userdata.json', 'a') as f:
                json.dump(lead, f)
    return lead
