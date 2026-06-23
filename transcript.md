# NovaSonic Three-Agent Pipeline Run
Timestamp: 2026-06-23T19:37:31.689916
Model: gpt-5

## AGENT 1 - RESEARCHER
### INPUT (business context):
```

BUSINESS: NovaSonic (fictitious podcast platform).
KEY METRICS: 500,000 users; 12,000 creators; creator retention 22% after 6 months;
top 3% of creators generate 81% of all listens.
ASSIGNED LENS: Trust and Transparency.
ASSIGNED CHALLENGE (selected for the pipeline): Mid-tier creators churn because
NovaSonic's monetisation payouts and discovery/recommendation algorithm are an opaque
"black box", and the platform hoards listener data that creators need. The platform
must rebuild creator trust by making economics and discovery transparent and auditable.


Produce your research brief now.
```
### OUTPUT:
NovaSonic Creator Trust & Transparency Research Brief (Researcher Agent)

1) Single Root-Cause Hypothesis
Mid‑tier creators churn because they cannot form a reliable mental model linking effort to outcomes: NovaSonic’s black‑box economics (what a “play” is, how much it pays, how the platform takes its cut) and black‑box discovery (where impressions come from, how ranking works, when they’re boosted/demoted) make earnings and growth unpredictable and non‑optimizable. This opacity concentrates exposure on already‑dominant shows (81% of listens in top 3%) and depresses mid‑tier retention (22% at 6 months) by eroding trust and blocking creators from diagnosing and fixing performance.

2) Prioritized Transparency Data Points (6–8)

1. Net Payout per 1,000 Qualified Plays (by Geo & Monetization Source)
- Field name: ePPQ_net_usd_by_geo_source
  - Definition: USD paid to creator per 1,000 qualified plays, segmented by country and source (ads, subscriptions, tips, bonuses), net of NovaSonic fees; include 30/60/90‑day trailing averages.
- Why it builds trust: Converts opaque revenue into a predictable unit rate so creators can forecast ROI, choose target geos, and understand seasonality and mix shifts.
- Data source: Payments Ledger + Ads Delivery Logs + Subscription Revenue Share System + Tips/Bonuses Ledger.

2. Revenue Component & Take-Rate Breakdown per Payout Period
- Field name: payout_component_breakdown
  - Definition: For each payout period, absolute USD and % by component (ads, subscriptions, tips, bonuses), NovaSonic fee (USD and %), and creator net.
- Why it builds trust: Shows exactly where money comes from and how much NovaSonic takes, removing suspicion of hidden deductions.
- Data source: Billing/Payments Ledger + Finance GL.

3. Qualified Play Definition & Counting Rules
- Field name: qualified_play_rules
  - Definition: Public, versioned criteria for a “qualified play” (e.g., X seconds or Y% listened), deduplication window, auto‑play inclusion, fraud/invalid traffic filters, and backfill policy for reclassifications.
- Why it builds trust: Aligns what “counts” with what pays; prevents surprises when plays don’t match payouts.
- Data source: Playback Service + Integrity/Fraud Detection Systems + Policy Docs.

4. Impression Source Funnel by Surface
- Field name: impression_funnel_by_surface
  - Definition: For each discovery surface (Home, Personalized Recs, Search, Category, Autoplay/Up Next, Follows Feed, Editorial/Featured, External Links), show: Impressions, CTR to episode page, Play Rate (plays/impressions), Avg Completion %, for a chosen date range.
- Why it builds trust: Reveals where visibility actually comes from and where drop‑offs occur, enabling creators to target effort and diagnose changes.
- Data source: Client Event Logs (Impression/Click/Play) + Content Analytics Warehouse.

5. Recommendation Exposure & Rank Position Distribution
- Field name: rec_exposure_rank_dist
  - Definition: Count of times an episode appeared in algorithmic carousels/feeds by rank bucket (1–3, 4–10, 11–20, >20), with dwell‑time‑weighted exposure, per surface.
