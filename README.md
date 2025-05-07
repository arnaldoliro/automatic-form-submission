# Automação de Envio de Convites

Script para envio automatizado de convites via API.

## Configuração

1. Renomeie `.env.example` para `.env`
2. Preencha com suas credenciais reais
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

Execute o script principal:
```bash
python main.py
```

## Estrutura do .env

- `API_URL`: Endpoint da API
- `BEARER_TOKEN`: Token de autenticação
- `EMAILS`: Lista de emails separados por vírgula
- `ROLE_NAME`: Nome do cargo/função
- `START_DATE`: Data de início no formato ISO 8601

## Segurança

- Todos os dados sensíveis são armazenados no arquivo `.env`
- O arquivo `.env` está listado no .gitignore e não será commitado
- Os logs protegem informações sensíveis usando hashes

## Dependências

- Python 3.6+
- Bibliotecas listadas em `requirements.txt`