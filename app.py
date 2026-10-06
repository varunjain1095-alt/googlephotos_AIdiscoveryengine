import time
from collections import Counter

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------------- page setup

st.set_page_config(
    page_title="AI Discovery Engine: Google Photos",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .block-container { padding-top: 2rem; }

    .kpi-card {
        background: #ffffff;
        border: 1px solid #e6e8eb;
        border-radius: 12px;
        padding: 18px 20px 14px 20px;
        box-shadow: 0 1px 2px rgba(16,24,40,.04);
    }
    .kpi-value { font-size: 30px; font-weight: 700; color: #111827; line-height: 1.1; }
    .kpi-label { font-size: 13px; color: #6b7280; margin-top: 4px; }
    .kpi-sub   { font-size: 12px; color: #9ca3af; margin-top: 2px; }

    .quote-card {
        background: #f8f9fc;
        border-left: 4px solid #6366f1;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 12px;
        font-size: 15px;
        color: #1f2937;
    }
    .quote-src { font-size: 12px; color: #6b7280; margin-top: 6px; }

    .finding-card {
        background: #ffffff;
        border: 1px solid #e6e8eb;
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 10px;
        height: 100%;
    }
    .finding-num {
        display:inline-block; background:#eef2ff; color:#4f46e5;
        font-weight:700; border-radius:8px; padding:2px 10px; font-size:13px;
        margin-bottom:6px;
    }
    .finding-title { font-weight: 650; font-size: 15px; color:#111827; margin-bottom:4px; }
    .finding-body  { font-size: 13.5px; color:#4b5563; }

    .step-card {
        background: #ffffff;
        border: 1px solid #e6e8eb;
        border-top: 4px solid #6366f1;
        border-radius: 12px;
        padding: 16px 18px;
        height: 100%;
    }
    .step-num   { font-size: 12px; font-weight:700; color:#6366f1; letter-spacing:.08em; }
    .step-title { font-size: 15px; font-weight:650; color:#111827; margin: 4px 0; }
    .step-body  { font-size: 13px; color:#4b5563; }

    .section-h { font-size: 20px; font-weight: 700; color:#111827; margin: 22px 0 4px 0; }
    .section-sub { font-size: 13px; color:#6b7280; margin-bottom: 12px; }

    .badge {
        display:inline-block; font-size:12px; font-weight:600;
        border-radius:999px; padding:2px 10px; margin-right:6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- data

CSV_PATH = "reviews_classified_claude.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(CSV_PATH)
    df["source_group"] = df["source"].replace(
        {"Play Store batch 2": "Play Store"}
    )
    return df


@st.cache_data
def exploded_counts(df, column):
    c = Counter()
    for cell in df[column].fillna(""):
        for part in str(cell).split(";"):
            part = part.strip()
            if part:
                c[part] += 1
    return pd.DataFrame(c.most_common(), columns=["value", "count"])


df = load_data()
rel = df[df["claude_relevance"] == "Retrieval difficulty"].copy()
searchers = rel[rel["claude_retrieval_mode"].isin(["Search", "Mixed"])]

TOTAL = len(df)
N_REL = len(rel)
N_SEARCH = len(searchers)

ACCENT = "#6366f1"
PALETTE = ["#6366f1", "#22c55e", "#f59e0b", "#ef4444", "#06b6d4", "#a855f7"]
PLOTLY_LAYOUT = dict(
    template="plotly_white",
    font=dict(family="Inter, Segoe UI, sans-serif", size=13, color="#374151"),
    margin=dict(l=8, r=8, t=34, b=8),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
)


def hbar(counts_df, title, color=ACCENT, height=None, pct_of=None):
    d = counts_df.iloc[::-1]
    fig = px.bar(d, x="count", y="value", orientation="h", title=title)
    fig.update_traces(marker_color=color, text=d["count"], textposition="outside")
    fig.update_layout(
        **PLOTLY_LAYOUT,
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
        height=height or max(260, 26 * len(d) + 80),
    )
    fig.update_xaxes(showgrid=True, gridcolor="#f1f2f4")
    return fig


def kpi(col, value, label, sub=""):
    col.markdown(
        f"""<div class="kpi-card">
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-sub">{sub}</div></div>""",
        unsafe_allow_html=True,
    )


def section(title, sub=""):
    st.markdown(f'<div class="section-h">{title}</div>', unsafe_allow_html=True)
    if sub:
        st.markdown(f'<div class="section-sub">{sub}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------- header

st.title("AI Discovery Engine")
st.caption(
    "Google Photos review intelligence, 1,802 reviews scraped, read and "
    "classified per-review. Built on `reviews_classified_claude.csv`."
)

tab_class, tab_insights, tab_csv, tab_ingest = st.tabs(
    ["Classification", "Derived Insights", "CSV Classification", "Data Ingestion Wizard"]
)

# ================================================================ TAB 1
with tab_class:
    section("How 1,802 reviews were classified")
    st.markdown(
        "Every review was read individually and labelled on a fixed schema: "
        "**is it about retrieval? → how was the user trying to find the photo? → "
        "what did they remember / forget / try? → where did it break? → which themes apply?**"
    )

    c1, c2, c3, c4 = st.columns(4)
    kpi(c1, f"{TOTAL:,}", "reviews ingested", "1,000 Play Store · 802 Reddit")
    kpi(c2, f"{N_REL:,}", "retrieval-difficulty reviews", f"{N_REL/TOTAL:.0%} of all reviews")
    kpi(c3, f"{N_SEARCH}", "searched via the search box", "Search + mixed-mode")
    kpi(c4, "26", "label columns per review", "incl. one-line reason per label")

    st.divider()

    col_a, col_b = st.columns([1, 1.2])

    with col_a:
        section("Step 1: Relevance", "Is the review about finding photos at all?")
        rel_counts = df["claude_relevance"].value_counts().reset_index()
        rel_counts.columns = ["value", "count"]
        fig = px.pie(
            rel_counts, values="count", names="value", hole=0.55,
            color_discrete_sequence=PALETTE,
        )
        fig.update_traces(textinfo="percent", textposition="inside")
        fig.update_layout(
            **PLOTLY_LAYOUT, height=360, showlegend=True,
            legend=dict(orientation="h", yanchor="top", y=-0.05, x=0.5, xanchor="center", title=None),
        )
        st.plotly_chart(fig, width="stretch")

    with col_b:
        section(
            "Step 2: How users tried to find the photo",
            "Among the 1,001 retrieval-difficulty reviews. 57% navigate rather than search.",
        )
        mode_counts = rel["claude_retrieval_mode"].value_counts().reset_index()
        mode_counts.columns = ["value", "count"]
        st.plotly_chart(hbar(mode_counts, "", ACCENT, height=340), width="stretch")

    st.divider()

    section(
        "What people actually complain about",
        "Reviews can carry several themes, shares sum to more than 100%.",
    )
    theme_counts = exploded_counts(rel, "claude_themes").head(18)
    st.plotly_chart(
        hbar(theme_counts, "", "#8b5cf6", height=max(340, 26 * len(theme_counts) + 80)),
        width="stretch",
    )

    st.divider()

    col_c, col_d = st.columns(2)

    with col_c:
        section("What they can't find", "Photo type named in the review.")
        q1 = exploded_counts(rel, "claude_q1_photo_type")
        q1 = q1[~q1["value"].isin(["Unspecified", "Not stated"])].head(12)
        st.plotly_chart(hbar(q1, "", "#0ea5e9"), width="stretch")

    with col_d:
        section("What they remember", "Memory cues stated in the review.")
        q2 = exploded_counts(rel, "claude_q2_remembered")
        q2 = q2[~q2["value"].isin(["Not stated"])].head(12)
        st.plotly_chart(hbar(q2, "", "#f59e0b"), width="stretch")

    st.divider()

    col_e, col_f = st.columns(2)

    with col_e:
        section(
            "Where the search journey breaks",
            f"Failure points flagged among the {N_SEARCH} reviews where the user searched.",
        )
        journey = pd.DataFrame(
            [
                ("Couldn't express the memory", int((searchers["claude_q5_cant_express"] == "Yes").sum())),
                ("App didn't understand the clue", int((searchers["claude_q6_app_misunderstood"] == "Yes").sum())),
                ("Results hard to judge", int((searchers["claude_q7_results_hard_to_judge"] == "Yes").sum())),
                ("Couldn't fix a failed search", int((searchers["claude_q8_couldnt_refine"] == "Yes").sum())),
            ],
            columns=["stage", "count"],
        )
        fig = px.funnel(journey, x="count", y="stage", color_discrete_sequence=[ACCENT])
        fig.update_traces(textinfo="value")
        fig.update_layout(**PLOTLY_LAYOUT, height=320)
        st.plotly_chart(fig, width="stretch")
        st.caption(
            "A review can fail at several steps. 'Couldn't express' shows zero, not because "
            "people always articulate well, but because someone who can't put a memory "
            "into words doesn't experience it as a product failure worth reviewing."
        )

    with col_f:
        section(
            "Play Store vs Reddit: different problems",
            "Share of each source's retrieval reviews carrying a theme group.",
        )
        THEME_GROUPS = {
            "Search got worse / AI": {"Worse after update", "AI / Gemini search"},
            "Fragmentation": {"Scattered across folders / sources", "Device vs cloud confusion"},
            "Timeline & layout": {"Layout changes", "Scrolling", "Scrubber / date breaks"},
            "Albums": {"Albums"},
            "Face grouping": {"Face grouping", "Can't correct the AI"},
            "Wants more control": {"Wants more control", "Sorting", "Result ranking / sort"},
            "Wrong dates": {"Wrong or unusable dates"},
            "Clutter / dupes": {"Duplicates / clutter", "Photos missing", "Stacking hid photos"},
        }
        comp_rows = []
        for group_name, members in THEME_GROUPS.items():
            for src in ["Play Store", "Reddit"]:
                sub = rel[rel["source_group"] == src]
                n = sum(
                    1 for cell in sub["claude_themes"].fillna("")
                    if any(m in {t.strip() for t in cell.split(";")} for m in members)
                )
                comp_rows.append({"theme": group_name, "source": src, "pct": n / len(sub) * 100})
        comp = pd.DataFrame(comp_rows)
        fig = px.bar(
            comp, y="theme", x="pct", color="source", barmode="group",
            orientation="h", color_discrete_sequence=["#6366f1", "#f59e0b"],
            labels={"pct": "% of retrieval reviews", "theme": "", "source": ""},
        )
        fig.update_layout(**PLOTLY_LAYOUT, height=380, legend=dict(orientation="h", y=1.12))
        fig.update_xaxes(showgrid=True, gridcolor="#f1f2f4")
        st.plotly_chart(fig, width="stretch")

# ================================================================ TAB 2
with tab_insights:
    section("What the classification reveals")

    c1, c2, c3, c4 = st.columns(4)
    kpi(c1, "57%", "navigate, don't search", "facets + scrolling + memories")
    kpi(c2, "82%", "of searches fail at matching", "the app didn't understand the clue")
    kpi(c3, "34%", "Play Store complaints: fragmentation", "folders, downloads, device vs cloud")
    kpi(c4, "44%", "Reddit complaints: search got worse", "incl. AI / Gemini search")

    st.divider()

    findings = [
        ("1", "Navigation is the majority case",
         "39% browsed facets (people, albums, folders, places) and 18% scrolled the timeline. "
         "Search, the journey most retrieval research focuses on, covers only 35% of complaints."),
        ("2", "Searches fail at matching, not at expression",
         "Of 385 search-mode reviews, 314 report the app not understanding a perfectly clear clue: "
         "\"monkeys\", \"museum\", \"when I was wearing the yellow dress\". Zero reviewers blamed "
         "their own ability to express the memory."),
        ("3", "Fragmentation is the biggest Play Store problem",
         "Downloads, WhatsApp images, screenshots, edited copies and freed-up backups each land "
         "somewhere different, and other apps can't see them. 34% of Play Store retrieval reviews."),
        ("4", "Face-grouping corrections don't stick",
         "142 reviews: the same person split into many, different people merged into one, and "
         "manual merges undone weeks later by the model. Users explicitly want to teach the AI "
         "and have the correction remembered."),
        ("5", "\"Show me where this sits in my library\"",
         "Small but unprompted, specific demand: 11 reviews ask to jump from a found photo to its "
         "position in the photostream, plus workarounds traded for its absence."),
        ("6", "Albums became their own retrieval problem",
         "130 reviews: album lists can't be searched or sorted when filing a photo, so people "
         "scroll through dozens or hundreds of albums."),
        ("7", "Every update resets the mental map",
         "124 layout complaints, date breaks and the scrubber are the landmarks people navigate "
         "by, and each redesign erases them."),
        ("8", "Utility photos behave differently",
         "70+ reviews name screenshots/documents, recalled by purpose, source app or file type, "
         "not by person/event/place, and often urgently needed (a ticket at a counter, a passport)."),
    ]

    for i in range(0, len(findings), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            num, title, body = findings[i + j]
            col.markdown(
                f"""<div class="finding-card">
                <div class="finding-num">Finding {num}</div>
                <div class="finding-title">{title}</div>
                <div class="finding-body">{body}</div></div>""",
                unsafe_allow_html=True,
            )

    st.divider()

    section("In their own words", "Quotes pulled directly from the classified reviews.")
    quotes = [
        ("it took me FOUR HOURS yesterday afternoon, to find a set of two pictures adjacent to each other.", "P511 · Play Store"),
        ("Not being able to find things quickly this way has added hours of labour to my day to day life.", "R197 · Reddit"),
        ("I have to attempt 3-4 different searches for other things that might be in the picture I'm looking for according to my memory.", "R060 · Reddit"),
        ("It's baffling that it doesn't exist… 'show in photostream' (or whatever Google calls it). To see it in context of where it sits in the gallery.", "R119 · Reddit"),
        ("I know they are there though, because when it prompts 'memories' I suddenly can access everything.", "P462 · Play Store"),
        ("My mother died recently, and Im trying to gather up her photos and google has them all over the place.", "R456 · Reddit"),
        ("Does not respect 'merging' two people into one… Weeks later it will yet again split those photos out… Lather rinse repeat, for eternity.", "R331 · Reddit"),
        ("cant remember when you were in Thailand, just search Thailand and every photo you've taken will show in the results.", "P715 · Play Store, what success looks like"),
    ]
    qc = st.columns(2)
    for i, (text, src) in enumerate(quotes):
        qc[i % 2].markdown(
            f'<div class="quote-card">“{text}”<div class="quote-src">{src}</div></div>',
            unsafe_allow_html=True,
        )

    st.divider()

    col_g, col_h = st.columns(2)

    with col_g:
        section("Lines up with prior research", "Where the reviews confirm the thesis.")
        st.markdown(
            """
            | Finding | Status |
            |---|---|
            | Auto-collections fail silently & can't be corrected | **Confirmed**: 142 reviews |
            | Albums become their own retrieval problem | **Confirmed**: 130 reviews |
            | Date breaks are navigation landmarks | **Confirmed**: Reddit thread erupted when removed |
            | Locate-on-timeline ("show in photostream") | **Confirmed**: unprompted demand ×11 |
            | Context/scene cues fail (season, person doing something) | **Confirmed**: every failed-clue example |
            | Can't express the memory | **Untestable in reviews**: interview-only |
            | "Find similar" demand | **Weak signal**: only 4 reviews |
            | Fragmentation = top problem | **New finding**: not prominent in prior research |
            | Updates reset users' mental map | **New finding**: reverse of the "map builds over time" claim |
            """
        )

    with col_h:
        section("What reviews can't tell you: interview priorities", "")
        st.markdown(
            """
            1. **Can people put the memory into words?** This is invisible in reviews, test with a live search task.
            2. **What do they remember and forget?** Ask them to describe a photo *before* searching.
            3. **Season / time-of-day memory**, untested here (1 mention of season, 0 of time of day).
            4. **Why browse instead of search?** 57% navigate, find out what makes someone choose to scroll.
            5. **Would "show me where this sits" get used?** Strong but small signal, watch for it during tasks.
            6. **Memories vs utility photos**, screenshots/documents carry urgency; probe both.
            """
        )


# ================================================================ TAB 3
with tab_csv:
    section(
        "The full classified dataset",
        f"All {TOTAL:,} reviews × 26 columns, every label behind every number on this page.",
    )

    with st.expander("Filters", expanded=True):
        f1, f2, f3, f4 = st.columns(4)
        f_source = f1.multiselect("Source", sorted(df["source"].unique()), default=list(df["source"].unique()))
        f_rel = f2.multiselect("Relevance", sorted(df["claude_relevance"].unique()), default=list(df["claude_relevance"].unique()))
        f_mode = f3.multiselect(
            "Retrieval mode",
            sorted(df["claude_retrieval_mode"].replace("", pd.NA).dropna().unique()),
            default=[],
            placeholder="All",
        )
        f_theme = f4.multiselect(
            "Theme contains",
            exploded_counts(rel, "claude_themes")["value"].tolist(),
            default=[],
            placeholder="All",
        )
        f_text = st.text_input("Search review text", placeholder='e.g. "photostream", "merge", "screenshot"')

    view = df[df["source"].isin(f_source) & df["claude_relevance"].isin(f_rel)]
    if f_mode:
        view = view[view["claude_retrieval_mode"].isin(f_mode)]
    if f_theme:
        view = view[
            view["claude_themes"].fillna("").apply(
                lambda cell: any(t in {x.strip() for x in cell.split(";")} for t in f_theme)
            )
        ]
    if f_text.strip():
        view = view[view["review_text"].str.contains(f_text.strip(), case=False, na=False)]

    m1, m2 = st.columns([3, 1])
    m1.markdown(f"**Showing {len(view):,} of {TOTAL:,} reviews**")
    m2.download_button(
        "Download filtered CSV",
        view.drop(columns=["source_group"]).to_csv(index=False),
        "reviews_filtered.csv",
        "text/csv",
        width="stretch",
    )

    LABELS = {
        "record_id": "ID",
        "source": "Source",
        "source_url": "URL",
        "review_text": "Review",
        "claude_relevance": "Relevance",
        "claude_retrieval_mode": "Retrieval mode",
        "claude_q1_photo_type": "Photo type",
        "claude_q2_remembered": "Remembered",
        "claude_q3_forgotten": "Forgotten",
        "claude_q4_how_searched": "How searched",
        "claude_q5_cant_express": "Can't express",
        "claude_q6_app_misunderstood": "App misunderstood",
        "claude_q7_results_hard_to_judge": "Hard to judge",
        "claude_q8_couldnt_refine": "Couldn't refine",
        "claude_themes": "Themes",
        "claude_reason": "Label reason",
        "model_disposition": "Model · disposition",
        "model_rationale": "Model · rationale",
        "model_q1": "Model · photo type", "model_q2": "Model · remembered",
        "model_q3": "Model · forgotten", "model_q4": "Model · how searched",
        "model_q5": "Model · can't express", "model_q6": "Model · app misunderstood",
        "model_q7": "Model · hard to judge", "model_q8": "Model · couldn't refine",
    }
    COL_ORDER = [
        "record_id", "source", "source_url", "review_text",
        "claude_relevance", "claude_retrieval_mode",
        "claude_q1_photo_type", "claude_q2_remembered", "claude_q3_forgotten",
        "claude_q4_how_searched", "claude_q5_cant_express", "claude_q6_app_misunderstood",
        "claude_q7_results_hard_to_judge", "claude_q8_couldnt_refine",
        "claude_themes", "claude_reason",
        "model_disposition", "model_rationale",
        "model_q1", "model_q2", "model_q3", "model_q4",
        "model_q5", "model_q6", "model_q7", "model_q8",
    ]

    st.dataframe(
        view[COL_ORDER].rename(columns=LABELS),
        width="stretch",
        height=620,
        column_config={
            "ID": st.column_config.TextColumn(width="small"),
            "Source": st.column_config.TextColumn(width="small"),
            "URL": st.column_config.LinkColumn(width="small", display_text="link"),
            "Review": st.column_config.TextColumn(width="large"),
            "Relevance": st.column_config.TextColumn(width="medium"),
            "Retrieval mode": st.column_config.TextColumn(width="medium"),
            "Themes": st.column_config.TextColumn(width="medium"),
            "Label reason": st.column_config.TextColumn(width="medium"),
        },
        hide_index=True,
    )
    st.caption(
        "Scroll right for the full 26-column schema, Claude labels first, "
        "then the earlier `model_*` labels kept for comparison."
    )

# ================================================================ TAB 4
with tab_ingest:
    section(
        "Data ingestion pipeline",
        "How raw reviews become the classified dataset powering this tool.",
    )

    steps = [
        ("STEP 1", "Sources",
         "Google Play Store reviews for Google Photos, plus Reddit threads and comments "
         "from r/googlephotos focused on search and finding photos."),
        ("STEP 2", "Scrape & normalize",
         "google-play-scraper pulls newest-first Play Store reviews; Reddit threads and "
         "comments are scraped from r/googlephotos. Both normalize to one schema: id, source, url, text."),
        ("STEP 3", "Classify: Claude Sonnet",
         "Each review goes through the Anthropic API (Claude Sonnet) with a structured-output "
         "prompt: relevance → retrieval mode → memory cues and failure points → themes → one-line reason. "
         "JSON mode + schema validation, batched with retries."),
        ("STEP 4", "Load & verify",
         "Labels land in reviews_classified_claude.csv, 1,802 rows × 26 columns, "
         "then feed the charts and insights in this app."),
    ]
    for col, (num, title, body) in zip(st.columns(4), steps):
        col.markdown(
            f"""<div class="step-card">
            <div class="step-num">{num}</div>
            <div class="step-title">{title}</div>
            <div class="step-body">{body}</div></div>""",
            unsafe_allow_html=True,
        )

    st.divider()

    col_w1, col_w2 = st.columns([1.1, 1])

    with col_w1:
        section("Run a demo ingestion", "Simulated run of the pipeline stages end to end.")
        w_src = st.multiselect(
            "Sources to ingest",
            ["Google Play Store", "Reddit (r/googlephotos)"],
            default=["Google Play Store", "Reddit (r/googlephotos)"],
        )
        w_limit = st.slider("Max reviews per source", 100, 1000, 1000, step=100)
        w_model = st.selectbox(
            "Classification model",
            ["claude-sonnet-4-5", "claude-sonnet-4", "claude-haiku-4-5"],
        )

        if st.button("Run ingestion", type="primary", width="stretch"):
            if not w_src:
                st.warning("Pick at least one source.")
            else:
                prog = st.progress(0, "Starting pipeline…")
                log = st.status("Ingesting…", expanded=True)

                stages = []
                if "Google Play Store" in w_src:
                    stages.append(("google-play-scraper", "Play Store", min(1000, w_limit)))
                if "Reddit (r/googlephotos)" in w_src:
                    stages.append(("Reddit scraper", "Reddit", min(802, w_limit)))

                pct = 0
                per = 60 / max(len(stages), 1)
                total_rows = 0
                for tool, name, n in stages:
                    log.write(f"**{tool}** → scraping {name} (newest first)…")
                    time.sleep(0.6)
                    log.write(f" • fetched {n:,} raw items, normalizing schema")
                    time.sleep(0.4)
                    total_rows += n
                    pct += per
                    prog.progress(min(int(pct), 60), f"Scraped {name}")

                log.write(f"**{w_model}** → classifying {total_rows:,} reviews (batched, JSON mode)…")
                prog.progress(75, "Classifying with Claude Sonnet…")
                time.sleep(0.9)
                log.write(" • schema validated: 26 columns, no parse failures")
                prog.progress(90, "Writing dataset…")
                time.sleep(0.4)
                log.write(f" • wrote {total_rows:,} rows → `reviews_classified_claude.csv`")
                prog.progress(100, "Done")
                log.update(label=f"Ingestion complete: {total_rows:,} reviews classified", state="complete")
                st.success(f"{total_rows:,} reviews ingested and classified.")
                st.balloons()

    with col_w2:
        section("Tooling", "What's under each step.")
        st.markdown(
            """
            | Stage | Tool | Why |
            |---|---|---|
            | Play Store scrape | `google-play-scraper` | Full review text, newest-first sort, no API key needed |
            | Reddit scrape | Reddit thread & comment scraper | Permalink kept per row for provenance |
            | Classification | **Claude Sonnet (Anthropic API)** | Structured JSON output; per-review labels on a fixed schema |
            | Validation | JSON schema + retries | Rejects malformed labels; every row carries a one-line reason |
            | Storage | Flat CSV | Auditable, diffable, feeds this app directly |
            """
        )
        st.markdown("**Label schema applied per review**")
        st.code(
            "relevance → retrieval_mode →\n"
            "photo_type · remembered · forgotten · how_searched →\n"
            "can't express · app misunderstood ·\n"
            "hard to judge · couldn't refine →\n"
            "themes[] + one-line reason",
            language=None,
        )
        st.caption(
            "The same pipeline re-runs on new reviews, scrape, classify, append, "
            "so the dataset and every chart above stay current."
        )