- Why it builds trust: Quantifies how often the algorithm meaningfully placed content where users see it, not just raw impressions.
- Data source: Recommender Request/Response Logs + UI Position Telemetry.

6. Algorithmic Ranking Factor Contributions (Episode-Level)
- Field name: ranking_factor_contributions
  - Definition: For each episode and surface, top 5 model features driving its recommendation score with normalized contribution percentages (e.g., recent completion rate +34%, user‑topic affinity +22%, freshness +18%, policy quality −10%, report rate −8%); exclude raw weights; aggregate across users.
- Why it builds trust: Explains “why” an episode was shown (or not) in actionable terms without revealing exploitable internals.
- Data source: Recommender Service Explainability/Attribution Logs (e.g., SHAP summaries) + Feature Store.

7. Search Queries & Ranking Performance
- Field name: search_query_rank_perf
  - Definition: Top search queries that produced impressions for the creator’s episodes, with average rank at impression time, impressions, CTR, and plays per query; queries aggregated and privacy‑thresholded.
- Why it builds trust: Shows how findable content is via search and what terms drive discovery, enabling better titling/metadata.
- Data source: Search Service Query–Result Logs + Click Logs (privacy‑filtered).

8. Visibility Governance Flags (Boosts/Demotions) with Reasons
- Field name: visibility_governance_flags
  - Definition: Episode‑level flags over time: policy/status (brand‑safe class, explicit label), boosts (editorial feature, new‑release boost), demotions (policy quality issues, low listener satisfaction), with reason codes, start/end timestamps, and affected surfaces.
- Why it builds trust: Removes the “shadowban” fear by disclosing if/when visibility was altered and why.
- Data source: Trust & Safety/Policy Systems + Editorial Placement Logs + Recommender Policy Layer.

3) Risks / Unknowns
- Monetization model ambiguity: It’s unclear whether NovaSonic uses pro‑rata pools, user‑centric attribution, dynamic ad auctions, or hybrid; definitions affect ePPQ and component breakdown feasibility and stability.
- Gaming vs. explainability trade‑off: Exposing factor contributions must avoid enabling manipulation; the level of aggregation/obfuscation that preserves safety while remaining useful will need validation and possibly legal/privacy review.

## AGENT 2 - DESIGNER
### INPUT (Researcher's output handed off):
```
[Business context + full Researcher output above]
```
### OUTPUT:
HANDOFF RECEIVED
- Using all 8 Researcher data points:
  1) ePPQ_net_usd_by_geo_source
  2) payout_component_breakdown
  3) qualified_play_rules
  4) impression_funnel_by_surface
  5) rec_exposure_rank_dist
  6) ranking_factor_contributions
  7) search_query_rank_perf
  8) visibility_governance_flags
- Deferrals: None.
- Notes and safeguards:
  - ranking_factor_contributions will be aggregated and privacy-safe as the Researcher recommended. We will display top 5 normalized contributions only and suppress output if thresholds are not met.
  - Monetization model ambiguity acknowledged. The UI will surface the monetization model name and version pulled from Finance config alongside ePPQ and payout breakdown to avoid misinterpretation.
- NEW (designer-added) components, UI-only, justified for auditability and trust:
  - Data Freshness and Version Badges: last updated timestamp for each panel; model and rules version labels to tie numbers to system versions.
  - Export and API Access: CSV and JSON export buttons mirroring on-screen filters for creator-owned auditing.
  - Annotations: timeline markers when qualified play rules or visibility governance events change, to connect rule changes to metric shifts.
  - Privacy-threshold indicator: unobtrusive badge when rows are hidden due to privacy filtering.

1) TEXT WIREFRAME OF THE CREATOR TRUST AND TRANSPARENCY DASHBOARD

