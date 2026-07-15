def load_css():
    return """
<style>

/* ==========================================
   Background
========================================== */

.stApp{
    background:#0F172A;
}

/* ==========================================
   Main Container
========================================== */

.block-container{
    max-width:1200px;
    padding-top:25px;
    padding-bottom:40px;
}

/* ==========================================
   Sidebar
========================================== */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #1F2937;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:white;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span{
    color:#CBD5E1;
}

/* ==========================================
   Title
========================================== */

.main-title{

    text-align:left;

    font-size:58px;

    font-weight:900;

    margin-top:15px;

    margin-bottom:0;

    background:linear-gradient(90deg,#60A5FA,#A855F7);

    -webkit-background-clip:text;

    -webkit-text-fill-color:transparent;

}

/* ==========================================
   Subtitle
========================================== */

.sub-title{

    color:#94A3B8;

    font-size:20px;

    margin-top:5px;

    margin-bottom:20px;

}

/* ==========================================
   Labels
========================================== */

label{

    color:white !important;

    font-weight:600;

}

/* ==========================================
   Text Area
========================================== */

textarea{

    background:#1E293B !important;

    color:white !important;

    border-radius:16px !important;

    border:1px solid #334155 !important;

    font-size:16px !important;

    padding:12px !important;

}

textarea:focus{
border:2px solid #3B82F6 !important;
box-shadow:0 0 15px rgba(59,130,246,.5);
}

/* ==========================================
   Selectbox
========================================== */

div[data-baseweb="select"]{

    border-radius:12px;

}

/* ==========================================
   Buttons
========================================== */

.stButton>button{

    width:100%;

    height:56px;

    border:none;

    border-radius:14px;

    background:linear-gradient(90deg,#2563EB,#3B82F6);

    color:white;

    font-size:18px;

    font-weight:700;

    transition:0.30s;

    box-shadow:0 8px 18px rgba(37,99,235,.30);

}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:0 12px 25px rgba(37,99,235,.45);

}

/* ==========================================
   Result Card
========================================== */

.result-box{

    background:#1E293B;

    border-radius:20px;

    padding:30px;

    border:1px solid #334155;

    color:white;

    font-size:18px;

    line-height:1.9;

    white-space:pre-wrap;

    box-shadow:0 10px 30px rgba(0,0,0,.35);

}

/* ==========================================
   Metrics
========================================== */

div[data-testid="metric-container"]{

    background:#1E293B;

    border-radius:16px;

    padding:15px;

    border:1px solid #334155;

}

/* ==========================================
   Code Block
========================================== */

pre{

    border-radius:14px !important;

}

/* ==========================================
   Success
========================================== */

div[data-testid="stAlert"]{

    border-radius:14px;

}

/* ==========================================
   Horizontal Line
========================================== */

hr{

    border:1px solid #1F2937;

}

/* ==========================================
   Footer
========================================== */

.footer{

    text-align:center;

    color:#64748B;

    font-size:15px;

    margin-top:35px;

    padding:10px;

}

/* ==========================================
   Scrollbar
========================================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#334155;

    border-radius:20px;

}

::-webkit-scrollbar-thumb:hover{

    background:#475569;

}

</style>
"""