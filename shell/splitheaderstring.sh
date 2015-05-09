sed 's/^[[:space:]]*//' $1 | sed 's/[[:space:]]*$//' | sed -z 's/\n//g' | sed 's/"/\\"/g' | fold -w76 -d\\ |  sed 's/^/  "/g' | sed 's/$/"/g' > $2
