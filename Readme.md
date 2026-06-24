
# NovaSonic — Three-Agent Trust & Transparency Pipeline

This repository contains the working three-agent AI pipeline built for an NCI assessment.

- **Assigned business:** NovaSonic (Scenario 5 — Media / Podcasting)
- **Assigned lens:** Trust and Transparency (Lens 3)
- **Assigned challenge:** Mid-tier creators churn because NovaSonic's payouts and discovery/recommendation algorithm are an opaque "black box", and the platform hoards listener data that creators need.

## Pipeline Architecture

The pipeline chains exactly three of the five studied archetypes. Each agent receives and explicitly uses the previous agent's output (a **visible handoff**).

```
Assigned Challenge
        |
        v
[ AGENT 1: RESEARCHER ]  diagnoses root cause + 8 transparency data points
        |  HANDOFF 1 (8 data points)
        v
[ AGENT 2: DESIGNER ]    builds the Creator Trust & Transparency Dashboard (10 traceable panels)
        |  HANDOFF 2 (dashboard panels)
        v
[ AGENT 3: COMMUNICATOR ] writes the creator launch package (email, in-app notice, trust FAQ)
        |
        v
   FINAL OUTPUT: business-actionable launch plan
```

![Pipeline Architecture](https://raw.githubusercontent.com/naosantana228-web/Build-It-Then-Distrust-It/main/architecture.png)

## Evidence the Pipeline Runs (Appendix B)

The complete machine-generated run is in **[transcript.md](https://github.com/naosantana228-web/Build-It-Then-Distrust-It/blob/main/transcript.md)**. The handoffs are visible: each downstream agent opens with a `HANDOFF RECEIVED` block.

- **Handoff 1 (Researcher to Designer):** the Designer lists all 8 of the Researcher's data points and maps every dashboard panel back to a specific field.
- **Handoff 2 (Designer to Communicator):** the Communicator names the exact dashboard panels it is announcing and promises only features the Designer specified.

## How to Run It Yourself

Requirements: Python 3 and an OpenAI API key.

```bash
pip3 install openai
export OPENAI_API_KEY="sk-...your key..."
python3 run_pipeline.py
```

The script prints each agent and each handoff to the console, then writes a fresh `transcript.md`.

> Note: the `MODEL` constant in `run_pipeline.py` defaults to `gpt-4o`. Change it to any model your key supports (e.g. `gpt-4o-mini`).

## Files

| File | Description |
|------|-------------|
| `run_pipeline.py` | The three-agent orchestration script (system prompts included). |
| `transcript.md` | Full transcript of a real run — evidence of execution and visible handoffs. |
| `architecture.png` | Pipeline / handoff diagram. |
