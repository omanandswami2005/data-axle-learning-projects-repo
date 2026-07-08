import os
import json
import re
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright


ARTIFACT_DIR = Path(__file__).resolve().parent / "artifacts"
NETWORK_DIR = ARTIFACT_DIR / "network"
SCREENSHOT_DIR = ARTIFACT_DIR / "screenshots"
TRACE_DIR = ARTIFACT_DIR / "traces"


def is_headless() -> bool:
    return os.getenv("HEADLESS", "false").lower() == "true"


def is_mobile() -> bool:
    return os.getenv("MOBILE", "false").lower() == "true"


def clean_name(name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", name).strip("_").lower()
    return cleaned or "scenario"


def before_all(context):
    ARTIFACT_DIR.mkdir(exist_ok=True)
    NETWORK_DIR.mkdir(exist_ok=True)
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    TRACE_DIR.mkdir(exist_ok=True)

    context.test_results = []
    context.playwright = sync_playwright().start()

    launch_options = {
        "headless": is_headless(),
        "slow_mo": 300,
    }

    context.browser = context.playwright.chromium.launch(
        **launch_options,
    )


def before_scenario(context, scenario):
    context.scenario_name = clean_name(scenario.name)
    context.network_calls = []

    if is_mobile():
        device_name = os.getenv("DEVICE", "Pixel 5")
        device_options = context.playwright.devices[device_name]
        context.browser_context = context.browser.new_context(**device_options)
    else:
        context.browser_context = context.browser.new_context(
            viewport={"width": 1280, "height": 720}
        )

    context.browser_context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
    )

    context.page = context.browser_context.new_page()

    def store_response(response):
        context.network_calls.append(
            {
                "method": response.request.method,
                "url": response.url,
                "status": response.status,
                "resource_type": response.request.resource_type,
            }
        )

    context.page.on("response", store_response)


def after_scenario(context, scenario):
    screenshot_path = SCREENSHOT_DIR / f"{context.scenario_name}.png"
    network_path = NETWORK_DIR / f"{context.scenario_name}.json"
    trace_path = TRACE_DIR / f"{context.scenario_name}.zip"

    if hasattr(context, "page"):
        context.page.screenshot(path=str(screenshot_path), full_page=True)

    if hasattr(context, "browser_context"):
        context.browser_context.tracing.stop(path=str(trace_path))
        context.browser_context.close()

    network_path.write_text(
        json.dumps(context.network_calls, indent=2),
        encoding="utf-8",
    )

    context.test_results.append(
        {
            "scenario": scenario.name,
            "status": scenario.status.name,
            "network_calls": len(context.network_calls),
            "screenshot": str(screenshot_path),
            "trace": str(trace_path),
            "network_log": str(network_path),
            "mobile": is_mobile(),
        }
    )


def after_all(context):
    report_json_path = ARTIFACT_DIR / "report.json"
    report_md_path = ARTIFACT_DIR / "report.md"

    report = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "mobile": is_mobile(),
        "results": context.test_results,
    }

    report_json_path.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# Behave Test Report",
        "",
        f"Created at: {report['created_at']}",
        f"Mobile mode: {report['mobile']}",
        "",
        "| Scenario | Status | Network Calls | Screenshot | Trace |",
        "| --- | --- | ---: | --- | --- |",
    ]

    for result in context.test_results:
        lines.append(
            "| {scenario} | {status} | {network_calls} | {screenshot} | {trace} |".format(
                **result
            )
        )

    report_md_path.write_text("\n".join(lines), encoding="utf-8")

    context.browser.close()
    context.playwright.stop()
