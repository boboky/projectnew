#!/bin/python

import sys, cgi

print "Content-type:text/html\n\n"
print "<html>"
print "<head><title>N28 PRO</title></head>"
print "<body>"
form = cgi.FieldStorage()
firstname = form.getvalue('firstname')
lastname = form.getvalue('lastname', '').upper()
sex = form.getvalue('gender')

print '<form method="post" action="button.py">'
print '<p>What is your First Name? <input type="text" name="firstname" /></p>'
print '<p>What is your Last Name? <input type="text" name="lastname" /></p>'

print '<input type="radio" name="gender" value="male"> Male<br>'
print '<input type="radio" name="gender" value="female"> Female<br>'
print '<input type="submit" value="Submit" />'

if (len(firstname)) > 0 and (len(lastname)) > 0:
        print "<h1> Hello %s %s  Welcome to my N28Pro" % (firstname, lastname) + "  and  " + "Your gender is %s</h1><br />" % (sex)

print "</form>"

print "</body>"
print "</html>"