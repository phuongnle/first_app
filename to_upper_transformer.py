def transform(entity):
    if 'name' in entity:
        entity['name'] = entity['name'].upper()
        
    return entity
