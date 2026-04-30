# AE318 Chapter 5 Extract — Wings and Fuselages with Structurally Significant Skin (Idealized Beams)

Source: `/home/devel/electrical_notes/content/ae318/AE318_export/AE318_Chapter 5_Textbook_Pages.pdf` (60 pages, internally numbered 5.1 – 5.66 with gaps).

Pages **5.14, 5.15, 5.16** are missing from the scan (the PDF jumps from page 5.13 to page 5.17). Several pages contain hand‑written derivations only (5.11, 5.13, 5.28, 5.48, 5.49, 5.57, 5.60, 5.61) — what is legible has been captured below. The PDF ends at page 5.66 (Example 5.3.1 result diagram); the chapter file does **not** include a stand‑alone "Problem 5.5" page — see note in §4 below.

---

## 1. Section Structure

| Section | Page | Topic |
|---|---|---|
| Chapter 5 (intro) | 5.1 | Why structurally significant skin matters; overview |
| **5.1 Idealization of Beam Cross‑Sections** | 5.1 – 5.16 | Stringer/web idealization assumptions; effective stringer area; 30×thickness rule (compression) and rivet‑to‑rivet rule (tension); Examples 5.1.1 and 5.1.2 |
| **5.2 Idealized Cross‑Section Beams Under Transverse Loading — Straight Webs / Open Cross‑Sections** | 5.17 – 5.46 | Shear panels; analysis steps (axes, centroid, I‑values, internals, σ, q); shear center; cutouts; Examples 5.2.1 and 5.2.2 |
| **5.3 Idealized Cross‑Section Beams Under Transverse Loading — Curved Webs / Closed Cross‑Sections** | 5.47 – 5.66 | Curved‑web shear flow; single‑cell vs multi‑cell; statically determinate vs indeterminate; $M_O = 2Aq$; Example 5.3.1 |

---

## 2. Named Equations

### 2.1 Idealization formulas (§5.1)

**(Eq. 5.1.1) 30× Thickness Rule** — width of web effective with each stiffener under compression:
$$w_{web} = 30\,t_{web}$$
applied around each rivet as $15 t_{web}$ on each side of the rivet centerline.

**(Eq. unnumbered, p. 5.9) Effective area, web in compression:**
$$A_{eff} = A_{z\text{-}beam} + \big[30\,t_{skin}\big]\,t_{skin}$$
with $w_{skin} = 30\,t_{skin}$, capped by available skin width.

**(Eq. unnumbered, p. 5.9) Effective area, web in tension:**
$$A_{eff} = A_{z\text{-}beam} + \tfrac{1}{2}\big(A_{web}\big)_{\text{Rivet-to-Rivet, Left}} + \tfrac{1}{2}\big(A_{web}\big)_{\text{Rivet-to-Rivet, Right}}$$

Variables: $t_{web},\,t_{skin}$ = web/skin thickness; $A_{z\text{-}beam}$ = actual stringer area; $A_{web}$ = web cross‑sectional area between adjacent rivets.

### 2.2 Section properties for idealized cross‑sections (§5.2, p. 5.26)

**(Eq. 5.2.1) I‑values for idealized cross‑sections** (parallel‑axis portion only; local stringer I neglected):
$$I_y = \sum_i A_i\,(z_i)^2 \qquad I_z = \sum_i A_i\,(y_i)^2 \qquad I_{yz} = \sum_i A_i\,y_i\,z_i$$

**Centroid (composite cross‑section, only $A_\sigma$ areas count):**
$$\bar{y} = \frac{\sum_i \bar{y}_i A_i}{\sum_i A_i} \qquad \bar{z} = \frac{\sum_i \bar{z}_i A_i}{\sum_i A_i}$$

Variables: $A_i$ = effective stringer area $i$ ($A_\sigma$ only — shear‑panel‑edge $A_\alpha$ areas are excluded from centroid and I computations); $y_i, z_i$ = centroidal coordinates of stringer $i$.

### 2.3 General Flexure Formula for Unsymmetric Bending (§5.2, Eq. 4.1.24, used on p. 5.29)

$$\boxed{\;\sigma_x \;=\; \frac{-\,y\,\bigl(I_y M_z + I_{yz} M_y\bigr) \;+\; z\,\bigl(I_{yz} M_z + I_z M_y\bigr)}{I_y I_z - (I_{yz})^2}\;}$$

When $M_y = 0$ this reduces to
$$\sigma_x = -y\,\frac{I_y M_z}{I_y I_z - I_{yz}^2} + z\,\frac{I_{yz} M_z}{I_y I_z - I_{yz}^2}$$

