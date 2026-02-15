# Four-Year Grouping Strategy - Usage Guide

## Overview

The `FourYearGroupingStrategy` creates a 4-year Bible reading plan with:
- **12 groupings per year** (one per month)
- **Matthew in Year 1, Mark in Year 2, Luke in Year 3, John in Year 4**
- **Psalms and Proverbs excluded** (customizable)
- **Remaining books randomized** across the 4 years
- **Isaiah split**: Isaiah 1-33 (Grouping 18), Isaiah 34-66 (Grouping 19)

## Running from main.py

Simply run:
```bash
python main.py
```

This will:
1. Generate the four-year grouping plan
2. Display it in the console
3. Export to CSV and JSON in the `output/` directory

## Using in Jupyter Notebook

```python
from src.config.settings import EXCEL_FILE
from src.services.data_loader import DataLoader
from src.strategies.four_year_grouping import FourYearGroupingStrategy
from src.services.plan_exporter import PlanExporter

# Load data
loader = DataLoader(EXCEL_FILE)
chapters = loader.load_chapters()

# Generate plan
strategy = FourYearGroupingStrategy(seed=42)  # seed for reproducible randomization
yearly_plans = strategy.generate_plan(chapters, total_days=1461)

# Display in console
PlanExporter.four_year_to_console(yearly_plans)

# Export to files
from src.config.settings import OUTPUT_DIR
PlanExporter.four_year_to_csv(yearly_plans, OUTPUT_DIR / "my_plan.csv")
PlanExporter.four_year_to_json(yearly_plans, OUTPUT_DIR / "my_plan.json")
```

## Customization Options

### Exclude Different Books
```python
strategy = FourYearGroupingStrategy(
    excluded_books={'Psalms', 'Proverbs', 'Song of Solomon'}
)
```

### Change Randomization
```python
# Different random distribution
strategy = FourYearGroupingStrategy(seed=123)

# New random distribution each time
strategy = FourYearGroupingStrategy(seed=None)
```

### Access Individual Year Plans
```python
yearly_plans = strategy.generate_plan(chapters, 1461)

# Access year 1
year_1_plan = yearly_plans[1]

# Iterate through months
for monthly_reading in year_1_plan:
    print(f"{monthly_reading.month_name}: {monthly_reading.book_names}")
    print(f"  Chapters: {len(monthly_reading.chapters)}")
    print(f"  Words: {monthly_reading.total_words:,}")
```

## Output Files

### CSV Format
Contains columns: Year, Month Number, Month, Grouping, Books, Chapters, Words

### JSON Format
Structured data with detailed chapter information for each month

## SOLID Principles Applied

- **Open/Closed**: Easily create new strategies without modifying existing code
- **Dependency Inversion**: Strategy implements `BaseStrategy` interface
- **Single Responsibility**: Each component has one clear purpose
  - Strategy: Generate the plan
  - Exporter: Export to different formats
  - DataLoader: Load from Excel
