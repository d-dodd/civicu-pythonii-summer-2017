def is_pangram(str):
    str = str.lower()
    l1 = [ord(s) for s in str]
    l2 = [(x in l1) for x in range(97, 123)]
    return not( (False in l2) or (len(str) == 0) )
    