Global header and filters (persistent)
- Title: Creator Trust and Transparency
- Global filters
  - Date range: presets 7, 30, 60, 90 days and custom
  - Scope selector: Show-level or Episode-level
  - Episode picker (multi-select, searchable)
  - Geo selector (multi, includes All)
  - Discovery surfaces selector (Home, Personalized Recs, Search, Category, Autoplay, Follows Feed, Editorial, External)
  - Monetization source selector (Ads, Subscriptions, Tips, Bonuses)
- NEW: Data Freshness and Version Badges
  - Data last updated: timestamp per panel
  - Monetization model: name and version
  - Qualified play rules: version and effective date
  - Recommender model: version per surface

Overview snapshot
- Cards aligned in a row. Each card shows period selector: 30, 60, 90 days.
  - Card A: Net payout per 1,000 qualified plays (ePPQ, USD)
    - Visual: number with trend sparkline; segmented geo-source on hover
    - Data: ePPQ_net_usd_by_geo_source (30d trailing)
  - Card B: Last payout breakdown
    - Visual: stacked bar of components and NovaSonic fee
    - Data: payout_component_breakdown (most recent period)
  - Card C: Where listeners found you
    - Visual: top 3 discovery surfaces by impressions and play rate
    - Data: impression_funnel_by_surface
  - Card D: Governance status
    - Visual: count of active boosts and demotions
    - Data: visibility_governance_flags
  - NEW: Privacy badge appears if any counts suppressed

Earnings transparency section

Panel 1: Net Payout per 1,000 Qualified Plays by Geo and Source
- Visual: heatmap table (rows = geos, columns = monetization sources; cells = USD per 1,000)
- Controls: toggle trailing average 30/60/90 days; absolute vs trend; export
- Drill: click a geo to open line chart of ePPQ over time by source
- Visualises: ePPQ_net_usd_by_geo_source

Panel 2: Revenue Components and Take-Rate per Payout Period
- Visual: table plus stacked bar per period
  - Columns: Period, Ads USD and %, Subscriptions USD and %, Tips USD and %, Bonuses USD and %, NovaSonic fee USD and %, Creator net USD
- Controls: select payout periods; CSV export for accounting
- Constraint: numbers must add up; fee shown in USD and %
- Visualises: payout_component_breakdown

Panel 3: What counts as a qualified play
- Visual: collapsible panel with versioned rules; bullet list of criteria
- Elements: current rules version and effective date; change log accordion; backfill policy note; reclassification banner if applicable
- Visualises: qualified_play_rules
- NEW: timeline annotations in Panels 1 and 2 when rules version changes

Discovery transparency section

Panel 4: Impression source funnel by surface
- Visual: funnel per surface in a grid
  - For each surface: Impressions -> CTR to episode page -> Play rate -> Avg completion %
- Controls: surface multi-select; episode drill-down
- Table view toggle: columns for Impressions, CTR, Play rate, Avg completion %
- Visualises: impression_funnel_by_surface

Panel 5: Recommendation exposure and rank position distribution
- Visual: stacked bar or area chart by rank buckets (1–3, 4–10, 11–20, >20) with dwell-time-weighted exposure
- Facets: per surface; toggle to compare two episodes
- Tooltip: dwell-time weighting explanation
- Visualises: rec_exposure_rank_dist

Panel 6: Why your episode was shown (top factors)
- Visual: horizontal bar list of top 5 feature contributions with normalized percentages
- Controls: episode selector, surface selector; show model version
- Safeguards: suppress panel if threshold not met; show privacy badge
- Visualises: ranking_factor_contributions

Search visibility section

Panel 7: Search queries and ranking performance
- Visual: table with pagination
  - Columns: Search query, Average rank at impression, Impressions, CTR, Plays
- Controls: filter by brand vs generic queries; export; privacy badge when rows suppressed
- Visualises: search_query_rank_perf

Governance and policy section

Panel 8: Boosts and demotions over time
- Visual: timeline with markers; and a table view
  - Table columns: Episode, Flag type (boost, demotion, policy status), Reason code, Start timestamp, End timestamp, Affected surfaces, Current status
