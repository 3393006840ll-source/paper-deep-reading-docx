---
name: paper-deep-reading-docx
description: Convert numbered Chinese or English academic papers into consistent, evidence-traceable Chinese “研0精读版” Word documents. Use when the user asks to read downloaded literature in order, apply the 研0 literature-reading workflow, extract and condense a paper, create an evidence-traceable reading document, or continue producing a numbered literature set.
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


Always produce the common reading sections. Then enable every applicable method branch. These branches describe research methods rather than a subject-area restriction:


- Numerical simulation: solver, governing/model choices, mesh, time settings, discretization, materials, assumptions, boundary/initial conditions, convergence, validation, and reproducibility gaps.
- Experiment: purpose, apparatus, media, variables, instruments, acquisition, operating matrix, repetitions, uncertainty, procedure, and safety/scale limitations.
- Theory/model: variable definitions, assumptions, derivation chain, dimensional meaning, and valid range.
- Review paper: search scope, classification framework, consensus, disputes, evidence gaps, and future directions.
- Data/AI: dataset, labels, split, features, baseline, metrics, leakage risk, uncertainty, and deployment limits.


For a non-applicable branch, write `不适用` briefly rather than fabricating content.


### 4. Draft in the fixed sequence


Read `references/output-spec.md` and follow its complete section order. Read `references/evidence-rules.md` before drafting tables, formulas, figures, and conclusions.
