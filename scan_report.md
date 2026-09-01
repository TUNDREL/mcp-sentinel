# MCP Sentinel — Security Audit Report
*Generated 2026-09-01 14:29 UTC*

## Summary
- **Servers scanned:** 29
- **Successfully connected:** 10
- **Total tools analyzed:** 255
- **Findings:** 0 critical, 23 high, 52 medium, 0 low

## Server Details

### DeepWiki MCP
URL: `https://mcp.deepwiki.com/mcp`

**Status: Failed to connect**
- Unsupported transport type: steamable-http
- (failed after 3 attempts)

### GitMCP Docs
URL: `https://gitmcp.io/docs`

**Status: OK** — 5 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`search_generic_documentation`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`search_generic_code`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`fetch_generic_url_content`) — Parameter 'url' looks like it could accept paths/commands/queries with no validation.

### 402.bot MCP
URL: `https://api.402.bot/mcp`

**Status: Failed to connect**
- ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1077)
- (failed after 3 attempts)

### BGPT Science MCP
URL: `https://mcp.bgpt.pro/mcp`

**Status: Failed to connect**
- ConnectError: [Errno 11001] getaddrinfo failed
- (failed after 3 attempts)

### Find-A-Domain MCP
URL: `https://api.findadomain.dev/mcp`

**Status: OK** — 2 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.

### Peek.com MCP
URL: `https://mcp.peek.com`

**Status: OK** — 6 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`search_experiences`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`search_regions`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.

### Context Awesome
URL: `https://www.context-awesome.com/api/mcp`

**Status: OK** — 2 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`find_awesome_section`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.

### Cloudflare Authless Remote Demo
URL: `https://remote-mcp-server-authless.workers.dev/sse`

**Status: Failed to connect**
- ConnectError: [Errno 11001] getaddrinfo failed
- (failed after 3 attempts)

### Cloudflare Docs MCP
URL: `https://docs.mcp.cloudflare.com/sse`

**Status: Failed to connect**
- HTTPStatusError: Client error '410 Gone' for url 'https://docs.mcp.cloudflare.com/sse'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410
- (failed after 3 attempts)

### Resemble AI MCP
URL: `https://mcp.resemble.ai/sse`

**Status: OK** — 6 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`resemble_search`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`resemble_get_page`) — Parameter 'path' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`resemble_api_endpoint`) — Parameter 'path' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`resemble_api_search`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.

### Remote MCP Directory Server
URL: `https://mcp.remote-mcp.com`

**Status: OK** — 1 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`ListRemoteMCPServers`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.

### OpenMesh MCP
URL: `https://api.openmesh.dev/mcp`

**Status: Failed to connect**
- ConnectError: [Errno 11001] getaddrinfo failed
- (failed after 3 attempts)

### JSON Toolkit MCP
URL: `https://json-toolkit-mcp.yagami8095.workers.dev/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### Regex Engine MCP
URL: `https://regex-engine-mcp.yagami8095.workers.dev/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### Color Palette MCP
URL: `https://color-palette-mcp.yagami8095.workers.dev/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### Timestamp Converter MCP
URL: `https://timestamp-converter-mcp.yagami8095.workers.dev/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### Prompt Enhancer MCP
URL: `https://prompt-enhancer-mcp.yagami8095.workers.dev/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### OpenClaw Intel MCP
URL: `https://openclaw-intel-mcp.yagami8095.workers.dev/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### OpenClaw Fortune MCP
URL: `https://openclaw-fortune-mcp.yagami8095.workers.dev/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### MoltBook Publisher MCP
URL: `https://moltbook-publisher-mcp.yagami8095.workers.dev/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### FlowZap Docs MCP
URL: `https://mcp.flowzap.xyz`

**Status: Failed to connect**
- ConnectError: [Errno 11001] getaddrinfo failed
- (failed after 3 attempts)

### Kiwi.com Flight Search MCP
URL: `https://mcp.kiwi.com`

**Status: OK** — 2 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.

### SiteSpeak Chatbot MCP
URL: `https://chatbot.sitespeak.ai/api/mcp`

**Status: Failed to connect**
- MCPError: Not Found
- (failed after 3 attempts)

### Brimble Platform MCP
URL: `https://mcp.brimble.io`

**Status: Failed to connect**
- MCPError: Server returned an error response
- (failed after 3 attempts)

### Cloudflare Weather MCP
URL: `https://weather-mcp-server.superhighfives.workers.dev/mcp`

**Status: OK** — 2 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.

### Data.gouv.fr MCP
URL: `https://mcp.data.gouv.fr/mcp`

**Status: OK** — 10 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`search_datasets`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`search_organizations`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`search_dataservices`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.

### MCP Time Server
URL: `https://mcp-time-server.workers.dev/mcp`

**Status: Failed to connect**
- ConnectError: [Errno 11001] getaddrinfo failed
- (failed after 3 attempts)

### BotSpot Trading MCP
URL: `https://mcp.botspot.trade/mcp`

**Status: Failed to connect**
- MCPError: Missing Authorization header
- (failed after 3 attempts)

### SpaceMolt MCP
URL: `https://game.spacemolt.com/mcp`

**Status: OK** — 219 tools found

**Findings:**
- **[HIGH]** broad_scope (`forum_delete_thread`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`create_faction`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_create_buy_order`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_edit_role`) — Tool name contains 'edit', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_edit`) — Tool name contains 'edit', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_write_room`) — Tool name contains 'write', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_create_role`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`create_note`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`captains_log_delete`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`forum_create_thread`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`forum_delete_reply`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_delete_room`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`create_sell_order`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_delete_role`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_create_sell_order`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`create_buy_order`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`modify_order`) — Tool name contains 'modify', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`write_note`) — Tool name contains 'write', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_deposit_credits`) — Tool name contains 'edit', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_remove_enemy`) — Tool name contains 'remove', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`delete_note`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_withdraw_credits`) — Tool name contains 'edit', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_remove_ally`) — Tool name contains 'remove', suggesting write or destructive capability.
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`register`) — Parameter 'registration_code' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`faction_write_room`) — Parameter 'description' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`search_systems`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`faction_post_mission`) — Parameter 'description' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`claim`) — Parameter 'registration_code' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`facility`) — Parameter 'description' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`upload_drone_script`) — Parameter 'script' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`station`) — Parameter 'description' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`login_link_poll`) — Parameter 'device_code' looks like it could accept paths/commands/queries with no validation.