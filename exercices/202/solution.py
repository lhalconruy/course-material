def starts_with(A, B):
    sA = str(A)
    sB = str(B)
    if sA[0:len(sB)] == sB:
        return True
    return False
