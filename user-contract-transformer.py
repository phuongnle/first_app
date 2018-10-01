def transform(entity, sql_helper):
    user_id = sql_helper.fetch_value("select Id from Users where Email = ?", entity['userEmail'])
    if user_id is None:
        raise RuntimeError('user does not exist')

    entity['userId'] = user_id
    entity['name'] = entity['name'].lower() if 'name' in entity else ''
    return entity
