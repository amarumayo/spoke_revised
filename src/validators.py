# validators

def is_required(v):
    return v.strip() != ""

def is_numeric(v):
    return v.isnumeric()

def is_positive(v):
    try:
        return float(v) > 0
    except:
        return False

