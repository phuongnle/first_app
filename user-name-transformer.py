def transform(entity):
    entity['firstName'] = entity['firstName'].lower() if 'firstName' in entity else ''
    entity['lastName'] = entity['lastName'].upper() if 'lastName' in entity else ''
    entity['name'] = (entity['firstName'] + ' ' + entity['lastName']).strip()
        
    return entity
