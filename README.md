SupCliente: Cliente Singleton Genérico para Supabase em Python
Autor: Matheus Brito
Licença: MIT

SupCliente é um pacote Python que implementa um cliente Supabase Singleton para facilitar operações comuns de banco de dados (CRUD + RPC) de forma simples, consistente e reaproveitável em múltiplas aplicações.

Desenvolvido inicialmente para uso pessoal e profissional no ecossistema de projetos com banco de dados Supabase, está agora aberto para a comunidade.

✨ Recursos Disponíveis
✅ Conexão automática e única (Singleton) com o Supabase via .env.

✅ Operações CRUD simplificadas:

Insert (salvar)

Select com filtros, ordenação, limites e comparação por operadores (buscar, buscar_in, buscar_or, buscar_por_colunas, buscar_comparando)

Update (atualizar)

✅ Execução de funções RPC:

Sem parâmetros (rpc_no_param)

Com parâmetros (rpc)

✅ Filtros dinâmicos com múltiplos operadores: eq, neq, gte, lte, gt, lt, like, in.

✅ Filtros compostos com lógica OR (buscar_or).

✅ Carregamento automático de variáveis de ambiente (.env).

📦 Instalação
Para instalar via pip diretamente do GitHub:

bash
Copiar
Editar
pip install git+https://github.com/seuusuario/supcliente.git
Ou clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seuusuario/supcliente.git
cd supcliente
pip install .
⚙️ Configuração
Crie um arquivo .env na raiz do seu projeto com:

ini
Copiar
Editar
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-api-key
🚀 Exemplos de Uso
Conectar ao cliente
python
Copiar
Editar
from supcliente import get_supabase_client

cliente = get_supabase_client()
Inserir dados
python
Copiar
Editar
dados = {"nome": "João", "idade": 30}
cliente.salvar("usuarios", dados)
Buscar registros com filtros
python
Copiar
Editar
cliente.buscar("usuarios", filtros={"idade": 30}, ordenar_por="nome")
Buscar por colunas específicas
python
Copiar
Editar
cliente.buscar_por_colunas("usuarios", colunas=["nome", "idade"])
Buscar usando operadores comparativos
python
Copiar
Editar
filtros = [("idade", "gte", 18), ("nome", "like", "%Jo%")]
cliente.buscar_comparando("usuarios", filtros)
Atualizar registros
python
Copiar
Editar
cliente.atualizar("usuarios", colunas={"idade": 31}, filtros={"nome": "João"})
Buscar com cláusula OR
python
Copiar
Editar
filtros = {"or_": [("nome", "Maria"), ("nome", "João")]}
cliente.buscar_or("usuarios", filtros)
Executar RPC (Stored Procedures)
python
Copiar
Editar
cliente.rpc_no_param("minha_funcao")
cliente.rpc("minha_funcao_com_param", {"param1": "valor"})
🛠️ Requisitos
Python 3.8 ou superior

supabase-py

python-dotenv

🔒 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

🙌 Créditos
Criado e mantido por Matheus Brito.

Caso utilize este pacote ou parte do seu código, mencione o autor para manter os créditos.

📢 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, pull requests ou sugerir melhorias.
