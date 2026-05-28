# COMMONWEALTH OF MASSACHUSETTS
## EXECUTIVE OFFICE OF HEALTH AND HUMAN SERVICES

### Data Warehouse

**Update Provider Budget Groups for Recently Added Provider Types in MMIS - DWHS-45401**

**Version:** 1.0  
**Date:** May 28, 2026

---

## Table of Contents

1. [Revision History](#revision-history)
2. [Data Security Requirements](#data-security-requirements)
3. [Acronyms](#acronyms)
4. [Background](#background)
5. [Task Description](#task-description)
6. [Logic and Output](#logic-and-output)
7. [Data Delivery Requirements](#data-delivery-requirements)
8. [Output File Field Names](#output-file-field-names)
9. [Code and Description Reference](#code-and-description-reference)
10. [Stakeholders and Approvers](#stakeholders-and-approvers)

---

## Revision History

| Date | Version | Description | Author |
|---|---|---|---|
| 05/28/2026 | 1.0 | Creation of Specs | Laurie D |

---

## Data Security Requirements

| SSA | PHI | PII | Data Input/Output | DUA | Privacy/Legal Approval | Contractor Statement | Restriction of Data Use |
|---|---|---|---|---|---|---|---|
| N | N | N | Input | N/A | N | [Link to contractor statement location] | Example 1: Only DW and MHA team can access this data<br><br>Example 2: All DW users can access this data |

---

## Acronyms

| Acronym | Definition |
|---|---|
| SSA | Data verified by Social Security Administration |
| PHI | Protected Health Information. Examples include medical histories, demographic data, and test results |
| PII | Personally Identifiable Information. Examples include social security number, driver's license number, or medical records |
| DUA | Data Use Agreement |
| MMIS | Medicaid Management Information System (Claims adjudicated by MassHealth) |
| HRSN | Health-Related Social Needs |
| PACT | Program of Assertive Community Treatment |

---

## Background

There are 3 new provider types for MMIS that were added in November. Those provider types need to have budget provider groups added to them in the nw_provider and family of tables/views. Currently they are set to xx. Based on discussions with Budget these provider groups should be set up as their own group for now.

---

## Task Description

EHS Data Warehouse will update source tables and tables they flow to based on specifications provided below:

### Provider Types

| CDE_PROV_TYPE | DSC_PROV_BUDGET_OFFICE | CDE_PROV_BUDGET_GROUP | DSC_PROV_BUDGET_GROUP |
|---|---|---|---|
| C6 | Office of Acute and Ambulatory Care | C6 | C6 - HRSN |
| C7 | Office of Behavioral Health | C7 | C7 - PACT |
| C8 | Office of Acute and Ambulatory Care | C8 | C8 - Correctional Facilities |

**Provider Type Details:**
- **C6** - HRSN (HEALTH-RELATED SOCIAL NEEDS) MCE ONLY
- **C7** - PROGRAM OF ASSERTIVE COMMUNITY TREATMENT (PACT)
- **C8** - CORRECTIONAL FACILITIES

**Requirements:**
- The `cde_prov_budget_group` should be C6, C7, and C8 respectively
- Descriptions: HRSN, PACT, and Correctional Facilities respectively
- The `dsc_prov_budget_office` should be:
  - Office of Acute and Ambulatory Care for C6 and C8
  - Office of Behavioral Health for C7

---

## Logic and Output

### 4.1 Date Period Filter

- First data extracts will be for the period from January 1, 2011 through June 30, 2015 based on the "from" dates of service on claims
- First data extracts are tentatively scheduled to be delivered on October/November 2015, dependent on Legal and Privacy approval

### 4.2 Member Data Filters and Logic

#### 4.2.1 Include members eligible for any of the following programs:
- MassHealth Standard - STD
- MassHealth CommonHealth - COM
- MassHealth Family Assistance - FADC
- CarePlus - CAREP

#### 4.2.2 Exclude members eligible for following programs:
- Health Safety Net - HSN
- Health Safety Net Family Planning - HSNF
- Health Safety Net Standard – HSNS
- Partial Health Safety Net - PHSN
- QHP - QHP

#### 4.2.3 Member Demographic Information and Eligibility Flags
- Retrieve member demographic information listed under output below as of the first of the month
- Monthly benefits eligibility flag (full benefits in month- yes/no)
  - Members who have full benefits on the first day of the month should be considered fully eligible for that month
- Monthly dual eligibility flag (Dual eligible in month- yes/no)

### 4.3 Claim Data Filters and Logic

#### 4.3.1 General Requirements
- Medical and Pharmacy extracts for MMIS and Encounter claims are included

#### 4.3.2 Claim Types Included
- **Medical Claim Types:** I - Inpatient, O - Outpatient, M – Physician, H - Home Health, L – Long Term Care, D – Dental, and MMIS crossover claims A, B, and C
- **Pharmacy Claim Types:** P – Pharmacy, Q – Compound Drugs Claims

#### 4.3.3 Claim Status, Revenue Code, Amount Paid Requirements
- **Claim Type A, I, and L:** Header paid claims - all provided where claim status equals paid on header line, regardless of claim status on detail line
- **Detail Amount Paid:** All detail lines will be zero for header paid claim types A, I, and L

#### 4.3.4 Special Claim Types
- Include PCPR zero-paid claims in MassHealth Medical Claim File

#### 4.3.5 Medical Claims - Allowed Billing Providers with Disbursement Codes

| Req# | Disbursement Code | Description | Included in Output? |
|---|---|---|---|
| 4.3.5.1 | 0 | Pay | Yes |
| 4.3.5.2 | 1 | State Agency | No |
| 4.3.5.3 | 2 | Muni-Med | No |
| 4.3.5.4 | 3 | Non-Billing | No |
| 4.3.5.5 | 4 | EHR Incentive Provider No-Pay | Yes |
| 4.3.5.6 | 5 | EHR Incentive Provider Expenditures Only | Yes |
| 4.3.5.7 | 6 | Health Safety Net (HSN) | No |

#### 4.3.6 HSN Claims Exclusion
- Exclude HSN claims based on Claim Code Origin Flag (CDE_CLM_ORIGIN) equal to 'H' on the claim
- This is not applicable to encounter claims

---

## Data Delivery Requirements

### 5.1 File Transfer
- Data warehouse will create Secure File Transfer Protocol (SFTP) account and drop files in secured folder where authenticated users can access the data files

### 5.2 Out of Scope
- Development of quality measures is not in the scope
- Vendor will use EHS DW data to develop the measures

---

## Output File Field Names

### 6.1 Member with Eligibility Flags Data by Month

| Req# | Field Name | Table | Type | Length | Description |
|---|---|---|---|---|---|
| 6.1.1 | id_medicaid | nw_member | Character | 12 | Unique identifier for the member. Encrypt Medicaid ID based on "Data Use Agreement" |
| 6.1.2 | dte_birth | nw_member | Date | - | The date of birth of the member |

### 6.2 MassHealth Medical Claims Data

| Req# | Field Name | Table | Type | Length | Description |
|---|---|---|---|---|---|
| 6.2.1 | id_medicaid | nw_member | Character | 12 | Unique identifier for the member. Encrypt Medicaid ID based on "Data Use Agreement" |
| 6.2.2 | num_icn | nw_claim_ub92_leg/nw_claim_phys_leg | Character | 13 | This represents the unique internal control number for a Medicaid claim |

### 6.3 MassHealth Pharmacy Claims Data

| Req# | Field Name | Table | Type | Length | Description |
|---|---|---|---|---|---|
| 6.3.1 | num_icn | nw_claim_phrm_leg | Character | 13 | This represents the unique internal control number for a Medicaid claim |
| 6.3.2 | num_dtl | nw_claim_phrm_leg | Number | 9 | Interchange number of a detail line on a claim |

### 6.4 Encounter Claims Data

This file contains both Medical and Pharmacy claims. Claim Type: M, O, P, D, L, and L are included.

| Req# | Field Name | Table | Type | Length | Description |
|---|---|---|---|---|---|
| 6.4.1 | id_medicaid | nw_member | Character | 12 | Unique identifier for the member. Encrypt Medicaid ID based on "Data Use Agreement" |
| 6.4.2 | cde_enc_mco | nw_encounter | Character | 3 | 3-letter Code that indicates the Managed Care Entity |

### 6.5 MCO Capitation Data

This file will contain monthly capitation payment and PCPR payment for those members listed in Member with Eligibility data file. PCPR payment can be identified where cde_rate_cell = 'PCR'. Code Payment Type Managed Care = 'C'

| Req# | Field Name | Table | Type | Length | Description |
|---|---|---|---|---|---|
| 6.5.1 | id_medicaid | nw_managed_care_hist | Number | 10 | Unique identifier for the member. Encrypt Medicaid ID based on "Data Use Agreement" |
| 6.5.2 | bill_pidsl | nw_provider | Character | 10 | Provider ID and service location for the billing provider |

### 6.6 MassHealth Provider Data

MassHealth provider details associated with MassHealth Claims, Pharmacy, and MCO capitation are included in the respective files.

### 6.7 Encounter Provider Data

Encounter provider details associated with MassHealth Claims, Pharmacy, and MCO capitation are included in the respective files.

### 6.8 Member High Risk and Chronic Condition Data by Year – Phase 2

| Req# | Field Name | Table | Type | Length | Description |
|---|---|---|---|---|---|
| 6.8.1 | id_medicaid | nw_member | Character | 12 | Unique identifier for the member. Encrypt Medicaid ID based on "Data Use Agreement" |
| 6.8.2 | risk_score_concurrent | Derived | binary_double | - | For example: 0.335 |

---

## Code and Description Reference

### 7.1 Claim Types (CDE_CLM_TYPE)

| Code | Description |
|---|---|
| A | INPATIENT PART A CROSSOVER UB92 |
| B | PROFESSIONAL PART B CROSSOVER |

### 7.2 Race Codes (CDE_RACE)

| Code | Description |
|---|---|
| ASIAN | ASIAN OR PACIFIC ISLANDER |
| BLACK | BLACK-NOT OF HISPANIC ORIGIN |

### 7.3 Admit Source Code (CDE_ADMIT_SOURCE)

| Code | Description |
|---|---|
| 1 | NON-HEALTH CARE FACILITY POINT OF ORIGIN |
| 2 | CLINIC OR PHYSICIANS OFFICE |

### 7.4 Priority Code (CDE_PRIORITY)

| Code | Description |
|---|---|
| 1 | EMERGENCY |
| 2 | URGENT |

### 7.5 Billing Frequency (CDE_BILL_FREQ)

| Code | Description |
|---|---|
| 0 | Nonpayment/zero claim |
| 1 | Admit through discharge claim |

### 7.6 Encounter MCO Code (CDE_ENC_MCO)

| Code | Description |
|---|---|
| BMC | Boston Medical Center |
| CAR | Celticare |

### 7.7 Special Characters

| Character | Meaning |
|---|---|
| + | Missing |
| - | Error |
| # | N/A |

### 7.8 Place of Service (CDE_PLACE_OF_SERVICE)

| Code | Description |
|---|---|
| 01 | PHARMACY |
| 03 | SCHOOL |

---

## Stakeholders and Approvers

The program team, HIE team, and EOHHS Data Warehouse have reviewed and acknowledged that the above defined requirements specification meets the criteria of supporting Pilot ACO CQM business requirement needs. Approval of this document acknowledges mutual understanding of requirements defined in this document through the JADs (joint application development), and that requirements will be developed and implemented by the DW team. All BRDs (Business Requirement Documents) for all three work streams will be developed by HIE Business Analyst and will be reviewed for DW BAs/SMEs.

### 8.1 Stakeholders

| Name | Role | Notes |
|---|---|---|
| Julie Fondurulia | Principal Analytics Implementation Mgr | Requestor |
| Bill Thomason | Operations Manager • Data Warehouse | |
| Bill Kearney | Data Warehouse Analyst II | Owner |
| Laurie DeVries | Business Analyst | |
| Rima Kayyali | App Dev & Support Supervisor | |
| Arun Chaudhari | EA/ACO Lead/SME, Data Warehouse | |
| Ming Luo | Software Engineer | |
| Naveen Yadla | Data Engineer | |
| Marty McCrory | Data Strategy Program Manager | Reporter |

### 8.2 Approvers

| Name | Role | Approved (Y/N) | Approval Date | Notes |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

**Document Owner:** Laurie DeVries  
**Last Updated:** May 28, 2026  
**Status:** Draft