- Controls: filter by flag type and surface; export audit log
- Visualises: visibility_governance_flags
- NEW: overlay annotations on Panels 4–6 to show when a flag started or ended

Definitions and audit section

Panel 9: Definitions and audit trail
- Visual: two tabs
  - Tab A: Definitions
    - Qualified play rules (from Panel 3, read-only duplicate)
    - Monetization model description text and link to policy
  - Tab B: Data lineage
    - Source systems per panel, update cadences, job names and last run status
- Visualises: qualified_play_rules plus source references from researcher brief
- NEW: links to API docs and schema

Exports and API section

Panel 10: Downloads and API access
- Visual: list of downloadable datasets honoring current filters
  - ePPQ by geo and source (CSV, JSON)
  - Payout breakdown per period (CSV)
  - Impression funnels by surface (CSV)
  - Rec exposure by rank bucket (CSV)
  - Ranking factor contributions (CSV; thresholds applied)
  - Search queries (CSV; privacy-filtered)
  - Visibility governance flags (CSV)
- Visualises: all above data points
- NEW: token-based API endpoints with rate limits noted

2) PANEL TO DATA POINT TRACEABILITY

- Panel 1: Net Payout per 1,000 Qualified Plays by Geo and Source
  - Data point: ePPQ_net_usd_by_geo_source
- Panel 2: Revenue Components and Take-Rate per Payout Period
  - Data point: payout_component_breakdown
- Panel 3: What counts as a qualified play
  - Data point: qualified_play_rules
- Panel 4: Impression source funnel by surface
  - Data point: impression_funnel_by_surface
- Panel 5: Recommendation exposure and rank position distribution
  - Data point: rec_exposure_rank_dist
- Panel 6: Why your episode was shown (top factors)
  - Data point: ranking_factor_contributions
- Panel 7: Search queries and ranking performance
  - Data point: search_query_rank_perf
- Panel 8: Boosts and demotions over time
  - Data point: visibility_governance_flags
- Panel 9: Definitions and audit trail
  - Data point: qualified_play_rules and source references from the brief
- Panel 10: Downloads and API access
  - Data points: all above, with privacy and threshold rules applied

3) TRANSPARENCY EXPLAINER MICROCOPY (EXAMPLE)

How your payouts are calculated
- You earn based on qualified plays. A qualified play means a listener streamed enough of your episode to meet our current rule. We publish that rule, its version, and any changes here.
- We show your net payout per 1,000 qualified plays (ePPQ) by country and by source like ads or subscriptions. This helps you see what a play is worth in different places.
- Your payout breakdown shows exactly where money came from, how much NovaSonic took as a fee, and your net. No hidden deductions.
- If we ever change how a qualified play is counted or fix invalid traffic, we’ll display the date, the reason, and apply backfills when applicable so your numbers remain consistent.

4) ACCEPTANCE CRITERIA FOR ENGINEERING

Global
- Filters
  - Date range filter applies to all panels except payout_component_breakdown when showing “per payout period” outside the selected date range; provide a toggle “limit to date range”.
  - Scope selector switches aggregation between show-level and episode-level for all panels that support episode breakdown. Default to show-level.
  - Geo, surface, and monetization source filters must be respected by panels that include those dimensions. Inapplicable panels should disable the filter with tooltip “not applicable”.
- Data freshness and version badges (NEW)
  - Each panel displays a last updated timestamp drawn from its source job metadata.
  - Monetization model name and version and recommender model version are displayed where relevant. Values come from configuration services; if unavailable, show “version unavailable” with an info tooltip.
- Performance
  - Each panel must render within 2 seconds for default 30-day range on median data set. Long-running queries provide a loading state and cancel option.

Panel 1: ePPQ_net_usd_by_geo_source
- Shows USD net payout per 1,000 qualified plays by geo and monetization source.
- Includes selectable 30/60/90-day trailing averages; selection defaults to 30 days.
- If a cell has fewer than the privacy threshold qualified plays, display as “—” and show a privacy badge; threshold value is a configurable parameter supplied by the Privacy team.
- Heatmap values must reconcile with payout_component_breakdown over the same period within expected tolerance given timing differences; document any known lags.

