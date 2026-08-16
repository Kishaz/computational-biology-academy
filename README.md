# Bioinformatics for Molecular Biology — Tutorials

Hands-on, beginner-friendly tutorials that guide scientists and students into the
**bioinformatics analysis of molecular data** — one small, verifiable step at a time.

No prior programming experience is assumed. If you have a biology background and a
willingness to practise, these tutorials meet you where you are.

**Live site → <https://kishaz.github.io/bioinformatics-tutorials/>**

## What you'll learn

This is a practical, growing series. Instead of dense theory, each module walks you
through real, copy-and-run steps — and shows you how to confirm each one actually
worked.

**Available now — Module 01: Set up your bioinformatics environment.** By the end
of it, you'll be able to:

- Get a proper Unix/Linux command line on your own machine — **Ubuntu via WSL2 on
  Windows**, or the built-in **Terminal on macOS** (both covered, including the
  Apple Silicon quirks).
- Install and manage scientific software cleanly with **Conda (Miniforge)** and the
  **Bioconda** / **conda-forge** channels — no more "it won't install" rabbit holes.
- Create **isolated, reproducible environments** and rebuild them from a file — the
  single habit that keeps real analyses trustworthy and shareable.

**Also available — Module 02: An introduction to R for biologists.** What R is and
why it's useful in biology, installing it via Conda, running it both interactively
(the console) and from the command line (`Rscript`), and installing packages from
**CRAN** and **Bioconductor**.

Beyond these, the series grows toward the everyday skills for working with molecular
data — from getting comfortable on the command line through to running real analysis
pipelines. New modules appear on the live site (and in the list below) as they're
ready.

## Who it's for

- Wet-lab biologists and students moving into computational analysis.
- **Windows and macOS** users who need a working environment for bioinformatics tools.
- Anyone who prefers clear, reproducible, do-it-yourself demos over dense theory.

## How the tutorials work

- **You follow along by typing.** These skills stick through practice, not reading.
- Watch for the callout boxes: ✅ **Check** (confirm a step worked), ⚠️ **Verify**
  (something that changes over time — confirm against current docs), and
  🧰 **Troubleshooting** (common errors and how to get unstuck).
- **This is a guided start, not the last word.** The tutorials get you moving;
  genuine comfort comes from your own practice and from the official documentation
  each module points you to.

> ⚠️ **Accuracy note:** Bioinformatics tooling changes fast. Every version number
> here is an **example** — verify commands against each tool's current official
> documentation, and pin versions in your own work.

## Modules

| # | Module |
|---|--------|
| 01 | [Environment Setup — Windows (WSL/Ubuntu) & macOS + Conda](modules/01-setup-environment/index.qmd) |
| 02 | [An Introduction to R for Biologists](modules/02-r-for-biologists/index.qmd) |
| 03 | [A Field Guide to Molecular Data Types](modules/03-molecular-data-types/index.qmd) |
| 04 | [The Command Line — Essential Commands](modules/04-command-line-essentials/index.qmd) |
| 05 | [Reads & Quality Control](modules/05-reads-and-quality-control/index.qmd) |

*New modules are added here as they're completed. "Watch" the repository on GitHub
to be notified when they land.*

## Feedback & corrections

Spotted an out-of-date command or a mistake? Please
[open an issue](https://github.com/Kishaz/bioinformatics-tutorials/issues) — accuracy
is the priority of this project, so corrections are genuinely appreciated.

## Building the site locally (private preview)

These tutorials are built with [Quarto](https://quarto.org), so you can write and
**preview everything privately on your own machine** before anything goes public.

1. Install Quarto — see the [official get-started guide](https://quarto.org/docs/get-started/).
   (On macOS with Homebrew: `brew install --cask quarto`.)
2. From the repository root, run a **live, local-only preview** — it opens in your
   browser at a `localhost` address and is visible only to you:

   ```bash
   quarto preview
   ```

3. To build the static site into the `_site/` folder without serving it:

   ```bash
   quarto render
   ```

`_site/` is the generated output and is **git-ignored** — it is never committed.

### Local vs. public — what's private and what isn't

- `quarto preview` / `quarto render` run **entirely on your computer**. Nothing is
  uploaded or published by these commands.
- The site only becomes public when you **`git push` to the `main` branch**: a
  GitHub Actions workflow (`.github/workflows/publish.yml`) then rebuilds the site
  and deploys it to GitHub Pages at the live URL above.
- So your normal workflow is: **edit → `quarto preview` privately → commit → push
  (which publishes)**. If you never push, your changes stay local.

> ⚠️ **Verify:** Quarto's install steps and CLI can change between releases; if a
> command behaves differently, check the current Quarto documentation.

Notes on the project layout and how modules are put together live in
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

© 2026 Samuel Mwamburi.

Licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)** — see
[`LICENSE`](LICENSE). In plain terms: you're free to share and adapt this material,
including for your own teaching, **as long as you credit Samuel Mwamburi** and note
any changes. Full terms: <https://creativecommons.org/licenses/by/4.0/>.
