# The Computational Biology Academy

**Learn computational biology by solving biological questions, not by memorizing
commands.**

A free, open course that teaches computational biology through stories, real datasets,
and hands-on projects. No command memorizing. No walls of text. Just curiosity, from
FASTQ to publication.

**Live site → <https://kishaz.github.io/computational-biology-academy/>**

## What makes it different

Most resources teach you the software. This one teaches you how to *think* like a
computational biologist. Every module is a complete story with the same shape:

1. Start with a mystery (a real question a scientist faces).
2. Think first, before any commands.
3. A plain-language story that makes the idea click.
4. Then, and only then, the commands.
5. What just happened, common mistakes, a mini challenge, and one key takeaway.

You learn alongside four recurring characters: **Amina** (the curious scientist, that is
you), **Pendo** (the PhD student), **Baraka** (the programmer), and **Prof. Zola** (the
impossible PI). Real tools, real data, real judgment.

## Modules

| # | Module | What you solve |
|---|--------|----------------|
| 01 | [Build Your Dry Lab Bench](modules/01-setup-environment/index.qmd) | Set up a Unix shell and Conda so every later experiment just works |
| 02 | [A Language for Asking Questions](modules/02-r-for-biologists/index.qmd) | Speak R to your data: install it, run it, and plot with it |
| 03 | [A Field Guide to Your Data](modules/03-molecular-data-types/index.qmd) | Recognise every kind of molecular data and where to find it |
| 04 | [Talking to Computers](modules/04-command-line-essentials/index.qmd) | Ask a machine politely: the essential command line |
| 05 | [Is This Data Any Good?](modules/05-reads-and-quality-control/index.qmd) | Check and clean raw sequencing reads with FastQC and fastp |

*New modules are added as they are ready. "Watch" the repository on GitHub to be notified
when they land.*

## Built with

The site is a [Quarto](https://quarto.org) website, published to GitHub Pages. To preview
it privately on your own machine:

```bash
quarto preview
```

Nothing is published until you push to the `main` branch, which triggers the deploy
workflow in `.github/workflows/`. Notes on the layout and how modules are written live in
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Feedback and corrections

Spotted a mistake or an out-of-date command? Please
[open an issue](https://github.com/Kishaz/computational-biology-academy/issues). Accuracy
is a priority here, so corrections are genuinely appreciated.

## License

© 2026 Samuel Mwamburi.

Licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**, see
[`LICENSE`](LICENSE). You are free to share and adapt this material, including for your
own teaching, as long as you credit Samuel Mwamburi and note any changes. Full terms:
<https://creativecommons.org/licenses/by/4.0/>.
