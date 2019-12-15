import psycopg2
from db_config import config


def connect(item, high_priority):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        id = item["id"]
        first_name = item["first_name"]
        last_name =  item["last_name"]
        email = item["email"]
        gender = item["gender"]
        cc = item["cc"]
        country = item["country"]
        birthdate = item["birthdate"]

        # if birthdate == '':
        #     birthdate = '01-01-2018'
        # if salary == '':
        #     salary = 0
        # else:
        #     salary = salary.replace("$",'')
        #     salary = float(salary)
        # if cc == '':
        #     cc = 0

        sql_script_leads = 'INSERT INTO leads(id, first_name, last_name, email, gender, cc, country, birthdate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        sql_script_high_priority = 'INSERT INTO high_priority(id, first_name, last_name, email, gender, cc, country, birthdate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        record_tuple = (id, first_name, last_name, email, gender, cc, country, birthdate)
        if high_priority:
            cur.execute(sql_script_high_priority, record_tuple)
        else:
            cur.execute(sql_script_leads, record_tuple)
        conn.commit()
        print("Record inserted successfully into Leads table")
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
