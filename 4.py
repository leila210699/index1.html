def myfunc(s):
 s = s.split('.')
 return s[0], s[1], s[2]      
myfunc('21.06.1999')
('21', '06', '1999')
date = myfunc('21.06.1999')
type(date)
date[0]
'21'
date[1]
'06'
date[2]
'1999'
