# Quick Start Guide - Daily Reading Plan

## What's New

Your Bible reading program now includes a **Daily Reading Plan** strategy that combines:

1. **Monthly Book Groupings**: 12 groupings per year (one book or set of books per month)
2. **Daily Psalms & Proverbs**: Distributed across every day of the year

## How to Run

### Generate the Daily Plan
```bash
python generate_daily_plan.py
```

### View the Output
Check the `output/` directory for:
- `daily_plan_with_monthly_groupings.csv` - Excel-friendly format
- `daily_plan_with_monthly_groupings.json` - Detailed JSON

## What a Day Looks Like

```
Day 5 (January): 
  Monthly: Leviticus 4 
  Daily: Psalms 2
  Total Words: 1,232
```

Each day you read:
- Chapters from the current month's book(s)
- One or more chapters from Psalms or Proverbs

## The Four-Year Plan

**Year 1**: Matthew + 11 other groupings
**Year 2**: Mark + 11 other groupings  
**Year 3**: Luke + 11 other groupings
**Year 4**: John + 11 other groupings

## Key Features

✅ **Consistency**: Read Psalms and Proverbs every day for wisdom and worship
✅ **Depth**: Focus on one book grouping per month for better context
✅ **Balance**: Chapters distributed evenly to avoid overwhelming days
✅ **Complete**: Read the entire Bible over 4 years

## File Structure

```
bible-reading-plan/
├── generate_daily_plan.py      # NEW: Daily plan generator
├── main.py                      # Original: Monthly groupings only
├── src/
│   ├── models/
│   │   └── daily_reading.py    # NEW: Model for daily readings
│   └── strategies/
│       ├── monthly_plus_daily.py  # NEW: Combined strategy
│       └── four_year_grouping.py  # Original: Monthly only
```

## Customization

See `USAGE_DAILY_PLAN.md` for:
- Changing which books are read daily
- Adjusting the randomization
- Accessing specific days programmatically
- Jupyter notebook examples

## SOLID Design

The new strategy follows the same SOLID principles:
- Extends `BaseStrategy` (Open/Closed Principle)
- Single responsibility for each component
- Easy to swap strategies or add new ones
