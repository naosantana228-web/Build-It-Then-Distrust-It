"""
NovaSonic Three-Agent Trust & Transparency Pipeline
Archetypes: Researcher -> Designer -> Communicator

This is a self-contained script designed to be run on your own machine (e.g. Mac terminal)
and recorded for Appendix B (evidence of the pipeline running).

It prints clear, recording-friendly banners for each agent and each HANDOFF, then writes a
full transcript.md you can scroll through on camera.

SETUP (see SETUP_GUIDE.txt):
    pip3 install openai
    export OPENAI_API_KEY="sk-...your key..."
    python3 run_pipeline.py
"""
import os
import sys
import time
import datetime
from openai import OpenAI

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
MODEL = "gpt-4o"  # A widely-available model. Change to any model your key supports.

if not os.getenv("OPENAI_API_KEY"):
    print("\nERROR: No OPENAI_API_KEY found.")
    print('Run this first:  export OPENAI_API_KEY="sk-...your key..."\n')
    sys.exit(1)

client = OpenAI()

# Simple colours for a clean on-camera look (works in Mac Terminal)
class C:
    HEAD = "\033[95m"; BLUE = "\033[94m"; GREEN = "\033[92m"
    YELLOW = "\033[93m"; BOLD = "\033[1m"; END = "\033[0m"

def banner(text, colour=C.BLUE):
    line = "=" * 70
    print(f"\n{colour}{C.BOLD}{line}\n{text}\n{line}{C.END}\n")

# ---------------------------------------------------------------------------
# Shared business context (the assigned challenge)
# ---------------------------------------------------------------------------
BUSINESS_CONTEXT = """
BUSINESS: NovaSonic (fictitious podcast platform).
KEY METRICS: 500,000 users; 12,000 creators; creator retention 22% after 6 months;
top 3% of creators generate 81% of all listens.
ASSIGNED LENS: Trust and Transparency.
ASSIGNED CHALLENGE (selected for the pipeline): Mid-tier creators churn because
NovaSonic's monetisation payouts and discovery/recommendation algorithm are an opaque
"black box", and the platform hoards listener data that creators need. The platform
must rebuild creator trust by making economics and discovery transparent and auditable.
"""

# ---------------------------------------------------------------------------
# Agent system prompts
# ---------------------------------------------------------------------------
RESEARCHER_PROMPT = """You are RESEARCHER-AGENT, the first agent in a three-agent pipeline for NovaSonic.
ROLE (Researcher archetype): Diagnose the trust-and-transparency root causes of creator churn
and specify EXACTLY what transparency data/signals would fix it.

You must:
1. State the single root-cause hypothesis tying the 22% retention and 81% listen concentration
   to opaque platform economics and discovery.
2. Produce a prioritised list of 6-8 concrete, measurable "transparency data points" that creators
   are currently denied (e.g., per-stream payout rate, impression source breakdown, algorithm
   ranking factors). For each: give the field name, why it builds trust, and the data source.
   Do not invent products or features.
3. Flag 2 risks or unknowns where you are uncertain (be honest about assumptions).

Be specific and concise. Output structured Markdown. Your output will be handed directly to a
DESIGNER-AGENT who will design a dashboard from it, so make the data points unambiguous.
"""

DESIGNER_PROMPT = """You are DESIGNER-AGENT, the second agent in a three-agent pipeline for NovaSonic.
ROLE (Designer archetype): Turn the Researcher's transparency data points into a concrete,
buildable prototype: a "Creator Trust & Transparency Dashboard".

CRITICAL: You MUST explicitly reference and use the Researcher's output. Begin your response with a
short section "HANDOFF RECEIVED" that lists which of the Researcher's data points you are using and
which (if any) you are deferring, with a reason. Do not invent metrics the Researcher did not provide
unless you clearly label them "NEW (designer-added)" with justification.

Then produce:
1. A text wireframe of the dashboard (sections, panels, key UI components) using Markdown.
2. For each panel, name the exact data point it visualises (traceable to the Researcher).
3. One "transparency explainer" microcopy example shown to creators (plain language).
4. Acceptance criteria the Maker/engineering team could build against.

Output structured Markdown. Your output goes to a COMMUNICATOR-AGENT who will announce this to creators.
"""

