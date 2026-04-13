uv init projeto_calculadora
cd projeto_calculadorag
new-item .gitignore
uv add numpy
uv sync
git status (Verifiquei que a branch estava como "master", por motivos de padronizacao, resolvi mudar)
git branch -m main
git commit -m "feat: setup inicial e modulo de calculadora seguindo padrao src-layout"
git push -u origin main (error: failed to push some refs to 'https://github.com/mrkewenn/projeto_calculadora.git')
git pull origin main --allow-unrelated-histories (puxando as informacoes do repositorio para forcar integracao)
git push -u origin main (bem-sucedido)

Para rodar, use: 
uv run calculadora

mudancas foram realizadas no pyproject.toml para suportar o padrao src-layout, sendo ela:
[tool.uv]
package = true

como sugerido pela documentacao do Astral UV. Assim, o uv trata meu diretorio como pacote instalavel e permite que o project.scripts funcione como esperado, e a execucao possa acontecer chamando o nome "calculadora" ao inves de inserir todo o diretorio para o programa.
