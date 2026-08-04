# Usage Examples

These examples are prompt patterns for `paper-deep-reading-docx`. They describe the expected workflow without inventing findings from any paper.

## Prerequisites

- Clone the complete repository and install the helper-script dependencies:
  `python -m pip install -r requirements.txt`
- Prepare the source PDF files.
- Enable the PDF-processing and Word-document skills required by the Codex workflow.
- Keep completed outputs in a separate directory from the source PDFs.

## Example 1: Single-paper reading

Use a prompt like:

```text
使用 $paper-deep-reading-docx，精读这篇 PDF。先确认论文页数和证据位置，再按固定结构生成中文研0精读版 Word 文档。每个重要数字、公式、图表和结论都要标注原文页码、章节、图号或表号；无法确认的位置标记“位置待人工复核”。不要引用外部资料，不要覆盖已有完成文档。
```

Expected behavior:

1. Establish a page-separated evidence base.
2. Classify the paper and enable only applicable method branches.
3. Generate `<编号>_<原题名>_研0精读版.docx`.
4. Run the structural audit and complete page-by-page visual QA.

## Example 2: Numbered batch reading

Use a prompt like:

```text
使用 $paper-deep-reading-docx，按文件名前的三位编号处理这个目录中的论文。跳过缺失或损坏的编号并记录阻塞原因；从第一个未完成编号继续；不要重编号、不要覆盖已完成文档。每篇完成证据审计和 Word 逐页视觉检查后，再处理下一篇。
```

## Evidence labels

Use these labels consistently:

- `论文明确支持`: directly locatable in the source.
- `研0理解`: learner-oriented explanation or reasonable interpretation.
- `论文未说明`: needed for reproduction or evaluation but absent from the paper.
- `批判性判断`: evaluation based on evidence completeness or study design.

## Validation checklist

- [ ] The PDF opens and its page count is recorded.
- [ ] Important numbers and conclusions have source locations.
- [ ] Non-applicable branches are marked `不适用`, not filled with guesses.
- [ ] `python scripts/audit_docx.py <output.docx>` passes.
- [ ] The rendered Word document has been inspected page by page.
- [ ] No source PDF, temporary extraction, rendered image, or audit log is committed.

For a complete section order and evidence policy, see [the output specification](../references/output-spec.md) and [the evidence rules](../references/evidence-rules.md).
