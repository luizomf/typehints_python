#
# Type Hints no Python (o básico) - Aula 1
#
# Vamos começar do mais BÁSICO até o mais AVANÇADO (só depende de você).
#
# Ao longo dessa playlist, vamos usar Type annotations, que é a sintaxe oficial.
# Mas o termo popular é "Type hints", inclusive na própria doc do Python.
#
# O que são Type Hints?
#
# São "dicas" (hints) de tipo que você adiciona no seu código.
# Elas não mudam como o Python roda seu código, ou seja, o interpretador ignora
# completamente. Mas elas servem pra coisas MUITO úteis, tipo:
# - Permitir que ferramentas como Mypy ou Pyright encontrem erros antes de rodar
# - Ativar autocompletar inteligente e mostrar docs nos editores
# - Ajudar você mesmo a entender melhor o seu código
# - Evitar bugs bobos (ex: passar int onde era str, etc...)
# - Melhorar a legibilidade do código, como se fosse uma documentação automática
#
# Hoje em dia, praticamente todo projeto Python moderno usa Type Hints.
# Portanto, considere como uma boa prática.
#
# Existem vários Type Checkers disponíveis: mypy, pyright, pyre, pytype, etc.
# Vou usar o Pyright por alguns motivos bem simples:
# - É o que eu uso no Neovim, Zed e VS Code;
# - É o que vem por padrão no VS Code (via extensão Pylance);
# - E é o que está incluso no nosso "Ambiente Python 2025".
#
# Glossário relacionado:
# - Type hint: Termo geral para qualquer dica de tipo adicionada ao código.
# - Type hinting: A ação de adicionar essas dicas de tipo.
# - Annotation: Qualquer anotação extra no código Python (não só de tipo).
# - Type annotation: Uma annotation usada especificamente para tipos no Python.
