def transform(event):
    try:
        name_column_index = event['columns'].index('name')
        for user in event['data']:
            user[name_column_index] = user[name_column_index].upper()
    except:
        pass

    return event