COMMUNICATOR_PROMPT = """You are COMMUNICATOR-AGENT, the third and final agent in a three-agent pipeline for NovaSonic.
ROLE (Communicator archetype): Produce the business-actionable final deliverable: a launch
communication to NovaSonic's 12,000 creators announcing the new Creator Trust & Transparency Dashboard.

CRITICAL: You MUST explicitly reference and use the Designer's output. Begin with a short section
"HANDOFF RECEIVED" that names the specific dashboard panels/features (from the Designer) you are
announcing. Do not promise features the Designer did not specify.

Then produce:
1. A creator-facing announcement email (subject line + body) in NovaSonic's honest, non-hyped voice.
2. A short in-app notification (under 280 characters).
3. An FAQ of 4 questions addressing the trust concerns (payout fairness, algorithm bias, data access, opt-out).
Be transparent, specific, and avoid marketing exaggeration. Output structured Markdown.
"""

def call_agent(system_prompt, user_content):
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
    )
    return resp.choices[0].message.content

def main():
    transcript = []
    ts = datetime.datetime.now().isoformat()
    banner("NOVASONIC THREE-AGENT PIPELINE  |  Researcher -> Designer -> Communicator", C.HEAD)
    print(f"Timestamp: {ts}")
    print(f"Model: {MODEL}")
    print(f"Assigned challenge: NovaSonic 'black box' economics & discovery (Trust & Transparency lens)")
    transcript.append(f"# NovaSonic Three-Agent Pipeline Run\nTimestamp: {ts}\nModel: {MODEL}\n")
    time.sleep(1)

    # ---- Agent 1: Researcher ----
    banner("AGENT 1 / 3  -  RESEARCHER  (diagnosing root cause + transparency data points)", C.BLUE)
    researcher_input = f"{BUSINESS_CONTEXT}\n\nProduce your research brief now."
    researcher_out = call_agent(RESEARCHER_PROMPT, researcher_input)
    print(researcher_out)
    transcript.append("## AGENT 1 - RESEARCHER\n### OUTPUT:\n" + researcher_out + "\n")
    time.sleep(1)

    # ---- HANDOFF 1 ----
    banner(">>> HANDOFF 1: Researcher output -> Designer input <<<", C.YELLOW)
    time.sleep(1)

    # ---- Agent 2: Designer ----
    banner("AGENT 2 / 3  -  DESIGNER  (turning data points into a dashboard prototype)", C.GREEN)
    designer_input = (
        f"{BUSINESS_CONTEXT}\n\n"
        "=== HANDOFF FROM RESEARCHER-AGENT (use this directly) ===\n"
        f"{researcher_out}\n"
        "=== END HANDOFF ===\n\nDesign the dashboard now."
    )
    designer_out = call_agent(DESIGNER_PROMPT, designer_input)
    print(designer_out)
    transcript.append("## AGENT 2 - DESIGNER\n### OUTPUT:\n" + designer_out + "\n")
    time.sleep(1)

    # ---- HANDOFF 2 ----
    banner(">>> HANDOFF 2: Designer output -> Communicator input <<<", C.YELLOW)
    time.sleep(1)

    # ---- Agent 3: Communicator ----
    banner("AGENT 3 / 3  -  COMMUNICATOR  (final actionable creator launch package)", C.HEAD)
    communicator_input = (
        f"{BUSINESS_CONTEXT}\n\n"
        "=== HANDOFF FROM DESIGNER-AGENT (use this directly) ===\n"
        f"{designer_out}\n"
        "=== END HANDOFF ===\n\nWrite the launch communication now."
    )
    communicator_out = call_agent(COMMUNICATOR_PROMPT, communicator_input)
    print(communicator_out)
    transcript.append("## AGENT 3 - COMMUNICATOR\n### OUTPUT:\n" + communicator_out + "\n")

    # Save transcript
    with open("transcript.md", "w") as f:
        f.write("\n".join(transcript))

    banner("PIPELINE COMPLETE  -  full transcript saved to transcript.md", C.GREEN)
    print("Open transcript.md and scroll to the two 'HANDOFF RECEIVED' blocks to show the handoffs.\n")

if __name__ == "__main__":
    main()
