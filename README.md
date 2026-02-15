# 4-Year Bible Reading Plan Generator

A Python application that generates customizable 4-year Bible reading plans

## Features

- Load Bible chapter data from Excel
- Multiple reading strategies:
  - **Four-Year Grouping**: 12 book groupings per year (one per month) - This is the primary
  - **Daily Plan with Monthly Groupings**: Monthly books + daily Psalms/Proverbs
  - **Balanced**: Distribute by word count
  - **Chronological**: Read in biblical order
- Export to CSV and JSON formats
- Clean, maintainable codebase following SOLID principles

## Available Plans

### 1. Four-Year Grouping Plan (Monthly Groupings Only)
```bash
python main.py
```
Generates a plan with 12 book groupings per year. See `USAGE_FOUR_YEAR.md` for details.

### 2. Daily Plan (Monthly + Daily Readings)
```bash
python generate_daily_plan.py
```
Generates a daily plan combining monthly groupings with daily Psalms/Proverbs. See `USAGE_DAILY_PLAN.md` for details.

## Project Structure

```
bible-reading-plan/
├── src/
│   ├── models/          # Data models (Chapter, ReadingDay, MonthlyReading, DailyReading)
│   ├── services/        # Business logic (DataLoader, PlanGenerator, PlanExporter)
│   ├── strategies/      # Reading plan strategies
│   └── config/          # Configuration
├── data/                # Input data files
├── output/              # Generated plans
├── tests/               # Unit tests
├── main.py             # Four-year grouping plan generator
└── generate_daily_plan.py  # Daily plan with monthly groupings generator
```

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Place your `Annual_Reading.xlsx` file in the `data/` directory

## Available Strategies

### 1. FourYearGroupingStrategy
- 12 groupings per year (one per month)
- Matthew→Year 1, Mark→Year 2, Luke→Year 3, John→Year 4
- Remaining books randomized
- Isaiah split: 1-33 and 34-66

### 2. MonthlyPlusDailyStrategy  
- 12 monthly groupings (main books)
- Daily Psalms and Proverbs every day
- Combines deep study with daily wisdom/worship

### 3. BalancedStrategy
- Distributes chapters evenly by word count
- ~600 words per day

### 4. ChronologicalStrategy
- Read in biblical order
- Configurable chapters per day

## Extending

To add a new reading strategy:
1. Create a new class in `src/strategies/` that inherits from `BaseStrategy`
2. Implement the `generate_plan()` method
3. Use it with the `PlanGenerator` or call directly

