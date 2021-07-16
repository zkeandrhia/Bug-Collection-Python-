def bug_collection():
    days = 5
    bugs = 0 
    
    for counts in range(1, days +1):
        user = int(input('Bugs ' + str(counts) + ':'))
        bugs += user
       
       
    print(f'Total: {bugs}')
        

bug_collection()