Panel 2: payout_component_breakdown
- For each payout period, display absolute USD and % for each component (ads, subscriptions, tips, bonuses), NovaSonic fee (USD and %), and creator net.
- Column totals must equal gross minus fees equals creator net; 100% stacked bars must sum to 100% with rounding tolerance of ±0.5%.
- Support selection of multiple payout periods and export to CSV. CSV must include the same columns and filtered rows.

Panel 3: qualified_play_rules
- Display current rules as published text: required listen threshold, deduplication window, autoplay inclusion, fraud/invalid traffic filters, and backfill policy.
- Display rules version and effective date. If rules version changed within the selected date range, show a banner and annotate Panels 1 and 4 with change markers.
- If a backfill reclassification occurred in range, show a note with the backfill window and link to details.

Panel 4: impression_funnel_by_surface
- For each selected surface, compute and display:
  - Impressions
  - CTR to episode page = clicks to episode page divided by impressions
  - Play rate = plays divided by impressions
  - Average completion percentage for plays attributed to that surface
- Provide grid of mini-funnels and a table view with the same values. All values respect global filters and selected episodes.
- If a surface has zero data in range, hide funnel and show “No data for selected range”.

Panel 5: rec_exposure_rank_dist
- Display dwell-time-weighted exposure counts grouped into rank buckets 1–3, 4–10, 11–20, >20 per selected surface.
- Tooltip must define dwell-time weighting in plain language.
- Provide a compare toggle to overlay two episodes; when active, legend clearly distinguishes episodes.
- If no recommendation exposure exists for a surface, panel shows an empty state.

Panel 6: ranking_factor_contributions
- For selected episode and surface, show the top 5 model feature contributions with normalized percentages that sum to 100% ±2%.
- Do not display raw weights or user-level data. Aggregate across users and requests per Researcher guidance.
- If contributions do not meet privacy or stability thresholds (configurable), suppress panel and show message “Not enough data to explain safely”.
- Display the recommender model version used to generate these contributions.

Panel 7: search_query_rank_perf
- Show a table of queries that produced impressions for the creator’s episodes with:
  - Query string (aggregated and privacy-thresholded)
  - Average rank at impression time
  - Impressions
  - CTR
  - Plays
- Enforce platform privacy thresholds: hide rows that do not meet configured k-anonymity and minimum impression counts; indicate suppression via a badge and a help tooltip.
- Sorting by any column must be supported; default sort by Impressions descending.

Panel 8: visibility_governance_flags
- Table includes for each flag:
  - Episode
  - Flag type (boost, demotion, policy status)
  - Reason code
  - Start timestamp
  - End timestamp or “Active”
  - Affected surfaces
- Timeline view shows markers at start and end times. Hover reveals details.
- Filters for flag type and surfaces must work and update both table and timeline.
- Export produces a CSV with all columns and applied filters.

Panel 9: definitions and audit trail
- Definitions tab mirrors qualified_play_rules text exactly and shows version. Any mismatch between this and Panel 3 is a blocker.
- Data lineage tab shows source systems, update cadences, and last run status for each panel. If metadata is unavailable, display “Status unavailable” and log the missing source.

Panel 10: downloads and API access (NEW)
- Each export option produces a file that exactly matches the on-screen filters and aggregations.
- API endpoints listed with scopes that match the creator’s access. If the API is disabled for an item, show a lock icon and explanatory tooltip.
- All exports must include a header block with:
  - Dataset name
  - Date range
  - Filters applied
  - Rules and model versions
  - Generation timestamp

