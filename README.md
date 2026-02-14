# verified-badges

Inline badges for formally verified theorems in LaTeX papers. Each badge is a small shield with a checkmark, linking to the proof source. Two badge kinds are available:

- **Verified** (green) — the full proof is formalized.
- **Formalized** (blue) — the statement (definition, lemma, theorem, etc.) is formalized, but the proof is not (yet).

<p align="center">
  <img src="badges/lean.svg" height="32" alt="Verified in Lean">&nbsp;&nbsp;
  <img src="badges/coq.svg" height="32" alt="Verified in Coq">&nbsp;&nbsp;
  <img src="badges/rocq.svg" height="32" alt="Verified in Rocq">&nbsp;&nbsp;
  <img src="badges/isabelle.svg" height="32" alt="Verified in Isabelle">&nbsp;&nbsp;
  <img src="badges/agda.svg" height="32" alt="Verified in Agda">&nbsp;&nbsp;
  <img src="badges/hol4.svg" height="32" alt="Verified in HOL4">&nbsp;&nbsp;
  <img src="badges/dafny.svg" height="32" alt="Verified in Dafny">&nbsp;&nbsp;
  <img src="badges/fstar.svg" height="32" alt="Verified in F*">&nbsp;&nbsp;
  <img src="badges/tla.svg" height="32" alt="Verified in TLA+">&nbsp;&nbsp;
  <img src="badges/idris.svg" height="32" alt="Verified in Idris">&nbsp;&nbsp;
  <img src="badges/pvs.svg" height="32" alt="Verified in PVS">
</p>
<p align="center">
  <img src="badges/lean-formalized.svg" height="32" alt="Formalized in Lean">&nbsp;&nbsp;
  <img src="badges/coq-formalized.svg" height="32" alt="Formalized in Coq">&nbsp;&nbsp;
  <img src="badges/rocq-formalized.svg" height="32" alt="Formalized in Rocq">&nbsp;&nbsp;
  <img src="badges/isabelle-formalized.svg" height="32" alt="Formalized in Isabelle">&nbsp;&nbsp;
  <img src="badges/agda-formalized.svg" height="32" alt="Formalized in Agda">&nbsp;&nbsp;
  <img src="badges/hol4-formalized.svg" height="32" alt="Formalized in HOL4">&nbsp;&nbsp;
  <img src="badges/dafny-formalized.svg" height="32" alt="Formalized in Dafny">&nbsp;&nbsp;
  <img src="badges/fstar-formalized.svg" height="32" alt="Formalized in F*">&nbsp;&nbsp;
  <img src="badges/tla-formalized.svg" height="32" alt="Formalized in TLA+">&nbsp;&nbsp;
  <img src="badges/idris-formalized.svg" height="32" alt="Formalized in Idris">&nbsp;&nbsp;
  <img src="badges/pvs-formalized.svg" height="32" alt="Formalized in PVS">
</p>

## Quick start

1. Copy the `badges/` folder and `verified-badges.sty` into your paper directory. PDF versions of each badge are included, so no conversion is needed.
2. Add to your preamble:
   ```latex
   \usepackage{verified-badges}
   ```
3. Use in theorem headers:
   ```latex
   % fully verified proof
   \begin{theorem}[Confluence \leanproof{https://github.com/you/repo/Confluence.lean}]
     ...
   \end{theorem}

   % statement formalized, proof not yet complete
   \begin{lemma}[Diamond \leanformalized{https://github.com/you/repo/Diamond.lean}]
     ...
   \end{lemma}

   % formalized definition
   \begin{definition}[Widget \leanformalized{https://github.com/you/repo/Widget.lean}]
     ...
   \end{definition}
   ```

Each badge becomes a clickable hyperlink to the source.

## Available commands

### Verified (green) — full proof formalized

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

### Formalized (blue) — statement/definition formalized, proof not yet

| Command | Prover |
|---------|--------|
| `\leanformalized{url}` | Lean |
| `\coqformalized{url}` | Coq |
| `\rocqformalized{url}` | Rocq |
| `\isabelleformalized{url}` | Isabelle |
| `\agdaformalized{url}` | Agda |
| `\holformalized{url}` | HOL4 |
| `\dafnyformalized{url}` | Dafny |
| `\fstarformalized{url}` | F* |
| `\tlaformalized{url}` | TLA+ |
| `\idrisformalized{url}` | Idris |
| `\pvsformalized{url}` | PVS |

### Generic commands

For custom badge files:

```latex
\verifiedproof[mybadge]{https://example.com/proof}      % looks for badges/mybadge.pdf
\formalizedstmt[mybadge]{https://example.com/statement}  % same, for formalized statements
```

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
2. Run `python3 generate.py` (install `cairosvg` for PDF output)
3. Add commands in `verified-badges.sty`:
   ```latex
   \newcommand{\myproverproof}[1]{\verifiedproof[myprover]{#1}}
   \newcommand{\myproverformalized}[1]{\formalizedstmt[myprover-formalized]{#1}}
   ```

PRs welcome for additional provers.

## License

The badge designs and LaTeX code are released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (public domain). Use them however you like, no attribution required.

Prover names remain trademarks of their respective projects.
