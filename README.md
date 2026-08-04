# paper-deep-reading-docx

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/3393006840ll-source/paper-deep-reading-docx?display_name=tag)](https://github.com/3393006840ll-source/paper-deep-reading-docx/releases)

A Codex skill for turning numbered academic papers into evidence-traceable Chinese reading documents in Word.

## 中文

### 定位

`paper-deep-reading-docx` 将按编号整理的中英文论文，尤其是油气储运、多相流、CFD、实验、流量测量和工程类文献，转换为结构统一、证据可追溯的中文“研0精读版”Word 文档。

### 安装

将完整仓库目录放入 Codex 的 skills 目录。不要只复制 `SKILL.md`，因为 `agents/`、`assets/`、`references/` 和 `scripts/` 均为 Skill 的组成部分。

```bash
git clone https://github.com/3393006840ll-source/paper-deep-reading-docx.git
cd paper-deep-reading-docx
python -m pip install -r requirements.txt
```

然后将目录放置到：

`C:/Users/<用户名>/.codex/skills/paper-deep-reading-docx`

或：

`~/.codex/skills/paper-deep-reading-docx`

### 快速使用

在 Codex 中调用：

```text
$paper-deep-reading-docx
```

示例：

```text
使用 $paper-deep-reading-docx，按文件名前的三位编号精读论文，为每篇生成中文 Word 文档，并保留原文页码、图表和证据位置。
```

使用前请准备论文 PDF，并启用 PDF 处理和 Word 文档处理相关 Skill。

### 工作流程

1. 按三位编号确定顺序，不重编号、不覆盖已完成文档。
2. 提取按页分隔的 PDF 文本，并在必要时检查原始页面、公式、图和表。
3. 按固定结构生成 `<编号>_<原题名>_研0精读版.docx`。
4. 运行结构审计，并完成 Word 渲染后的逐页视觉检查。

### 证据标签

| 标签 | 含义 |
| --- | --- |
| `论文明确支持` | 原文文字、公式、图、表或数据直接支持。 |
| `研0理解` | 面向学习者的解释或合理解读。 |
| `论文未说明` | 原文未提供、但复现或评价需要的信息。 |
| `批判性判断` | 基于证据完整性或研究设计作出的评价。 |

### 验证

```bash
python scripts/extract_pdf_evidence.py <paper.pdf> <evidence.txt>
python scripts/audit_docx.py <output.docx>
```

结构审计不能替代逐页视觉检查；正式交付前仍需确认字体、表格、分页、公式和图表没有排版问题。

### 仓库结构

```text
SKILL.md
agents/openai.yaml
assets/icon.svg
references/evidence-rules.md
references/output-spec.md
scripts/audit_docx.py
scripts/extract_pdf_evidence.py
examples/README.md
```

### 原则

- 论文是默认事实来源；外部研究须得到明确授权。
- 不虚构公式、参数、精度、网格、样本量、不确定度、结论或适用范围。
- 每个重要数字和结论都应带有页码、章节、图号或表号。
- 明确区分作者结论、通俗解释和批判性判断。

### 反馈

请通过 [Issues](https://github.com/3393006840ll-source/paper-deep-reading-docx/issues) 提交可复现的问题、功能建议或文档改进意见。请勿上传私人、机密或受版权保护的论文原文件。

## English

### Purpose

`paper-deep-reading-docx` is a Codex skill that converts numbered Chinese or English academic papers—especially oil and gas storage and transportation, multiphase flow, CFD, experimental, flow-measurement, and engineering papers—into consistent, evidence-traceable Chinese reading documents in Word.

### Installation

Copy the complete repository into your Codex skills directory. Do not copy only `SKILL.md`: `agents/`, `assets/`, `references/`, and `scripts/` are part of the Skill bundle.

```bash
git clone https://github.com/3393006840ll-source/paper-deep-reading-docx.git
cd paper-deep-reading-docx
python -m pip install -r requirements.txt
```

Place the directory at `C:/Users/<username>/.codex/skills/paper-deep-reading-docx` or `~/.codex/skills/paper-deep-reading-docx`.

### Quick start

Invoke the Skill in Codex with:

```text
$paper-deep-reading-docx
```

Example:

```text
Use $paper-deep-reading-docx to read papers in three-digit filename order, create one Chinese Word document per paper, and retain source pages, figures, tables, and evidence locations.
```

Provide the source PDFs and enable the PDF-processing and Word-document Skills required by the workflow.

### Workflow

1. Resolve the order from the three-digit filename prefix; do not renumber or overwrite completed outputs.
2. Extract page-separated PDF text and inspect source pages, equations, figures, and tables when needed.
3. Generate `<number>_<original-title>_研0精读版.docx` using the fixed document structure.
4. Run the structural audit and complete a page-by-page visual inspection of the rendered Word document.

### Evidence labels

| Label | Meaning |
| --- | --- |
| `论文明确支持` | Directly supported by source text, equations, figures, tables, or data. |
| `研0理解` | A learner-oriented explanation or reasonable interpretation. |
| `论文未说明` | Not reported in the paper but required for reproduction or evaluation. |
| `批判性判断` | An evaluation based on evidence completeness or study design. |

### Validation

```bash
python scripts/extract_pdf_evidence.py <paper.pdf> <evidence.txt>
python scripts/audit_docx.py <output.docx>
```

A structural audit does not replace visual QA. Before delivery, check fonts, tables, pagination, equations, and figures page by page.

### Repository contents

```text
SKILL.md
agents/openai.yaml
assets/icon.svg
references/evidence-rules.md
references/output-spec.md
scripts/audit_docx.py
scripts/extract_pdf_evidence.py
examples/README.md
```

### Principles

- Treat the paper as the default factual source; use external research only when explicitly authorized.
- Never invent equations, parameters, accuracy, mesh settings, sample sizes, uncertainty, conclusions, or applicability limits.
- Attach a page, section, figure, or table reference to every important number and conclusion.
- Clearly separate author claims, plain-language explanations, and critical judgments.

### Feedback

Please use [Issues](https://github.com/3393006840ll-source/paper-deep-reading-docx/issues) for reproducible bugs, focused feature requests, or documentation improvements. Do not upload private, confidential, or copyrighted source papers.