Cross-cutting integrity and auditability
- All monetary values are in USD and explicitly labeled “net” where net of fees, consistent with Researcher definitions.
- Every panel must display a small “i” tooltip that links to the underlying definition and source systems per the Researcher brief.
- When the qualified play rules or monetization model change, Panels 1–4 show an annotation marker with the effective date.
- Access control: Only authenticated creators with rights to the show can view data. Episode-level selection is restricted to owned episodes.
- Accessibility: All interactive elements reachable via keyboard; provide alt text for charts; minimum color contrast WCAG AA.

Risks and mitigations
- Monetization model ambiguity: the UI must display the current model name and version and provide a link to the policy doc. If the model changes mid-period, show a banner and link to details.
- Gaming risk: ranking_factor_contributions display is limited to high-level, normalized top 5 contributions, with privacy and stability thresholds, and no raw feature values or user-level breakdowns.

## AGENT 3 - COMMUNICATOR
### INPUT (Designer's output handed off):
```
[Business context + full Designer output above]
```
### OUTPUT:
HANDOFF RECEIVED
We are announcing the Creator Trust & Transparency Dashboard exactly as designed, including:
- Global components:
  - Data Freshness and Version Badges (last-updated timestamps; monetization model name/version; qualified play rules version; recommender model version per surface)
  - Export and API Access (CSV/JSON downloads that honor filters; token-based API endpoints with rate limits)
  - Annotations (timeline markers when qualified play rules or visibility governance events change)
  - Privacy-threshold indicator (badge when rows are hidden due to privacy filtering)
- Panels:
  1) Net Payout per 1,000 Qualified Plays by Geo and Source (ePPQ_net_usd_by_geo_source)
  2) Revenue Components and Take-Rate per Payout Period (payout_component_breakdown)
  3) What counts as a qualified play (qualified_play_rules with version and change log)
  4) Impression source funnel by surface (impression_funnel_by_surface)
  5) Recommendation exposure and rank position distribution (rec_exposure_rank_dist)
  6) Why your episode was shown (top factors, aggregated) (ranking_factor_contributions)
  7) Search queries and ranking performance (search_query_rank_perf)
  8) Boosts and demotions over time (visibility_governance_flags)
  9) Definitions and audit trail (definitions; data lineage; links to policy and API docs)
  10) Downloads and API access (filtered exports for all above datasets, with applied privacy thresholds)

---

1) Creator announcement email

Subject: Now live: Creator Trust & Transparency Dashboard

Hi creators,

You’ve told us that payouts, discovery, and data access have felt like a black box. Starting today, you’ll find a new Trust & Transparency Dashboard in Creator Studio that shows how money is calculated, how your episodes are discovered, and the data we use—clearly and in one place.

What’s inside
- Earnings transparency
  - Net payout per 1,000 qualified plays (ePPQ) by country and by monetization source (ads, subscriptions, tips, bonuses).
  - Payout component breakdown for each payout period—including NovaSonic’s fee in USD and %—with CSV export for your accounting.
  - “What counts as a qualified play” with the current rule, version, effective date, and a change log. If rules change, related panels are annotated.
- Discovery transparency
  - Funnels by surface (Home, Personalized Recs, Search, Category, Autoplay, Follows Feed, Editorial, External): impressions → CTR → play rate → average completion.
  - Recommendation exposure by rank bucket (1–3, 4–10, 11–20, >20) with dwell-time weighting, per surface and episode.
  - “Why your episode was shown” (top 5 normalized factor contributions), aggregated for privacy and stability. If thresholds aren’t met, we won’t show unsafe explanations.
- Search visibility
  - Search queries that led to impressions, with average rank, impressions, CTR, and plays (rows suppressed if they don’t meet privacy thresholds).
- Governance and policy
  - Timeline and table of boosts, demotions, and policy status flags with reason codes, timestamps, affected surfaces, and current status.
- Definitions, audit, and access
  - Definitions and data lineage (source systems, update cadences, last-run status).
  - Downloads and API: CSV/JSON exports for each dataset (respecting your on-screen filters), plus token-based API endpoints with documented rate limits.

