"""
Validate application.

Run from the repository root with:
    python examples/example3.py
"""

from pathlib import Path

from yini_parser import YiniParseError, load


def require(section: dict[str, object], key: str) -> object:
    if key not in section:
        raise ValueError(f"Missing required setting: {key}")
    return section[key]


def main() -> None:
    try:
        config = load(Path(__file__).with_name("application.yini"))
    except YiniParseError as exc:
        raise SystemExit(f"Could not parse application.yini: {exc}") from exc

    app = config["Application"]
    server = app["Server"]
    features = app["Features"]
    limits = app["Limits"]

    app_name = require(app, "name")
    environment = require(app, "environment")
    host = require(server, "host")
    port = require(server, "port")

    enabled_features = [
        feature_name
        for feature_name, enabled in features.items()
        if isinstance(enabled, bool) and enabled
    ]
    enabled_text = ", ".join(enabled_features) or "none"

    print(f"{app_name} ({environment})")
    print(f"Server: {host}:{port}")
    print(f"Enabled boolean features: {enabled_text}")
    print(f"Request timeout: {limits['requestTimeoutSeconds']} seconds")


if __name__ == "__main__":
    main()
