def internet_on():
    return (lambda a: True if 0 == a.system('ping www.google.com -n 3 -l 32 -w 3 > clear') else False)(__import__('os'))
 
 
print(internet_on())

# Import libraries
import dns.resolver
  
# Finding A record
result = dns.resolver.resolve('google.com', 'A')

  
# Printing record
for val in result:
    print('A Record : ', val.to_text())
