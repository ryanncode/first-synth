import sys

input_file = 'whitepaper.md'
output_file = 'whitepaper.qmd'

frontmatter = """---
title: "Acyclic by Design: Interaction Nets for Non-Well-Founded Sets"
format:
  html:
    toc: true
    toc-depth: 3
    toc-title: "Contents"
    number-sections: false
---

:::{style="margin-top: 2rem; margin-bottom: 3rem; text-align: center;"}
<a href="whitepaper.pdf" class="btn-primary" style="display: inline-block; padding: 1rem 2rem; font-weight: 600;" target="_blank">Download Full PDF Version</a>
:::

"""

with open(input_file, 'r') as f:
    content = f.read()

# The markdown document already starts with "# Acyclic by Design...", so we can just append it.

js_script = """
<script>
document.addEventListener("DOMContentLoaded", function() {
  const refs = document.getElementById('references');
  const appendix = document.getElementById('quarto-appendix');
  if (refs && appendix) {
    refs.parentNode.insertBefore(appendix, refs);
  }
});
</script>
"""

with open(output_file, 'w') as f:
    f.write(frontmatter + content + "\n" + js_script)

print("Whitepaper successfully generated.")
