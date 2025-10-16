# Playing Card Drawer (turtle graphics)

A simple Python program that draws a selected playing card using the `turtle` module. You can choose a suit and rank or let the program pick randomly. The app also includes a test mode to quickly try any card/suit combination and renders face cards (J, Q, K) with custom images.

- **Entry point**: `main.py`
- **Language**: Python 3
- **Graphics**: `turtle`

## Features
- **Draw any card** from Ace through King in all 4 suits: Spades, Diamonds, Clubs, Hearts.
- **Random selection** for suit and/or number.
- **Validation and fallbacks**: invalid inputs display a fun "snek" image and exit.
- **Test mode**: name your turtle `Test` to enter a loop that lets you render any card quickly.
- **Face cards with images**: Jacks, Queens, and Kings use custom `.gif` shapes when available.

## Requirements
- Python 3.x
- Standard library only (uses `turtle`, `random`, `sys`).
- The following image assets placed in the same directory as `main.py`:
  - `jacks.gif`
  - `queens.gif`
  - `kings.gif`
  - `snek.gif`

## Running
Run with IDLE or the command line.

```bash
python main.py
```

Follow the on-screen prompts:
- Enter a turtle name.
  - If you enter `Test`, you can opt into test mode to repeatedly render any suit/number.
- Choose a suit: `Spade`, `Diamond`, `Club`, `Heart`, or `Random`.
- Choose a number: `1-13` or `Random`.

The program creates a card via `Card(suit, number)` and draws it with `turtle` graphics.

## Usage Tips
- **Faster testing**: Name the turtle `Test` to access the built-in testing loop quickly.
- If you choose a face card (J, Q, K) and the corresponding images exist, the program registers them as shapes for the auxiliary turtle used in face card rendering.

## File Overview
- `main.py`
  - Defines a `Card` class and dozens of drawing functions for suits, pips, and ranks.
  - `draw(card, turtle)` dispatches to the correct renderer based on suit and number.
  - Interactive flow collects inputs, validates them, and displays the final card.
- `README.md` (this file)

## Notes
- The program expects `.gif` images; ensure the filenames exactly match those listed above and are located in the same directory as `main.py`.
- Designed for educational purposes and to demonstrate geometric drawing with `turtle`.
- Code is the same as the submitted work.
