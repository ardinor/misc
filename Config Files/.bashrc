# Useful additions to .bashrc I've found around the place

# makes it jordan@oneirism ~ $
PS1='\[\e[0;32m\]\u@\h\[\e[m\] \[\e[1;34m\]\w\[\e[m\] \[\e[1;32m\]\$\[\e[m\]\[\e[1;37m\]'

# Enable extended globbing
shopt -s extglob

# Enable spelling correction of directory names during completion
shopt -s dirspell
# Need this for the above to work it seems, replaces directory names with the results of word expansions
shopt -s direxpand

# Fix minor spelling errors when using cd
shopt -s cdspell

# Updates the size of the lines and columns when the window size changes
shopt -s checkwinsize

# Use launch <program>, launches a program that keeps running even if the terminal that spawned it is closed
launch(){ disown "$1" && exit; }

# Colourises the man pages
function man()
{
    env \
    LESS_TERMCAP_mb=$(printf "\e[1;31m") \
    LESS_TERMCAP_md=$(printf "\e[1;31m") \
    LESS_TERMCAP_me=$(printf "\e[0m") \
    LESS_TERMCAP_se=$(printf "\e[0m") \
    LESS_TERMCAP_so=$(printf "\e[1;44;33m") \
    LESS_TERMCAP_ue=$(printf "\e[0m") \
    LESS_TERMCAP_us=$(printf "\e[1;32m") \
    man "$@"
}

# cd and ls in one (from the Arch wiki)
cl() {
    dir=$1
    if [[ -z "$dir" ]]; then
        dir=$HOME
    fi
    if [[ -d "$dir" ]]; then
        cd "$dir"
        ls -hal --color=auto
    else
        echo "bash: cl: '$dir': Directory not found"
    fi
}

#mkdir and cd in one
mkcd() {
    mkdir -p $1
    cd $1
}