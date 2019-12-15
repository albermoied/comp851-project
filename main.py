import s3_data, json
from send_data import send_to_leads, send_to_high_priority, send_to_txt


def filter(lead):
    if lead["country"] == 'United States':
        leads_table(lead)
    elif lead["cc"]:
        high_priority_table(lead)
    else:
        text_file(lead)

def leads_table(item):
    send_to_leads(item)

def high_priority_table(item):
    send_to_high_priority(item)

def text_file(item):
    send_to_txt(item)

if __name__ == "__main__":
    lead = s3_data.download_data()
    filter(lead)
