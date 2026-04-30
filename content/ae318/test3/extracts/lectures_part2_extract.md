# AE318 Test 3 — Lecture Slides Extract (Part 2)

Coverage: Mar 25 → Apr 10 (Sec 4.4 fix-up, 4.5 Largest Shear Flow, Ex 4.5.1 Z-beam, 5.1 Idealization, 5.2 Open idealized cross-sections, 5.3 Closed/curved idealized cross-sections).

Standard sign conventions used throughout:
- $x$ axial; $y$, $z$ in cross-section plane; origin at centroid for GFF/GSFF.
- Internal bending moment $M_z$ about $z$-axis, internal shear $V_y$ along $y$.
- $V_y = -\,dM_z/dx$, $V_z = +\,dM_y/dx$.
- Shear stress on a free surface is zero; $\tau$ is internal only.
- $q_{out} - q_{in}$ form of GSFF retains sign; "out" = direction along chosen swept area $A'$, "in" = opposite end.
- For an "ideal" stringer/web cross-section: $\sigma$ lives only on stringers; $q$ is constant in webs and changes abruptly across each stringer.

Key equations referenced (derived earlier in course):

- General Flexure Formula (GFF): $\sigma_x = \dfrac{-y(I_y M_z + I_{yz} M_y) + z(I_{yz} M_z + I_z M_y)}{I_y I_z - I_{yz}^2}$
- General Shear Flow Formula (GSFF), free-surface form: $q = \dfrac{(I_y V_y - I_{yz} V_z)\,\bar{y}'A' + (-I_{yz} V_y + I_z V_z)\,\bar{z}'A'}{I_y I_z - I_{yz}^2}$
- Reduced ($I_{yz}=0$, $V_z=0$): $\tau = VQ/(Ib)$, $q = VQ/I$.

---

## Lecture 2026-03-25 — Section 4.3 fix, Section 4.4 derivation, Section 4.5 (largest shear flow), Ex 4.5.1 Part (a)

- Correction to Sec 4.3 example (cantilever I-beam, 60", 1400 lb tip load, flange 1.5"×3", t=1/8"): instructor (Radosta) had used $V=+1400$ lb but shear diagram says $V=-1400$ lb. Resolution: keep computed $\tau$ magnitudes ($(\tau_{xz})_{flange}$ peak $1521.5$ psi, $(\tau_{xy})_{web}$ peak $4377$ psi, junction $3043$ psi) but reverse the load arrow direction.
- Sec 4.4 — derivation of $q_{out}-q_{in}$:
  - Take element of length $dx$, top/bottom at $y_1$, $y_2$ from N.A.
  - Sum $F_x=0$: $(F_\tau)_2 - (F_\tau)_1 = dF_\sigma$.
  - Result: $\tau_2 - \tau_1 = \dfrac{V Q_{12}}{I b}$ where $Q_{12}$ = first moment of shaded area between $y_1$ and $y_2$.
  - When one end is a free surface, $\tau$ there $=0$, recovering classical $\tau = VQ/(Ib)$.
  - General version: $q = \dfrac{(I_y V_y - I_{yz} V_z)\bar{y}'A' + (-I_{yz} V_y + I_z V_z)\bar{z}'A'}{I_y I_z - I_{yz}^2}$ when free surface bounds $A'$.
- Sec 4.5 — Largest shear flow location:
  - Define rotated $y^*$-$z^*$ frame with $z^*$ along the neutral axis.
  - Note: derivation requires one cross-section dimension thin (textbook omits this caveat).
  - $\sigma_x=0$ when $y^*=0$ implies $M_{y^*} = -(I_{y^*z^*}/I_{z^*}) M_{z^*}$.
  - Differentiating w.r.t. $x$ (assumes untapered: $I_z$, $I_{yz}$ const): $V_{z^*} = (I_{y^*z^*}/I_{z^*}) V_{y^*}$.
  - Sub into GSFF, simplify (the $\bar{z}'A'$ coefficient collapses to 0): $q = \dfrac{V_{y^*}(\bar{y}'A')^*}{I_{z^*}} = \dfrac{V_{y^*} Q^*}{I_{z^*}}$.
  - Same form as $\tau = VQ/(Ib)$ → max $q$ on the neutral axis.
  - Caveat: holds for transverse forces only; if pure couples present, max $q$ is on the N.A. that would result with couples removed.

### Example 4.5.1 Part (a) — Z-beam, find max bending stress

