def TrouverCase(Cases, v):
    for elem in Cases:
        if elem['case'] == v:
            return elem
    return None
