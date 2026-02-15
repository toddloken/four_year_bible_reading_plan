# Daily Reading Plan with Monthly Groupings - Usage Guide

## Overview

The `MonthlyPlusDailyStrategy` creates a comprehensive 4-year Bible reading plan that combines:

1. **Monthly Groupings**: 12 book groupings per year (one per month) - the main books of the Bible
2. **Daily Readings**: Psalms and Proverbs distributed across every day of the year

### Structure
Each day includes:
- Chapters from the current month's grouping (distributed across the month)
- Daily portions of Psalms and Proverbs

## Running the Plan

### Command Line
```bash
python generate_daily_plan.py
```

This will:
- Generate a 4-year daily reading plan
- Display sample days in the console  
- Export to CSV and JSON in the `output/` directory

### Output Files
- `daily_plan_with_monthly_groupings.csv` - Spreadsheet format with all days
- `daily_plan_with_monthly_groupings.json` - Detailed JSON with full chapter info

## CSV Format

Columns:
- `Year` - Which year (1-4)
- `Day` - Day number (1-365)
- `Month` - Month name
- `Monthly Grouping` - The grouping number for this month
- `Monthly Reading` - Bible references for monthly books
- `Daily Reading` - Psalms/Proverbs for the day
- `Total Words` - Combined word count
- `Monthly Words` - Words from monthly reading
- `Daily Words` - Words from daily reading

## Example Days

```
Day 3 (January): Monthly: Leviticus 2 | Daily: Psalms 1
  Total Words: 580 (Monthly: 435, Daily: 145)

Day 15 (March): Monthly: 1 Kings 5-6 | Daily: Psalms 7
  Total Words: 2,177 (Monthly: 1,827, Daily: 350)
```

## Gospel Distribution

- **Year 1**: Matthew
- **Year 2**: Mark
- **Year 3**: Luke
- **Year 4**: John

## Customization in Jupyter Notebook

```python
from src.config.settings import EXCEL_FILE, OUTPUT_DIR
from src.services.data_loader import DataLoader
from src.strategies.monthly_plus_daily import MonthlyPlusDailyStrategy
from src.services.plan_exporter import PlanExporter

# Load chapters
loader = DataLoader(EXCEL_FILE)
chapters = loader.load_chapters()

# Create strategy
strategy = MonthlyPlusDailyStrategy(
    daily_books={'Psalms', 'Proverbs'},  # Which books to read daily
    seed=42  # For reproducible randomization
)

# Generate plan
yearly_plans = strategy.generate_plan(chapters, total_days=365)

# View Year 1
for day in yearly_plans[1][:10]:
    print(f"Day {day.day_number}: {day.all_references}")
    print(f"  Words: {day.total_words}")

# Export to files
PlanExporter.daily_plan_to_csv(yearly_plans, OUTPUT_DIR / "my_daily_plan.csv")
PlanExporter.daily_plan_to_json(yearly_plans, OUTPUT_DIR / "my_daily_plan.json")
```

### Customization Options

**Change daily books:**
```python
# Read Song of Solomon daily instead
strategy = MonthlyPlusDailyStrategy(
    daily_books={'Song of Solomon'}
)

# Multiple books daily
strategy = MonthlyPlusDailyStrategy(
    daily_books={'Psalms', 'Proverbs', 'Ecclesiastes'}
)
```

**Different randomization:**
```python
# Different random distribution
strategy = MonthlyPlusDailyStrategy(seed=123)

# New random each time
strategy = MonthlyPlusDailyStrategy(seed=None)
```

**Access specific year/day:**
```python
yearly_plans = strategy.generate_plan(chapters, 365)

# Get Year 2, Day 100
day_100 = yearly_plans[2][99]  # 0-indexed

print(f"Month: {day_100.month_name}")
print(f"Monthly: {day_100.monthly_references}")
print(f"Daily: {day_100.daily_references}")
print(f"Total words: {day_100.total_words}")
```

## How It Works

1. **Assigns Gospels**: Matthew→Year 1, Mark→Year 2, Luke→Year 3, John→Year 4
2. **Randomizes Remaining Groupings**: 11 other groupings randomly distributed to fill 12 months
3. **Distributes Monthly Chapters**: Chapters from each month's grouping spread across that month's days
4. **Distributes Daily Books**: Psalms (150 chapters) + Proverbs (31 chapters) = 181 chapters spread across 365 days

## Benefits

- **Consistent Daily Reading**: Psalms and Proverbs every day for wisdom and worship
- **Focused Monthly Study**: One main book/grouping per month for deeper context
- **Balanced Workload**: Distributes chapters to avoid overwhelming days
- **Complete Coverage**: Read entire Bible over 4 years

## SOLID Principles

- **Single Responsibility**: Each class has one purpose (loading, generating, exporting)
- **Open/Closed**: Easy to add new strategies without modifying existing code
- **Strategy Pattern**: Swap reading strategies without changing the export logic
- **Dependency Inversion**: Depends on abstractions (BaseStrategy) not concrete classes
