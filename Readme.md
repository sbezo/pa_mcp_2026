## Build Palo Alto MCP server image and wrap it to mcpo (one time)
docker build -t pa-mcp -f Dockerfile .

## Install requirements for python


## start Ollama server first:
First terminal:
```
ollama serve
```
Second terminal:
```
ollama run qwen3:4b
```

## start containers

Set these values in `.env`:

```
MCPO_API_KEY=your-local-mcpo-api-key
PANOS_HOST=your-firewall-or-panorama-ip-or-hostname
PANOS_API_KEY=your-panos-api-key
```

Build and start Open WebUI plus the Palo MCP proxy:

```
docker compose up -d --build
```

Test the MCP OpenAPI proxy from the host:

```
set -a
. ./.env
set +a

curl http://localhost:8000/docs
curl -H "Authorization: Bearer $MCPO_API_KEY" http://localhost:8000/openapi.json
```

Test read-only connectivity to the configured PA device:

```
curl -X POST http://localhost:8000/get_firewall_info \
  -H "Authorization: Bearer $MCPO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Open WebUI can reach the Palo MCP service on the Docker network at:

```
http://pa_mcp:8000
```
