# 2025.2 Data Visualization Repository Guide

This file is the first document an automation agent should read before making changes in this repository.

Also read [`guideline.md`](guideline.md). It stores the course guideline link and reminds maintainers that repo changes should follow this project guide. If an external `AGENTS.md` or local Codex rule is provided by the runtime, follow it as the higher-priority operating rule.

## Project Purpose

This repository contains the team's 2025.2 Data Visualization project on customer churn. The project combines:

- an English LaTeX report in `pdf/`,
- final dashboard screenshots in `img/` and report-ready copies in `pdf/figures/`,
- a cloned/embedded group workflow in `group_repo/`,
- Phase 2 feature-selection/modeling notebooks and Kaggle outputs,
- course slide extracts and distilled visualization knowledge in `Slide data viz/2024/notes/`.

The raw customer-level dataset is not committed. The project uses the public Kaggle dataset:

- `isandeep06/customer-churn-prediction-dataset-1m`

Some older Phase 2 work also references a private staging dataset:

- `minhhuyen3012nguyen/datavis-customer-churn-phase2`

Use the public Kaggle source as the source of truth when checking dataset provenance in the report.

## Read Order For Agents

1. Read this `readme.md`.
2. Read [`guideline.md`](guideline.md) for the course guideline link.
3. Check `git status --short --untracked-files=all` before editing.
4. Read the files related to the requested task instead of guessing from memory.
5. Preserve existing user changes. Do not revert unrelated changes.
6. After editing, run the smallest useful verification command.
7. Commit only when the user explicitly asks.

## Repository Map

| Path | Purpose |
| --- | --- |
| `pdf/main.tex` | LaTeX report entry point. |
| `pdf/sections/en/` | English report sections. Most report text changes happen here. |
| `pdf/figures/` | Images included in the PDF, copied from final screenshots or generated artifacts. |
| `pdf/main.pdf` | Built report output kept in the repo. |
| `img/` | Final dashboard screenshots used for reporting/presentation. |
| `group_repo/` | Team workflow repo content: Power BI assets, Phase 2 pipelines, Kaggle kernels. |
| `group_repo/phase2/` | Local and Kaggle Phase 2 model scripts. |
| `group_repo/phase2/kaggle_feature_selection_kernel/` | Public-source Kaggle notebook/script for correlation screening and Random Forest feature selection. |
| `group_repo/powerbi_dashboard/` | Power BI input workbook builders, dashboard data tables, and dashboard documentation. |
| `outputs/` | Downloaded Kaggle outputs and generated correlation/model figures. |
| `Slide data viz/2024/` | Course slides and extracted notes. |
| `Slide data viz/2024/notes/00_distilled_knowledge.md` | Condensed visualization knowledge used to improve report/dashboard reasoning. |
| `assets/` | External/reference figure assets used while studying dashboard design. |
| `old_materials/` | Older materials moved out of the active workflow. Avoid editing unless explicitly requested. |

## Current Report Workflow

The report is English and optimized to compile on Overleaf. The main files are:

- `pdf/main.tex`
- `pdf/sections/en/00_title_abstract.tex`
- `pdf/sections/en/01_introduction.tex`
- `pdf/sections/en/02_dataset_workflow.tex`
- `pdf/sections/en/03_feature_selection_grouping.tex`
- `pdf/sections/en/03_repository_and_modeling.tex`
- `pdf/sections/en/04_eda_plan.tex`
- `pdf/sections/en/04_visualization_design_principles.tex`
- `pdf/sections/en/05_technique_application.tex`
- `pdf/sections/en/05_expected_insights.tex`
- `pdf/sections/en/06_limitations_next_steps.tex`

When updating report content:

- keep the report in English,
- keep the dataset source aligned with the public Kaggle slug,
- keep Power BI language cautious if the `.pbix` is still being revised,
- include concrete metrics only if they exist in `outputs/` or `group_repo/powerbi_dashboard/data/`,
- use `pdf/figures/` for images referenced from LaTeX,
- rebuild `pdf/main.pdf` after changing any `.tex` or included figure.

## PDF Build Command

Always build from inside `pdf/`:

```bash
cd pdf
latexmk -pdf main.tex
latexmk -c main.tex
find . -maxdepth 1 -type f \( \
  -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o \
  -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.synctex.gz" -o \
  -name "*.nav" -o -name "*.snm" -o -name "*.vrb" -o \
  -name "*.bbl" -o -name "*.blg" \
\) -delete
```

Expected result: `pdf/main.pdf` exists, and no LaTeX intermediate files remain directly under `pdf/`.

## Dashboard Image Workflow

The active final screenshots are in `img/`:

- `img/pic1.png`
- `img/pic2.png`
- `img/pic3.png`

The report uses copies in `pdf/figures/`:

- `pdf/figures/dashboard_overview.png`
- `pdf/figures/dashboard_drivers.png`
- `pdf/figures/dashboard_prediction.png`

