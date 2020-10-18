#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tags.py (Python)
# 
# Objetivo: Formatar lista de tags para vídeo do Youtube.
# 
# Site: https://dirack.github.io
# 
# Versão 1.0
# 
# Programador: Rodolfo A C Neves (Dirack) 18/10/2020
# 
# Email: rodolfo_profissional@hotmail.com
# 
# Licença: GPL-3.0 <https://www.gnu.org/licenses/gpl-3.0.txt>.

import pyperclip

# Copia tags da área de transferência
string = pyperclip.paste()

# Novas tags
tags=['nova tag 1','nova tag 2','nova tag 3']

# Tags anteriores + tags novas
string = string+','+(','.join(tags))

# Copia tags para a área de transferência
pyperclip.copy(string)

msg=input("Copied to clipboard, use Ctrl+v to paste. Press enter to exit the program")
