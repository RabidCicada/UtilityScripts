sed -z 's/\("\n\)\|\(  "\)//g' $1 | sed -z 's/\\"/"/g' | tidy -xml -i - > $2
