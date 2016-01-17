x=['un', 'cuvant', 'va', 'aparea', 'intre', 'toate', 'astea']
y="TEST"
z=y.join(x)
print z

m=z.lower()
print m

propoz="I love to smile"
print propoz.replace('smile','fly')


print "________________"


book={'Tata':'Ion','Mama':'Ioana','Fiul':'Ionel'}

print book['Tata']+' '+book['Mama']
 
varsta={'Ea':'21','El':'41'}

print varsta['Ea']

book.clear()
print book

varsta2=varsta.copy()
print varsta2

print varsta2.has_key('Ea')
