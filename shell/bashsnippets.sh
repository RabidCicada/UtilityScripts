#title + green user@machine + blue path + regular $

function settitle () {
	  export PS1="\[\e]0;$1\a\]\[\033[1m\033[92m\]\u@\h:\[\033[94m\]\w\[\033[0m\]$"
}

