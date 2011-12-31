a=raw_input()
" ".join(a)
if a.count("(")==a.count(")"):
	while a.count("()")!=0:
		a=a.replace("()", "")
if len(a)==0:
	print "YES"
else:
	print "NO"
