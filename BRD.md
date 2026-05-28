# Business Requirements Document
## Provider Budget Groups Update for New MMIS Provider Types

**Document Version:** 1.0  
**Date:** May 28, 2026  
**Status:** Active  

---

## 1. Executive Summary

Three new provider types were added to MMIS in November and require the addition of corresponding budget provider groups. This update establishes dedicated budget provider groups (C6, C7, C8) for these new provider types across the nw_provider and related family of tables/views. Currently, these provider types are set to "xx" and need to be configured with their proper budget group assignments and office designations.

---

## 2. Background and Context

### Current State
- Three new provider types were added to MMIS in November
- These provider types are currently assigned to budget provider group "xx" (placeholder)
- The provider types do not have dedicated budget groups in the nw_provider and related tables/views

### Business Need
- Provider Budget Groups are required for proper budget tracking and allocation
- Budget department has determined that these provider types should each have their own dedicated group
- Proper categorization enables accurate financial reporting and budget management by provider type

---

## 3. Requirements

### 3.1 New Provider Budget Groups

| Provider Type | Budget Group Code | Description | Budget Office |
|---|---|---|---|
| HRSN | C6 | HEALTH-RELATED SOCIAL NEEDS - MCE ONLY | Office of Acute and Ambulatory Care |
| PACT | C7 | PROGRAM OF ASSERTIVE COMMUNITY TREATMENT | Office of Behavioral Health |
| Correctional Facilities | C8 | CORRECTIONAL FACILITIES | Office of Acute and Ambulatory Care |

### 3.2 Data Updates Required

The following must be updated in the nw_provider and family of tables/views:

1. **cde_prov_budget_group** field assignments:
   - HRSN provider type → C6
   - PACT provider type → C7
   - Correctional Facilities provider type → C8

2. **dsc_prov_budget_group** field assignments:
   - C6 → "HEALTH-RELATED SOCIAL NEEDS"
   - C7 → "PROGRAM OF ASSERTIVE COMMUNITY TREATMENT"
   - C8 → "CORRECTIONAL FACILITIES"

3. **dsc_prov_budget_office** field assignments:
   - C6 → "Office of Acute and Ambulatory Care"
   - C7 → "Office of Behavioral Health"
   - C8 → "Office of Acute and Ambulatory Care"

### 3.3 In Scope
- Creation of three new budget provider group codes (C6, C7, C8)
- Updates to nw_provider table
- Updates to related views in the nw_provider family
- Assignment of budget codes to new provider types

### 3.4 Out of Scope
- Retroactive updates to historical data
- Changes to existing provider types or budget groups
- Budget office restructuring or changes

---

## 4. Stakeholders

- **Budget Department** - Approval and validation authority
- **MMIS Team** - Implementation and testing
- **Data Management** - Database updates and table maintenance
- **Reporting/Analytics** - Budget reporting and tracking

---

## 5. Success Criteria

- [ ] All three new budget group codes (C6, C7, C8) are created
- [ ] Budget group codes are correctly assigned to respective provider types
- [ ] Descriptions are accurately populated for all codes
- [ ] Budget office assignments are correct per specifications
- [ ] Updates are reflected across nw_provider and all related views
- [ ] Data validation confirms no "xx" assignments remain for these provider types
- [ ] Budget reporting reflects accurate allocations by new provider type

---

## 6. Timeline and Priorities

- **Priority:** High
- **Target Completion:** [To be determined]
- **Dependencies:** Budget department approval and provider type confirmation

---

## 7. Technical Considerations

- Database tables affected: nw_provider and family of tables/views
- Fields to be modified:
  - cde_prov_budget_group
  - dsc_prov_budget_group (if applicable)
  - dsc_prov_budget_office
- Testing required: Data validation, view refresh, reporting verification
- Documentation: Update data dictionary and system documentation

---

## 8. Assumptions

- The three new provider types are already created in MMIS as of November
- Budget department has final approval authority
- The budget office assignments provided are final and definitive
- The nw_provider table structure supports the required updates

---

## 9. Sign-Off

| Role | Name | Date | Signature |
|---|---|---|---|
| Budget Department | | | |
| Project Lead | | | |
| Technical Lead | | | |

---

## 10. Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | May 28, 2026 | Laurie DeVries | Initial BRD creation |
