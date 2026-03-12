import gradio as gr
import time
from datetime import datetime

from core.crew import ContentCrew
from core.knowledge_base import KnowledgeBase

kb = KnowledgeBase()


def agent_msg(icon, text):
    return f"""
    <div class="agent-row">
        <div class="agent-icon">{icon}</div>
        <div class="agent-bubble">{text}</div>
    </div>
    """


def generate_article(topic):
    if topic.strip() == "":
        yield "", "", None
        return

    log = ""

    log += agent_msg("🧠", "Debate agent analyzing topic...")
    yield "", log, None
    time.sleep(1)

    log += agent_msg("🔎", "Research agent searching web...")
    yield "", log, None
    time.sleep(1)

    log += agent_msg("✍️", "Writer drafting article...")
    yield "", log, None
    time.sleep(1)

    crew = ContentCrew()
    result = crew.run(topic)
    article = str(result)

    log += agent_msg("🧹", "Editor polishing article...")
    yield "", log, None
    time.sleep(1)

    yield article, log, None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    md_file = f"article_{timestamp}.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(article)

    kb.add_document({"topic": topic, "content": article})

    yield article, log, md_file


css = """
body{
background:#020617;
font-family:Inter,system-ui;
color:#e2e8f0;
}

#title{
text-align:center;
font-size:42px;
font-weight:800;
color:#e0e7ff;
text-shadow:0 0 8px #6366f1;
margin-bottom:6px;
}

#subtitle{
text-align:center;
color:#cbd5e1;
margin-bottom:25px;
font-size:16px;
}

.sidebar{
background:#020617;
border-right:1px solid #334155;
padding:20px;
}

.sidebar h3{
color:#f1f5f9 !important;
font-size:15px !important;
font-weight:700 !important;
margin-top:20px !important;
margin-bottom:12px !important;
}

textarea{
background:#1e293b !important;
color:#f1f5f9 !important;
border-radius:10px !important;
border:1px solid #475569 !important;
}

label{
color:#cbd5e1 !important;
font-weight:600 !important;
}

button{
background:linear-gradient(90deg,#6366f1,#8b5cf6) !important;
color:white !important;
border-radius:10px !important;
font-weight:600 !important;
}

button:hover{
background:linear-gradient(90deg,#4f46e5,#7c3aed) !important;
}

.agent-panel{
background:#020617;
border:1px solid #334155;
border-radius:12px;
padding:20px;
margin-bottom:20px;
}

.agent-row{
display:flex;
align-items:center;
margin-bottom:10px;
}

.agent-icon{
font-size:22px;
margin-right:10px;
}

.agent-bubble{
background:#1e293b;
padding:8px 12px;
border-radius:8px;
border:1px solid #475569;
font-size:14px;
color:#f1f5f9;
}

.section-heading{
color:#f1f5f9 !important;
font-size:18px !important;
font-weight:700 !important;
margin-top:20px !important;
margin-bottom:15px !important;
}

.article-box{
background:#0f172a;
border:1px solid #334155;
padding:30px;
border-radius:12px;
font-size:17px;
line-height:1.8;
}

.article-box *{
color:#e2e8f0 !important;
}

.article-box h1{
font-size:32px !important;
color:#ffffff !important;
font-weight:800 !important;
margin-bottom:20px !important;
}

.article-box h2{
font-size:24px !important;
color:#f1f5f9 !important;
font-weight:700 !important;
margin-top:25px !important;
margin-bottom:12px !important;
}

.article-box h3{
font-size:20px !important;
color:#f1f5f9 !important;
font-weight:600 !important;
}

.article-box p{
color:#cbd5e1 !important;
margin-bottom:14px !important;
}

.article-box li{
color:#cbd5e1 !important;
}

.article-box a{
color:#60a5fa !important;
}

.article-box strong, .article-box b{
color:#f1f5f9 !important;
}

.download-row{
margin-top:15px;
gap:10px;
}
"""


with gr.Blocks(css=css) as app:

    gr.Markdown("# 🤖 Multi-Agent Content Team", elem_id="title")
    gr.Markdown("Research → Debate → Write → Edit → Publish", elem_id="subtitle")

    with gr.Row():

        with gr.Column(scale=1, elem_classes="sidebar"):

            topic = gr.Textbox(
                label="Content Topic",
                placeholder="Example: AI impact on healthcare",
                lines=3
            )

            generate_btn = gr.Button("🚀 Generate Article", size="lg")

            gr.Markdown("### 📚 Example Topics")

            ex1 = gr.Button("Future of renewable energy in 2026")
            ex2 = gr.Button("AI impact on healthcare")
            ex3 = gr.Button("Quantum computing breakthroughs")
            ex4 = gr.Button("Blockchain technology trends")

        with gr.Column(scale=3):

            gr.Markdown("### 🤖 Agent Conversation", elem_classes="section-heading")
            agent_log = gr.HTML(elem_classes="agent-panel")

            gr.Markdown("### ✨ Generated Article", elem_classes="section-heading")
            output = gr.Markdown(elem_classes="article-box")

            with gr.Row(elem_classes="download-row"):
                md_download = gr.DownloadButton("📄 Download Markdown")

    generate_btn.click(
        generate_article,
        inputs=topic,
        outputs=[output, agent_log, md_download]
    )

    ex1.click(lambda: "Future of renewable energy in 2026", None, topic)
    ex2.click(lambda: "AI impact on healthcare", None, topic)
    ex3.click(lambda: "Quantum computing breakthroughs", None, topic)
    ex4.click(lambda: "Blockchain technology trends", None, topic)

app.launch()