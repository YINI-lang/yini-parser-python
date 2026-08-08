"""
Validate application.

Run from the repository root with:
    python examples/example3.py
"""

from pathlib import Path

from yini_parser import YiniParseError, load


def require(section: dict[str, object], key: str) -> object:
    # A tiny validation helper for settings the program cannot run without.
    if key not in section:
        raise ValueError(f"Missing required setting: {key}")
    return section[key]


def main() -> None:
    try:
        # Load the YINI file beside this script, regardless of the
        # current directory.
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

    # Select boolean feature toggles, ignoring list/object settings.
    enabled_features = [
        feature_name
        for feature_name, enabled in features.items()
        if isinstance(enabled, bool) and enabled
    ]
    enabled_text = ", ".join(enabled_features) or "none"

    print("Application validation report")
    print("=============================")
    print(f"[ok] name: {app_name}")
    print(f"[ok] environment: {environment}")
    print(f"[ok] server: {host}:{port}")
    print(f"[ok] enabled boolean features: {enabled_text}")
    print(f"[ok] request timeout: {limits['requestTimeoutSeconds']} seconds")


if __name__ == "__main__":
    main()
