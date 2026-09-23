# Repository Guidelines

## Project Structure & Module Organization

`spider_vpn.py` is the sole application script. It logs in to a remote site, extracts a VPN address from an HTML attribute, and sends notifications through Server酱. `.github/workflows/spider_vpn.yml` installs dependencies and runs the script on a schedule or by manual dispatch. `README.md` gives a short project description. There are currently no test files, package manifest, or build artifacts in the repository.

## Build, Test, and Development Commands

- `python -m pip install requests beautifulsoup4` installs the same dependencies as the workflow.
- `python -m py_compile spider_vpn.py` checks syntax without making network requests.
- `python spider_vpn.py` runs the scraper locally. Set `EMAIL`, `PASSWD`, `SEND_KEY`, and `SEND_KEY_BB` first; this command contacts the remote site and sends real notifications.

There is no build step or configured test command. The GitHub Actions workflow uses Python 3.x and runs daily at `0 8 * * *` UTC.

## Coding Style & Naming Conventions

Use four spaces for Python indentation and `snake_case` for variables and functions, consistent with `spider_vpn.py`. Keep login, parsing, and notification changes easy to trace. No formatter or linter is configured; follow the surrounding style and keep imports and comments clear.

## Testing Guidelines

No automated test framework or coverage threshold is configured. For scraper changes, check syntax with `py_compile` and verify HTML extraction against a saved or mocked response before a live run. If adding tests, place them in `tests/`, name files `test_*.py`, and mock HTTP and notification calls so tests do not send messages.

## Commit & Pull Request Guidelines

Recent commits use short messages such as `Update spider_vpn.py` and `Update spider_vpn.yml`. Keep the concise style, but describe the behavior changed when possible. In pull requests, explain the affected login, selector, or notification behavior; include verification steps and any related issue. Screenshots are only useful when showing a changed external page or workflow result.

## Security & Configuration

Keep credentials and Server酱 keys in environment variables or GitHub Actions secrets. Do not commit `.env` files or paste credentials, webhook URLs, or private VPN addresses into issues and logs.
