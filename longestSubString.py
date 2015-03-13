from test import testEqual
def longest_substring(s):
    '''
    Function that will find the longest substring in alphabetical order
    '''
    start = 0
    end = 1
    new_start = 0
    new_end = 1
    max_len = 1
    
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            if (new_end - new_start) > max_len:
                max_len = (new_end - new_start)+1
                start = new_start
                end = new_end
            new_start = i+1
            new_end = i+2
        else:
            new_end +=1
    if (new_end - new_start) > max_len:
        max_len = (new_end - new_start)+1
        start = new_start
        end = new_end

    return  s[start:end]

s = 'azcbobobegghakl'        
testEqual(longest_substring(s),'beggh')
testEqual(longest_substring('c'),'c')
testEqual(longest_substring('ahtajkybcdeg'),'bcdeg')



