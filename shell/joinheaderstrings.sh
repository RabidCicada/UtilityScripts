#/bin/bash
#This script takes a c++ header file with an
#xml-document-giant-continuous-string split across multiple lines as delimited
#string portions and turns it into a well formated xml document

# Its been used to convert lightdm-gtk's default xml in c++ headers into real
#xml documents for editing

#Example
# "<xml><field attribute=\"derp\"><more-nested-shit>words</more-nested-shit></f"
# "ield></xml>"
sed -z 's/\("\n\)\|\(  "\)//g' $1 | sed -z 's/\\"/"/g' | tidy -xml -i - > $2