Variables: $\sigma_x$ = normal bending stress at point $(y,z)$ on cross‑section; $M_y, M_z$ = internal bending moments about centroidal $y$ and $z$ axes; $I_y, I_z, I_{yz}$ as above; $y, z$ = coordinates of point in centroidal axes.

**(Eq. 5.2.2) Result of plugging Example 5.2.1 numbers into Eq. 4.1.24:**
$$\sigma_x = -(6{,}341)\,y - (1{,}087)\,z \quad [\mathrm{psi}]$$
(negative = compression; positive = tension).

### 2.4 Neutral‑Axis Equation for Unsymmetric Bending

The neutral axis is the locus where $\sigma_x = 0$. Setting Eq. 4.1.24 to zero and solving:
$$y\bigl(I_y M_z + I_{yz} M_y\bigr) = z\bigl(I_{yz} M_z + I_z M_y\bigr)$$
$$\boxed{\;\Bigl(\tfrac{y}{z}\Bigr)_{\!NA} \;=\; \frac{I_{yz} M_z + I_z M_y}{I_y M_z + I_{yz} M_y}\;}$$
The slope of the NA on the cross‑section is the ratio above; it is independent of moment magnitude (only the ratio $M_y/M_z$ matters).

### 2.5 General Shear‑Flow Formula (§5.2, Eq. 4.1.24's companion 4.4.11; used pages 5.32, 5.43, 5.62)

