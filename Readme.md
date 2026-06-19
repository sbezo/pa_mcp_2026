## Build Palo Alto MCP server image and wrap it to mcpo (one time)
docker build -t pa-mcp -f Dockerfile .



## start Ollama server first:
First terminal:
```
ollama serve
```
Second terminal:
```
ollama run qwen3:4b
```