- Geometry: simply supported beam, supports 0/42", loads 100 lb at $x=12"$, 70 lb at $x=24"$ (12"/12"/18" spans). Z cross-section: vertical web 1" tall, horizontal flanges 9/16" wide at top-right and bottom-left, $t = 0.064"$.
- Reactions $R_1=101.4$ lb, $R_2=68.57$ lb. Shear diagram: 101.4 → 1.4 → -68.57. Max $M = 1234$ in·lb at $x=24"$, all about $z$ ($M_y=0$).
- Section properties (already known from Mar 4 example): $\bar{y}=0.5"$, $\bar{z}=0.5305"$, $I_y=0.006392\,in^4$, $I_z=0.01933\,in^4$, $I_{yz}=0.008400\,in^4$.
- $\sigma_x = \dfrac{-y I_y M_z + z I_{yz} M_z}{I_y I_z - I_{yz}^2}$ with $M_y=0$ → $\sigma_x = -(148{,}800)y + (195{,}600)z$.
- Neutral axis: $y = 1.315\,z$ → slope $\tan\theta = 1.315$ → $\theta = 52.75°$.
- Critical points A $(0.5", -0.032")$, B $(-0.5", 0.032")$ are farthest from N.A.
- $(\sigma_x)_A = -80{,}660$ psi (compression), $(\sigma_x)_B = +80{,}660$ psi (tension). Max bending stress $= 80{,}660$ psi.

Note: pages with hand-drawn V/M diagrams and Z-section figures are images, but values are transcribed.

---

## Lecture 2026-03-27 — Example 4.5.1 Part (b) (largest shear flow on Z-beam)

