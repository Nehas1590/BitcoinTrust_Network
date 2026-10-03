import streamlit as st
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Bitcoin Alpha Network Analysis",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

GRAPH_PATH = BASE_DIR / "graphs" / "bitcoin_trust_network_top50.png"
DATASET_PATH = BASE_DIR / "dataset" / "soc-sign-bitcoinalpha.csv"


# ============================================================
# THEME
# ============================================================

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

if st.session_state.dark_mode:

    BG = "#0b1120"
    CARD = "#111827"
    CARD2 = "#172033"
    TEXT = "#f8fafc"
    MUTED = "#a7b0c0"
    BORDER = "#263247"
    ACCENT = "#60a5fa"
    SIDEBAR = "#080d18"

else:

    BG = "#f5f7fb"
    CARD = "#ffffff"
    CARD2 = "#eef2f7"
    TEXT = "#172033"
    MUTED = "#5f6b7a"
    BORDER = "#dfe5ee"
    ACCENT = "#2563eb"
    SIDEBAR = "#172033"


# ============================================================
# CSS ONLY
# ============================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {BG};
        color: {TEXT};
    }}

    .main .block-container {{
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }}

    h1, h2, h3 {{
        color: {TEXT} !important;
    }}

    p {{
        color: {MUTED};
    }}

    /* SIDEBAR */

    section[data-testid="stSidebar"] {{
        background-color: {SIDEBAR} !important;
    }}

    section[data-testid="stSidebar"] > div {{
        background-color: {SIDEBAR} !important;
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    section[data-testid="stSidebar"] .stRadio label {{
        color: white !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stMetricLabel"] {{
        color: #aeb9ca !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stMetricValue"] {{
        color: white !important;
    }}

    /* METRIC CARDS */

    div[data-testid="stMetric"] {{
        background-color: {CARD};
        border: 1px solid {BORDER};
        border-radius: 15px;
        padding: 18px;
    }}

    div[data-testid="stMetricLabel"] {{
        color: {MUTED} !important;
    }}

    div[data-testid="stMetricValue"] {{
        color: {TEXT} !important;
    }}

    /* BUTTONS */

    .stButton > button {{
        border-radius: 10px;
        font-weight: 600;
    }}

    .stDownloadButton > button {{
        border-radius: 10px;
        font-weight: 600;
    }}

    /* HERO */

    .hero-box {{
        background-color: {CARD};
        border: 1px solid {BORDER};
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 25px;
    }}

    /* INFO BOX */

    .info-box {{
        background-color: {CARD};
        border: 1px solid {BORDER};
        border-radius: 15px;
        padding: 20px;
    }}

    /* DIVIDER */

    hr {{
        border: none;
        border-top: 1px solid {BORDER};
        margin: 25px 0;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA
# ============================================================

degree_data = {
    "User 1": 0.2348,
    "User 3": 0.1306,
    "User 4": 0.1100,
    "User 7": 0.1076,
    "User 11": 0.1074,
    "User 2": 0.1058,
    "User 177": 0.1058,
    "User 8": 0.1039,
    "User 10": 0.0902,
    "User 15": 0.0846
}

closeness_data = {
    "User 2": 0.3668,
    "User 11": 0.3653,
    "User 1": 0.3588,
    "User 10": 0.3529,
    "User 4": 0.3462,
    "User 42": 0.3413,
    "User 3": 0.3402,
    "User 9": 0.3399,
    "User 26": 0.3384,
    "User 95": 0.3372
}

betweenness_data = {
    "User 1": 0.1492,
    "User 2": 0.0625,
    "User 4": 0.0592,
    "User 11": 0.0508,
    "User 3": 0.0477,
    "User 10": 0.0429,
    "User 15": 0.0412,
    "User 8": 0.0360,
    "User 13": 0.0360,
    "User 177": 0.0352
}


# ============================================================
# CHART FUNCTION
# ============================================================

def create_chart(data, title, xlabel):

    fig, ax = plt.subplots(figsize=(10, 5))

    users = list(data.keys())[::-1]
    values = list(data.values())[::-1]

    bars = ax.barh(users, values)

    ax.set_title(title, fontweight="bold")
    ax.set_xlabel(xlabel)

    ax.grid(axis="x", alpha=0.2)
    ax.set_axisbelow(True)

    for bar, value in zip(bars, values):

        ax.text(
            value + max(values) * 0.015,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.4f}",
            va="center",
            fontsize=9
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    fig.tight_layout()

    return fig


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## 🔗 Bitcoin Alpha")
st.sidebar.caption("Web of Trust Network")

st.sidebar.divider()

st.sidebar.markdown("### 🧭 Explore")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🕸️ Network Explorer",
        "📈 Centrality Explorer",
        "🌐 Network Measures",
        "🔎 Dataset Explorer",
        "💡 Key Findings",
        "📚 About Project"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

st.sidebar.markdown("### 🎨 Appearance")

if st.session_state.dark_mode:

    if st.sidebar.button(
        "☀️ Switch to Light Mode",
        use_container_width=True
    ):
        st.session_state.dark_mode = False
        st.rerun()

else:

    if st.sidebar.button(
        "🌙 Switch to Dark Mode",
        use_container_width=True
    ):
        st.session_state.dark_mode = True
        st.rerun()

st.sidebar.divider()

st.sidebar.markdown("### 📊 Network Snapshot")

st.sidebar.metric("Users", "3,783")
st.sidebar.metric("Connections", "24,186")
st.sidebar.metric("Reciprocity", "0.8321")

st.sidebar.divider()

st.sidebar.caption("B.E. Artificial Intelligence & Data Science")
st.sidebar.caption("Academic Project")


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.title("🔗 Bitcoin Alpha Web of Trust")

    st.write(
        "Interactive Network Visualization and Structural Analysis Dashboard"
    )

    st.divider()

    st.subheader("📊 Network at a Glance")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("👥 Nodes", "3,783")
    c2.metric("🔗 Directed Edges", "24,186")
    c3.metric("↔️ Reciprocity", "0.8321")
    c4.metric("🔺 Transitivity", "0.0780")

    st.divider()

    left, right = st.columns([1.35, 1])

    with left:

        st.subheader("🕸️ Network Visualization")

        if GRAPH_PATH.exists():

            st.image(
                str(GRAPH_PATH),
                caption="Bitcoin Alpha Trust Network – Top 50 Connected Users",
                use_container_width=True
            )

        else:

            st.warning(
                "Network visualization image was not found."
            )

    with right:

        st.subheader("📌 Project Overview")

        st.info(
            "The Bitcoin Alpha dataset represents a directed "
            "Web of Trust network where users provide ratings "
            "to other users."
        )

        st.markdown("**Node:** User")

        st.markdown("**Edge:** Directed rating relationship")

        st.markdown("**Rating range:** -10 to +10")

        st.warning(
            "Centrality measures describe structural position "
            "and should not be interpreted as direct measures "
            "of trustworthiness."
        )

    st.divider()

    st.subheader("📈 Analysis Areas")

    a, b, c = st.columns(3)

    with a:

        st.info(
            "**📈 Centrality**\n\n"
            "Degree, closeness and betweenness centrality "
            "describe different structural positions of users."
        )

    with b:

        st.info(
            "**🌐 Network Structure**\n\n"
            "Transitivity, reciprocity and degree assortativity "
            "describe broader network characteristics."
        )

    with c:

        st.info(
            "**🔎 Dataset Explorer**\n\n"
            "Inspect source, target, rating and timestamp "
            "fields directly from the dataset."
        )

    st.divider()

    st.subheader("🏆 Top Structural Positions")

    x, y, z = st.columns(3)

    x.metric(
        "Highest Degree",
        "User 1",
        "0.2348"
    )

    y.metric(
        "Highest Closeness",
        "User 2",
        "0.3668"
    )

    z.metric(
        "Highest Betweenness",
        "User 1",
        "0.1492"
    )


# ============================================================
# NETWORK EXPLORER
# ============================================================

elif page == "🕸️ Network Explorer":

    st.title("🕸️ Network Explorer")

    st.write(
        "Explore the visual structure of the Bitcoin Alpha Web of Trust Network."
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("👥 Total Users", "3,783")
    c2.metric("🔗 Total Connections", "24,186")
    c3.metric("👁️ Users Visualized", "50")

    st.divider()

    if GRAPH_PATH.exists():

        st.image(
            str(GRAPH_PATH),
            caption="Bitcoin Alpha Trust Network – Top 50 Connected Users",
            use_container_width=True
        )

    else:

        st.error(
            "Network visualization image was not found."
        )

    st.divider()

    st.subheader("🧩 Understanding the Visualization")

    c1, c2 = st.columns(2)

    c1.info(
        "**🔵 Nodes**\n\n"
        "Each node represents a user in the network."
    )

    c2.info(
        "**➡️ Directed Edges**\n\n"
        "Each directed edge represents a rating relationship "
        "from one user to another."
    )


# ============================================================
# CENTRALITY EXPLORER
# ============================================================

elif page == "📈 Centrality Explorer":

    st.title("📈 Centrality Explorer")

    st.write(
        "Compare the three centrality measures calculated for the network."
    )

    st.divider()

    measure = st.selectbox(
        "Select centrality measure",
        [
            "Degree Centrality",
            "Closeness Centrality",
            "Betweenness Centrality"
        ]
    )

    top_n = st.slider(
        "Number of users",
        5,
        10,
        10
    )

    if measure == "Degree Centrality":

        data = dict(
            list(degree_data.items())[:top_n]
        )

        description = (
            "Degree centrality examines the connectivity "
            "of users within the network."
        )

    elif measure == "Closeness Centrality":

        data = dict(
            list(closeness_data.items())[:top_n]
        )

        description = (
            "Closeness centrality examines users based "
            "on their relative network distances."
        )

    else:

        data = dict(
            list(betweenness_data.items())[:top_n]
        )

        description = (
            "Betweenness centrality identifies users that "
            "occur on shortest paths between others."
        )

    st.info(description)

    fig = create_chart(
        data,
        f"Top {top_n} Users by {measure}",
        measure
    )

    st.pyplot(fig, use_container_width=True)

    plt.close(fig)

    st.divider()

    top_user = list(data.keys())[0]
    top_value = data[top_user]

    c1, c2 = st.columns(2)

    c1.metric("Top User", top_user)
    c2.metric("Centrality Value", f"{top_value:.4f}")


# ============================================================
# NETWORK MEASURES
# ============================================================

elif page == "🌐 Network Measures":

    st.title("🌐 Network-Level Measures")

    st.write(
        "Structural properties of the complete Bitcoin Alpha network."
    )

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("🔺 Transitivity", "0.0780")
    c2.metric("↔️ Reciprocity", "0.8321")
    c3.metric("🔗 Degree Assortativity", "-0.1635")

    st.divider()

    measure = st.radio(
        "Choose a measure",
        [
            "Transitivity",
            "Reciprocity",
            "Degree Assortativity"
        ],
        horizontal=True
    )

    if measure == "Transitivity":

        st.subheader("🔺 Transitivity")

        st.write(
            "The network has an undirected transitivity value "
            "of **0.0780**. This describes the tendency of "
            "connected users to form triangular relationships."
        )

    elif measure == "Reciprocity":

        st.subheader("↔️ Reciprocity")

        st.write(
            "The reciprocity value is **0.8321**, indicating "
            "a high level of mutual connections between users."
        )

    else:

        st.subheader("🔗 Degree Assortativity")

        st.write(
            "The degree assortativity value is **-0.1635**, "
            "indicating a weak negative relationship between "
            "the degrees of connected users."
        )

    st.divider()

    st.subheader("📌 Overall Interpretation")

    st.info(
        "Together, these measures provide information about "
        "clustering, mutual relationships and degree-based "
        "connectivity patterns."
    )


# ============================================================
# DATASET EXPLORER
# ============================================================

elif page == "🔎 Dataset Explorer":

    st.title("🔎 Dataset Explorer")

    st.write(
        "Inspect the original Bitcoin Alpha Web of Trust dataset."
    )

    st.divider()

    if DATASET_PATH.exists():

        df = pd.read_csv(
            DATASET_PATH,
            header=None,
            names=[
                "source",
                "target",
                "rating",
                "time"
            ]
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Rows", f"{len(df):,}")
        c2.metric("Columns", len(df.columns))
        c3.metric(
            "Missing Values",
            int(df.isna().sum().sum())
        )
        c4.metric(
            "Rating Range",
            f"{df['rating'].min()} to {df['rating'].max()}"
        )

        st.divider()

        st.subheader("📋 Dataset Preview")

        rows = st.slider(
            "Rows to display",
            5,
            50,
            10
        )

        st.dataframe(
            df.head(rows),
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("🔍 Filter by Rating")

        rating_range = st.slider(
            "Rating range",
            int(df["rating"].min()),
            int(df["rating"].max()),
            (
                int(df["rating"].min()),
                int(df["rating"].max())
            )
        )

        filtered = df[
            df["rating"].between(
                rating_range[0],
                rating_range[1]
            )
        ]

        st.write(
            f"Matching records: **{len(filtered):,}**"
        )

        st.dataframe(
            filtered.head(100),
            use_container_width=True,
            hide_index=True
        )

    else:

        st.error(
            "Dataset not found at dataset/soc-sign-bitcoinalpha.csv"
        )


# ============================================================
# KEY FINDINGS
# ============================================================

elif page == "💡 Key Findings":

    st.title("💡 Key Findings")

    st.write(
        "Main results obtained from the Bitcoin Alpha network analysis."
    )

    st.divider()

    st.subheader("📈 Centrality Findings")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Degree Centrality",
        "User 1",
        "0.2348"
    )

    c2.metric(
        "Closeness Centrality",
        "User 2",
        "0.3668"
    )

    c3.metric(
        "Betweenness Centrality",
        "User 1",
        "0.1492"
    )

    st.divider()

    st.subheader("🌐 Network-Level Findings")

    c1, c2, c3 = st.columns(3)

    c1.metric("Transitivity", "0.0780")
    c2.metric("Reciprocity", "0.8321")
    c3.metric("Assortativity", "-0.1635")

    st.info(
        "The results show that different users occupy different "
        "structural positions in the network, while network-level "
        "measures describe the broader connectivity pattern."
    )


# ============================================================
# ABOUT PROJECT
# ============================================================

elif page == "📚 About Project":

    st.title("📚 About the Project")

    st.write(
        "Bitcoin Alpha Web of Trust Network Analysis"
    )

    st.divider()

    st.subheader("📌 Dataset")

    st.write(
        "The Bitcoin Alpha dataset represents a Web of Trust "
        "network in which users provide ratings to other users. "
        "Each connection represents a directed rating relationship."
    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("🧩 Dataset Structure")

        st.markdown(
            """
            - **Source:** User giving the rating
            - **Target:** User receiving the rating
            - **Rating:** Rating assigned by the source user
            - **Time:** Timestamp of the rating
            - **Rating range:** -10 to +10
            """
        )

    with c2:

        st.subheader("🛠️ Technologies")

        st.markdown(
            """
            - Python
            - Pandas
            - NetworkX
            - Matplotlib
            - Jupyter Notebook
            - Streamlit
            """
        )

    st.divider()

    st.subheader("🎯 Project Objective")

    st.write(
        "The project applies network visualization and analysis "
        "techniques to study user connectivity and structural "
        "characteristics using degree, closeness, betweenness, "
        "transitivity, reciprocity and degree assortativity."
    )

    st.divider()

    st.subheader("📊 Project Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric("Nodes", "3,783")
    c2.metric("Edges", "24,186")
    c3.metric("Network Type", "Directed")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Bitcoin Alpha Web of Trust Network Analysis • "
    "Python • NetworkX • Matplotlib • Streamlit"
)

st.caption(
    "B.E. Artificial Intelligence and Data Science | Academic Project"
)