import streamlit as st



from utils import rewrite_text
from style import load_css
# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="ToneShift AI",
    page_icon="✨",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# -----------------------------
# SESSION
# -----------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    try:
        st.image("assets/logo.png", width=150)
    except:
        pass

    st.markdown("## ToneShift AI")
    st.caption("Professional AI Writing Assistant")

    st.divider()

    st.markdown("### Features")

    st.markdown("""
- ✨ Rewrite Text
- 🎭 Multiple Tones
- 📏 Multiple Lengths
- 🤖 Gemini AI
- 📄 TXT Download
- 📊 Word Analytics
""")

    st.divider()

    st.markdown("### Recent History")

    if len(st.session_state.history) == 0:

        st.info("No rewrites yet.")

    else:

        for i,item in enumerate(st.session_state.history):

            with st.expander(f"Rewrite {i+1}"):

                st.write(item)

    st.divider()

    st.success("Powered by Gemini")

# -----------------------------
# HEADER
# -----------------------------

left,right=st.columns([1,5])

with left:

    try:

        st.image("assets/logo.png",width=220)

    except:

        pass

with right:

    st.markdown("""
<h1 class='main-title'>
ToneShift AI
</h1>
""",unsafe_allow_html=True)

    st.markdown("""
<p class='sub-title'>
Rewrite anything in seconds using Google's Gemini AI.
</p>
""",unsafe_allow_html=True)

st.divider()

# -----------------------------
# INPUT
# -----------------------------

st.markdown("## 📝 Enter Text")

user_text=st.text_area(
    "",
    height=250,
    placeholder="Write or paste your content here..."
)

col1,col2=st.columns(2)

with col1:

    tone=st.selectbox(

        "Tone",

        [

            "Formal",

            "Professional",

            "Friendly",

            "Casual",

            "Executive Summary"

        ]

    )

with col2:

    length=st.selectbox(

        "Length",

        [

            "Short",

            "Medium",

            "Long"

        ]

    )

st.write("")



# -----------------------------
# REWRITE BUTTON
# -----------------------------

if st.button(
    "✨ Rewrite Text",
    use_container_width=True,
    type="primary"
):

    if user_text.strip() == "":

        st.warning("⚠ Please enter some text.")

    else:

        with st.spinner("🤖 Gemini AI is rewriting your text..."):

            result = rewrite_text(
                user_text,
                tone,
                length
            )

        # Save History
        st.session_state.history.insert(0, result)
        st.session_state.history = st.session_state.history[:5]

        st.success("✅ Rewrite Completed!")

        st.markdown("## 🤖 AI Response")

        st.markdown(
            f"""
<div class="result-box">

{result}

</div>
""",
            unsafe_allow_html=True
        )

        st.write("")

        # ------------------------------------
        # Analytics
        # ------------------------------------

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric(
                "📝 Words",
                len(result.split())
            )

        with m2:
            st.metric(
                "🔤 Characters",
                len(result)
            )

        with m3:
            st.metric(
                "📄 Lines",
                len(result.splitlines())
            )

        st.write("")

        # ------------------------------------
        # Download Section
        # ------------------------------------

        st.markdown("### 📥 Export")

        d1, d2 = st.columns(2)

        with d1:

            st.download_button(
                "⬇ Download TXT",
                result,
                file_name="ToneShift_Output.txt",
                mime="text/plain",
                use_container_width=True
            )

        with d2:

            st.text_area(
                "📋 Copy Output",
                value=result,
                height=180
            )

# ------------------------------------
# FOOTER
# ------------------------------------

st.divider()

st.markdown(
"""
<div class="footer">

🚀 Powered by <b>Google Gemini AI</b><br>

Made with ❤️ using Streamlit

</div>
""",
unsafe_allow_html=True
)