def comp(str1, str2):
    if not isinstance(str1,str) or not isinstance(str2,str):
        return 0
    if str1 == str2:
        return 1    
    if len(str1) > len(str2):
        return 2 
    if str2 == 'learn':
        return 3

print(comp('pyt', 'learn'))