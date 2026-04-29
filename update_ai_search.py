from upload_sql_records_to_ai_search import ingest_all_records

def update_all_records_created_in_last_week():
    sql_query = "SELECT * FROM Products WHERE [Date Modified] >= date('now', '-7 days')"
    ingest_all_records(sql_query)