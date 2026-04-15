// Lab 09 PT1: mp_apsr_to_ccs
//
// Derives the 10 condition-code suffix (CCS) values from the four APSR flags
// (N, Z, C, V) per the ARM condition-code table discussed in Lctr 19.
//
// Signed comparisons use the fact that after CMP rX, rY:
//   N == V  iff  (rX - rY) has non-negative signed value  iff  rX >= rY (signed)
// Unsigned comparisons use C ("no borrow" = rX >= rY unsigned) and Z.
//
// File: /opt/proj_mp/fo4b_ccs_n_cond_branch/src/fo4b_ccs_n_cond_branch_cfns.c

#include "fo4b_ccs_n_cond_branch_fns.h"

__attribute__((weak))
void mp_apsr_to_ccs(APSR_t apsr, CCS_t *pCcs) {
    // Equality (uses Z only)
    pCcs->EQ = apsr.Z;
    pCcs->NE = !apsr.Z;

    // Signed comparisons (use N and V, plus Z for LE / GT)
    pCcs->LT = (apsr.N != apsr.V);
    pCcs->LE = apsr.Z || (apsr.N != apsr.V);
    pCcs->GE = (apsr.N == apsr.V);
    pCcs->GT = !apsr.Z && (apsr.N == apsr.V);

    // Unsigned comparisons (use C and Z)
    pCcs->LO = !apsr.C;
    pCcs->LS = !apsr.C || apsr.Z;
    pCcs->HS = apsr.C;
    pCcs->HI = apsr.C && !apsr.Z;
}
