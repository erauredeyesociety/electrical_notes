# AE318 Test 3 — Lecture Extracts (Part 1)

Source PDFs: `content/ae318/AE318_export/AE318 <date> 2026 lecture slides.pdf`. Topics span Sections 4.1 (General Flexure Formula), 4.2 (Largest Bending Stress), 4.3 (Shear Stresses in Thin-Walled Beams), 4.4 (Shear Flow). Many slides have hand-drawn (blue/green/red ink) annotations on top of typeset content; transcribed below where legible.

## Lecture 2026-02-27 — 4.1 General Flexure Formula (derivation)

- Recap simplified flexure: $\sigma_x = \dfrac{My}{I}$, special case $\sigma_x = -\dfrac{M_z y}{I_z}$.
  - $M_z$: applied moment about $z$.
  - $y$: distance of differential area element above/below neutral axis (which lies in the $z$ direction).
  - $I_z$: area moment of inertia about $z$ (resistance to rotation about $z$).
- Simplified form valid only when (1) applied moment is strictly about $z$ and (2) cross-section is symmetric in $y$ or $z$.
- Setup: beam along $x$, pure bending (no axial, no torsion); two equal/opposite couples $\bar{M}_0$ with components $M_{0y}, M_{0z}$ in the $y$-$z$ plane.
- Cutting beam exposes internal moments; $M_y = -M_{0y}$, $M_z = -M_{0z}$ (sign convention: internal components opposite end couples).
- Stress resultants at interior face:
  - $M_y = \int_A z\,\sigma_x\,dA$
  - $M_z = -\int_A y\,\sigma_x\,dA$
- Pure-bending kinematics: take infinitesimal slice $dx$; line $\overline{CS}$ on $x$-axis (length $dx$) bends to arc of radius $R$, parallel line $\overline{HG}$ at offset $a$ bends to arc of radius $R+a$. Centers of curvature ($D, E$) of all fibers lie on a common line (artifact of pure bending).
- Hooke's law $\sigma_x = E\varepsilon_x = E\,\delta/L$. Applied to $\overline{HG}$: $\sigma_x = E\dfrac{(R+a)d\theta - dx}{dx}$.
- Assume $\overline{CS}$ undeformed $\Rightarrow dx = R\,d\theta$, giving $\sigma_x = E\dfrac{a}{R}$.
- Geometry of pie slice viewed along $x$: $a = z\cos\phi - y\sin\phi$, where $\phi$ is angle of pie slice with $y$-$z$ plane.
- Substituting: $\sigma_x = E\!\left[-\dfrac{\sin\phi}{R}y + \dfrac{\cos\phi}{R}z\right]$.
- Define $B_1 = \dfrac{\sin\phi}{R}$, $B_2 = \dfrac{\cos\phi}{R}$ $\Rightarrow \sigma_x = -EB_1 y + EB_2 z$.
- Plug into $M_y$, $M_z$ integrals; recognize $\int_A z^2 dA = I_y$, $\int_A y^2 dA = I_z$, $\int_A yz\,dA = I_{yz}$ (area product of inertia).
  - $M_y = EB_2 I_y - EB_1 I_{yz}$
  - $M_z = EB_1 I_z - EB_2 I_{yz}$
- Solve for $B_1, B_2$:
  - $B_1 = \dfrac{I_y M_z + I_{yz} M_y}{E(I_y I_z - I_{yz}^2)}$
  - $B_2 = \dfrac{I_{yz} M_z + I_z M_y}{E(I_y I_z - I_{yz}^2)}$
- **General Flexure Formula:**
  $$\sigma_x = \dfrac{-y\,(I_y M_z + I_{yz} M_y) + z\,(I_{yz} M_z + I_z M_y)}{I_y I_z - I_{yz}^2}$$
