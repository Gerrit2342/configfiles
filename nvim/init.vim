"Abschnitt für vim-plug den Plugin-Manager 
call plug#begin('~/.nvim/plugged')
"Hier folgen die zu ladenden Plugins
Plug 'maxboisvert/vim-simple-complete'
Plug 'L3MON4D3/LuaSnip', {'do': 'make install_jsregexp'} "Snippet Manager
Plug 'lervag/vimtex'
"Plug 'neoclide/coc.nvim', {'branch': 'release'} "Autocompletion
call plug#end()

set number "Zeilennummer anzeigen
set signcolumn=yes

filetype on
filetype plugin on
filetype indent on

" Change Color when entering Insert Mode
autocmd InsertEnter * highlight CursorLine guifg=white guibg=blue ctermfg=white ctermbg=darkblue
" Revert Color to default when leaving Insert Mode
autocmd InsertLeave * highlight default 
":h highlight

inoremap jj <Esc>
nnoremap WW :w<CR>
noremap j gj
noremap k gk

"Rechtschreiprüfung mit F8 aktivieren/deaktivieren
map <F8>  :setlocal spell! spelllang=de <return>

let g:tex_flavor = "latex" "Texdateien nicht als Plaintex interpretieren

"Abschnitt für LuaSnip einen Snippet-Manager (LaTeX)
" Use Tab to expand and jump through snippets
imap <silent><expr> <Tab> luasnip#expand_or_jumpable() ? '<Plug>luasnip-expand-or-jump' : '<Tab>' 
smap <silent><expr> <Tab> luasnip#jumpable(1) ? '<Plug>luasnip-jump-next' : '<Tab>'

" Use Shift-Tab to jump backwards through snippets
imap <silent><expr> <S-Tab> luasnip#jumpable(-1) ? '<Plug>luasnip-jump-prev' : '<S-Tab>'
smap <silent><expr> <S-Tab> luasnip#jumpable(-1) ? '<Plug>luasnip-jump-prev' : '<S-Tab>'


"Angabe des Ordners für das Laden der .lua Dateien
lua require("luasnip.loaders.from_lua").lazy_load({paths = "~/.nvim/LuaSnip/"})
"Externe Konfigurationsdatei (lua) einbinden
luafile  ~/.nvim/LuaSnip/config.lua

"Abschnitt für coc.nvim eine Autocompletion Engine
"ctrl +j um durch die Vorschläge zu wandern
"inoremap <silent><expr> <C-j>
"      \ coc#pum#visible() ? coc#pum#next(1) :
"      \ CheckBackspace() ? "\<Tab>" :
"      \ coc#refresh()
"inoremap <expr><C-k> coc#pum#visible() ? coc#pum#prev(1) : "\<C-k>"
"inoremap <expr><C-h> coc#pum#visible() ? coc#pum#confirm() : "\<C-k>"

"Compiler Optionen für Vimtex
 let g:vimtex_compiler_latexmk = {
        \ 'build_dir' : '',
        \ 'callback' : 1,
        \ 'continuous' : 1,
        \ 'executable' : 'latexmk',
        \ 'hooks' : [],
        \ 'options' : [
        \   '-verbose',
        \   '-file-line-error',
        \   '-synctex=1',
        \   '-interaction=nonstopmode',
        \ ],
        \}

