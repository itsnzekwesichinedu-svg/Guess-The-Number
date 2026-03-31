# Guess the Number 🎮

A Python terminal game where the player tries to guess a randomly generated number.

## How to Play

Run the game in your terminal:

```
python guess_the_number.py
```

Then:
1. Choose a difficulty level
2. Guess the number — the game tells you if you're too high or too low
3. Try to guess it in as few attempts as possible to earn more points
4. Play as many rounds as you want and track your score

## Difficulty Levels

| Level  | Range  | Guesses |
|--------|--------|---------|
| Easy   | 1–50   | 10      |
| Medium | 1–100  | 7       |
| Hard   | 1–200  | 5       |

## Scoring

- Base points: 50 per correct guess
- Bonus: +10 points for each guess you had remaining
- The faster you guess, the higher your score

## What I Learned Building This

- Functions and how to structure a program into reusable parts
- While loops and input validation (handling bad input without crashing)
- Random number generation with Python's `random` module
- How to use `try / except` to catch errors gracefully
- Thinking about user experience — clear feedback, difficulty options, score tracking

## Built With

- Python 3
- No external libraries — just the standard library

---

Built by Nzekwesi Chinedu — CS student based in Madrid, Spain.
