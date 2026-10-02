import streamlit as st
from pathlib import Path
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Bitcoin Alpha Web of Trust Network Analysis",
    page_icon="🔗",
    layout="wide"
)
# ============================================================
# PROFESSIONAL DASHBOARD THEME
# ============================================================

st.markdown("""
<style>

    /* ---------- Main Background ---------- */
    .stApp {
        background-color: #f5f7fb;
    }

    /* ---------- Main Content ---------- */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1400px;
    }

    /* ---------- Main Titles ---------- */
    h1 {
        font-size: 2.4rem !important;
        font-weight: 700 !important;
        color: #172033 !important;
        letter-spacing: -0.5px;
    }

    h2 {
        font-size: 1.7rem !important;
        font-weight: 650 !important;
        color: #172033 !important;
        margin-top: 1.5rem !important;
    }

    h3 {
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        color: #273449 !important;
    }

    /* ---------- Normal Text ---------- */
    p {
        color: #4b5563;
        line-height: 1.7;
        font-size: 1rem;
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background-color: #172033;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    section[data-testid="stSidebar"] .stRadio label {
        font-size: 0.98rem;
        font-weight: 500;
    }

    /* ---------- Metric Cards ---------- */
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.06);
    }

    div[data-testid="stMetricLabel"] {
        font-weight: 600;
        color: #6b7280 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #172033 !important;
        font-weight: 700;
    }

    /* ---------- Information Boxes ---------- */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* ---------- Buttons ---------- */
    .stButton > button,
    .stDownloadButton > button {
        border-radius: 10px;
        font-weight: 600;
        padding: 0.55rem 1.2rem;
        border: none;
    }

    /* ---------- Tables ---------- */
    .stTable {
        border-radius: 12px;
        overflow: hidden;
    }

    /* ---------- Dividers ---------- */
    hr {
        border: none;
        border-top: 1px solid #e5e7eb;
        margin: 2rem 0;
    }

    /* ---------- Captions ---------- */
    .stCaption {
        color: #6b7280 !important;
        font-size: 0.95rem;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

GRAPH_PATH = BASE_DIR / "graphs" / "bitcoin_trust_network_top50.png"

RESULTS_PATH = BASE_DIR / "results" / "network_analysis_summary.csv"


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

# ============================================================
# PROFESSIONAL SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div style="text-align:center; padding:10px 5px 20px 5px;">
        <div style="font-size:2.5rem;">🔗</div>
        <div style="
            color:white;
            font-size:1.3rem;
            font-weight:700;
            margin-top:5px;
        ">
            Bitcoin Alpha
        </div>
        <div style="
            color:#b8c1d1;
            font-size:0.85rem;
            margin-top:5px;
        ">
            Web of Trust Network
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div style="
        color:#9ca9bd;
        font-size:0.75rem;
        font-weight:600;
        letter-spacing:1px;
        margin-bottom:8px;
    ">
        DASHBOARD
    </div>
    """,
    unsafe_allow_html=True
)

section = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Network Visualization",
        "Centrality Analysis",
        "Network-Level Measures",
        "Key Findings",
        "About the Dataset"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

# ------------------------------------------------------------
# Project Details
# ------------------------------------------------------------

st.sidebar.markdown("### 📊 Project Details")

st.sidebar.markdown(
    """
    **NetworkX + Streamlit**

    👥 **3,783** Nodes

    🔗 **24,186** Edges
    """
)

st.sidebar.divider()

st.sidebar.caption(
    "B.E. Artificial Intelligence & Data Science"
)

st.sidebar.caption(
    "Academic Network Analysis Project"
)

# ============================================================
# OVERVIEW
# ============================================================

