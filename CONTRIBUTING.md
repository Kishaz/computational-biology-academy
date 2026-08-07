# Contributing

Thanks for helping improve these tutorials! The guiding principle of this project
is **accuracy over polish**: a clear, correct, verifiable step beats an impressive
but wrong one.

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
4. **Flag anything that changes over time** — installation methods, licensing,
   channel configuration, API syntax — with a **⚠️ Verify** note.
5. **Keep it beginner-friendly.** Assume no prior programming experience. Explain
   *why*, not just *what*. Show how to check that a step worked (✅ **Check**).

## Voice & tone style guide (applies to every module)

These tutorials teach nervous beginners. The tone is as important as the accuracy.

1. **Open every topic with a gentle introduction.** Before any commands, include a
   short, warm intro that (a) says what the topic is in plain language, (b)
   highlights *why it matters*, and (c) sets realistic expectations. Ease the
   reader in — never open with a wall of commands.
2. **Reassure, and be honest about effort.** Make clear that the tutorial is a
   *guide into* the topic, not a complete education. Readers must put in their own
   effort — reading official docs, experimenting — and must **practise** to get
   comfortable. Say so, kindly.
3. **Normalise getting stuck.** Errors are part of learning, not a sign of failure.
   Encourage and support the reader; never make them feel behind.
4. **Use light humour where it fits.** A warm, human aside is welcome. Keep it
   gentle and inclusive — never at anyone's expense, and never so much that it
   buries the instructions.
5. **Emoji rules — avoid brand/trademark glyphs.** Do **not** use platform or
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
   - `::: {.callout-note}` ✅ **Check** — how to confirm a step worked
   - `::: {.callout-warning}` ⚠️ **Verify** — something that changes over time
   - `::: {.callout-warning}` 🧰 **Troubleshooting** — common errors and fixes
5. Preview locally with `quarto preview` before opening a pull request.

## Reporting problems

If a command is out of date or wrong, please open an issue with:

- Your OS and versions (`lsb_release -a`, `conda --version`, tool `--version`).
- The exact command you ran and the exact output/error.
- What the official documentation currently says, if you've checked.
