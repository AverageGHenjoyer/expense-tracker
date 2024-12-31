
def gen_id(data):
    if not data:
        return 1
    else:
        return max(item['ID'] for item in data) + 1
