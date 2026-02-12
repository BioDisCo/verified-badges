# verified-badges

Inline badges for formally verified theorems in LaTeX papers. Each badge is a small shield with a checkmark, linking to the proof source.

<p align="center">
  <img src="badges/lean.svg" height="32" alt="Lean">&nbsp;&nbsp;
  <img src="badges/coq.svg" height="32" alt="Coq">&nbsp;&nbsp;
  <img src="badges/rocq.svg" height="32" alt="Rocq">&nbsp;&nbsp;
  <img src="badges/isabelle.svg" height="32" alt="Isabelle">&nbsp;&nbsp;
  <img src="badges/agda.svg" height="32" alt="Agda">&nbsp;&nbsp;
  <img src="badges/hol4.svg" height="32" alt="HOL4">&nbsp;&nbsp;
  <img src="badges/dafny.svg" height="32" alt="Dafny">&nbsp;&nbsp;
  <img src="badges/fstar.svg" height="32" alt="F*">&nbsp;&nbsp;
  <img src="badges/tla.svg" height="32" alt="TLA+">&nbsp;&nbsp;
  <img src="badges/idris.svg" height="32" alt="Idris">&nbsp;&nbsp;
  <img src="badges/pvs.svg" height="32" alt="PVS">
</p>

## Quick start

1. Copy the `badges/` folder and `verified-badges.sty` into your paper directory. PDF versions of each badge are included, so no conversion is needed.
2. Add to your preamble:
   ```latex
   \usepackage{verified-badges}
   ```
3. Use in theorem headers:
   ```latex
   \begin{theorem}[Confluence \leanproof{https://github.com/you/repo/Confluence.lean}]
     ...
   \end{theorem}
   ```

The badge becomes a clickable hyperlink to the proof source.

## Available commands

| Command | Prover |
|---------|--------|
| `\leanproof{url}` | Lean |
| `\coqproof{url}` | Coq |
| `\rocqproof{url}` | Rocq |
| `\isabelleproof{url}` | Isabelle |
| `\agdaproof{url}` | Agda |
| `\holproof{url}` | HOL4 |
| `\dafnyproof{url}` | Dafny |
| `\fstarproof{url}` | F* |
| `\tlaproof{url}` | TLA+ |
| `\idrisproof{url}` | Idris |
| `\pvsproof{url}` | PVS |

There is also a generic command if you need a different badge file:

```latex
\verifiedproof[mybadge]{https://example.com/proof}
```

This looks for `badges/mybadge.pdf`.

## Customization

**Badge size and alignment.** Adjust in your preamble after loading the package:

```latex
\setlength{\badgeheight}{1.2em}   % smaller
\setlength{\badgeraise}{-1pt}     % vertical alignment tweak
```

**Custom colors.** Edit `generate.py` and re-run to produce new SVGs and PDFs (requires `cairosvg`):

```python
provers = {
    "lean": {"name": "Lean", "color": "#2a6e3f"},
    "myprover": {"name": "MyProver", "color": "#aa3366"},
}
```

**Without the .sty file.** If you prefer not to use the package, the minimal LaTeX setup is:

```latex
\usepackage{hyperref}
\usepackage{graphicx}

\newcommand{\leanproof}[1]{%
  \href{#1}{\raisebox{-2pt}{\includegraphics[height=1.2em]{badges/lean}}}%
}
```

## Standalone use (without LaTeX)

The SVGs work anywhere: Markdown, HTML, Typst, etc.

**Markdown / GitHub:**
```markdown
![Lean verified](badges/lean.svg)
```

**HTML:**
```html
<a href="https://github.com/you/repo/Proof.lean">
  <img src="badges/lean.svg" height="18" alt="Verified in Lean">
</a>
```

**Typst:**
```typst
#link("https://github.com/you/repo/Proof.lean")[#image("badges/lean.svg", height: 1.2em)]
```

## Adding a new prover

1. Add an entry to the `provers` dict in `generate.py`
2. Run `python3 generate.py`
3. Convert the new SVG to PDF
4. Add a command in `verified-badges.sty`:
   ```latex
   \newcommand{\myproverproof}[1]{\verifiedproof[myprover]{#1}}
   ```

PRs welcome for additional provers.

## License

The badge designs and LaTeX code are released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (public domain). Use them however you like, no attribution required.

Prover names remain trademarks of their respective projects.