if section == "Overview":

    st.title("🔗 Bitcoin Alpha Web of Trust Network Analysis")

    st.caption(
        "Interactive Network Visualization and Analysis Dashboard"
    )

    st.write(
        "Explore the structure and connectivity of the Bitcoin Alpha "
        "Web of Trust Network using NetworkX."
    )

    st.divider()

    # --------------------------------------------------------
    # NETWORK SUMMARY
    # --------------------------------------------------------

    st.subheader("📊 Network Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="👥 Number of Nodes",
            value="3,783"
        )

    with col2:
        st.metric(
            label="🔗 Number of Edges",
            value="24,186"
        )

    with col3:
        st.metric(
            label="↔️ Reciprocity",
            value="0.8321"
        )

    st.divider()

    # --------------------------------------------------------
    # ABOUT THE PROJECT
    # --------------------------------------------------------

    st.subheader("📌 About the Project")

    st.write(
        "This project analyzes the Bitcoin Alpha Web of Trust Network, "
        "a directed network in which users provide ratings to other users. "
        "NetworkX is used to construct, visualize, and analyze the network."
    )

    st.info(
        "💡 Use the navigation menu to explore network visualization, "
        "centrality measures, network-level measures, key findings, "
        "and dataset information."
    )

    st.divider()

    # --------------------------------------------------------
    # QUICK HIGHLIGHTS
    # --------------------------------------------------------

    st.subheader("✨ Quick Highlights")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            ### 📈 Centrality Analysis

            The dashboard examines three important centrality measures:

            • **Degree Centrality**  
            Identifies highly connected users.

            • **Closeness Centrality**  
            Examines users based on network distance.

            • **Betweenness Centrality**  
            Identifies users positioned on shortest paths.
            """
        )

    with col2:

        st.markdown(
            """
            ### 🌐 Network Structure

            The dashboard examines three network-level measures:

            • **Transitivity**  
            Measures triangular connectivity.

            • **Reciprocity**  
            Measures mutual connections.

            • **Degree Assortativity**  
            Examines relationships between connected users' degrees.
            """
        )

    st.divider()

    # --------------------------------------------------------
    # ANALYSIS SNAPSHOT
    # --------------------------------------------------------

    st.subheader("🔍 Analysis Snapshot")

    snapshot_col1, snapshot_col2 = st.columns(2)

    with snapshot_col1:

        st.markdown(
            """
            **Highest Degree Centrality**

            👤 **User 1**

            Value: **0.2348**
            """
        )

    with snapshot_col2:

        st.markdown(
            """
            **Highest Closeness Centrality**

            👤 **User 2**

            Value: **0.3668**
            """
        )

    st.success(
        "✅ Network analysis completed successfully using NetworkX."
    )

    # --------------------------------------------------------
    # Dashboard Summary Cards
    # --------------------------------------------------------

    st.subheader("📊 Network Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="👥 Number of Nodes",
            value="3,783"
        )

    with col2:
        st.metric(
            label="🔗 Number of Edges",
            value="24,186"
        )

    with col3:
        st.metric(
            label="↔️ Reciprocity",
            value="0.8321"
        )

    st.divider()

    # --------------------------------------------------------
    # Project Summary
    # --------------------------------------------------------

    st.subheader("📌 About the Project")

    st.write(
        "This project analyzes the Bitcoin Alpha Web of Trust Network, "
        "a directed network in which users provide ratings to other users. "
        "NetworkX is used to construct, visualize, and analyze the network."
    )

    st.info(
        "Use the navigation menu on the left to explore the network "
        "visualization, centrality measures, network-level measures, "
        "key findings, and dataset information."
    )

    st.divider()

    # --------------------------------------------------------
    # Quick Highlights
    # --------------------------------------------------------

    st.subheader("✨ Quick Highlights")

    highlight1, highlight2 = st.columns(2)

    with highlight1:
        st.markdown(
            """
            **📈 Centrality Analysis**

            The dashboard analyzes:

            - Degree Centrality
            - Closeness Centrality
            - Betweenness Centrality
            """
        )

    with highlight2:
        st.markdown(
            """
            **🌐 Network Structure**

            The dashboard analyzes:

            - Transitivity
            - Reciprocity
            - Degree Assortativity
            """
        )

# ============================================================
# NETWORK VISUALIZATION
# ============================================================

elif section == "Network Visualization":

    st.title("🌐 Network Visualization")

    st.caption(
        "Visual representation of the Bitcoin Alpha Web of Trust Network"
    )

    st.write(
        "The visualization below presents the top 50 connected users "
        "from the complete Bitcoin Alpha Web of Trust Network."
    )

    st.divider()

    # ========================================================
    # NETWORK STATISTICS
    # ========================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="👥 Total Users",
            value="3,783"
        )

    with col2:
        st.metric(
            label="🔗 Total Connections",
            value="24,186"
        )

    with col3:
        st.metric(
            label="📊 Users Visualized",
            value="50"
        )

    st.divider()

    # ========================================================
    # NETWORK GRAPH
    # ========================================================

    st.subheader("📊 Top 50 Connected Users")

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

    # ========================================================
    # VISUALIZATION DESCRIPTION
    # ========================================================

    st.subheader("📖 Understanding the Visualization")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            ### 🔵 Nodes

            Each node represents a user in the Bitcoin Alpha
            Web of Trust Network.
            """
        )

    with col2:

        st.markdown(
            """
            ### ➡️ Directed Edges

            Each directed edge represents a rating relationship
            from one user to another.
            """
        )

    st.info(
        "The complete network contains 3,783 users and 24,186 "
        "directed connections. The top 50 connected users are "
        "displayed in the visualization to make the network "
        "structure easier to interpret."
    )

