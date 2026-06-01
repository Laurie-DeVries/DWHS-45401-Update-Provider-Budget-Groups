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
# ANALYSIS 2: DEMOGRAPHIC ANALYSIS
# ============================================================================
print("\n\n" + "=" * 80)
print("DEMOGRAPHIC ANALYSIS")
print("=" * 80)

# ============================================================================
# 2A: ANALYSIS BY SEX
# ============================================================================
print("\n" + "-" * 80)
print("BREAKDOWN BY SEX")
print("-" * 80)

sex_summary = df.groupby('DSC_SEX').agg({
    'CALENDAR_YEAR': 'count',
    'TOTAL_AMT_PAID': ['sum', 'mean'],
    'MEMBER_MONTHS': 'sum',
    'TOTAL_NUM_ICN': 'sum',
    'IP_ADMIT_CNT': 'sum',
    'ED_VISIT_CNT': 'sum',
    'PCP_VISIT_CNT': 'sum'
}).round(2)

sex_summary.columns = [
    'Member_Count',
    'Total_Amount_Paid',
    'Avg_Amount_Per_Member',
    'Total_Member_Months',
    'Total_Claims',
    'Inpatient_Admissions',
    'ED_Visits',
    'PCP_Visits'
]

sex_summary['Pct_of_Total'] = (sex_summary['Member_Count'] / sex_summary['Member_Count'].sum() * 100).round(2)
sex_summary = sex_summary.sort_values('Member_Count', ascending=False)

print("\n" + sex_summary.to_string())

# ============================================================================
# 2B: ANALYSIS BY RACE
# ============================================================================
print("\n" + "-" * 80)
print("BREAKDOWN BY RACE")
print("-" * 80)

race_summary = df.groupby('DSC_RACE').agg({
    'CALENDAR_YEAR': 'count',
    'TOTAL_AMT_PAID': ['sum', 'mean'],
    'MEMBER_MONTHS': 'sum',
    'TOTAL_NUM_ICN': 'sum',
    'IP_ADMIT_CNT': 'sum',
    'ED_VISIT_CNT': 'sum',
    'PCP_VISIT_CNT': 'sum'
}).round(2)

race_summary.columns = [
    'Member_Count',
    'Total_Amount_Paid',
    'Avg_Amount_Per_Member',
    'Total_Member_Months',
    'Total_Claims',
    'Inpatient_Admissions',
    'ED_Visits',
    'PCP_Visits'
]

race_summary['Pct_of_Total'] = (race_summary['Member_Count'] / race_summary['Member_Count'].sum() * 100).round(2)
race_summary = race_summary.sort_values('Member_Count', ascending=False)

print("\n" + race_summary.to_string())

# ============================================================================
# 2C: ANALYSIS BY ETHNICITY
# ============================================================================
print("\n" + "-" * 80)
print("BREAKDOWN BY ETHNICITY")
print("-" * 80)

ethnicity_summary = df.groupby('DSC_ETHNICITY').agg({
    'CALENDAR_YEAR': 'count',
    'TOTAL_AMT_PAID': ['sum', 'mean'],
    'MEMBER_MONTHS': 'sum',
    'TOTAL_NUM_ICN': 'sum',
    'IP_ADMIT_CNT': 'sum',
    'ED_VISIT_CNT': 'sum',
    'PCP_VISIT_CNT': 'sum'
}).round(2)

ethnicity_summary.columns = [
    'Member_Count',
    'Total_Amount_Paid',
    'Avg_Amount_Per_Member',
    'Total_Member_Months',
    'Total_Claims',
    'Inpatient_Admissions',
    'ED_Visits',
    'PCP_Visits'
]

ethnicity_summary['Pct_of_Total'] = (ethnicity_summary['Member_Count'] / ethnicity_summary['Member_Count'].sum() * 100).round(2)
ethnicity_summary = ethnicity_summary.sort_values('Member_Count', ascending=False)

print("\n" + ethnicity_summary.to_string())

# ============================================================================
# 2D: ANALYSIS BY AGE GROUP
# ============================================================================
print("\n" + "-" * 80)
print("BREAKDOWN BY AGE GROUP")
print("-" * 80)

