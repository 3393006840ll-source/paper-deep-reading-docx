---
name: paper-deep-reading-docx
description: Convert numbered Chinese or English academic papers, especially oil-and-gas storage/transport, multiphase flow, CFD, experiments, flow measurement, and engineering papers, into consistent Chinese “研0精读版” Word documents. Use when the user asks to read downloaded literature in order, apply the 研0 literature-reading prompt workflow, extract and condense a paper, create an evidence-traceable reading document, or continue producing the numbered literature set.
---

# 研0文献精读文档

Create one polished Chinese Word document per paper. Preserve the source number and title, distinguish source facts from explanation and critique, and make every important claim traceable to the paper.

## Required supporting skills

1. Read the PDF skill before extracting or visually inspecting a paper PDF.
2. Read the documents skill before creating or modifying the Word output.
3. If the final document must persist, follow the active workspace's file-saving rules.

## Workflow

### 1. Resolve the next paper

- Sort papers by their three-digit filename prefix.
- Continue from the first unfinished number; do not renumber gaps.
- Use one output file per paper.
- Name it `<编号>_<原题名>_研0精读版.docx`.
- Never overwrite an existing completed document unless the user asks for a revision.

### 2. Establish the evidence base

- Confirm that the PDF opens and record its total pages.
- Extract page-separated text with `scripts/extract_pdf_evidence.py`.
- Render every source page when figures, tables, equations, scans, or extraction errors may matter.
- Inspect the title page, methods, results, conclusion, and every cited figure/table.
- Treat the paper as the only factual source unless the user explicitly authorizes external research.
- Record bibliographic data, headings, methods, operating conditions, numerical results, figure/table meanings, limitations, and missing information.

Use these evidence labels consistently:

- `论文明确支持` — directly locatable in the source.
- `研0理解` — a plain-language explanation or reasonable interpretation.
- `论文未说明` — required information is absent.
- `批判性判断` — an evaluation based on evidence completeness, not an author claim.

Never invent equations, parameters, instrument accuracy, mesh settings, uncertainty, conclusions, or applicability.

### 3. Classify the paper and enable branches

Always produce the common reading sections. Then enable every applicable method branch:

- CFD/numerical simulation: solver, governing/model choices, mesh, time settings, discretization, materials, assumptions, boundary/initial conditions, convergence, validation, and reproducibility gaps.
- Experiment: purpose, apparatus, media, variables, instruments, acquisition, operating matrix, repetitions, uncertainty, procedure, and safety/scale limitations.
- Theory/model: variable definitions, assumptions, derivation chain, dimensional meaning, and valid range.
- Review paper: search scope, classification framework, consensus, disputes, evidence gaps, and future directions.
- Data/AI: dataset, labels, split, features, baseline, metrics, leakage risk, uncertainty, and deployment limits.

For a non-applicable branch, write `不适用` briefly rather than fabricating content.

### 4. Draft in the fixed sequence

Read `references/output-spec.md` and follow its complete section order. Read `references/evidence-rules.md` before drafting tables, formulas, figures, and conclusions.

Minimum content requirements:

- five-minute screening decision;
- complete reading and research logic;
- applicable method-specific analysis;
- equation/model and figure/table interpretation;
- important results ranked by importance;
- innovation, limitations, critical evaluation, and course/research relevance;
- a 2,000–3,000 Chinese-character deep condensed version;
- 50-character, 150-character, and about-500-character summaries;
- literature card, three-minute oral report, and review-ready formal paragraph;
- final hallucination and evidence audit.

### 5. Attach evidence

- Put `原文 p.X`, `第 X 节`, `图 X`, or `表 X` beside every important number or conclusion.
- For a PDF whose printed page differs from its file page, prefer the printed page and mention the file page once in the evidence note.
- When exact location cannot be established, weaken the wording and mark `位置待人工复核`.
- Clearly separate author-stated limitations from inferred limitations.
- Do not convert qualitative comparisons into quantitative superiority.

### 6. Build the Word document

- Use a compact academic-reference design: restrained blue accent, white background, readable Chinese type, fixed-width tables, header with series/number/short title, and page number footer.
- Start with an editorial cover containing metadata and a reading recommendation.
- Use real Word heading styles and real bullets.
- Repeat table headers across pages.
- Prevent table rows from splitting across pages.
- Keep each section heading with at least one following paragraph or table row.
- Use one-inch margins unless content or locale requires otherwise.
- Leave document author metadata blank.

When the environment lacks a Chinese font, install or embed an available CJK font before rendering. Never deliver a document with blank glyphs or substituted boxes.

### 7. Verify

1. Run `scripts/audit_docx.py <output.docx>`.
2. Render the Word document to page images using the documents skill.
3. Inspect every rendered page at readable resolution.
4. Fix clipped text, blank glyphs, broken tables, split rows, orphan headings, overflow, bad page breaks, or excessive empty pages.
5. Re-render and re-inspect after every layout change.

Do not deliver the source PDF, temporary extraction, rendered PNGs, or audit logs unless requested. Deliver only the completed Word document.

## Batch continuation

After one paper passes both evidence and visual QA, mark it complete and move to the next numbered paper with this same workflow. Reuse the structure and styling, but rebuild the content from the new paper; never carry over facts, values, figure numbers, or conclusions from an earlier paper.

If a source is corrupted, incomplete, image-only without usable OCR, or missing, record the blocker against that number and continue with the next available paper unless the user requests a stop.
