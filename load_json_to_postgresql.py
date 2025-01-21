import json
import psycopg2

# Load JSON data
with open('output_updated.json', 'r') as json_file:
    data = json.load(json_file)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="g_motions",
    user="g_motions_user",
    password="E3ohbqZuMTdu1UucUvSKXtyugYFdQQJ9",
    host="dpg-cu7olgdsvqrc739aav2g-a.oregon-postgres.render.com",
    port="5432"
)
cursor = conn.cursor()

# Fetch User IDs from user_authentication_customuser table
cursor.execute("SELECT id FROM user_authentication_customuser")
user_ids = cursor.fetchall()
user_id_mapping = [user_id[0] for user_id in user_ids]

# Convert boolean fields
def convert_boolean_fields(row, cursor, table_name):
    cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
    columns_info = cursor.fetchall()
    for column, data_type in columns_info:
        if data_type == 'boolean' and column in row:
            row[column] = bool(row[column])
    return row

# Rename columns if necessary
def rename_columns(row, table_name):
    column_renames = {
        'auto_parts_cart': {'CustomUser_id': 'customuser_id'}
    }
    if table_name in column_renames:
        for old_name, new_name in column_renames[table_name].items():
            if old_name in row:
                row[new_name] = row.pop(old_name)
    return row

# Check if a session_key exists in django_session table
def session_key_exists(session_key):
    cursor.execute("SELECT 1 FROM django_session WHERE session_key = %s LIMIT 1", (session_key,))
    return cursor.fetchone() is not None

# Insert data into PostgreSQL tables
for table_name, rows in data.items():
    if table_name in ['sqlite_sequence', 'django_migrations', 'django_content_type']:
        continue

    for row in rows:
        row = convert_boolean_fields(row, cursor, table_name)
        row = rename_columns(row, table_name)

        # Handle customuser_id assignment only for the relevant tables
        if table_name in ['auto_parts_cart', ...]:  # Add additional tables where 'customuser_id' should be included
            if 'customuser_id' not in row or row['customuser_id'] is None:
                if user_id_mapping:
                    row['customuser_id'] = user_id_mapping[0]  # Assign the first valid user ID
                else:
                    print(f"No valid user ID available for {row}. Cannot set 'customuser_id'.")
                    continue  # Skip this row if no valid user IDs exist

        # Skip customuser_id for auth_permission if it's included
        if table_name == 'auth_permission' and 'customuser_id' in row:
            del row['customuser_id']  # Remove customuser_id if present

        # Apply any additional constraints or changes specific to your table logic here...

        if table_name == 'payments_order' and 'phone' in row:
            row['phone'] = row['phone'][:15]  # Truncate phone numbers to 15 characters

        # Insert data
        columns = ', '.join(row.keys())
        values = ', '.join([f"%({key})s" for key in row.keys()])
        print(f"Inserting into {table_name}: {row}")

        if table_name == 'django_session':
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        else:
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values}) ON CONFLICT (id) DO NOTHING"

        try:
            cursor.execute(query, row)
        except psycopg2.IntegrityError as e:
            print(f"Integrity Error inserting into {table_name}: {e}")
            conn.rollback()
        except psycopg2.Error as e:
            print(f"Error inserting into {table_name}: {e}")
            print(f"Query: {query}")
            print(f"Row data: {row}")
            conn.rollback()

# Commit the transaction
conn.commit()
cursor.close()
conn.close()




