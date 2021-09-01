
def textResponseFormatter(data) -> str:
    """ Response formatter based on dict data or list of dict data"""
    if isinstance(data, list):
        headers = data[0].keys()
        final_data = ",".join(headers)
        for d in data:
            final_data += "\n"
            for h in headers:
                final_data += str(d[h]) + ','
        return final_data
    if isinstance(data, dict):
        headers = data.keys()
        final_data = ",".join(headers)
        final_data += "\n"
        for h in headers:
            final_data += str(data[h]) + ','

        return final_data
    return ""



        