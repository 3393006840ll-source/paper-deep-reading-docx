# paper-deep-reading-docx

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/3393006840ll-source/paper-deep-reading-docx?display_name=tag)](https://github.com/3393006840ll-source/paper-deep-reading-docx/releases)

A Codex skill for turning numbered Chinese or English academic papers into structured, evidence-traceable Chinese Word reading documents.

## 中文

### 定位

`paper-deep-reading-docx` 将按编号整理的中文或英文论文转换为结构统一、证据可追溯的中文“研0精读版” Word 文档，帮助研究者系统梳理文献内容、研究方法、证据与局限。它不限定具体学科或研究对象，会根据论文类型启用适用的方法分析分支。

### 安装

克隆仓库并安装 Python 依赖：

```bash
git clone https://github.com/3393006840ll-source/paper-deep-reading-docx.git
cd paper-deep-reading-docx
python -m pip install -r requirements.txt
```

将完整仓库目录放入 Codex 的 skills 目录。不要只复制 `SKILL.md`，因为 `agents/`、`assets/`、`references/` 和 `scripts/` 都是 Skill 的组成部分。

- Windows：`C:/Users/<用户名>/.codex/skills/paper-deep-reading-docx`
- macOS/Linux：`~/.codex/skills/paper-deep-reading-docx`

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

### 验证

```bash
python -m compileall scripts
python scripts/extract_pdf_evidence.py <paper.pdf> <evidence.txt>
python scripts/audit_docx.py <output.docx>
python scripts/audit_docx.py --help
python scripts/extract_pdf_evidence.py --help
```

结构审计不能替代逐页视觉检查；正式交付前仍需确认字体、表格、分页、公式和图表没有排版问题。

### 证据标签

| 标签 | 含义 |
| --- | --- |
| `论文明确支持` | 原文文字、公式、图、表或数据直接支持。 |
| `研0理解` | 面向学习者的解释或合理解读。 |
| `论文未说明` | 原文未提供、但复现或评价需要的信息。 |
| `批判性判断` | 基于证据完整性或研究设计作出的评价。 |

### 原则

- 论文是默认事实来源；外部研究须得到明确授权。
- 不虚构公式、参数、精度、网格、样本量、不确定度、结论或适用范围。
- 每个重要数字和结论都应带有页码、章节、图号或表号。
- 具体方法分支仅在论文适用时启用，不适用的分支简要标记为“不适用”。

更多示例见 [`examples/README.md`](examples/README.md)，问题与建议请提交到 [Issues](https://github.com/3393006840ll-source/paper-deep-reading-docx/issues)。

## English

### Overview

`paper-deep-reading-docx` converts numbered Chinese or English academic papers into structured, evidence-traceable Chinese Word reading documents. It helps researchers organize findings, methods, evidence, and limitations without restricting the project to a particular discipline or research object.

### Installation

Clone the repository and install the Python dependencies:

```bash
git clone https://github.com/3393006840ll-source/paper-deep-reading-docx.git
cd paper-deep-reading-docx
python -m pip install -r requirements.txt
```

Copy the complete repository directory into the Codex skills directory. Do not copy only `SKILL.md`; the `agents/`, `assets/`, `references/`, and `scripts/` directories are part of the Skill.

- Windows: `C:/Users/<username>/.codex/skills/paper-deep-reading-docx`
- macOS/Linux: `~/.codex/skills/paper-deep-reading-docx`

### Quick start

Invoke it in Codex:

```text
$paper-deep-reading-docx
```

Example:

```text
Use $paper-deep-reading-docx to read numbered papers in order, create one Chinese Word document per paper, and preserve source pages, figures, tables, and evidence locations.
```

Prepare the paper PDFs and enable the PDF and Word document processing skills before use.

### Verification

```bash
python -m compileall scripts
python scripts/extract_pdf_evidence.py <paper.pdf> <evidence.txt>
python scripts/audit_docx.py <output.docx>
python scripts/audit_docx.py --help
python scripts/extract_pdf_evidence.py --help
```

Structural auditing does not replace page-by-page visual inspection. Before delivery, check fonts, tables, pagination, formulas, and figures in the rendered Word document.

See [`examples/README.md`](examples/README.md) for usage patterns and use [Issues](https://github.com/3393006840ll-source/paper-deep-reading-docx/issues) for feedback.