age_summary = df.groupby('AGE').agg({
    'CALENDAR_YEAR': 'count',
    'TOTAL_AMT_PAID': ['sum', 'mean'],
    'MEMBER_MONTHS': 'sum',
    'TOTAL_NUM_ICN': 'sum',
    'IP_ADMIT_CNT': 'sum',
    'ED_VISIT_CNT': 'sum',
    'PCP_VISIT_CNT': 'sum'
}).round(2)

age_summary.columns = [
    'Member_Count',
    'Total_Amount_Paid',
    'Avg_Amount_Per_Member',
    'Total_Member_Months',
    'Total_Claims',
    'Inpatient_Admissions',
    'ED_Visits',
    'PCP_Visits'
]

age_summary['Pct_of_Total'] = (age_summary['Member_Count'] / age_summary['Member_Count'].sum() * 100).round(2)
age_summary = age_summary.sort_values('Member_Count', ascending=False)

print("\n" + age_summary.to_string())

# ============================================================================
# 2E: CROSS-TABULATION: SEX AND RACE
# ============================================================================
print("\n" + "-" * 80)
print("CROSS-TABULATION: SEX AND RACE")
print("-" * 80)

sex_race_crosstab = pd.crosstab(df['DSC_SEX'], df['DSC_RACE'], margins=True)
print("\n" + sex_race_crosstab.to_string())

# ============================================================================
# 2F: DEMOGRAPHIC INSIGHTS
# ============================================================================
print("\n" + "-" * 80)
print("KEY DEMOGRAPHIC INSIGHTS")
print("-" * 80)

# Most common race
most_common_race = race_summary.index[0]
most_common_race_count = race_summary.iloc[0]['Member_Count']
print(f"\nMost Common Race: {most_common_race} ({int(most_common_race_count)} members)")

# Most common ethnicity
most_common_ethnicity = ethnicity_summary.index[0]
most_common_ethnicity_count = ethnicity_summary.iloc[0]['Member_Count']
print(f"Most Common Ethnicity: {most_common_ethnicity} ({int(most_common_ethnicity_count)} members)")

# Sex distribution
for sex, row in sex_summary.iterrows():
    print(f"{sex}: {int(row['Member_Count'])} members ({row['Pct_of_Total']}%)")

# Age group with highest costs
highest_cost_age = age_summary.loc[age_summary['Total_Amount_Paid'].idxmax()]
print(f"\nAge Group with Highest Total Costs: {age_summary['Total_Amount_Paid'].idxmax()}")
print(f"  Total Amount: ${highest_cost_age['Total_Amount_Paid']:,.2f}")

# Age group with highest average cost per member
highest_avg_cost_age = age_summary.loc[age_summary['Avg_Amount_Per_Member'].idxmax()]
print(f"\nAge Group with Highest Avg Cost per Member: {age_summary['Avg_Amount_Per_Member'].idxmax()}")
print(f"  Avg Amount: ${highest_avg_cost_age['Avg_Amount_Per_Member']:,.2f}")

# ============================================================================
# EXPORT RESULTS TO CSV
# ============================================================================
print("\n" + "=" * 80)
print("EXPORTING RESULTS")
print("=" * 80)

# Export summaries to CSV
service_area_summary.to_csv('service_area_summary.csv')
print(f"✓ Service Area Summary exported to: service_area_summary.csv")

sex_summary.to_csv('demographic_summary_by_sex.csv')
print(f"✓ Sex Demographics exported to: demographic_summary_by_sex.csv")

race_summary.to_csv('demographic_summary_by_race.csv')
print(f"✓ Race Demographics exported to: demographic_summary_by_race.csv")

ethnicity_summary.to_csv('demographic_summary_by_ethnicity.csv')
print(f"✓ Ethnicity Demographics exported to: demographic_summary_by_ethnicity.csv")

age_summary.to_csv('demographic_summary_by_age.csv')
print(f"✓ Age Demographics exported to: demographic_summary_by_age.csv")

sex_race_crosstab.to_csv('demographic_crosstab_sex_race.csv')
print(f"✓ Sex/Race Cross-tabulation exported to: demographic_crosstab_sex_race.csv")

print("\n" + "=" * 80)
print("READY FOR ADDITIONAL ANALYSES")
print("=" * 80)
print("\nYou can easily add more analyses such as:")
print("  • Summary by PLAN_TYPE")
print("  • Summary by RISK_LEVEL")
print("  • Summary by MCO_REGION")
print("  • Condition prevalence analysis")
print("  • Visit type breakdown")
print("  • Dual eligibility analysis")
print("\n" + "=" * 80)