- Neutral-axis location: $\overline{CS}$ has zero strain $\Rightarrow \sigma_x = 0$ where $y = \dfrac{B_2}{B_1} z$. NA makes angle $\tan^{-1}(B_2/B_1)$ with the horizontal ($z$-axis).
- Pure-bending net axial force on cross-section is zero: $\int_A \sigma_x\,dA = 0 \Rightarrow B_2 \int_A z\,dA - B_1 \int_A y\,dA = 0$. Using $\int z\,dA = A\bar z$, $\int y\,dA = A\bar y$: $B_2 \bar z - B_1 \bar y = 0$. This is the same line as the NA $\Rightarrow$ **NA passes through the centroid**; place origin at centroid so $\bar y = \bar z = 0$.
- Simplifications:
  - $M_y=0$: $\sigma_x = \dfrac{(-yI_y + zI_{yz})M_z}{I_y I_z - I_{yz}^2}$
  - $M_z=0$: $\sigma_x = \dfrac{(-yI_{yz} + zI_z)M_y}{I_y I_z - I_{yz}^2}$
  - $I_{yz}=0$: $\sigma_x = \dfrac{-yI_y M_z + zI_z M_y}{I_y I_z}$
  - $M_z=0$, $I_{yz}=0$: $\sigma_x = \dfrac{zM_y}{I_y}$
  - $M_y=0$, $I_{yz}=0$: $\sigma_x = -\dfrac{yM_z}{I_z}$ (familiar form).
- "$My/I$" is valid whenever applied moment direction aligns with a **principal axis** of the cross-section (i.e. $I_{yz}=0$) — the symmetric-cross-section requirement is over-strong; the real requirement is principal-axis alignment.

## Lecture 2026-03-02 — 4.1 General Flexure Formula (Z-beam example)