- Steps: get max $V$ from shear diagram, find points where N.A. crosses cross-section, evaluate GSFF at each.
- Max $V_y = 101.4$ lb, $V_z=0$. Plug into GSFF $q_{out}-q_{in}$ form: $q_{out}-q_{in} = [(12{,}230)\bar{y}' - (16{,}070)\bar{z}']A'$.
- N.A. (from Part a) crosses the section at three points: C (top flange), D (centroid), E (bottom flange).
- Sign convention: pick a swept portion such that one end is a free surface ($q_{in}=0$). Then $q$ at the cut equals $q_{out}$.
- At C: shaded area = top flange right of C. $A' = 0.064 \cdot (9/16 - 0.032 - 0.3559) = 0.01117\,in^2$, centroid $(\bar{y}', \bar{z}') = (0.468", 0.4431")$. $q_C - 0 = -15.60$ lb/in → $q_C = -15.60$ lb/in. (Picking left side: $q_{in}=q_C$, $q_{out}=0$, gives same answer.)
- At D (centroid): combine top flange + half of vertical web above $y=0$. $A' = 0.0639\,in^2$, $\bar{y}'=0.3589"$, $\bar{z}'=0.008973"$. $q_D = +271.3$ lb/in. (Sign of textbook differs; instructor's signs are opposite.)
- At E (bottom flange, mirror of C): $q_E = -15.60$ lb/in.
- Caveat: N.A. intersects the horizontal flange in a locus of points (not single point). Treating C, D, E as discrete is an assumption. By tracking $q(s)$: $q$ starts at 0 at upper-right, decreases to $-15.60$ at C, increases through 0 (at $\bar{y}=1.315\bar{z}$, i.e. centroid at C), continues positive to $+271.3$ at D, decreases to 0 at E-centroid, etc. Local extrema at C, D, E confirm max shear flow $= 271.3$ lb/in at point D.

Pages with figures showing the shaded swept areas and N.A. line at $52.75°$ on the Z-section are image-only but key numerics are transcribed.

---

## Lecture 2026-04-01 — Section 5.1 Idealization of Beam Cross-Sections

- Semi-monocoque vs fully-monocoque; structural significance of skin.
- Wing components: spar caps (flanges), spar webs, ribs, stringers/stiffeners, skin.
- Idealization assumptions:
  1. Stringers carry only $\sigma$, constant over their cross-section ($\sigma = P/A$).
  2. Thin webs/skin carry only $\tau$, constant through thickness.
  3. Ribs rigid in their own plane, no resistance to warping out-of-plane.
- Concept of "ideal" / "effective stringer area": lump some adjacent web area onto the stringer. Place new lumped area at centroid along web centerline.
- Terms: textbook uses "stringer" ↔ "stiffener" and "web" ↔ "skin" interchangeably.
- Bending stress $\sigma$ on actual section varies linearly over stringers and webs; in idealization $\sigma$ acts only on effective stringers (discrete).
- Shear flow $q$ in actual section varies linearly/parabolically; in idealization $q$ is constant between stringers (changes abruptly at each stringer).

### "30× Thickness" Rule for effective area

- For compression: web stiffened a distance $w_{skin} = 30\,t_{skin}$ around rivet (15$t$ each side of rivet centerline). Distribute equally on both sides of rivet:
$$A_{eff} = A_{stringer} + [30(t_{skin})]\,t_{skin}$$
- For tension: full web between successive rivets is effective:
$$A_{eff} = A_{stringer} + \tfrac{1}{2}(A_{web})_{rivet\text{-}to\text{-}rivet}\big|_{left} + \tfrac{1}{2}(A_{web})_{rivet\text{-}to\text{-}rivet}\big|_{right}$$
- Modification rule: if rivet spacing or available skin length is less than $30\,t$, truncate the lumped width accordingly.

### Example 5.1.1 — Z-beam stiffener under compression

- Given: skin $t=0.050"$, stringer 1.228" web with 0.064" thickness, two 0.468" flanges 0.064" thick. Single rivet row.
- $w_{skin} = 30(0.05) = 1.5"$ → 0.75" each side of rivet.
- $A_{eff} = A_{stringer} + A_{skin} = [1.228(0.064) + 2(0.468)(0.064)] + [1.5(0.05)] = 0.1385 + 0.075 = 0.2135\,in^2$.

### Example 5.1.2 — Upper J-beam spar cap under compression

- Skin $t=0.040"$ (double rivet row, 7/16" + 7/16" = 0.875" between centerlines), J stiffener (1-3/8" tall, 0.072" caps, 7/16" lower flange), spar web 0.064" attached by single rivet row 5/8" below upper rivet.
- Skin: $w_{skin} = 30(0.04) = 1.2"$ but rivet-to-rivet only 0.875" < 1.2 → use $0.6 + 0.875 + 0.6 = 2.075"$.
- Web: $30(0.064) = 1.92"$ but upper end of spar webbing only 5/8" (0.625"), so $w_{web} = 0.625 + 0.96 = 1.585"$.
- $A_{eff} = A_{stringer} + A_{skin} + A_{web} = 0.2371 + 0.083 + 0.1014 = 0.4215\,in^2$.

### Section 5.2 setup — Idealized open cross-section under transverse load

- Cantilever beam, 60", $V_y = 1{,}000$ lb at free end (acting at "shear center" through structure-to-support fixture). Cross-section: rectangular layout with stringers A (top-left, 0.5 in²), B (top-right, 0.3 in²), C (bottom-right, 0.2 in²), D (bottom-left, 0.2 in²); 4" wide × 6" tall; web $t=0.035"$.
- Find: (a) $\sigma$ at each stringer at the wall, (b) shear flow values, (c) "e" so that no torsion, (d) shear center.

Pages with isometric drawings of actual aluminum wing skin/stringer/spar construction and the cantilever-with-fixture sketch are image-only.

---

## Lecture 2026-04-03 — Section 5.2 continued — Example Part (a): centroid, inertias, $\sigma$

- Step 1: Centroid (using only stringer areas; webs neglected since thin and don't bear $\sigma$). With $y_{temp}, z_{temp}$ at point D:
  - $\bar{y} = \dfrac{6(0.5) + 6(0.3) + 0(0.2) + 0(0.2)}{1.2} = 4"$
  - $\bar{z} = \dfrac{0(0.5) + 4(0.3) + 4(0.2) + 0(0.2)}{1.2} = 1.667"$
- Step 2: stringer coordinates relative to centroid:
  - A $(2, -1.667)$, B $(2, 2.333)$, C $(-4, 2.333)$, D $(-4, -1.667)$.
- Step 3: For each stringer treat as circle with $r_i = \sqrt{A_i/\pi}$. Parallel-axis term dominates own-centroidal $\pi r^4/4$ by ~2 orders → drop self term:
$$I_y = \sum A_i z_i^2,\quad I_z = \sum A_i y_i^2,\quad I_{yz} = \sum A_i y_i z_i$$
- Computed: $I_y = 4.667\,in^4$, $I_z = 9.600\,in^4$, $I_{yz} = -0.8000\,in^4$.
- Step 4: bending moment at wall. Load 1000 lb up at free end 60" away, with $V_y$ acting offset $e$ from D → $M_z = 60{,}000$ in·lb (interior face 1 sign convention shown in figure with arrow rules).
- Step 5: GFF with $M_y=0$:
$$\sigma_x = \dfrac{-y I_y M_z + z I_{yz} M_z}{I_y I_z - I_{yz}^2} = -(6{,}341)y - (1{,}087)z$$
- Stringer stresses: $(\sigma_x)_A = -10{,}870$ psi, $(\sigma_x)_B = -15{,}210$ psi, $(\sigma_x)_C = +22{,}830$ psi, $(\sigma_x)_D = +27{,}180$ psi. Signs match expectation (top stringers in compression, bottom in tension).

---

## Lecture 2026-04-06 — Section 5.2 Example Parts (b)–(d): Shear flows, "e" for no torsion, Shear center

### Part (b) — shear flow distribution

- Reaction at wall: $V_y = -1000$ lb (constant along beam from FBD).
- Idealization rules: $q$ jumps at each stringer (since stringers carry $\sigma$), $q$ is constant in each web between stringers.
- Plug into GSFF: $q_{out} - q_{in} = [-(105.7)\bar{y}' - (18.12)\bar{z}']A'$ (computed for interior face directed away from wall; textbook does not specify face).
- Walking around the section starting at A with $q_{in}=0$ from free edge:
  - $q_{AB}$: $A'=0.5$, $(\bar{y}', \bar{z}')=(2", -1.667")$ → $q_{AB} = -90.60$ lb/in.
  - $q_{BC}$: $A'=0.3$, $(2", 2.333")$, $q_{in}=q_{AB}$ → $q_{BC} = -166.7$ lb/in.
  - $q_{CD}$: $A'=0.2$, $(-4", 2.333")$, $q_{in}=q_{BC}$ → $q_{CD} = -90.59$ lb/in.
- Cross-check from opposite end (start at D, $q_{in}=0$): $q_{CD}=-90.60$ lb/in. Consistent.
- Diagram: arrows AB→, BC↓, CD← all at -90.60, -166.7, -90.60; or flip arrows and use +90.60, +166.7, +90.60.
- Force-equivalence check vs $V_y=1000$ lb at offset $e$ from D:
  - $\sum F_y$: $1000 \approx 166.7(6) = 1000.2$ ✓
  - $\sum F_z$: $0 = -(90.60)(4) + (90.60)(4) = 0$ ✓

### Part (c) — distance "e" so no torsion

- Moment equivalence about D: $-1000 e = (90.60)(4)(6) + (166.7)(6)(4) = 6175 \Rightarrow e = -6.175"$ (i.e. 6.175" to right of D).
- Reasoning: GSFF derivation assumes loading acts through shear center → no torsion. If $V_y$ were elsewhere, an extra torsional shear flow would have to be added. For two diagrams to be moment-equivalent at any point, they must be torsion-free → $V_y$ must act 6.175" right of D for this section.

### Part (d) — Shear center

- Definition: point where transverse force may be applied so beam bends but does not twist.
- Procedure: assume shear center is $e_y$ above D, $e_z$ left of D. Apply general $V_y$, $V_z$ at SC.
- General GSFF: $q_{out}-q_{in} = \{[(0.1057)\bar{y}' + (0.01811)\bar{z}']V_y + [(0.01811)\bar{y}' + (0.2174)\bar{z}']V_z\}A'$.
- Compute each web in terms of $V_y, V_z$:
  - $q_{AB} = (0.09060)V_y - (0.1631)V_z$.
  - $q_{BC} = q_{AB} + [(0.07610)V_y + (0.1630)V_z] = (0.1667)V_y - (0.0001)V_z$.
  - $q_{CD} = (0.09060)V_y + (0.08700)V_z$.
- Moment equivalence about D: $e_z V_y + e_y V_z = -[q_{AB}(4)(6) + q_{BC}(6)(4)]$.
- Substitute: $(e_z + 6.175)V_y + (e_y - 3.916)V_z = 0$. Must hold $\forall V_y, V_z$:
  - $e_z = -6.175"$, $e_y = +3.916"$.
- Shear center is 3.916" above D and 6.175" right of D.

---

## Lecture 2026-04-08 — (continuation: Sec 5.2 Part (b)/(c)/(d) review and torsion-free derivation)

Same content as covered Apr 6 lecture: walks through computing $q_{AB}, q_{BC}, q_{CD}$, force-equivalence checks, "e = -6.175"" for no torsion, justification via $\tau = TR/J$ and additivity of torsional + transverse shear, and SC derivation. (Apr 8 PDF appears to repeat/finish the Sec 5.2 example shown on Apr 6 — both lectures cover the same material; this aligns with continuation across class periods.)

Key takeaway equations recap:
- Torsion-free shear-flow check: net moment of $q$ distribution about any point = moment of $V$ about same point.
- For idealized straight-web open sections, total moment of $q$ field = $\sum (q_{web}) \cdot L_{web} \cdot d_{perp}$.

---

## Lecture 2026-04-10 — Section 5.3: Idealized cross-section beams under transverse load — curved webs / closed cross-sections

### Curved-web force equivalence

- Two stringers connected by single curved web; force $V$ at angle $\beta$ to $z$-axis acting at shear center.
- Magnitude of $q$ constant along the web (idealization), but direction changes (web is curved).
- For ds element with components $dy = ds\sin\theta$, $dz = ds\cos\theta$:
  - $V_y = \int q\,ds\sin\theta = q\int dy = q L_y$ where $L_y$ = $y$-component of straight chord between the two stringers.
  - $V_z = \int q\,ds\cos\theta = q L_z$.
- Magnitude/direction: $V = \sqrt{V_y^2 + V_z^2} = q\sqrt{L_y^2 + L_z^2} = qL$ where $L$ = straight chord length. Direction $\tan\beta = V_y/V_z = L_y/L_z = \tan\alpha \Rightarrow \alpha = \beta$, so $V \parallel L$.
- **Key result**: equivalent shear force from $q$ along a curved web between two stringers equals that for a straight web between the same two stringers. (Direction and magnitude both match.)

### Moment equivalence and swept area

- Moment about arbitrary pivot O for the curved-web $q$ distribution:
  - $V e = \int R(q\,ds) = \int q (2\,dA/R)\,R\,ds /\,ds$... cleaning up: $Ve = 2q \int dA = 2qA$.
  - $$Ve = 2 A q$$ where $A$ = area swept from O along the web.
- For a circular-arc web: swept area = sector of circle + triangle from O to the chord endpoints.
- Swept area is invariant along any line parallel to the chord between stringers (and along the chord itself):
  - $A_{swept} = A_{circ} + (1/2) a b$ for off-chord parallel lines (with $a$ = perpendicular offset, $b$ = chord length).
  - $A_{swept} = A_{circ}$ when the line passes through both stringers (the two triangles cancel).
  - Semicircle: $A_{circ} = \tfrac{1}{2}\pi (b/2)^2$.

### Example 5.3.1 — Six-stringer-style closed cross-section with two semicircles (relates directly to textbook Problem 5.5)

- Geometry (at interior cross-section view): Cantilever 180" long. Two-stringer "racetrack" shape: stringers A (top-right), B (top-left), C (bottom-left), D (bottom-right); rectangular center 7" wide, 8" tall; semicircular caps on left (radius 4") and right (radius 4"). Wait — re-reading the slide: stringers labeled A, B (top), C, D (bottom); 4" between top and middle, 4" middle to bottom (so 8" total height); 7" between left and right centers; 10" overall horizontal extent. Areas: A=0.1, B=0.1, C=0.2, D=0.3 in². $V_z=700$ lb, $V_y=500$ lb. Web $t=0.040"$. Both end curves are semicircles.
- Assumption: $V_y, V_z$ act at shear center (so GSFF gives full $q$, no torsion correction).
- Centroid (only 4 stringers, total 0.7 in², temp axes at C):
  - $\bar{y} = 2(0.1)(8)/0.7 = 2.286"$, $\bar{z} = (0.1(10) + 0.3(10))/0.7 = 5.714"$.
- Coords w.r.t. centroid: A $(5.714, 4.286)$, B $(5.714, -5.714)$, C $(-2.286, -5.714)$, D $(-2.286, 4.286)$.
- Inertias (parallel-axis only): $I_y = 17.14\,in^4$, $I_z = 9.143\,in^4$, $I_{yz} = -1.143\,in^4$.
- Shear forces at wall: $V_y = +500$ lb, $V_z = -700$ lb.
- GSFF reduced: $q_{out} - q_{in} = [(50.00)\bar{y}' - (37.51)\bar{z}']A'$.
- **Closed section ⇒ no free surface**: cannot start at $q_{in}=0$. Define unknowns relative to one shear flow.
  - At A: $q_{AB} - q_{AD} = [(50.00)(5.714) - (37.51)(4.286)](0.1) = 12.49$ → $q_{AB} = q_{AD} + 12.49$.
  - At B: $q_{BC} - q_{AB} = [(50.00)(5.714) - (37.51)(-5.714)](0.1) = 50.00$ → $q_{BC} = q_{AD} + 62.49$.
  - At D: $q_{AD} - q_{CD} = [(50.00)(-2.286) - (37.51)(4.286)](0.3) = -82.52$ → $q_{CD} = q_{AD} + 82.52$.
  - At C: $q_{CD} - q_{BC} = [(50.00)(-2.286) - (37.51)(-5.714)](0.2) = 20.01$ → $q_{CD} = q_{AD} + 82.50$. (Same equation, modulo round-off ⇒ need 4th equation.)
- 4th equation from **moment equivalence** between (a) the two transverse forces acting at SC and (b) the closed-section $q$ distribution.
  - About C: $-500(7) - 700(4) = q_{AB}(10)(8) + 2 A_{swept,qBC} (q_{BC}) + 2 A_{swept,qAD} (q_{AD})$.
  - $A_{swept,qBC} = (1/2)\pi(4)^2 = 8\pi$ in² (semicircle, line through B and C — equals $A_{circ}$).
  - $A_{swept,qAD} = (1/2)(10)(8) + (1/2)\pi(4)^2 = (40 + 8\pi)$ in² (off-chord by full rectangle width: parallelism trick gives $A_{circ} + (1/2)ab$).
  - The straight web AB contributes via $q_{AB} \cdot 10 \cdot 8$ (length × perpendicular distance from C).
- Solve: $q_{AD} = -40.07$ lb/in. Back-substitute:
  - $q_{AB} = -27.58$ lb/in
  - $q_{BC} = +22.42$ lb/in
  - $q_{CD} = +42.43$ lb/in
- Force-equivalence check: $\sum F_y$: $22.42(8) + 40.07(8) = 499.92 \approx 500$ ✓; $\sum F_z$: $27.58(10) + 42.43(10) = 700.1 \approx 700$ ✓.

Diagrams of the racetrack section with arrows (qAB ←, qBC ↺ on left semicircle, qCD →, qAD ↻ on right semicircle) appear on multiple slides; geometry transcribed above.

---

## Special terminology / convention summary (for quick reference)

- **Effective stringer area** ($A_{eff}$): actual stringer area + lumped adjacent web area.
- **Lumped-mass model / idealization**: discretize cross-section so $\sigma$ resides only at stringer points and $q$ is piecewise-constant on webs.
- **30× thickness rule**: for compressed skin/web adjacent to a stringer, count $30\,t$ width as effective.
- **Cut**: in closed-section analysis, picking a swept area requires assuming a cut (free surface) — but here $q_{in}=0$ is unavailable; instead build relative equations and add moment-equivalence.
- **Shear center (SC)**: point at which a transverse force produces bending without twisting. For open idealized sections, found via moment equivalence after solving $q$ in terms of $V_y, V_z$ separately and equating coefficients.
- **Swept area** $A$: area swept from the moment-pivot point O along the web; $Ve = 2Aq$ for a single curved web with constant $q$.
- $V \parallel L$ rule: total transverse force resultant of constant-$q$ curved web is parallel to and equal in magnitude to $qL$ (chord between endpoints).
- **Closed section, no free surface**: requires an extra moment-equivalence equation in addition to the $N-1$ jump equations across $N$ stringers.

## Notes on figure-only / hand-drawn pages

- Mar 25: Z-beam isometric with stress/shear distribution, V/M diagrams, NA-locus diagram (red dots) — geometry transcribed but visual layouts not included.
- Mar 27: hand-drawn Z-section with shaded sweep regions — values transcribed; arrows/orientations described in prose.
- Apr 1: actual aluminum wing photo-style cross-sections, fuselage with Z-stringers (idealized vs actual). Hand-drawn NACA 4412 wing for Problem 5.1. Cantilever-fixture isometric.
- Apr 6/8: rectangular open section diagrams with arrows for $q_{AB}, q_{BC}, q_{CD}$; SC-distance moment-arm diagrams.
- Apr 10: racetrack closed section with two semicircles — geometry, $A_{swept}$ partition (sector-plus-triangle) figures conveyed in prose.
