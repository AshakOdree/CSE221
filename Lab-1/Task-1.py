#!/usr/bin/env python
# coding: utf-8

# In[ ]:


file=open('C:/Users/User/Desktop/Lab-1/input.txt')

read_lines=file.readlines()
even_count=0
odd_count=0
not_parity_count=0
pal_count=0
non_pal_count=0

file2=open('C:\\Users\\User\\Desktop\\Lab-1\\output.txt','w')
file3=open('C:\\Users\\User\\Desktop\\Lab-1\\record.txt','w')
for i in read_lines:
    
    string=i.split(' ')
    num=string[0]
    m=string[1]
    word1=m.split('\n')
    word=word1[0]
    
    if '.' in num:
        floaat=float(num)
        not_parity_count+=1
        
        if word == None:
            file2.write(num +' cannot have parity and '+word+' is not a palindrome\n')
                     
        
        elif word == word[::-1]:
        
            pal_count+=1
            file2.write(num +' cannot have parity and '+word+' is a palindrome\n')
    
        else:
            non_pal_count+=1
            file2.write(num +' cannot have parity and '+word+' is not a palindrome\n')
        
    else:
        intger=int(num)
        
        if intger%2 ==0:
            even_count=even_count+1
            
            if word == None:
                file2.write(str(intger) +' has even parity and '+word+' is not a palindrome\n')
        
            elif word == word[::-1]:
                pal_count+=1
                file2.write(str(intger) +' has even parity and '+word+' is a palindrome\n')
    
            else:
                non_pal_count+=1
                file2.write(str(intger) +' has even parity and '+word+' is not a palindrome\n')
                
        else:
            odd_count=odd_count+1
            
            if word == None:
                file2.write(str(intger) +' has odd parity and '+word+' is not a palindrome\n')
        
        
        
            elif word == word[::-1]:
                pal_count+=1
                
                file2.write(str(intger) +' has odd parity and '+word+' is a palindrome\n')
    
            else:
                non_pal_count+=1
                file2.write(str(intger) +' has odd parity and '+word+' is not a palindrome\n')
                

                
odd_p=int(100*(odd_count/(even_count+odd_count+not_parity_count)))
even_p=int(100*(even_count/(even_count+odd_count+not_parity_count)))
no_p=int(100*(not_parity_count/(even_count+odd_count+not_parity_count)))
pali=int(100*(pal_count/(pal_count+non_pal_count)))
non_pali=int(100*(non_pal_count/(pal_count+non_pal_count)))
                
file3.write('Percentage of odd parity: '+str(odd_p)+'%\n')                
file3.write('Percentage of even parity: '+str(even_p)+'%\n')                 
file3.write('Percentage of no parity: '+str(no_p)+'%\n')
file3.write('Percentage of palindrome: '+str(pali)+'%\n')
file3.write('Percentage of palindrome: '+str(non_pali)+'%\n')
                
                
file3.close() 
file2.close()    
file.close()  


# %%
