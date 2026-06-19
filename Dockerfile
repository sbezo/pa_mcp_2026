FROM node:alpine AS palo-build

WORKDIR /opt/palo-mcp

RUN apk add --no-cache git ca-certificates

RUN git clone https://github.com/apius-tech/Palo-MCP.git . \
    && npm ci \
    && npm run build \
    && npm prune --omit=dev

FROM python:alpine

WORKDIR /app

RUN apk add --no-cache ca-certificates nodejs

RUN pip install --no-cache-dir mcpo

COPY --from=palo-build /opt/palo-mcp /opt/palo-mcp

EXPOSE 8000

CMD ["sh", "-c", ": \"${MCPO_API_KEY:?MCPO_API_KEY must be set}\"; : \"${PANOS_HOST:?PANOS_HOST must be set}\"; : \"${PANOS_API_KEY:?PANOS_API_KEY must be set}\"; exec mcpo --host 0.0.0.0 --port 8000 --api-key \"$MCPO_API_KEY\" -- node /opt/palo-mcp/dist/index.js"]
