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

<style>
/* Whitepaper-specific dense academic formatting */
.quarto-container { max-width: 1400px !important; }
#quarto-margin-sidebar { font-size: 0.85rem !important; }
p, li, td, th { 
  font-size: 0.96rem !important; 
  line-height: 1.4 !important; 
}
.math, mjx-container {
  font-size: 1.04em !important;
}
.math.display, mjx-container[display="true"] {
  font-size: 1.07em !important;
}
pre {
  font-size: 0.81em !important;
}
p > code, li > code {
  font-size: 0.85em !important;
  padding: 0.06em 0.22em !important;
}
</style>

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
