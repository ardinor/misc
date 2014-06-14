# Useful additions to .bashrc I've found around the place

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