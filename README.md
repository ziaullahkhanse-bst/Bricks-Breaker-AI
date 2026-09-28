# Brick Breaker AI

A fun little Brick Breaker game I built using Python and Pygame. It has an AI that can play the game by itself if you want to sit back and watch.


## What It Is

This is a classic Brick Breaker game. You control a paddle at the bottom, and you bounce a ball to break bricks at the top. There are 18 bricks in total.

The special part is the AI. If you don't feel like playing, just click "Auto Play" and the paddle will move on its own. The AI predicts where the ball is going to land and moves the paddle there in advance.

You can switch between playing yourself and letting the AI play anytime you want.


## Features

- Play the game yourself with the arrow keys
- Let the AI play for you with one click
- Ball gets faster as your score goes up
- Clean green theme
- Win screen when you break all bricks
- Game over screen when you miss the ball


## How to Run It

You need Python and Pygame installed.

**Step 1:** Install Python 3.12.8 or newer from python.org.

**Step 2:** Open a terminal in this folder.

**Step 3:** Install Pygame:

    pip install pygame

**Step 4:** Run the game:

    python game.py

That's it. The game opens and you can play.


## Controls

- Hold **Left Arrow** to move the paddle left
- Hold **Right Arrow** to move the paddle right
- Click **Auto Play** to let the AI play
- Click **Manual** to take back control
- Close the window to quit

---

## How the AI Works

When the ball is falling, the AI does a quick calculation:

1. It figures out how long the ball will take to reach the paddle.
2. It predicts where the ball will be at that moment.
3. If the ball would bounce off a wall, the AI simulates that too.
4. Then it moves the paddle to that spot.

So the paddle is always waiting where the ball is going to land. That is why it almost never misses.


## Ball Speed

The ball gets faster as you score more:

- Score 0 to 4 → normal speed
- Score 5 to 9 → a bit faster
- Score 10 to 14 → fast
- Score 15 and up → very fast

This keeps the game interesting and challenging.


## What I Used

- Python 3.12.8
- Pygame
- Simple collision detection
- A bit of math for the AI prediction


## About AI Help

I used AI tools to help me learn, debug, and improve the game. But I wrote, tested, and understood all the final code myself.

---

## About Me

**Ziaullah Khan**
Built for the First Commit Hackathon.

GitHub: github.com/ziaullahkhanse-bst
