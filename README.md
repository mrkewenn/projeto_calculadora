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