# ============================================================
# CENTRALITY ANALYSIS
# ============================================================

elif section == "Centrality Analysis":

    import matplotlib.pyplot as plt

    st.title("📈 Centrality Analysis")

    st.caption(
        "Identifying structurally important users within the network"
    )

    st.write(
        "Centrality measures help identify users that occupy important "
        "positions within the Bitcoin Alpha Web of Trust Network."
    )

    st.divider()

    # ========================================================
    # DEGREE CENTRALITY
    # ========================================================

    st.subheader("🔹 Degree Centrality")

    st.write(
        "Degree centrality measures the number of connections associated "
        "with a user within the network."
    )

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

    fig, ax = plt.subplots(figsize=(10, 5))

    users = list(degree_data.keys())[::-1]
    values = list(degree_data.values())[::-1]

    bars = ax.barh(users, values)

    ax.set_xlabel("Degree Centrality")
    ax.set_title("Top 10 Users by Degree Centrality", fontweight="bold")
    ax.grid(axis="x", alpha=0.2)

    for bar, value in zip(bars, values):
        ax.text(
            value + 0.003,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.4f}",
            va="center",
            fontsize=9
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig, use_container_width=True)

    plt.close(fig)

    st.info(
        "User 1 has the highest degree centrality with a value of 0.2348."
    )

    st.divider()

    # ========================================================
    # CLOSENESS CENTRALITY
    # ========================================================

    st.subheader("🔹 Closeness Centrality")

    st.write(
        "Closeness centrality measures the relative distance of a user "
        "from other users in the network."
    )

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

    fig, ax = plt.subplots(figsize=(10, 5))

    users = list(closeness_data.keys())[::-1]
    values = list(closeness_data.values())[::-1]

    bars = ax.barh(users, values)

    ax.set_xlabel("Closeness Centrality")
    ax.set_title("Top 10 Users by Closeness Centrality", fontweight="bold")
    ax.grid(axis="x", alpha=0.2)

    for bar, value in zip(bars, values):
        ax.text(
            value + 0.003,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.4f}",
            va="center",
            fontsize=9
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig, use_container_width=True)

    plt.close(fig)

    st.info(
        "User 2 has the highest closeness centrality with a value of 0.3668."
    )

    st.divider()

    # ========================================================
    # BETWEENNESS CENTRALITY
    # ========================================================

    st.subheader("🔹 Betweenness Centrality")

    st.write(
        "Betweenness centrality measures how frequently a user lies "
        "on shortest paths between other users."
    )

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

    fig, ax = plt.subplots(figsize=(10, 5))

    users = list(betweenness_data.keys())[::-1]
    values = list(betweenness_data.values())[::-1]

    bars = ax.barh(users, values)

    ax.set_xlabel("Betweenness Centrality")
    ax.set_title("Top 10 Users by Betweenness Centrality", fontweight="bold")
    ax.grid(axis="x", alpha=0.2)

    for bar, value in zip(bars, values):
        ax.text(
            value + 0.002,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.4f}",
            va="center",
            fontsize=9
        )

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    plt.tight_layout()

    st.pyplot(fig, use_container_width=True)

    plt.close(fig)

    st.info(
        "User 1 has the highest betweenness centrality with a value of 0.1492."
    )

