# Mem0 Configuration Reference

## Core Configuration Options

### Vector Store

- **`provider`** – Vector‑store backend (e.g. `qdrant`, `memory`, `faiss`)
- **`host`** – Host address (default: `localhost`)
- **`port`** – Port number (Qdrant default: `6333`)
- **`collection_name`** – Name of the collection
- **`dimension`** – Dimensionality of each vector
- **`path`** – Filesystem path for index & metadata (FAISS only)
- **`distance_strategy`** – Distance metric (`euclidean`, `inner_product`, `cosine`)
- **`normalize_L2`** – Apply L2‑normalization (`true` / `false`)

### LLM

- **`provider`** – LLM provider (`openai`, `anthropic`, `ollama`, …)
- **`model`** – Model name or ID
- **`temperature`** – Sampling temperature
- **`api_key`** – API key
- **`max_tokens`** – Maximum tokens to generate
- **`top_p`** – Nucleus‑sampling threshold
- **`top_k`** – Keep top‑k tokens
- **`openai_base_url`** – Base URL for OpenAI
- **`ollama_base_url`** – Base URL for Ollama
- **`deepseek_base_url`** – Base URL for DeepSeek
- **`azure_kwargs`** – Additional Azure LLM arguments
- **`http_client_proxies`** – HTTP proxy settings
- **`models`** – Model list (for multi‑model providers)
- **`route`** – Routing strategy (OpenRouter)
- **`openrouter_base_url`** – Base URL for OpenRouter
- **`site_url`** – Site URL (OpenRouter)
- **`app_name`** – Application name (OpenRouter)

### Embedder

- **`provider`** – Embedding provider (default: `openai`)
- **`model`** – Embedding model (default: `text-embedding-3-small`)
- **`api_key`** – API key for the embedding service

### Graph Store

- **`provider`** – Graph database backend (default: `neo4j`)
- **`url`** – Connection URL
- **`username`** – Username
- **`password`** – Password

### History Store

- **`provider`** – History‑store backend (default: `sqlite`)
- **`config`** – Additional history‑store settings
- **`history_db_path` / `historyDbPath`** – Path to database (default: `/history.db`)
- **`disable_history` / `disableHistory`** – Disable history storage (`false` by default)

### General

- **`version`** – API version (`v1.1` for Python, `v1.0` for Node.js)
- **`custom_fact_extraction_prompt` / `customPrompt`** – Custom prompt for memory extraction
- **`custom_update_memory_prompt`** – Custom prompt for updating memory (Python only)

## Global Options (Mem0 Platform)

When running on the Mem0 platform you can also supply:

- **`user_id`** – User identifier  
- **`agent_id`** – Agent identifier  
- **`app_id`** – Application identifier  
- **`run_id`** – Run identifier  
- **`org_id`** – Organization identifier  
- **`project_id`** – Project identifier  

## Environment Variables

```bash
MEM0_API_KEY        # Mem0 API key
OPENAI_API_KEY      # OpenAI API key
NEO4J_URL           # Neo4j connection URL
NEO4J_USERNAME      # Neo4j username
NEO4J_PASSWORD      # Neo4j password
SUPABASE_URL        # Supabase URL
SUPABASE_KEY        # Supabase key
MEM0_DIR            # Mem0 storage directory (useful for AWS Lambda)
