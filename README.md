# Smart Light promotions

Interactive prototype of four promotion concepts for [smartlighteg.com](https://www.smartlighteg.com), shown on a clone of the live homepage and styled with the Smart Light Figma tokens.

1. **Spin the wheel**: homepage popup. Drag or tap Spin; the prize is applied to the cart automatically, with a 48-hour countdown.
2. **Mystery boxes**: homepage popup. Pick one of six gift boxes; the prize is applied the same way.
3. **Lucky cashback**: at checkout. After payment a lucky order gets its full total back in the wallet, then the order page and My Wallet show the credit.
4. **Campaign popup**: homepage popup controlled from a settings panel (text and button, text over a background photo, or a full creative visual).

Use the tabs at the top of the page to switch between ideas, and **Replay as new visitor** to restart one.

## Run it

Open `index.html` through any static server, for example:

```bash
python3 -m http.server 8765
```

## Edit it

The source is `src/promos.src.html`. After editing, run `python3 build.py` to regenerate `index.html` (it inlines the Paralucent heading font). Images live in `assets/`.