- Worked example: cantilevered Z-beam (aircraft stiffener riveted to skin). Cross-section: top horizontal flange of length $9/16$" at top, vertical web of height $1$", bottom horizontal flange of length $9/16$" offset to left. Wall thickness $t = 0.064$". Tip loads: $900\;\mathrm{in\cdot lb}$ along $+z$ and $500\;\mathrm{in\cdot lb}$ along $-y$.
- Symmetry: section has point (rotational) symmetry about its centroid only — no axis of symmetry.
- Tasks: (a) $\sigma_x$ over cross-section; (b) NA equation; (c) sketch stress distribution.
- Plug into general formula $\sigma_x = \dfrac{-y(I_y M_z + I_{yz} M_y) + z(I_{yz} M_z + I_z M_y)}{I_y I_z - I_{yz}^2}$.
- Four-step procedure (textbook misses Step 3's "place at centroid"):
  1. Choose axes: $x$ into page (along beam), $y$ up $\Rightarrow z$ to the right.
  2. Locate centroid using temporary $y_{Temp}, z_{Temp}$ axes at lower-left.
  3. Place coordinate frame at centroid; compute $I_y, I_z, I_{yz}$ via parallel-axis theorem.
  4. Determine internal moment components on the chosen face.
- Centroid (3 segments — top flange, web, bottom flange):
  - Areas: top flange $A_1 = 0.036\;\mathrm{in}^2$, web $A_2 = 0.05581\;\mathrm{in}^2$, bottom flange $A_3 = 0.036\;\mathrm{in}^2$. Total $A = 0.1278\;\mathrm{in}^2$.
  - $\bar y = 0.5"$, $\bar z = 0.5305"$.
- Moments / product of inertia (parallel-axis $I = \tfrac{bh^3}{12} + Ad^2$):
  - $I_y = 0.006392\;\mathrm{in}^4$
  - $I_z = 0.01933\;\mathrm{in}^4$
  - $I_{yz} = 0.008400\;\mathrm{in}^4$
- Internal moments on "Interior Face 1" (free-end face): $M_y = +500\;\mathrm{in\cdot lb}$, $M_z = -900\;\mathrm{in\cdot lb}$.
- Substitute: $\sigma_x = (29{,}300)\,y + (39{,}720)\,z$ (psi, with $y, z$ in in).
- Sanity check: upper-right corner has $+y, +z \Rightarrow$ tension; lower-left has $-y, -z \Rightarrow$ compression. Choosing Interior Face 2 reverses signs.
- (b) NA: set $\sigma_x=0 \Rightarrow 29300y + 39720z = 0 \Rightarrow y = -1.356 z$. Angle with $z$-axis: $\tan^{-1}(-1.356) = -53.39^\circ$.
- (c) Stress distribution is a plane in $(y,z,\sigma_x)$. Critical points: top-right corner $(0.5,\,0.5305)$ gives $\sigma_x = 35{,}721\;\mathrm{psi}$ (max tension); bottom-left $(-0.5,\,-0.5305)$ gives $-35{,}721\;\mathrm{psi}$ (max compression). Slide labels stress values $\pm13{,}380, \pm14{,}050, \pm33{,}850, \pm35{,}720\;\mathrm{psi}$ at the four flange corners.

## Lecture 2026-03-04 — 4.2 Largest Bending Stress in Beams

- Question: in the general (unsymmetric) case, where on the cross-section is $|\sigma|$ maximum?
- Place rotated frame $y^*$-$z^*$ at the centroid such that $z^*$ lies along the NA. General formula in starred frame:
  $$\sigma_x = \dfrac{-y^*(I_{y^*} M_{z^*} + I_{y^*z^*} M_{y^*}) + z^*(I_{y^*z^*} M_{z^*} + I_{z^*} M_{y^*})}{I_{y^*} I_{z^*} - I_{y^*z^*}^2}$$
- NA condition: $\sigma_x=0$ when $y^*=0$ for all $z^* \Rightarrow I_{y^*z^*} M_{z^*} + I_{z^*} M_{y^*} = 0 \Rightarrow M_{y^*} = -\dfrac{I_{y^*z^*}}{I_{z^*}} M_{z^*}$.
- Sub back and simplify $\Rightarrow$ formula collapses to the simplified form
  $$\sigma_x = -\dfrac{y^* M_{z^*}}{I_{z^*}}$$
- Interpretation: **$\sigma_{\max}$ occurs at the point with the greatest perpendicular distance from the NA**, regardless of cross-section shape.
- Confirmed by Z-beam example: the two critical points (CP#1 top-right, CP#2 bottom-left) are exactly the two corners farthest from the NA line.
- Two ways the simple "$My/I$" form arises: (1) align $y$, $z$ with principal axes ($I_{yz}=0$); (2) align $z$ with the NA. Practical workflow: usually you must use general form to find the NA first, then can switch.

## Lecture 2026-03-06 — 4.3 Shear Stresses in Thin-Walled Beams

- Problem context: cantilevered I-beam, length $60$", tip load $1{,}400\;\mathrm{lb}$ downward; cross-section flange width $1.5$", total height $3$", uniform thickness $1/8$".
- Familiar formula $\tau = \dfrac{VQ}{Ib}$:
  - $\tau$: shear stress at point in cross-section.
  - $V$: shear force on entire cross-section.
  - $Q$: first moment of area of section above (or below) point of interest.
  - $I$: moment of inertia of entire cross-section.
  - $b$: thickness at the point of interest.
- Distribution is parabolic in $y$ in the web, zero at top/bottom of section, max at the NA midpoint.
- Assumption: $\tau$ constant across thickness (constant in $z$ at given $y$). Reality: $\tau$ varies parabolically in $z$ across web thickness; $\tau_{actual}$ peaks at the outer edges of the thickness, $(\tau_{xy})_{average} = VQ/(Ib)$.
- Thin-wall validity: $\tau_{largest}$ exceeds $\tau_{average}$ by $\le 0.8\%$ if $h > 4b$. For this I-beam: $h=2.75$", $b=1/8$" $\Rightarrow h = 22b$ $\Rightarrow$ assumption excellent.
- Convention: the $\tau$ being computed is $\tau_{xy}$ (shear on $x$-face in $y$-direction).
- Web $\tau_{xy}$ calculation:
  - Decompose section into 3 segments: top flange (1), web (2), bottom flange (3); $I_1 = I_3$.
  - $I = I_2 + 2I_1$ via parallel axis: $I_2 = \tfrac{(1/8)(3 - 2/8)^3}{12}$, $I_1 = \tfrac{1.5(1/8)^3}{12} + (1.5)(1/8)(1.5 - 1/16)^2$.
  - Result: $I = 0.9920\;\mathrm{in}^4$.
  - For point at height $y$ in web: section above = top flange + sliver of web from $(1.5 - 1/8)$ down to $y$. $Q = \bar y' A'$ via composite-centroid:
    - $\bar y_1 A_1 = (1.5 - \tfrac{1}{16})(1.5 \times \tfrac{1}{8})$
    - $\bar y_2 A_2 = \tfrac{(1.5 - 1/8) + y}{2}\,\bigl[(1.5 - 1/8 - y)\,\tfrac{1}{8}\bigr]$
  - Insert into $\tau_{xy} = VQ/(Ib)$:
    $$(\tau_{xy})_{Web} = (705.6)\bigl\{[(1.375)^2 - y^2] + 4.3125\bigr\}\;\mathrm{psi}$$
  - Max at $y=0$: $\tau_{xy,web,max} = 4{,}377\;\mathrm{psi}$. Min at $y = \pm 1.375$": $3{,}043\;\mathrm{psi}$.
- Flange $\tau_{xy}$ calculation:
  - Same $V$, $I$; here $b = 1.5$" and $\bar y' A' = \tfrac{1.5+y}{2}(1.5 - y)(1.5)$ for $y \in [1.375, 1.5]$.
  - $(\tau_{xy})_{Flanges} = (705.6)[(1.5)^2 - y^2]\;\mathrm{psi}$.
  - $\tau_{xy,flange} = 0$ at outer edge $y=1.5$"; peaks at inner edge $y=1.375$" giving $253.6\;\mathrm{psi}$.
- Plot of $\tau_{xy}(y)$: parabolic in web (max 4377, min 3043 psi), small parabolic bumps in flanges (max 253.6 psi). Web $\tau$ dominates — $\min(\tau_{xy,web}) > \max(\tau_{xy,flange})$ by factor 12.

## Lecture 2026-03-09 — 4.3 Shear Stresses (cont'd) and 4.4 Shear Flow intro

- Thin-wall convention: for any section with one dimension $\ll$ the other, **neglect the shear stress component pointing parallel to the thinner dimension**.
- For this I-beam: keep $\tau_{xy,web}$ and $\tau_{xz,flange}$; treat $\tau_{xz,web}$ and $\tau_{xy,flange}$ as negligible.
- Flange $\tau_{xz}$:
  - $V = 1400\;\mathrm{lb}$, $I = 0.9920\;\mathrm{in}^4$, $b = 1/8$".
  - For a horizontal cut at horizontal coordinate $z$ in upper flange, $\bar y' = (1.5 - 1/16)$ is constant; $A'$ varies with $z$: $A' = (0.75 - z)(1/8)$.
  - $(\tau_{xz})_{Flanges} = (2{,}029)\bigl[(0.75) - z\bigr]\;\mathrm{psi}$, with $z\in[0, 0.75]$ for right half.
  - Linear: $1521.5$ psi at midpoint $z=0$, zero at right edge $z=0.75$"; mirrored on the left half.
  - Note: $\tau_{xz,flange}$ exceeds $\tau_{xy,flange}$ by factor 6; $\min(\tau_{xy,web}) = 2\,\max(\tau_{xz,flange})$ — flange $\tau_{xz}$ is **not** negligible vs. web.
- Slide warns "Textbook depicts this incorrectly" for the flange $\tau_{xz}$ triangle.
- **Section 4.4 Shear Flow** introduced: $q = \tau \cdot b$, units lb/in. Inserting $\tau = VQ/(Ib)$ gives $q = VQ/I$ (no $b$).
- For constant-thickness cross-section, $\tau$ and $q$ are proportional, so $q$-distribution in I-beam is the $\tau$-distribution multiplied by $b=1/8$.
- Numerical $q$-values (lb/in): outer flange edges $q=0$ (free); inner flange ends $q = 1521.5/8 = 190.2$; web ends $q = 3043/8 = 380.4$; web midpoint $q_{max} = 4377/8 = 547.1$.
- Conservation observation: at the flange/web junction, $q$ flowing in from each flange half ($190.2$) sums to web $q$ ($380.4 = 2 \times 190.2$) — exactly fluid-flow continuity.
- Constant-thickness implies $q$-fluid-analogy holds for both $q$ and $\tau$. Variable thickness: analogy only holds for $q$.
- $\tau = VQ/(Ib)$ is a special case; derivation of **General Shear Flow Formula** begins:
  - Consider thin-walled cross-section with internal $V_y, V_z, M_y, M_z$ from a transverse load $w$.
  - Retain only shear flow perpendicular to thickness; parallel-to-thickness $q$ assumed negligible.
  - Cut a slice of length $dx$, take a sector bounded by free inner/outer walls and two cuts $A'$. Two $x$-faces carry $\sigma_x$ and shear flow; two cut faces carry $q_{in}$ and $q_{out}$.
  - $q$ assumed constant across $dx$, varies along circumference.
- Sum $F_x = 0$ on the sector:
  - $-q_{out}\,dx + q_{in}\,dx - \int_{A'}\sigma_x\,dA + \int_{A'}\!\bigl(\sigma_x + \tfrac{\partial\sigma_x}{\partial x}dx\bigr)dA = 0$
  - $\Rightarrow [q_{out} - q_{in}]\,dx = \int_{A'}\dfrac{\partial \sigma_x}{\partial x}\,dx\,dA$
  - $$\boxed{\;q_{out} - q_{in} = \int_{A'} \dfrac{\partial \sigma_x}{\partial x}\,dA\;}$$
- (Slide notes textbook uses a confusing "$\sigma$" subscript on $q$ in this derivation; can be ignored.)
- Justification for using General Flexure Formula despite non-pure bending: long slender beam ($L \gg$ section dim) makes flexure formula a good approximation; assumes $yz$ origin is on NA (centroid).

## Lecture 2026-03-13 — 4.4 Shear Flow (formula completion) + I-beam example

- Page 1: residual content from Mar 9 derivation (sketch of sector with $q_{in}, q_{out}, \sigma_x, \sigma_x + \partial\sigma_x/\partial x\,dx$ on the four faces; $A'$ finite, $dx$ infinitesimal).
- Untapered beam $\Rightarrow I_y, I_z, I_{yz}$ independent of $x$. Differentiate the General Flexure Formula:
  $$\dfrac{\partial \sigma_x}{\partial x} = \dfrac{-y\!\left[I_y \tfrac{\partial M_z}{\partial x} + I_{yz}\tfrac{\partial M_y}{\partial x}\right] + z\!\left[I_{yz}\tfrac{\partial M_z}{\partial x} + I_z\tfrac{\partial M_y}{\partial x}\right]}{I_y I_z - I_{yz}^2}$$
- Use shear/moment relations (derived end of textbook §4.4): $V_y = -\dfrac{dM_z}{dx}$, $V_z = \dfrac{dM_y}{dx}$.
  $$\dfrac{\partial \sigma_x}{\partial x} = \dfrac{-y\!\left[I_y(-V_y) + I_{yz}(+V_z)\right] + z\!\left[I_{yz}(-V_y) + I_z(+V_z)\right]}{I_y I_z - I_{yz}^2}$$
- Insert into the $q_{out} - q_{in}$ integral; use $\int_{A'} y\,dA = \bar y' A'$, $\int_{A'} z\,dA = \bar z' A'$.

  $$\boxed{\;q_{out} - q_{in} = \dfrac{(I_y V_y - I_{yz} V_z)\,\bar y' A' + (-I_{yz} V_y + I_z V_z)\,\bar z' A'}{I_y I_z - I_{yz}^2}\;}$$
  (**General Shear Flow Formula**.)
- Notation: $\bar y' A' = Q_z$, $\bar z' A' = Q_y$ (first moments of partial-area $A'$ about $z$, $y$).
- Simplifications:
  - $V_y=0$: $q_{out} - q_{in} = \dfrac{(\bar z I_z - \bar y I_{yz}) V_z A'}{I_y I_z - I_{yz}^2}$
  - $V_z=0$: $q_{out} - q_{in} = \dfrac{(\bar y I_y - \bar z I_{yz}) V_y A'}{I_y I_z - I_{yz}^2}$
  - $I_{yz}=0$: $q_{out} - q_{in} = \dfrac{\bar y I_y V_y A' + \bar z I_z V_z A'}{I_y I_z}$
  - $V_y=0$, $I_{yz}=0$: $q_{out} - q_{in} = \dfrac{V_z Q_y}{I_y}$
  - $V_z=0$, $I_{yz}=0$: $q_{out} - q_{in} = \dfrac{V_y Q_z}{I_z}$ — recovers familiar $\tau = VQ/(Ib)$ form.
- Pages 4-12 of the Mar 13 PDF revisit the I-beam shear flow numerical sketch (190.2, 380.4, 547.1 lb/in arrows along the cross-section showing the fluid-flow continuity at junctions) and the sector free-body for the derivation. These sketches reproduce content already itemized under Mar 9.

## Lecture 2026-03-23 — 4.4 Shear Flow (formula recap) + transition to shear center

- Slide 1: rewrites $\partial\sigma_x/\partial x$ using $V_y = -dM_z/dx$, $V_z = dM_y/dx$ (mirrors Mar 13 slide).
- Slide 2: substitutes into Mar-13 boxed equation $q_{out} - q_{in} = \int_{A'}\partial\sigma_x/\partial x\,dA$ and rearranges using $\int_A y\,dA = Q_z = \bar y A$, $\int_A z\,dA = Q_y = \bar z A$.
- Slide 3: states the **General Shear Flow Formula** in its boxed form (same as Mar 13) and lists the same 5 simplification cases. Highlight: "When $V_z=0$ and $I_{yz}=0$, $q_{out}-q_{in} = V_y Q_z / I_z$" — leads to the familiar $\tau = VQ/(Ib)$.
- Only 3 slides extracted from this PDF (it is short — likely the rest of the day's content was on the board / leads into the shear-center material covered in the next lecture).

## Sign Conventions / Figure Conventions (cross-cutting)

- Right-handed $(x, y, z)$: $x$ along beam length, typically $y$ up, $z$ out of page (or rotated as convenient).
- Internal moment components on a cut face are opposite to the end-couple components: $M_y = -M_{0y}$, $M_z = -M_{0z}$.
- "Interior Face 1" vs "Interior Face 2" of a cut beam carry opposite-sign internal moment components — picking the wrong face flips all $\sigma$ signs.
- Place $y$-$z$ origin at the centroid for the General Flexure Formula to hold as derived.
- $\sigma_x$ along $\overline{CS}$ (the $x$-axis at the centroid) is zero by construction (NA passes through centroid).
- Shear-stress subscript: $\tau_{xy}$ = stress on $x$-face in $y$-direction. Thin-wall convention discards components parallel to the thinner dimension of each segment.
- Shear-flow direction follows fluid-flow continuity: at junctions, $q$ in = $q$ out; free edges carry $q=0$.
- Sign of $V_y, V_z$ vs. moment derivatives: $V_y = -dM_z/dx$, $V_z = +dM_y/dx$.

## Thin-Walled Aerospace Terminology (as introduced)

- **Web**: connecting/joining segment of a built-up section (e.g., the vertical strip of an I-beam between flanges).
- **Flange**: outer wide segment of a built-up section (top/bottom horizontal pieces of an I-beam).
- **Z-beam / stiffener**: thin-walled Z-shaped section riveted to aircraft skin to stiffen panels.
- **Thin-walled (criterion)**: $h > 4b$ keeps $\tau$ approximately constant across thickness (within 0.8%).
- **Shear flow $q$**: $q = \tau b$ (lb/in); behaves like fluid mass flow — continuous along the section, zero at free edges, conserved at junctions.
- **Principal axes**: axes through the centroid for which $I_{yz} = 0$. Aligning $y, z$ here lets the simple "$My/I$" form be used directly.
- **Neutral axis (NA)**: locus on the cross-section with $\varepsilon_x = \sigma_x = 0$. Passes through the centroid; orientation $\tan^{-1}(B_2/B_1) = \tan^{-1}(M_y\text{-related}/M_z\text{-related})$.
- **Critical point**: cross-section point of maximum $|\sigma|$ — always at the greatest perpendicular distance from the NA.
- (Idealized stringer-web sections, "boom" / "effective area" terminology — not yet introduced in this date range; expected in subsequent lectures.)

## Extraction Issues / Pages Not Fully Transcribed

- Mar 4 slides 5 and 7 ("STEP 3" inertia calcs): typed equations transcribed; hand-drawn blue/orange marker annotations (parallel-axis decomposition with arrows and $b_1, h_1, A z_1^2$ labels) are summarized but not pixel-exact.
- Mar 9 slide 6 ($I$ calculation for I-beam) and slide 8 ($Q$ calculation): handwritten work for $\bar y_1 A_1$, $\bar y_2 A_2$ summarized; the colored ink shows intermediate algebraic steps reproduced in the bullets above.
- Mar 6 slides 6 and 7 (referenced sketches of the Z-beam stress plane and N.A. with image renderings) only have figure content; equations covered from preceding analytical slides.
- Mar 13 PDF slides 4-12 largely overlap the Mar 9 derivation (shear-flow sketch and free-body diagram). Captured as a summary rather than re-listing identical equations.
- Mar 23 PDF only contains 3 slides — likely the bulk of the lecture was on a whiteboard that was not exported. Subsequent lecture (not in this batch) presumably introduces shear center.
- All slide figures of cross-sections, beam free-body diagrams, and the I-beam $\tau$ / $q$ envelope plots are described in prose; they are not transcribed verbatim as ASCII art.
