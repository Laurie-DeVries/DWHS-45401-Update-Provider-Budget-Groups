import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows

# Load the CSV file
file_path = 'Untitled 6_2026-06-01-1108.csv'
df = pd.read_csv(file_path)

print("=" * 80)
print("HEALTHCARE DATA ANALYSIS")
print("=" * 80)
print(f"\nTotal Records: {len(df)}")
print(f"Data Loaded Successfully\n")

# ============================================================================
# Create Excel workbook with all analyses
# ============================================================================
excel_file = 'Healthcare_Data_Analysis.xlsx'
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:

    # ========================================================================
    # SHEET 1: SERVICE AREA ANALYSIS
    # ========================================================================
    print("Processing: Service Area Analysis...")
    
    service_area_summary = df.groupby('AHEMS_SERVICE_AREA').agg({
        'CALENDAR_YEAR': 'count',
        'TOTAL_AMT_PAID': ['sum', 'mean', 'min', 'max'],
        'MEMBER_MONTHS': 'sum',
        'TOTAL_NUM_ICN': 'sum',
        'IP_ADMIT_CNT': 'sum',
        'ED_VISIT_CNT': 'sum',
        'PCP_VISIT_CNT': 'sum',
        'TELEHEALTH_VISIT_CNT': 'sum',
        'DENTAL_VISIT_CNT': 'sum'
    }).round(2)

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

    service_area_summary = service_area_summary.sort_values('Member_Count', ascending=False)
    service_area_summary.to_excel(writer, sheet_name='Service Area')

    # ========================================================================
    # SHEET 2: DEMOGRAPHICS BY SEX
    # ========================================================================
    print("Processing: Demographics by Sex...")
    
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
    sex_summary.to_excel(writer, sheet_name='Demographics - Sex')

    # ========================================================================
    # SHEET 3: DEMOGRAPHICS BY RACE
    # ========================================================================
    print("Processing: Demographics by Race...")
    
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
    race_summary.to_excel(writer, sheet_name='Demographics - Race')

    # ========================================================================
    # SHEET 4: DEMOGRAPHICS BY ETHNICITY
    # ========================================================================
    print("Processing: Demographics by Ethnicity...")
    
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
    ethnicity_summary.to_excel(writer, sheet_name='Demographics - Ethnicity')

    # ========================================================================
    # SHEET 5: DEMOGRAPHICS BY AGE
    # ========================================================================
    print("Processing: Demographics by Age...")
    
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
    age_summary.to_excel(writer, sheet_name='Demographics - Age')

    # ========================================================================
    # SHEET 6: SEX AND RACE CROSS-TABULATION
    # ========================================================================
    print("Processing: Sex and Race Cross-tabulation...")
    
    sex_race_crosstab = pd.crosstab(df['DSC_SEX'], df['DSC_RACE'], margins=True)
    sex_race_crosstab.to_excel(writer, sheet_name='Crosstab - Sex x Race')

    # ========================================================================
    # SHEET 7: PLAN TYPE ANALYSIS
    # ========================================================================
    print("Processing: Plan Type Analysis...")
    
    plan_type_summary = df.groupby('PLAN_TYPE').agg({
        'CALENDAR_YEAR': 'count',
        'TOTAL_AMT_PAID': ['sum', 'mean', 'median', 'std'],
        'MEMBER_MONTHS': 'sum',
        'TOTAL_NUM_ICN': 'sum',
        'IP_ADMIT_CNT': 'sum',
        'ED_VISIT_CNT': 'sum',
        'PCP_VISIT_CNT': 'sum',
        'TELEHEALTH_VISIT_CNT': 'sum',
        'DENTAL_VISIT_CNT': 'sum',
        'ROUTINE_EXAM_CNT': 'sum'
    }).round(2)

    plan_type_summary.columns = [
        'Member_Count',
        'Total_Amount_Paid',
        'Avg_Amount_Per_Member',
        'Median_Amount_Per_Member',
        'StdDev_Amount_Per_Member',
        'Total_Member_Months',
        'Total_Claims',
        'Inpatient_Admissions',
        'ED_Visits',
        'PCP_Visits',
        'Telehealth_Visits',
        'Dental_Visits',
        'Routine_Exams'
    ]

    plan_type_summary['Pct_of_Total_Members'] = (plan_type_summary['Member_Count'] / plan_type_summary['Member_Count'].sum() * 100).round(2)
    plan_type_summary = plan_type_summary.sort_values('Member_Count', ascending=False)
    plan_type_summary.to_excel(writer, sheet_name='Plan Type')

    # ========================================================================
    # SHEET 8: PLAN TYPE AND RISK LEVEL CROSS-TABULATION
    # ========================================================================
    print("Processing: Plan Type and Risk Level Cross-tabulation...")
    
    plan_risk_crosstab = pd.crosstab(df['PLAN_TYPE'], df['RISK_LEVEL'], margins=True)
    plan_risk_crosstab.to_excel(writer, sheet_name='Crosstab - Plan x Risk')

    # ========================================================================
    # SHEET 9: SUMMARY STATISTICS
    # ========================================================================
    print("Processing: Summary Statistics...")
    
    summary_stats = pd.DataFrame({
        'Metric': [
            'Total Members',
            'Total Amount Paid',
            'Average Cost Per Member',
            'Median Cost Per Member',
            'Total Member Months',
            'Total Claims',
            'Total Inpatient Admissions',
            'Total ED Visits',
            'Total PCP Visits',
            'Total Telehealth Visits',
            'Total Dental Visits',
            'Total Routine Exams'
        ],
        'Value': [
            len(df),
            f"${df['TOTAL_AMT_PAID'].sum():,.2f}",
            f"${df['TOTAL_AMT_PAID'].mean():,.2f}",
            f"${df['TOTAL_AMT_PAID'].median():,.2f}",
            f"{df['MEMBER_MONTHS'].sum():,.0f}",
            f"{df['TOTAL_NUM_ICN'].sum():,.0f}",
            f"{df['IP_ADMIT_CNT'].sum():,.0f}",
            f"{df['ED_VISIT_CNT'].sum():,.0f}",
            f"{df['PCP_VISIT_CNT'].sum():,.0f}",
            f"{df['TELEHEALTH_VISIT_CNT'].sum():,.0f}",
            f"{df['DENTAL_VISIT_CNT'].sum():,.0f}",
            f"{df['ROUTINE_EXAM_CNT'].sum():,.0f}"
        ]
    })
    
    summary_stats.to_excel(writer, sheet_name='Summary Statistics', index=False)

print("\n" + "=" * 80)
print("EXPORT COMPLETE")
print("=" * 80)
print(f"\n✓ All analyses exported to: {excel_file}")
print("\nSheet names included:")
print("  1. Service Area")
print("  2. Demographics - Sex")
print("  3. Demographics - Race")
print("  4. Demographics - Ethnicity")
print("  5. Demographics - Age")
print("  6. Crosstab - Sex x Race")
print("  7. Plan Type")
print("  8. Crosstab - Plan x Risk")
print("  9. Summary Statistics")
print("\n" + "=" * 80)
