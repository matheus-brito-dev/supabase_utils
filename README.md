# SupCliente: Cliente Singleton Genérico para Supabase em Python

**Autor:** Matheus Brito  
**Licença:** MIT

SupCliente é um pacote Python que implementa um cliente **Supabase Singleton** para facilitar operações comuns de banco de dados (CRUD + RPC) de forma simples, consistente e reaproveitável em múltiplas aplicações.

Desenvolvido inicialmente para uso pessoal e profissional no ecossistema de projetos com banco de dados Supabase, está agora aberto para a comunidade.

---

## ✨ Recursos Disponíveis

- ✅ Conexão automática e única (Singleton) com o Supabase via `.env`.
- ✅ Operações CRUD simplificadas:
  - **Insert** (`salvar`)
  - **Select** com filtros, ordenação, limites e comparação por operadores (`buscar`, `buscar_in`, `buscar_or`, `buscar_por_colunas`, `buscar_comparando`)
  - **Update** (`atualizar`)
- ✅ Execução de funções RPC:
  - Sem parâmetros (`rpc_no_param`)
  - Com parâmetros (`rpc`)
- ✅ Filtros dinâmicos com múltiplos operadores: `eq`, `neq`, `gte`, `lte`, `gt`, `lt`, `like`, `in`.
- ✅ Filtros compostos com lógica OR (`buscar_or`).
- ✅ Carregamento automático de variáveis de ambiente (.env).

---

## 📦 Instalação

Para instalar via pip diretamente do GitHub:

```bash
pip install git+https://github.com/seuusuario/supcliente.git
