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
[ AGENT 1: RESEARCHER ]  diagnoses root cause + 7 transparency data points
        |  HANDOFF 1 (7 data points)
        v
[ AGENT 2: DESIGNER ]    builds the Creator Trust & Transparency Dashboard (traceable panels)
        |  HANDOFF 2 (dashboard panels)
        v
[ AGENT 3: COMMUNICATOR ] writes the creator launch package (email, in-app notice, trust FAQ)
        |
        v
   FINAL OUTPUT: business-actionable launch plan
```

![Pipeline Architecture](https://raw.githubusercontent.com/naosantana228-web/Build-It-Then-Distrust-It/main/architecture.png)

## Visible Handoffs (Evidence)

The pipeline was executed live on **Gemini 2.5 Flash-Lite**. The handoffs are visible because each downstream agent opens with a `HANDOFF RECEIVED` block naming exactly what it inherited:

- **Handoff 1 (Researcher → Designer):** the Designer lists all 7 Researcher data points and states *"No data points are being deferred."*
- **Handoff 2 (Designer → Communicator):** the Communicator names the exact dashboard panels it is announcing, and only promises features the Designer specified.

## Files in this repository

| File | What it is |
|------|------------|
| `NovaSonic_Pipeline.ipynb` | The three-agent pipeline (Colab notebook, Gemini). System prompts inside = Appendix A. |
| `transcript.md` | **Full clean run transcript** — evidence of execution + visible handoffs (Appendix B). |
| `NovaSonic_Flawed_Run.ipynb` | A deliberately weakly-constrained run used to surface genuine failures. |
| `flawed_transcript.md` | The flawed run output — source of the Failure Dossier quotes. |
| `architecture.png` | The pipeline / handoff diagram. |

## How to reproduce

1. Open `NovaSonic_Pipeline.ipynb` in Google Colab.
2. Paste a Gemini API key into Cell 2 (free key from Google AI Studio).
3. Run Cell 1 → Cell 2 → Cell 3. The run is saved to `transcript.md`.