# ============================================================
# NETWORK-LEVEL MEASURES
# ============================================================

elif section == "Network-Level Measures":

    st.title("🌐 Network-Level Measures")

    st.caption(
        "Structural properties of the Bitcoin Alpha Web of Trust Network"
    )

    st.write(
        "These measures describe important structural characteristics "
        "of the overall network."
    )

    st.divider()

    # ========================================================
    # MEASURE CARDS
    # ========================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🔺 Transitivity",
            value="0.0780"
        )

    with col2:
        st.metric(
            label="↔️ Reciprocity",
            value="0.8321"
        )

    with col3:
        st.metric(
            label="🔗 Degree Assortativity",
            value="-0.1635"
        )

    st.divider()

    # ========================================================
    # TRANSITIVITY
    # ========================================================

    st.subheader("🔺 Transitivity")

    st.write(
        "The network has an undirected transitivity value of **0.0780**. "
        "This represents the tendency of connected users to form "
        "triangular relationships in the undirected version of the network."
    )

    st.divider()

    # ========================================================
    # RECIPROCITY
    # ========================================================

    st.subheader("↔️ Reciprocity")

    st.write(
        "The reciprocity value is **0.8321**, indicating a high level "
        "of mutual connections between users."
    )

    st.divider()

    # ========================================================
    # DEGREE ASSORTATIVITY
    # ========================================================

    st.subheader("🔗 Degree Assortativity")

    st.write(
        "The degree assortativity value is **-0.1635**, indicating "
        "a weak negative relationship between the degrees of connected users."
    )

    st.divider()

    # ========================================================
    # OVERALL INTERPRETATION
    # ========================================================

    st.subheader("📌 Overall Interpretation")

    st.info(
        "Together, these measures provide a view of the network's "
        "clustering, mutual connections, and degree-based connectivity pattern."
    )
    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    st.subheader("📌 Measure Summary")

    st.info(
        "Together, these measures provide a view of the network's "
        "clustering, mutual connections, and degree-based connectivity pattern."
    )

# ============================================================
# KEY FINDINGS
# ============================================================

