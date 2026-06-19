

### Build Palo Alto MCP server docker image and wrap it to mcpo
> MCP server 'https://github.com/apius-tech/Palo-MCP' uses **stdio**
> MCP client Open WebUI supports **MCP Streamable HTTP** or **OpenAPI**
> mcpo acts as a bridge
```
docker build -t pa-mcp -f Dockerfile .
```

### Install requirements for python script (for obtaining API key)
pip install -r requirements.txt

### PA setup
- Create new Admin role on PA firewall 
  *Device > Admin Roles > Add; Enable XML API permissions needed for this integration*
- Create new API user
  *Device > Administrators > Add; Assign the newly created API role*
- Add username, password and PA FW IP address to `.env`

Generate/Refresh `PA_TOKEN` from `PA_HOST`, `PA_USERNAME`, and `PA_PASSWORD`:
```
python3 ./get_panos_api_key.py
```

### Generate random keys for OpenWebUI and MCP server and add them to .env
- WEBUI_SECRET_KEY
- MCPO_API_KEY

### start Ollama server:
> Open 2 terminals:
First terminal:
```
ollama serve
```
Second terminal:
```
ollama run qwen3:4b
```

### Add link to LLM model to .env
```
OLLAMA_BASE_URL=http://host.docker.internal:11434
```

### Spin up Open WebUI and the Palo MCP:

```
docker compose up --build
```

### Test the MCP OpenAPI proxy from the host:

```
set -a
. ./.env
set +a

curl http://localhost:8000/docs
curl -H "Authorization: Bearer $MCPO_API_KEY" http://localhost:8000/openapi.json
```

### Test connectivity to the configured PA device:

```
curl -X POST http://localhost:8000/get_firewall_info \
  -H "Authorization: Bearer $MCPO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Open and set up Open WebUI:
- Open WebUI at: [[http://localhost:8080]]
- Create account if needed (first time)
- Add MCP: Settings > Admin Settings > Integrations > Add Connection
  
```
Type: OpenAPI
Name: PA MCP
URL: http://pa_mcp:8000
Auth: Bearer + MCPO_API_KEY
```
- Verify connection
- Save

- New Chat > Integrations > Tools > PA MCP enable
