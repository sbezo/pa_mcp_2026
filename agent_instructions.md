PA MCP tool rules:

The Palo Alto firewall is configured in environment mode.

When calling PA MCP tools, do not send the `firewall` parameter.

`list_firewalls` may show a firewall named `env`, but `env` is only an internal environment-mode placeholder. Do not pass `"firewall": "env"` to tools.

Do call `list_firewalls` only once per chat.

Always call tools like `get_firewall_info`, `get_interfaces`, `get_zones`, `get_security_rules`, and other PA MCP tools with an empty JSON body: `{}`.

Only use a `firewall` parameter if the user explicitly configures named multi-firewall mode with `firewalls.json`.