If the user updates `img/`, inspect the images first, then copy/rename the report versions into `pdf/figures/`, update captions or discussion in `pdf/sections/en/04_visualization_design_principles.tex`, and rebuild the PDF.

## Phase 2 Modeling Workflow

The project uses Phase 2 modeling as support for retention prioritization, not as a perfect churn classifier. Important files:

- `group_repo/phase2/phase2_pipeline.py`
- `group_repo/phase2/kaggle_kernel/phase2_pipeline.py`
- `group_repo/phase2/kaggle_kernel/run_phase2.py`
- `group_repo/phase2/kaggle_feature_selection_kernel/feature_selection_phase2.py`
- `group_repo/phase2/kaggle_feature_selection_kernel/feature_selection_phase2.ipynb`

Key output folders:

- `outputs/kaggle/phase2_correlation_20260612_0351/`
- `outputs/kaggle/top10_rf_20260612/`
- `outputs/kaggle/top16_rf_20260612/`
- `outputs/kaggle/model_compare_20260612/`
- `outputs/kaggle/all_features_20260612/`
- `outputs/figures/`

Current interpretation to preserve unless new evidence replaces it:

- the churn class is imbalanced,
- accuracy alone is not the main metric,
- precision/recall/F1/ROC-AUC/PR-AUC should be discussed together,
- grouped dashboard features are useful for explanation but can lose raw numeric signal,
- correlation is only a univariate screening signal, not proof of causality,
- churn-only data cannot train a binary churn classifier because the target has one class.

## Power BI Workflow

Active Power BI-related files live under `group_repo/powerbi_dashboard/`:

- `DataVis_PowerBI_Input.xlsx`
- `build_powerbi_pack.py`
- `build_powerbi_excel_input.py`
- `docs/`
- `data/`

The final `.pbix` currently lives at:

- `group_repo/dashboard_final.pbix`

If editing the report while the dashboard is still changing, avoid claiming the dashboard is fully final unless the user says so. If the user explicitly says `/img` is the final reporting version, use those screenshots as the report source.

## Python And Dependency Rules

When running Python in this repo, prefer:

```bash
uv run ...
```

Do not use bare `python` unless there is a clear reason. For quick syntax checks:

```bash
uv run python -m py_compile <file.py>
```

If creating a new Python environment, use `uv` and Python 3.10 unless the user specifies another version.

## Kaggle Notes

For Kaggle notebook push/run tasks:

- do not commit Kaggle credentials,
- do not print secrets,
- use temporary staging for generated Kaggle metadata when possible,
- keep downloaded result summaries under `outputs/kaggle/`,
- summarize metrics in Markdown/CSV/JSON so the report can cite them.

The repo may contain generated Kaggle outputs, but credentials must never be committed.

## Change Checklist

Before ending a task:

- Run `git status --short --untracked-files=all`.
- If code changed, run a relevant syntax/test command.
- If `.tex` or report figures changed, rebuild `pdf/main.pdf` and clean LaTeX intermediates.
- If only root documentation changed, PDF rebuild is normally `N/A`.
- Check that no `.zip`, `.env`, credentials, or local scratch files are staged.
- Report what changed and what was verified.

Before committing:

- Commit only if the user asks.
- Use Conventional Commits, for example `docs(repo): add agent guide`.
- Review staged files with `git diff --cached --stat`.
- Confirm the working tree after commit.

## Common Task Patterns

### Update Report Text

1. Edit the relevant file in `pdf/sections/en/`.
2. Keep claims tied to available outputs or screenshots.
3. Rebuild `pdf/main.pdf`.
4. Clean LaTeX intermediates.

### Add Or Replace Dashboard Screenshots

1. Inspect `img/`.
2. Copy final images into `pdf/figures/` with stable names.
3. Update the report figure captions/discussion.
4. Rebuild `pdf/main.pdf`.

### Add Model Results

1. Read the relevant `outputs/kaggle/.../SUMMARY.md`, metrics JSON, or summary CSV.
2. Update `pdf/sections/en/03_repository_and_modeling.tex` or `06_limitations_next_steps.tex`.
3. Avoid overclaiming performance. For imbalanced churn data, discuss recall, precision, F1, ROC-AUC, and PR-AUC.
4. Rebuild `pdf/main.pdf`.

### Update Group Workflow

1. Read `group_repo/README.md`.
2. Update scripts under `group_repo/phase2/` or `group_repo/powerbi_dashboard/`.
3. Run a targeted `uv run python -m py_compile ...` or script dry run.
4. Update `group_repo/README.md` if commands, features, or outputs changed.

## Files To Avoid Unless Asked

- `old_materials/`: archive/history.
- raw downloaded datasets if present locally.
- `.pbix` internals: treat as binary and only replace when the user supplies/requests it.
- `.zip` files: ignored and usually not committed.
