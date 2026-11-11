
import streamlit as st  # type: ignore
from analyze import analyze_password

# Page configuration
st.set_page_config(
    page_title="MYTRUF | Password Analyzer",
    page_icon="🛡️",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #e5e7eb;
}

h1, h2, h3 {
    color: #38bdf8 !important;
}

div[data-testid="stMetric"] {
    background-color: #172033;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #263449;
}

.stButton button {
    background-color: #0284c7;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# Application heading
st.title("🛡️ MYTRUF")
st.subheader("Intelligent Password Security Analyzer")

st.markdown("""
Evaluate password characteristics using automated security checks.
Identify common weaknesses and receive recommendations.
""")

st.divider()

# Password input
st.markdown("### 🔐 Password Analysis")

password = st.text_input(
    "Enter a test password",
    type="password",
    placeholder="Enter a sample password..."
)

analyze_button = st.button("Analyze Password")

if analyze_button:

    if not password:
        st.warning("Please enter a password first.")

    else:
        result = analyze_password(password)

        st.divider()

        # Display results
        st.markdown("### 📊 Security Report")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Security Score",
                f"{result['score']}/100"
            )

        with col2:
            st.metric(
                "Security Rating",
                result["rating"]
            )

        with col3:
            st.metric(
                "Estimated Entropy",
                f"{result['entropy']} bits"
            )

        # Score progress bar
        st.markdown("### Overall Security Score")
        st.progress(result["score"] / 100)

        # Findings
        st.markdown("### 🔍 Security Findings")

        for finding in result["findings"]:
            st.write("⚠️", finding)

        # Recommendations
        st.markdown("### 💡 Recommendations")

        for recommendation in result["recommendations"]:
            st.write("✅", recommendation)
        # Downloadable security report
        st.markdown("### 📄 Download Security Report")

        report = f"""
MYTRUF - PASSWORD ANALYSIS REPORT
===================================

Security Score: {result['score']}/100
Security Rating: {result['rating']}
Estimated Entropy: {result['entropy']} bits

SECURITY FINDINGS:
------------------
"""

        for finding in result["findings"]:
            report += f"- {finding}\n"

        report += "\nRECOMMENDATIONS:\n----------------\n"

        for recommendation in result["recommendations"]:
            report += f"- {recommendation}\n"

        report += """
DISCLAIMER:
This report uses educational heuristic checks.
It does not guarantee password security.
"""

        st.download_button(
            label="Download Security Report",
            data=report,
            file_name="mytruf_security_report.txt",
            mime="text/plain"
        )

        st.divider()

        st.caption(
            "MYTRUF uses educational heuristic checks. "
            "Its score and entropy estimate are not security guarantees."
        )

st.markdown("---")
st.caption("MYTRUF | Educational Cybersecurity Project")

        