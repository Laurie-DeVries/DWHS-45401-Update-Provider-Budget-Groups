import pandas as pd
import numpy as np

# Load the CSV file
file_path = 'Untitled 6_2026-06-01-1108.csv'
df = pd.read_csv(file_path)

print("=" * 80)
print("HEALTHCARE DATA ANALYSIS")
print("=" * 80)
print(f"\nTotal Records: {len(df)}")
print(f"Data Loaded Successfully\n")

# ============================================================================
# ANALYSIS 1: SUMMARY BY SERVICE AREA
# ============================================================================
print("\n" + "=" * 80)
print("SERVICE AREA ANALYSIS")
print("=" * 80)

service_area_summary = df.groupby('AHEMS_SERVICE_AREA').agg({
    'CALENDAR_YEAR': 'count',  # Member count
    'TOTAL_AMT_PAID': ['sum', 'mean', 'min', 'max'],
    'MEMBER_MONTHS': 'sum',
    'TOTAL_NUM_ICN': 'sum',
    'IP_ADMIT_CNT': 'sum',
    'ED_VISIT_CNT': 'sum',
    'PCP_VISIT_CNT': 'sum',
    'TELEHEALTH_VISIT_CNT': 'sum',
    'DENTAL_VISIT_CNT': 'sum'
}).round(2)

# Rename columns for clarity
service_area_summary.columns = [
    'Member_Count',
    'Total_Amount_Paid',
    'Avg_Amount_Per_Member',
    'Min_Amount_Paid',
    'Max_Amount_Paid',
    'Total_Member_Months',
    'Total_Claims',
    'Inpatient_Admissions',
    'ED_Visits',
    'PCP_Visits',
    'Telehealth_Visits',
    'Dental_Visits'
]

# Sort by Member Count (descending)
service_area_summary = service_area_summary.sort_values('Member_Count', ascending=False)

print("\n" + service_area_summary.to_string())

# Create a detailed breakdown
print("\n" + "-" * 80)
print("DETAILED SERVICE AREA BREAKDOWN")
print("-" * 80)

for service_area in service_area_summary.index:
    area_data = df[df['AHEMS_SERVICE_AREA'] == service_area]
    print(f"\n{service_area}:")
    print(f"  Members: {len(area_data)}")
    print(f"  Total Amount Paid: ${area_data['TOTAL_AMT_PAID'].sum():,.2f}")
    print(f"  Avg Amount Per Member: ${area_data['TOTAL_AMT_PAID'].mean():,.2f}")
    print(f"  Total Claims: {area_data['TOTAL_NUM_ICN'].sum():.0f}")
    print(f"  Inpatient Admissions: {area_data['IP_ADMIT_CNT'].sum():.0f}")
    print(f"  ED Visits: {area_data['ED_VISIT_CNT'].sum():.0f}")
    print(f"  PCP Visits: {area_data['PCP_VISIT_CNT'].sum():.0f}")

# ============================================================================
# EXPORT RESULTS TO CSV
# ============================================================================
print("\n" + "=" * 80)
print("EXPORTING RESULTS")
print("=" * 80)

# Export summary to CSV
output_file = 'service_area_summary.csv'
service_area_summary.to_csv(output_file)
print(f"\n✓ Service Area Summary exported to: {output_file}")

print("\n" + "=" * 80)
print("READY FOR ADDITIONAL ANALYSES")
print("=" * 80)
print("\nYou can easily add more analyses such as:")
print("  • Summary by PLAN_TYPE")
print("  • Summary by RISK_LEVEL")
print("  • Summary by AGE group")
print("  • Summary by MCO_REGION")
print("  • Condition prevalence analysis")
print("  • Visit type analysis")
print("  • Demographics breakdown")
print("\n" + "=" * 80)
