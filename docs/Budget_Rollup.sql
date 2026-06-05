SELECT   prvgrps.ROLLUP_KEY_NAME,

           prvgrps.ROLLUP_KEY_VALUE CDE_PROV_TYPE,

           prvgrps.ROLLUP_NAME,

           prvgrps.ROLLUP_VALUE CDE_PROV_BUDGET_GROUP,

           provgrps.ROLLUP_VALUE DSC_PROV_BUDGET_GROUP,

           offgrps.ROLLUP_VALUE DSC_PROV_BUDGET_OFFICE

    FROM         MHDWPROD.NW.NW_USER_ROLLUP prvgrps

              LEFT OUTER JOIN

                 MHDWPROD.NW.NW_USER_ROLLUP provgrps

              ON (    prvgrps.ROLLUP_VALUE = provgrps.ROLLUP_KEY_VALUE

                  AND 'CDE_PROV_BUDGET_GROUP' = provgrps.ROLLUP_KEY_NAME

                  AND 'DSC_PROV_BUDGET_GROUP' = provgrps.ROLLUP_NAME)

           LEFT OUTER JOIN

              MHDWPROD.NW.NW_USER_ROLLUP offgrps

           ON (    prvgrps.ROLLUP_VALUE = offgrps.ROLLUP_KEY_VALUE

               AND 'CDE_PROV_BUDGET_GROUP' = offgrps.ROLLUP_KEY_NAME

               AND 'DSC_PROV_BUDGET_OFFICE' = offgrps.ROLLUP_NAME)

   WHERE   prvgrps.ROLLUP_KEY_NAME = 'CDE_PROV_TYPE'

           AND prvgrps.ROLLUP_NAME = 'CDE_PROV_BUDGET_GROUP'

ORDER BY   prvgrps.ROLLUP_VALUE, prvgrps.ROLLUP_KEY_VALUE