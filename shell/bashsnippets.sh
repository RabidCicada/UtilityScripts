#title + green user@machine + blue path + regular $

function settitle () {
	  export PS1="\[\e]0;$1\a\]\[\033[32m\]\u@\h:\w\[\033[34m\]~\[\033[0m\]$"
}

