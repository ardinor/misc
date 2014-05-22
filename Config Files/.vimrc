execute pathogen#infect()

syntax on

if has("gui_running")
    if has("gui_gtk2")
        set guifont=Ubuntu\ Mono\ 12
    endif
    set t_Co=256
    colorscheme smyck "nightshimmer
else
    set t_Co=16
    "colorscheme ir_black
    colorscheme smyck
endif

if $COLORTERM == 'gnome-terminal'
    set t_Co=256
endif

set nocompatible  " vim, not vi

" Filetype plugins
filetype plugin on
filetype indent on

set ruler

" Line numbers
set number

set autoindent smartindent

set smarttab

" Use spaces instead of tab
set expandtab

"1 tab = 4 spaces
set tabstop=4
set shiftwidth=4

" Show matching brackets
set showmatch

set incsearch " incremental search

" Read when a file is changed from the outside
set autoread

" Height of the command bar
"set cmdheight=2

"A buffer becomes hidden when abandoned
set hid

"Ignore case when searching
set ignorecase

" Used when searching
set smartcase

"Highlight search results
set hlsearch

" Don't redraw while executing macros
set lazyredraw

"Set utf8
set encoding=utf8
set fileencoding=utf8

"set file type as unix
set ffs=unix,dos,mac

"Get Airline to show up all the time
set laststatus=2
"Airline Theme
let g:airline_theme='murmur'

"Show what command we pushed
set showcmd

"Default the path to the directory containing the current file (.)
"then the current directory (,,) 
"then each directory under the current (**)
set path=.,,**
