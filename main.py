"""
 @fileoverview

 Main entry point for the 4-year Bible reading plan generator.
 Produces a single Excel file with monthly_out and daily_out tabs.

 @author tjl
 @version 1.0.0
 @since February 2026
"""

from src.config.settings import EXCEL_FILE, OUTPUT_DIR
from src.services.data_loader import DataLoader
from src.services.plan_exporter import PlanExporter
from src.strategies.four_year_grouping import FourYearGroupingStrategy
from src.strategies.four_year_daily import FourYearDailyStrategy


def main():
    chapters = DataLoader(EXCEL_FILE).load_chapters()
    print(f'Loaded {len(chapters)} chapters from {EXCEL_FILE.name}')

    grouping_strategy = FourYearGroupingStrategy(seed=42)
    monthly_plans = grouping_strategy.generate_plan(chapters, 365)

    grouped_by_year = {
        year: set(mr.grouping for mr in monthly_plans[year])
        for year in range(1, 5)
    }

    daily_strategy = FourYearDailyStrategy()
    daily_plans = daily_strategy.generate_plan(chapters, grouped_by_year)

    output_file = OUTPUT_DIR / 'Four_Year_Plan.xlsx'
    PlanExporter.to_excel(monthly_plans, daily_plans, output_file)

    monthly_rows = sum(len(monthly_plans[y]) for y in range(1, 5))
    daily_rows = sum(len(daily_plans[y]) for y in range(1, 5))
    print(f'Monthly rows: {monthly_rows}')
    print(f'Daily rows: {daily_rows}')
    print(f'Exported to {output_file}')


if __name__ == '__main__':
    main()
