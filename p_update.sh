#!/bin/zsh

conda_prompt="$CONDA_PROMPT_MODIFIER"
export PROMPT="╭─%{$FG[086]%}%n%{$reset_color%} %{$FG[239]%}at%{$reset_color%} %{$FG[012]%}$(box_name)%{$reset_color%} %{$FG[239]%}in%{$reset_color%} %{$terminfo[bold]$FG[210]%}%~%{$reset_color%}\$(git_prompt_info)\$(ruby_prompt_info) %D - %*
╰─\$(virtualenv_info)\${conda_prompt}\$(prompt_char) "
