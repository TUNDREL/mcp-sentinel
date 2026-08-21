# MCP Sentinel — Security Audit Report
*Generated 2026-08-20 13:48 UTC*

## Summary
- **Servers scanned:** 12
- **Successfully connected:** 4
- **Total tools analyzed:** 226
- **Findings:** 0 critical, 23 high, 19 medium, 0 low

## Server Details

### DeepWiki
URL: `https://mcp.deepwiki.com/mcp`

**Status: OK** — 3 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.

### Semgrep
URL: `https://mcp.semgrep.ai/sse`

**Status: Failed to connect**
- HTTPStatusError: Client error '404 Not Found' for url 'https://mcp.semgrep.ai/sse'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
- (failed after 3 attempts)

### GitMCP (example: modelcontextprotocol/python-sdk)
URL: `https://gitmcp.io/modelcontextprotocol/python-sdk`

**Status: OK** — 4 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`search_python_sdk_documentation`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`search_python_sdk_code`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`fetch_generic_url_content`) — Parameter 'url' looks like it could accept paths/commands/queries with no validation.

### Chainflip Broker
URL: `https://chainflip-broker.io/mcp`

**Status: OK** — 6 tools found

**Findings:**
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.

### 402.bot Discovery Oracle
URL: `https://api.402.bot/mcp`

**Status: Failed to connect**
- ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:1077)
- (failed after 3 attempts)

### WZRD Velocity Oracle
URL: `https://app.twzrd.xyz/api/mcp`

**Status: Failed to connect**
- ConnectError: [Errno 11001] getaddrinfo failed
- (failed after 3 attempts)

### SpaceMolt
URL: `https://game.spacemolt.com/mcp`

**Status: OK** — 213 tools found

**Findings:**
- **[HIGH]** broad_scope (`faction_create_buy_order`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`create_faction`) — Tool name contains 'create', suggesting write or destructive capability.
  - *AI review: **false_positive** — The description only specifies standard parameters and constraints for creating a faction without any malicious instructions or manipulation attempts.*
- **[HIGH]** broad_scope (`forum_delete_reply`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`write_note`) — Tool name contains 'write', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`captains_log_delete`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`forum_create_thread`) — Tool name contains 'create', suggesting write or destructive capability.
  - *AI review: **false_positive** — The description merely provides standard operational details and category options for creating a forum thread without any manipulative instructions.*
- **[HIGH]** broad_scope (`forum_delete_thread`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_delete_room`) — Tool name contains 'delete', suggesting write or destructive capability.
  - *AI review: **false_positive** — The tool description is standard for game/faction management functionality and contains no prompt injection or manipulative instructions.*
- **[HIGH]** broad_scope (`modify_order`) — Tool name contains 'modify', suggesting write or destructive capability.
  - *AI review: **false_positive** — The tool description merely outlines standard order modification and bulk processing capabilities without any prompt injection or malicious instructions.*
- **[HIGH]** broad_scope (`faction_create_role`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_withdraw_credits`) — Tool name contains 'edit', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_write_room`) — Tool name contains 'write', suggesting write or destructive capability.
  - *AI review: **false_positive** — The tool description contains legitimate game-related worldbuilding instructions and parameters without any prompt injection or malicious behavior manipulation.*
- **[HIGH]** broad_scope (`faction_deposit_credits`) — Tool name contains 'edit', suggesting write or destructive capability.
  - *AI review: **false_positive** — The tool description is standard functional text describing a game mechanic and contains no prompt injection, malicious instructions, or AI manipulation.*
- **[HIGH]** broad_scope (`faction_delete_role`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_create_sell_order`) — Tool name contains 'create', suggesting write or destructive capability.
  - *AI review: **false_positive** — The tool description merely outlines legitimate game/market functionality and parameter specifications without any prompt-injection or agent-manipulating instructions.*
- **[HIGH]** broad_scope (`create_sell_order`) — Tool name contains 'create', suggesting write or destructive capability.
  - *AI review: **false_positive** — The tool description merely outlines game mechanics, fees, and parameter details for creating market sell orders with no malicious prompt-injection or behavioral override attempts.*
- **[HIGH]** broad_scope (`faction_remove_ally`) — Tool name contains 'remove', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_edit_role`) — Tool name contains 'edit', suggesting write or destructive capability.
  - *AI review: **false_positive** — The tool description merely outlines standard permission checks and business logic for editing a faction role without containing prompt injection or manipulative instructions.*
- **[HIGH]** broad_scope (`faction_edit`) — Tool name contains 'edit', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`create_note`) — Tool name contains 'create', suggesting write or destructive capability.
- **[HIGH]** broad_scope (`faction_remove_enemy`) — Tool name contains 'remove', suggesting write or destructive capability.
  - *AI review: **false_positive** — The description provides standard functional details and parameters for a faction management tool with no indicators of prompt injection or malicious intent.*
- **[HIGH]** broad_scope (`create_buy_order`) — Tool name contains 'create', suggesting write or destructive capability.
  - *AI review: **false_positive** — The tool description merely outlines normal game mechanics, parameters, and business logic for placing buy orders without any prompt injection or malicious instructions.*
- **[HIGH]** broad_scope (`delete_note`) — Tool name contains 'delete', suggesting write or destructive capability.
- **[MEDIUM]** missing_auth — Server accepts unauthenticated connections — anyone with the URL can invoke its tools.
- **[MEDIUM]** unconstrained_schema (`upload_drone_script`) — Parameter 'script' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`claim`) — Parameter 'registration_code' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`faction_write_room`) — Parameter 'description' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`faction_post_mission`) — Parameter 'description' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`search_systems`) — Parameter 'query' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`login_link_poll`) — Parameter 'device_code' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`facility`) — Parameter 'description' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`register`) — Parameter 'registration_code' looks like it could accept paths/commands/queries with no validation.
- **[MEDIUM]** unconstrained_schema (`station`) — Parameter 'description' looks like it could accept paths/commands/queries with no validation.

### Webflow MCP
URL: `https://mcp.webflow.com/`

**Status: Failed to connect**
- OAuth not yet supported — skipping

### Apify Actors MCP
URL: `https://mcp.apify.com`

**Status: Failed to connect**
- requires_auth is true but no token found in env var 'APIFY_TOKEN'

### Tally MCP
URL: `https://api.tally.so/mcp`

**Status: Failed to connect**
- requires_auth is true but no token found in env var 'TALLY_API_KEY'

### Asana MCP
URL: `https://mcp.asana.com/sse`

**Status: Failed to connect**
- OAuth not yet supported — skipping

### Egnyte MCP
URL: `https://mcp-server.egnyte.com/sse`

**Status: Failed to connect**
- OAuth not yet supported — skipping