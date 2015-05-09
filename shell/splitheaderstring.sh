#This requires a specially created version of fold that supports the -d<char> option (avoid breaking on character) it was created by kyle stapp to facilitate easy header file style split strings with fold.
sed 's/^[[:space:]]*//' $1 | sed 's/[[:space:]]*$//' | sed -z 's/\n//g' | sed 's/"/\\"/g' | fold -w76 -d\\ |  sed 's/^/  "/g' | sed 's/$/"/g' > $2