For thin‑walled beams (idealized **and** non‑idealized — they share the same formula; only $A'$ choice differs):
$$\boxed{\;q_{out} - q_{in} \;=\; \frac{\bigl(I_y V_y - I_{yz} V_z\bigr)\,\bar{y}'\,A' \;+\; \bigl(-I_{yz} V_y + I_z V_z\bigr)\,\bar{z}'\,A'}{I_y I_z - (I_{yz})^2}\;}$$

For **non‑idealized** sections, $A'$ is the running area along the web from a chosen origin, and $\bar y', \bar z'$ are the centroidal coordinates of $A'$. The magnitude of $q$ varies linearly or parabolically along the web.

For **idealized** sections, $A' = $ area of a single stringer (the simplest choice), $\bar y', \bar z'$ are the coordinates of that stringer, and **$q$ is constant between successive stringers** (it does not change as it flows through an $A_\alpha$ web area).

Variables: $q_{in}, q_{out}$ = shear flow flowing into / out of the chosen $A'$; $V_y, V_z$ = internal shear forces along centroidal $y, z$; $A'$ = chosen stringer area (idealized) or running web area (non‑idealized); $\bar y', \bar z'$ = $y, z$ of $A'$'s centroid.

### 2.6 Shear‑Center Location

The shear center is the unique point through which the resultant transverse shear must act for the beam to bend without twisting. Procedure used in Example 5.2.2 (pp. 5.41 – 5.46):

1. Apply the General Shear Flow Formula leaving $V_y$ and $V_z$ as symbolic variables — the shear‑center location is independent of force magnitude.
2. Compute each $q$ as a linear combination of $V_y$ and $V_z$ (Eqs. 5.2.7 – 5.2.10 in the text).
3. Take moment equivalence about a convenient corner (here D) for the two equivalent interior faces:
$$e_z V_y + e_y V_z \;=\; -\sum_i q_i L_i d_i$$
where $L_i$ is the length of web segment $i$ and $d_i$ is the perpendicular moment arm from the reference point.
4. The result must hold for arbitrary $V_y, V_z$, so the coefficients of $V_y$ and of $V_z$ each vanish independently — yielding two equations for $(e_y, e_z)$.

For Example 5.2.2:
$$\boxed{\;e_y = 3.916''\,,\qquad e_z = -6.175''\;}$$
(measured from a chosen reference corner of the cross‑section).

### 2.7 Sign Conventions for $V_y, V_z, M_y, M_z$ (Step 1 of every analysis)

- **Axes:** the cross‑section view is drawn so that the $x$‑axis points **into the page**; $y$ is upward; $z$ completes a right‑handed triad (here pointing to the right).
- **Internal shear $V$:** positive $V_y$ acts in $+y$ on Interior Face 2 (the cut face whose outward normal is $+x$) and in $-y$ on Interior Face 1. Same convention for $V_z$.
- **Internal moment $M$:** positive $M_z$ follows the right‑hand rule about $+z$; positive $M_y$ likewise about $+y$. In Example 5.2.1, $V_y = -1{,}000\,\mathrm{lb}$ and $M_z = +60{,}000\,\mathrm{in\!\cdot\!lb}$ at the wall (note $V_y$ negative because the 1000 lb up force on the free end produces internal $V_y$ pointing $-y$ on Interior Face 2 by equilibrium; "thumb is z" right‑hand‑rule check).
- **Shear flow $q$:** drawn as an arrow on each web segment between successive stringers; assumed direction must be shown on Interior Face 2 figure; a negative $q$ value means actual direction is opposite the assumed direction. Strictly $q$ acts on the web edge perpendicular to the cross‑section, but the textbook uses a "short‑cut" arrow connecting two stringers (Figure 5.2.5) with the more rigorous version (Figure 5.2.6) showing arrows on the web edges.

### 2.8 Closed‑Section Torsion Relation (§5.3)

For a closed cell with constant shear flow $q$ around the cell:
$$\boxed{\;M_O = 2 A q\;}$$
where $A$ = enclosed area of the cell (the "cell area"), $M_O$ = moment of $q$ about any point $O$ in the plane of the cross‑section. Direction of $q$ (CW vs CCW around the cell) determines the sign.

**Curved‑web shear (force resultant of $q$ on a curved segment):**
For a curved segment from one endpoint to another with straight chord length $L$ ($L_y$ and $L_z$ are the $y$‑ and $z$‑projections of the chord):
$$V_y = q\,L_y \qquad V_z = q\,L_z$$
The direction of $V$ on the cell relative to the chord is at angle $\beta$ with $\tan\beta = V_y/V_z = L_y/L_z$ (text page 5.49).

---

## 3. Worked Examples

| # | Title | Cross‑section | Solves for |
|---|---|---|---|
| **5.1.1** (p. 5.10) | Cross‑Section Idealization | Z‑beam stiffener attached to skin by single rivet row, **compression** | Effective stringer area $A_{eff}$ via 30× rule. Result on hand‑work page: $A_{eff} \approx 0.213\,\mathrm{in}^2$ |
| **5.1.2** (p. 5.12) | Cross‑Section Idealization | J‑beam stiffener: double row of rivets to skin, single row to vertical spar web; all under **compression** | Effective area combining contributions from skin and spar web (subject to available width); hand‑work shows partial result $A_{eff} \approx 0.421$ in² |
| **5.2.1** (p. 5.21) | Transverse Loading of Idealized Open Cross‑Section Beam | 60" cantilever, "C"‑shape of 4 stringers (A=0.5, B=0.3, C=0.2, D=0.2 in²) on 4"×6" rectangle, web $t=0.035$"; 1000 lb tip load | (a) σ at each stringer at the wall; (b) shear flows + diagram; (c) location $e$ for no‑torsion; (d) shear‑center location |
| **5.2.2** (p. 5.41) | Shear Center for Idealized Open Cross‑Section Beams | Same cross‑section as 5.2.1 | Shear‑center coordinates $(e_y, e_z) = (3.916'', -6.175'')$ |
| **5.3.1** (p. 5.56) | Transverse Loading of Idealized Closed Cross‑Section Beam | 180" cantilever, single‑cell stadium shape (rectangle $7''\times 8''$ flanked by two semicircles, total $z$‑span $10''$); 4 stringers (A=0.1, B=0.1, C=0.2, D=0.3 in²), web $t=0.040''$; tip loads $V_y = 500\,\mathrm{lb}$, $V_z = 700\,\mathrm{lb}$ | Shear flows in each web at the wall. Final results: $q_{AB}=27.58$, $q_{BC}=22.42$, $q_{CD}=42.43$, $q_{AD}=40.07$ lb/in (with computed torque $T = 1{,}843$ in·lb about centroid) |

---

## 4. Note on "Problem 5.5"

The PDF supplied is the **textbook chapter** (§§5.1–5.3 with Examples 5.1.1, 5.1.2, 5.2.1, 5.2.2, 5.3.1). The pages end at 5.66 with the Example 5.3.1 answer diagram and **do not include numbered end‑of‑chapter problems**.

Throughout the chapter the text directs the reader: *"You should now have the ability to do Problem 5.2"* (p. 5.35) and *"You should now have the ability to do Problem 5.3"* (p. 5.46). A "Problem 5.5" mentioned elsewhere on the exam is therefore **not contained in this PDF** — it must be in the chapter‑5 problem set (a separate file). The closed‑section single‑cell stadium geometry of Example 5.3.1 is the most likely template Problem 5.5 builds on (4 stringers, 2 semicircular ends, transverse $V_y$ and $V_z$).

If the exam's Problem 3 references "Problem 5.5" the relevant geometry/load template — based on the example that immediately precedes it — is:

- Closed single‑cell idealized beam, statically determinate.
- Stadium / "tic‑tac" cross‑section: rectangular center web with semicircular caps left and right.
- 4 stringers, one at each corner of the rectangular center; both transverse loads $V_y$ and $V_z$ may be present.
- Solve via General Shear Flow Formula (Eq. 4.4.11) for $q_{AB}-q_{AD}$, $q_{BC}-q_{AB}$, $q_{CD}-q_{AD}$, then close the system using $M_O = 2Aq$ moment equivalence about an interior point.

(If the exam's Problem 5.5 has a different geometry, fetch the AE318 chapter‑5 problem PDF — it is not in this textbook scan.)

---

## 5. Sign and Figure Conventions

- **Coordinate frame.** $x$ along the beam span, pointing from wall to free end on the **span view**, but pointing **into the page** on every **cross‑section view**. $y$ vertical, $z$ horizontal — right‑handed.
- **Interior Face 1 vs Interior Face 2.** When a cut is made through the beam, the two exposed faces are labeled. Interior Face 2 is the face whose outward normal is $+x$ (the face seen when looking down the span from wall toward tip). The cross‑section diagrams in §§5.2 and 5.3 are drawn for Interior Face 2.
- **Effective stringers** drawn as filled circles ($A_\sigma$); **idealized webs / shear panels** drawn as single lines along the centerline of the original webbing ($A_\alpha$).
- **Shear flow arrows** are drawn between successive stringers in the assumed direction; a negative answer means the actual direction is opposite the arrow shown.
- **Closed‑cell area $A$** in $M_O = 2Aq$ is the **enclosed** area of the cell; for the stadium of Example 5.3.1 with rectangle $7\times 8$ and two semicircles of diameter $8$: $A = 7\cdot 8 + \pi(4)^2 = 56 + 16\pi$.
- **Open‑section idealized beams cannot resist torsion.** Therefore the load *must* be applied at the shear center for small‑deflection theory to hold. **Closed‑section beams** can resist torsion, so loads need not pass through the shear center.

---

## 6. Summary / Boxed Statements (verbatim)

**(p. 5.2) Box: $A_\alpha$ Areas.** "Assumption 2 causes the web thicknesses to be $A_\alpha$ cross‑sectional areas."

**(p. 5.7) Recall box.**
- For Non‑Idealized Cross‑Sections, the magnitude of $q$ varies linearly or parabolically as it "flows" along the $A_\sigma$ cross‑sectional web length.
- For Idealized Cross‑Sections, the magnitude of $q$ = constant as it "flows" along the $A_\alpha$ cross‑sectional web length.

**(p. 5.31) Idealized $q$ box.** "All $q$'s between successive stringers have the same magnitude since they are flowing through an $A_\alpha$ area."

**(p. 5.32) Choice of $A'$ box.** "For Idealized Cross‑Sections, the simplest method is to always choose $A'$ as the area of a single stringer."

**(p. 5.37) Summary box.**
- *Shear Center.* Point on a beam cross‑section at which the transverse forces must be applied so that the beam is bent but not twisted.
- *Open Cross‑Section Beams.* Open cross‑section beams cannot resist torsion. Hence, they cannot be allowed to twist. Therefore, open‑section beams **must** have the transverse forces applied at the shear center.
- *Closed Cross‑Section Beams.* Closed cross‑section beams can resist torsion very well. Hence they can be allowed to twist. Therefore, closed‑section beams **may** have the transverse forces applied away from the shear center.

**(p. 5.47) Curved‑web $q$ box.** "The magnitude of $q$ is constant since this is an idealized cross‑section and the magnitude of $q$ does not change as it moves through an $A_\alpha$ area. However, we see that the direction of $q$ is now changing since the webbing is curved."

**(p. 5.55) Determinacy.**
- Single‑Cell idealized beams are statically **determinate**.
- Multi‑Cell idealized beams are statically **indeterminate** (the additional interior webs are redundant members).

---

## 7. Key Idealization Rules Used in This Text (§5.1, p. 5.7)

Two — and only two — idealization rules are used:
1. **Web in compression:** 30× thickness rule (§5.1.1); $w_{web} = 30\,t_{web}$, applied as $15\,t_{web}$ each side of every rivet centerline.
2. **Web in tension:** include all rivet‑to‑rivet web area, half to each adjacent stringer.

The *Effective Stringer Area* is then placed at the centroid of the new combined area, along the centerline of the webbing.