elif section == "Key Findings":

    st.title("🔍 Key Findings")

    st.caption(
        "Summary of the main results obtained from the network analysis"
    )

    st.write(
        "The following findings summarize the centrality measures "
        "and network-level properties calculated for the Bitcoin "
        "Alpha Web of Trust Network."
    )

    st.divider()

    # --------------------------------------------------------
    # Centrality Findings
    # --------------------------------------------------------

    st.subheader("📈 Centrality Findings")

    st.markdown(
        """
        **🔹 Degree Centrality**

        User 1 has the highest degree centrality with a value of
        **0.2348**, indicating a highly connected position in the network.

        **🔹 Closeness Centrality**

        User 2 has the highest closeness centrality with a value of
        **0.3668**, indicating a relatively central position based
        on network distances.

        **🔹 Betweenness Centrality**

        User 1 has the highest betweenness centrality with a value of
        **0.1492**, indicating that the user lies on a comparatively
        large number of shortest paths.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # Network-Level Findings
    # --------------------------------------------------------

    st.subheader("🌐 Network-Level Findings")

    st.markdown(
        """
        **🔺 Transitivity:** The network has an undirected
        transitivity value of **0.0780**.

        **↔️ Reciprocity:** The reciprocity value of **0.8321**
        indicates a high level of mutual connections between users.

        **🔗 Degree Assortativity:** The degree assortativity value
        of **-0.1635** indicates a weak negative relationship between
        the degrees of connected users.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # Overall Summary
    # --------------------------------------------------------

    st.subheader("📌 Overall Summary")

    st.info(
        "The analysis shows that different users occupy different "
        "structural positions in the network. Centrality measures "
        "identify highly connected and structurally important users, "
        "while network-level measures describe the overall pattern "
        "of connections within the network."
    )


# ============================================================
# ABOUT THE DATASET
# ============================================================

elif section == "About the Dataset":

    st.title("📚 About the Dataset")

    st.caption(
        "Bitcoin Alpha Web of Trust Network"
    )

    st.write(
        "The Bitcoin Alpha dataset represents a Web of Trust network "
        "in which users provide ratings to other users. Each connection "
        "represents a directed rating relationship between two users."
    )

    st.divider()

    # --------------------------------------------------------
    # Dataset Information
    # --------------------------------------------------------

    st.subheader("📋 Dataset Information")

    dataset_info = pd.DataFrame(
        {
            "Property": [
                "Dataset",
                "Network Type",
                "Number of Nodes",
                "Number of Edges",
                "Rating Range",
                "Data Source"
            ],
            "Details": [
                "Bitcoin Alpha Web of Trust",
                "Directed Network",
                "3,783",
                "24,186",
                "-10 to +10",
                "Stanford SNAP"
            ]
        }
    )

    st.table(dataset_info)

    st.divider()

    # --------------------------------------------------------
    # Dataset Structure
    # --------------------------------------------------------

    st.subheader("🧩 Dataset Structure")

    st.write(
        "The dataset contains four main attributes:"
    )

    st.markdown(
        """
        - **Source:** User who gives the rating.
        - **Target:** User who receives the rating.
        - **Rating:** Rating assigned by the source user to the target user.
        - **Time:** Timestamp indicating when the rating was recorded.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # Project Objective
    # --------------------------------------------------------

    st.subheader("🎯 Project Objective")

    st.write(
        "The objective of this project is to visualize and analyze "
        "the Bitcoin Alpha Web of Trust Network using NetworkX. "
        "The analysis focuses on degree, closeness, and betweenness "
        "centrality, along with transitivity, reciprocity, and "
        "degree assortativity."
    )

    st.divider()

    # --------------------------------------------------------
    # Data Source
    # --------------------------------------------------------

    st.subheader("🔗 Data Source")

    st.info(
        "Dataset: Bitcoin Alpha Web of Trust Network — Stanford SNAP"
    )

# ============================================================
# DOWNLOAD RESULTS
# ============================================================

st.divider()

st.subheader("📥 Download Analysis Results")

results_csv = """Measure,Value
Number of Nodes,3783
Number of Edges,24186
Top Degree Centrality,User 1 (0.2348)
Top Closeness Centrality,User 2 (0.3668)
Top Betweenness Centrality,User 1 (0.1492)
Transitivity,0.0780
Reciprocity,0.8321
Degree Assortativity,-0.1635
"""

st.download_button(
    label="📄 Download Network Analysis Summary",
    data=results_csv,
    file_name="network_analysis_summary.csv",
    mime="text/csv"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Bitcoin Alpha Web of Trust Network Analysis | "
    "Developed using Python, NetworkX and Streamlit"
)

st.caption(
    "B.E. Artificial Intelligence and Data Science | Academic Project"
)