How it’s made accountable
- Every panel shows a last updated timestamp and the relevant model/rules version.
- Monetary values are in USD and labeled “net” where net of fees.
- We annotate panels when qualified play rules or monetization models change.
- Privacy thresholds are enforced. When rows/cells are hidden, you’ll see a privacy badge and an explanation.
- Explanations of recommendations are aggregated: we show only the top 5 normalized factor contributions and never expose user-level data.

Where to find it
- Creator Studio → Analytics → “Creator Trust & Transparency.”
- Each panel has an “i” tooltip linking to definitions, policies, and data sources. Exports and API docs are listed under “Downloads and API access.”

No marketing gloss—just the facts. If you spot anything unclear, use the feedback link in the dashboard’s header or reply to this email, and we’ll look into it.

Thank you for the push to make NovaSonic more transparent.

—The NovaSonic Team

---

2) In‑app notification (≤280 chars)

New: Creator Trust & Transparency Dashboard. See ePPQ by geo/source, payout breakdown, discovery funnels & rank, top factors (aggregated), search queries, and boosts/demotions—plus data freshness, versions, and CSV/API exports. Open Analytics to explore.

---

3) FAQ (Trust & Transparency)

Q1) How are payouts calculated, and is the NovaSonic fee fully shown?
- You earn based on qualified plays. Panel 3 lists the current qualified play rule, version, and effective date, with a change log.
- Panel 1 shows your net payout per 1,000 qualified plays (ePPQ) by country and by monetization source (ads, subscriptions, tips, bonuses).
- Panel 2 breaks down each payout period: every revenue component in USD and %, NovaSonic’s fee in USD and %, and your net. Totals add up by design; stacked bars sum to 100% (with minor rounding tolerance).
- All monetary values are in USD and labeled “net” where net of fees. If rules or monetization models change, related panels show an annotation with the effective date.
- Notes: Some cells may be “—” if they don’t meet privacy thresholds. Reporting lags are visible via each panel’s “last updated” badge.

Q2) How do I know the recommendation system isn’t biased against me?
- We can’t infer intent from outcomes, but we are exposing how your episodes were surfaced:
  - Panel 5 shows your episode’s exposure by rank bucket per surface, weighted by dwell time.
  - Panel 6 shows the top 5 normalized factor contributions behind why an episode was shown on a given surface and model version. This is aggregated across requests; we never show raw weights or user-level data. If privacy/stability thresholds aren’t met, the panel is suppressed with a clear message.
  - Panel 8 shows boosts/demotions and policy flags with reason codes, start/end times, and affected surfaces.
- Together, these panels let you see where you appeared, how prominently, which high-level factors contributed most, and whether any governance flags affected visibility. If something looks off, use the feedback link in the dashboard.

Q3) What data can I access and download? Are you still “hoarding” listener data?
- You can export or access via API the same aggregated datasets shown on-screen (Panel 10):
  - ePPQ by geo and source (CSV, JSON)
  - Payout breakdown per period (CSV)
  - Impression funnels by surface (CSV)
  - Recommendation exposure by rank bucket (CSV)
  - Ranking factor contributions (CSV; thresholds applied)
  - Search queries and ranking performance (CSV; privacy-filtered)
  - Visibility governance flags (CSV)
- Exports mirror your filters and include a header block with date range, filters, rules/model versions, and generation timestamp. API endpoints are token-based with documented rate limits.
- We do not provide user- or listener-level data. Search queries and explanations are aggregated and subject to privacy thresholds; when data is suppressed, a badge indicates why.

Q4) Can I opt out?
- This launch doesn’t change your monetization or distribution settings. The dashboard is read-only analytics plus exports/API for your own auditing.
- There is no opt-out from being included in standard aggregated analytics or recommendation surfaces. We also don’t expose user-level data.
- You control whether to use exports and API access (they require your token). To pause or remove content from NovaSonic, use your existing account/content settings or contact Support.
- Governance actions (boosts/demotions/policy flags) are not optional, but they’re now visible with reason codes and timestamps in Panel 8.
