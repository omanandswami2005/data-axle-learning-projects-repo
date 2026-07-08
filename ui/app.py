import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
FEATURES_DIR = ROOT / "features"
STORIES_DIR = ROOT / "stories"
RELATIONS_PATH = ROOT / "relations.json"


def load_relations():
    with RELATIONS_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def list_feature_files():
    return sorted([p.name for p in FEATURES_DIR.glob("*.feature") if p.is_file()])


def count_scenarios(feature_path: Path) -> int:
    content = feature_path.read_text(encoding="utf-8")
    return content.count("Scenario:")


def status_badge(status: str) -> str:
    color = {"PASS": "#2e7d32", "FAIL": "#c62828"}.get(status, "#ef6c00")
    return (
        f'<span style="display:inline-block; background-color:{color}; color:white; '
        f'padding:2px 8px; border-radius:999px; font-size:0.85rem; font-weight:600;">{status}</span>'
    )


def get_feature_context(feature_name: str, relations: dict):
    story = next(
        (item for item in relations.get("stories", []) if feature_name in item.get("features", [])),
        None,
    )
    page = next(
        (item for item in relations.get("pages", []) if feature_name in item.get("feature_files", [])),
        None,
    )
    step_file = story.get("step_file") if story else None
    if not step_file and page:
        step_files = page.get("step_files") or []
        step_file = step_files[0] if step_files else None
    return story, page, step_file


def read_story_content(story_path: Path) -> str:
    try:
        return story_path.read_text(encoding="utf-8")
    except Exception:
        return "_No story content is available yet._"


def render_feature_card(feature_name: str, feature_path: Path, relations: dict, headed_mode: bool):
    story, page, step_file = get_feature_context(feature_name, relations)
    scenario_count = count_scenarios(feature_path)
    result = st.session_state.run_results.get(feature_name)
    status = result.get("status") if result else None

    story_title = story["title"] if story else "No story mapping"
    page_name = page["name"] if page else "No page mapping"
    step_module = step_file or "No step mapping"

    with st.container():
        st.markdown(
            f"<div style='border:1px solid #e6eaf1; border-radius:12px; padding:14px; margin-bottom:12px;'>"
            f"<h4 style='margin:0 0 6px 0;'>{feature_name}</h4>"
            f"<div><b>Story:</b> {story_title}</div>"
            f"<div><b>Page:</b> {page_name}</div>"
            f"<div><b>Step module:</b> {step_module}</div>"
            f"<div><b>Scenarios:</b> {scenario_count}</div>"
            f"</div>",
            unsafe_allow_html=True,
        )
        action_row = st.columns([3, 1])
        with action_row[0]:
            if status:
                st.caption(f"Last run: {result['timestamp']} ({status})")
        with action_row[1]:
            if st.button("Run feature", key=f"run_{feature_name}", use_container_width=True):
                env = os.environ.copy()
                env["PLAYWRIGHT_HEADLESS"] = "false" if headed_mode else "true"
                command = [sys.executable, "-m", "behave", str(feature_path)]
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with st.spinner(f"Running {feature_name}..."):
                    completed = subprocess.run(
                        command,
                        cwd=str(ROOT),
                        env=env,
                        capture_output=True,
                        text=True,
                    )
                status_name = "PASS" if completed.returncode == 0 else "FAIL"
                st.session_state.run_results[feature_name] = {
                    "status": status_name,
                    "timestamp": timestamp,
                    "output": completed.stdout + completed.stderr,
                }
                st.session_state.last_run_feature = feature_name
                if status_name == "PASS":
                    st.success(f"{feature_name} — PASS at {timestamp}")
                else:
                    st.error(f"{feature_name} — FAIL at {timestamp}")

        latest_result = st.session_state.run_results.get(feature_name)
        if latest_result and latest_result.get("status") == "FAIL" and latest_result.get("output"):
            with st.container():
                st.markdown(
                    "<div style='margin-top:10px; padding:10px 12px; border-left:4px solid #d32f2f; background:#fff5f5; border-radius:8px;'>"
                    "<b>Failure details</b>"
                    "</div>",
                    unsafe_allow_html=True,
                )
                st.code(latest_result["output"], language="text")


if "run_results" not in st.session_state:
    st.session_state.run_results = {}


st.set_page_config(page_title="Behave Runner", page_icon="▶️", layout="wide")
st.title("Behave + Playwright Feature Runner")
st.caption("Run and review BDD scenarios from a story-first view.")

relations = load_relations()

st.sidebar.header("Controls")
headed_mode = st.sidebar.checkbox("Show browser window (headed mode)", value=False)
st.sidebar.caption("Checked = headed mode. Unchecked = headless mode.")
refresh = st.sidebar.button("Refresh")

sample_server_status = "OFF"
try:
    with urlopen("http://127.0.0.1:8000/app/index.html", timeout=1) as response:
        if response.status == 200:
            sample_server_status = "ON"
except Exception:
    sample_server_status = "OFF"

st.sidebar.markdown(
    f"**Sample page server:** {status_badge(sample_server_status)}",
    unsafe_allow_html=True,
)

if st.sidebar.button("Start sample page server"):
    subprocess.Popen(
        [sys.executable, "-m", "http.server", "8000"],
        cwd=str(ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1)
    st.sidebar.success("Sample page server started on http://127.0.0.1:8000")

if refresh:
    st.rerun()

feature_files = list_feature_files()
if not feature_files:
    st.warning("No .feature files found in the features folder.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Features", len(feature_files))
with col2:
    st.metric("Stories", len(relations.get("stories", [])))
with col3:
    st.metric("Pages", len(relations.get("pages", [])))
with col4:
    mapped_features = sum(1 for name in feature_files if get_feature_context(name, relations)[0])
    st.metric("Mapped features", mapped_features)

feature_tab, story_map_tab, story_docs_tab = st.tabs(["Features", "Story map", "Story docs"])

with feature_tab:
    st.subheader("Run features")
    for feature_name in feature_files:
        feature_path = FEATURES_DIR / feature_name
        if feature_path.exists():
            render_feature_card(feature_name, feature_path, relations, headed_mode)

with story_map_tab:
    st.subheader("Story → Page → Feature mapping")
    for story in relations.get("stories", []):
        st.markdown(f"### {story['title']}")
        st.write(f"Story file: {story['file']}")
        st.write(f"Pages: {', '.join(story['pages'])}")
        st.write(f"Step module: {story.get('step_file', '—')}")
        for feature_name in story.get("features", []):
            feature_path = FEATURES_DIR / feature_name
            if feature_path.exists():
                scenario_count = count_scenarios(feature_path)
                result = st.session_state.run_results.get(feature_name)
                badge = status_badge(result["status"]) if result else ""
                st.markdown(
                    f"- {feature_name} — {scenario_count} scenario(s) {badge}",
                    unsafe_allow_html=True,
                )

with story_docs_tab:
    st.subheader("Story documents")
    for story_file in sorted(STORIES_DIR.glob("*.md")):
        with st.expander(story_file.stem, expanded=True):
            content = read_story_content(story_file)
            st.markdown(content)
