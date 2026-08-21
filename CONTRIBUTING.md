# Contributing

Thanks for helping build **The Computational Biology Academy**. The guiding
principle is **accuracy over polish**: a clear, correct, verifiable step beats an
impressive but wrong one. The second principle is the whole point of the Academy:
teach people to solve biological questions, not to memorize commands.

## The Academy model (read this first)

Every module is a **complete, self-contained story**, not a tiny snippet and not a
wall of text. Follow this shape:

1. 🧩 **Start with a mystery.** A real situation a scientist faces (a PI drops data
   on your desk and asks a question).
2. 🤔 **Think first.** Ask the reader a question before showing any commands.
3. 💬 **Story.** A plain-language analogy that makes the idea click.
4. 🛠 **Let's do it.** Only now, the commands.
5. 🎉 **What just happened.** Explain the result in one clear idea.
6. 🚧 **Common mistake.** What beginners get wrong, and why.
7. 🧩 **Mini challenge** plus a short, ungraded self-quiz.
8. 🎯 **Key takeaway.** One sentence. End with a "Go make coffee ☕" sign-off.

**Hard style rules:**

- **No em-dashes. Ever.** Use commas, periods, colons, or parentheses.
- Short sentences. Teach **why before how**. Draw or use a box instead of a
  paragraph where you can.
- Say **"publication"**, not "Nature".
- Recurring characters: **Amina** (the curious scientist, the reader's avatar),
  **Pendo** (the PhD student), **Baraka** (the programmer), **Prof. Zola** (the
  impossible PI).
- Use the branded boxes (defined in `styles.css`, they auto-label themselves, so do
  not repeat the label inside):
  `::: {.think}`, `::: {.story}`, `::: {.mistake}`, `::: {.takeaway}`,
  `::: {.reality}`, `::: {.insight}`, `::: {.didyouknow}`, `::: {.challenge}`.
- Keep all technical content **complete and accurate**. Preserve real commands and
  real captured output verbatim. The accuracy rules below still apply in full.

The gold-standard example is `modules/05-reads-and-quality-control/index.qmd`.

## Ground rules for content

1. **Don't state guesses as facts.** If you're unsure whether a command, flag, or
   function exists in the current version, say so and add a **⚠️ Verify** callout
   pointing to the official documentation.
2. **Don't invent** tool names, function names, version numbers, paper titles,
   author names, or URLs. If you can't point to a real, verifiable source, don't
   cite one.
3. **Treat version numbers as examples.** Prefer telling readers *how to find* the
   current version (`conda search`, official docs) over hard-coding one that will
   go stale.
4. **Flag anything that changes over time**, installation methods, licensing,
   channel configuration, API syntax, with a **⚠️ Verify** note.
5. **Keep it beginner-friendly.** Assume no prior programming experience. Explain
   *why*, not just *what*. Show how to check that a step worked (✅ **Check**).

## Voice & tone style guide (applies to every module)

These tutorials teach nervous beginners. The tone is as important as the accuracy.

1. **Open every topic with a gentle introduction.** Before any commands, include a
   short, warm intro that (a) says what the topic is in plain language, (b)
   highlights *why it matters*, and (c) sets realistic expectations. Ease the
   reader in, never open with a wall of commands.
2. **Reassure, and be honest about effort.** Make clear that the tutorial is a
   *guide into* the topic, not a complete education. Readers must put in their own
   effort, reading official docs, experimenting, and must **practise** to get
   comfortable. Say so, kindly.
3. **Normalise getting stuck.** Errors are part of learning, not a sign of failure.
   Encourage and support the reader; never make them feel behind.
4. **Use light humour where it fits.** A warm, human aside is welcome. Keep it
   gentle and inclusive, never at anyone's expense, and never so much that it
   buries the instructions.
5. **Emoji rules, avoid brand/trademark glyphs.** Do **not** use platform or
   brand emoji/logos (e.g. the apple, the Windows squares, the penguin, or the
   Apple-logo glyph). They risk trademark trouble and render inconsistently. Use
   plain text labels instead ("On a Mac?", "On Windows?", "Apple menu → About This
   Mac"). The **functional callout icons are fine and encouraged**: ✅ Check,
   ⚠️ Verify, 💡 Tip, 🧰 Troubleshooting.
6. **Encourage at the end, too.** Close modules with a brief, sincere note of
   encouragement and a nudge to keep practising and to consult primary docs.

## Adding a new module

1. Create a folder `modules/NN-short-topic/` with a zero-padded number that places
   it correctly in the learning order.
2. Copy the skeleton of an existing module: an `index.qmd`, plus `env/`, `img/`,
   and `scripts/` subfolders as needed.
3. Register it in the sidebar in `_quarto.yml` and in the tables in `index.qmd`
   and `README.md`.
4. Use the standard callouts:
   - `::: {.callout-note}` ✅ **Check**, how to confirm a step worked
   - `::: {.callout-warning}` ⚠️ **Verify**, something that changes over time
   - `::: {.callout-warning}` 🧰 **Troubleshooting**, common errors and fixes
5. Preview locally with `quarto preview` before opening a pull request.

## Reporting problems

If a command is out of date or wrong, please open an issue with:

- Your OS and versions (`lsb_release -a`, `conda --version`, tool `--version`).
- The exact command you ran and the exact output/error.
- What the official documentation currently says, if you've checked.
