# Render CLI Reference

## Installation

```shell
# Homebrew (macOS/Linux)
brew update
brew install render

# Linux/macOS direct
curl -fsSL https://raw.githubusercontent.com/render-oss/cli/refs/heads/main/bin/install.sh | sh
```

## Authentication

```shell
# Interactive login (generates CLI token)
render login

# Set active workspace
render workspace set

# Non-interactive (CI/CD) - use API key
export RENDER_API_KEY=rnd_RUExip…
```

## Common Commands

| Command | Description |
|---------|-------------|
| `render` | List all available commands |
| `render help <command>` | Details about specific command |
| `render login` | Authorize CLI with Render account |
| `render workspace set` | Set active workspace |
| `render services` | List all services/datastores, select for actions |
| `render deploys list [SERVICE_ID]` | List deploys for a service |
| `render deploys create [SERVICE_ID]` | Trigger a deploy |
| `render psql [DATABASE_ID]` | Open psql session to PostgreSQL |
| `render ssh [SERVICE_ID]` | SSH into running service instance |

## Deploy Options

```shell
# Wait for deploy to complete (exit non-zero on failure)
render deploys create SERVICE_ID --wait

# Deploy specific commit (Git-backed services)
render deploys create SERVICE_ID --commit SHA

# Deploy specific image tag/digest (image-backed services)
render deploys create SERVICE_ID --image URL
```

## Non-Interactive Mode

Required flags for scripting/CI:

| Flag | Description |
|------|-------------|
| `-o` / `--output` | Output format: `json`, `yaml`, `text` |
| `--confirm` | Skip confirmation prompts |

```shell
# List services as JSON
render services --output json --confirm

# Deploy in CI/CD
render deploys create $SERVICE_ID --output json --confirm
```

## GitHub Actions Example

```yaml
name: Render CLI Deploy
on:
  push:
    branches:
      - main
jobs:
  Deploy-Render:
    runs-on: ubuntu-latest
    steps:
      - name: Install Render CLI
        run: |
          curl -L https://github.com/render-oss/cli/releases/download/v1.1.0/cli_1.1.0_linux_amd64.zip -o render.zip
          unzip render.zip
          sudo mv cli_v1.1.0 /usr/local/bin/render
      - name: Trigger deploy
        env:
          RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
          CI: true
        run: |
          render deploys create ${{ secrets.RENDER_SERVICE_ID }} --output json --confirm
```

**Required secrets:**
- `RENDER_API_KEY` - Render API key
- `RENDER_SERVICE_ID` - Service ID to deploy

## Environment Variables

| Variable | Description |
|----------|-------------|
| `RENDER_API_KEY` | API key for authentication (takes precedence over CLI tokens) |
| `RENDER_CLI_CONFIG_PATH` | Custom config file path (default: `$HOME/.render/cli.yaml`) |

## CLI Token Management

- Tokens expire periodically; re-authenticate with `render login`
- View/revoke tokens: Dashboard → Account Settings → Render CLI Tokens
