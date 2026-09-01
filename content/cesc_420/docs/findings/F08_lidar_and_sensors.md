# F08 · Lidar Failure Modes and Complementary Sensors

Verification of the five lidar claims made in [`../../init_transcript.md`](../../init_transcript.md), plus a sensor survey judged against the 15 g / 7.9 W Crazyflie budget.

**Three of the five claims needed correction before they could go in a graded document.** Supports [IR-11](../01_idea_register.md#ir-11--lidar-disambiguation-for-glass-and-chain-link-fence), [IR-13](../01_idea_register.md#ir-13--mutual-interference-between-lidars-in-a-swarm), [IR-18](../01_idea_register.md#ir-18--ground-penetrating-radar-for-subsurface-sensing), [IR-20](../01_idea_register.md#ir-20--sonar-for-aerial-mapping--rejected-physics).

---

## Verification scorecard

| Claim | Verdict |
| --- | --- |
| 1. Chain-link = mixed pixels from beam divergence | ⚠ **Numbers wrong, mechanism only conditionally right** |
| 2. Glass = no return or a ghost at ~2× true range | ⚠ **Incomplete (4 outcomes, not 2); "2×" wrong in general; thickness unsupported** |
| 3. Solid-state internal glare | ✅ **Correct — and now has a CVPR 2026 primary source** |
| 4. Grass causes systematic positive DTM bias | ✅ **Directionally correct, needs a magnitude caveat** |
| 5. Lidar mutual interference in a swarm | ✅ **Correct and quantified** |

---

## Claim 1 — chain-link fence

**The numbers were wrong.** Velodyne's own VLP-16 User Manual (Table F-1) gives beam divergence **3.0 mrad (0.18°) horizontal × 1.5 mrad (0.09°) vertical**, and Table F-2 lists the spot at 10 m as **30.0 × 15.0 mm** — not the asserted ~40 × 25 mm. A proposal that misquotes a vendor spec *by name* is an easy target in review, and this is checkable in one appendix.

**The mechanism was borrowed from the wrong sensor class.** "Reported range is a blend of multiple surfaces" is strictly the **AMCW/phase-shift** model, where the detector integrates a phasor sum and returns an intermediate range corresponding to *no real scatterer*. **Pulsed time-of-flight sensors instead produce two resolvable peaks** once separation exceeds the pulse-derived range resolution. The VLP-16 records two separate returns only when objects are **≥1 m apart** — so a fence with a wall 2 m behind it yields two discrete returns, not a blend.

That is a *better* thesis, because 1 m is a testable threshold the team could design an experiment around.

**The core idea survives:** mixed pixels at edges are a genuine, documented systematic effect — when the footprint crosses a discontinuity the resulting points carry biases well above the instrument's stated precision. Keep it, with the numbers and the ranging-principle caveat fixed.

**A better reframing of chain-link.** Standard 11-gauge fabric is 0.120 in (3.05 mm) wire on a 2 in (50 mm) diamond mesh, so wire occupies roughly **2d/p ≈ 12%** of a footprint large relative to the wire — **~88% of pulse energy passes straight through.** That makes chain-link a **sub-footprint partial-return detection-threshold problem, not a range-blending problem.**

> ⚠ **Mark as derived.** No published lidar study specific to chain-link fence was found. The fill-factor arithmetic is ours, from CLFMI fabric dimensions plus the Velodyne spot table — label it as such in any graded document.

Corroboration: NASA aerial-lidar geofencing work reports outright **dropouts** for ~3/8 in guy wires, stating very thin objects cannot be completely enclosed due to lidar sampling. So dropout, not blending, is the dominant thin-structure failure.

---

## Claim 2 — glass

**There are four outcomes, not two:**

1. A strong return **at the glass** near normal incidence,
2. a **transmitted** return from the object behind it (attenuated by the double pass),
3. a **specular ghost**,
4. **no return at all** when incidence is too oblique.

The team's draft omits #1 entirely. The test plan needs all four as distinguishable cases.

**"Twice the true range" is wrong in general.** The ghost is the **mirror image of a real object reflected about the glass plane**, so its reported range equals the folded path length (sensor→glass + glass→object). That equals 2× only in the degenerate case where the reflected object sits at the sensor's own perpendicular distance from the glass. Stating 2× as a rule would be flatly incorrect in the SRS — and **mirror symmetry about the plane is also what makes the standard removal algorithm work.**

**Keep the angle argument, drop the thickness argument.** Incidence-angle dependence is confirmed and severe: intensity peaks near perpendicular and drops quickly until the return falls below threshold. In Foster & Kuipers' framing, lidar light off glass *"only returns to the sensor from a small number of directions"* and detecting observations *"are vastly outnumbered by those missing it."* **That is exactly why glass walls read as empty space in an occupancy grid** — the failure that would fly a drone into an atrium window.

> ⚠ **Strike the thickness claim.** No primary source supports glass *thickness* as a determinant. Physically, the two Fresnel surface returns from a 6 mm pane are ~6 mm apart — far below the ~1 m dual-return separation of a VLP-16, so thickness cannot produce distinguishable range effects.

The exact angular threshold at which a glass return drops below detection is **not published as a single number** — sources say only "near normal" and "drops quickly." It depends jointly on range, coating and receiver sensitivity, so it would have to be measured.

---

## Claim 3 — solid-state glare ✅

**The strongest of the five, and now citable to a CVPR 2026 paper** rather than asserted. Internal-multipath glare: bright returns undergo multiple internal reflections between lens and sensor, plus scattering within the optical assembly, redistributing light across a neighbourhood of pixels and creating phantom structures.

**Critically — glare does not merely add phantom points, it *suppresses* true returns.** The paper's motivating example is a child beneath a retroreflective stop sign being obscured. **Additive-noise mitigation is the wrong model; the hazard is a safety-relevant false negative**, which changes how the test plan must be written.

**The "newer compact solid-state" qualifier is precise, not hand-waving.** Legacy rotating scanners like the HDL-64e grouped detectors behind separate optical paths and fired one per group at a time *explicitly to prevent blooming*; modern high-resolution SPAD arrays share optics and therefore enable glare. That's a defensible sensor-selection rationale.

**Vendor corroboration is stronger than a paper alone:** Ouster firmware v1.12 fixed retroreflective objects appearing **20–40 cm closer** than true distance, plus "blooming" false positives around retroreflector edges.

A distinct second mechanism exists at silicon level — SPAD optical crosstalk, where secondary photons from an avalanche re-trigger neighbouring pixels, now largely mitigated by deep trench isolation. Worth separating: the optics-path effect is observable by the team, the silicon-level one is not.

---

## Claim 4 — vegetation ✅ with a caveat

Hopkinson et al. measured ground-elevation bias **by cover class** — every vegetated class positive, none negative:

| Cover | Raw bias | After 1 m rasterising |
| --- | ---: | ---: |
| Highway (control) | 0.00 m | 0.00 m |
| **Grass / herb** | **+0.02 m** | **0.00 m** |
| Low shrub | +0.06 m | — |
| Tall shrub | +0.06 m | +0.11 m |
| Aquatic vegetation | +0.15 m | +0.12 m |

**"Averaging does not remove it" is empirically supported** — gridding to 1 m *is* spatial averaging and it demonstrably failed to remove the offset for aquatic and tall-shrub cover.

> ⚠ **Magnitude caveat.** For actual **short grass the bias was only +0.02 m raw and 0.00 m after rasterising.** The large biases come from aquatic and dense shrub cover. Honest framing: *"positive-signed and systematic, but small for short grass and large for dense or aquatic cover."* Overstating grass bias invites a mentor correction.

Causal mechanism: measured foliage penetration ranged from 0.10 m (33% of canopy depth) for grass and herbs to 0.84 m (22%) for tall shrub — incomplete penetration to true ground.

**Full-waveform mitigation confirmed:** it recovers weak returns backscattered from bare terrain beneath vegetation, producing DTMs with more terrain detail than progressive-TIN processing of discrete returns. Far outside a Crazyflie payload — frame as future work.

> ⚠ **Don't conflate RMSE with bias.** The commonly cited Hodgson & Bresnahan benchmark (17–19 cm pavement/low grass/evergreen, 26 cm deciduous) is **RMSE, a scatter statistic** — not evidence of systematic offset. A reviewer will notice.

---

## Claim 5 — mutual interference ✅ and the most project-relevant finding here

Two Velodyne HDL-64s mounted ~1 m apart on the same vehicle produced **1468 crosstalk points (1.31%)** and **1138 points (1.53%)** in worst-case 360° scans.

**Crosstalk points are not random noise.** They require specific geometric and temporal constellations, cluster densely enough to be mistaken for vegetation or cars, and **recur at regular intervals** because two scanner heads run at slightly different rotation frequencies. That rules out statistical outlier rejection and predicts a periodic, structured artifact findable in logs.

> ### The single most project-relevant finding in this pass
>
> The same paper reports that **PCL Radius Outlier Removal with min-neighbours above 2 is likely to delete small objects such as a UAV** along with the crosstalk points.
>
> **For a swarm where every peer *is* a small sparse object, the standard crosstalk filter would delete the very neighbours the swarm needs to see.**

Two more points: most crosstalk in that system was **self-induced** by a reflective pan-tilt head ~1 m from each scanner *on the same vehicle* — so one robot carrying a lidar plus reflective structure generates its own ghosts before any second vehicle is involved. And interference has **two separable impacts**: false-alarm ghost targets (visible) and **SNR reduction degrading detection probability** (silent). Only the first shows as spurious points; the second needs a different test.

---

## Other lidar failure modes

| Mode | Effect |
| --- | --- |
| **Low albedo** | Range scales ≈ √reflectivity (250 m @10% ≡ 500 m @40% ≡ 750 m @90%). Measured: white material 9.5% power reflectivity, **black 4.7% and 0.3%** |
| Rain / fog | ~50% detection loss in fog-chamber tests; 25% shorter detection on-road in fog and snow |
| **1550 nm vs 905 nm** | **Counterintuitive: 1550 nm degrades *more* (~60% difference); light fog worse than heavy rain** |
| Water / wet floor | Specular mirror reflects the beam away — no-return regions, plus scattered droplet noise at 905 nm |
| **Dust** | Attenuates *and* generates false positives. **Rotor downwash lofts dust into the sensor's own FOV — self-inflicted for any low-flying drone** |
| Foliage | Sub-footprint material mixing degrades intensity-based methods in cluttered scenes |
| Adversarial mirrors | An actuated planar mirror injects ghosts and dropouts into lidar SLAM with no signal injection — justifies treating mirrors/glass as a safety case |

**Black 3D-printed drone frames and black chassis are exactly the 0.3–4.7% case — swarm peers may be among the hardest targets in the room.**

---

## The sensor the team already owns

> ### VL53L1X range collapse — a real flight-safety constraint
>
> | Condition | 88% white target | 17% grey target |
> | --- | ---: | ---: |
> | Dark | **360 cm** | 170 cm |
> | Under 200 kcps/SPAD ambient IR | **73 cm** | 68 cm |
>
> **The team's actual obstacle sensor loses roughly 80% of its range on a dark target under bright ambient light** — in their Lighthouse lab. Write the SRS obstacle-detection requirement against the degraded number, not the headline 4 m.

Other VL53L1X facts: 4 cm minimum range, 27° typical FOV (programmable to 15°), ±20 mm error in dark rising to ±25 mm under ambient light, 940 nm Class-1 SPAD, 20 mW at 10 Hz.

**A 27° cone at 1 m subtends ~48 cm — a Multi-ranger reading is an *area minimum*, not a point range.** This is the team's own version of the mixed-pixel problem, on hardware they already have.

**Two free opportunities:**

- The **programmable region-of-interest** can subdivide the field of view — turning the existing Multi-ranger into a coarse multi-zone sensor with **zero procurement**. Underused, and it suits a hardware-first Semester 1.
- **Multiple 940 nm ToF sensors in the same volume can interfere**, so a swarm of Multi-ranger Crazyflies *is* a mutual-interference experiment whether or not the team intends one. **No published quantitative study exists for VL53L1X crosstalk between Crazyflies** — all the numbers above are for large automotive lidars. That makes [IR-13](../01_idea_register.md#ir-13--mutual-interference-between-lidars-in-a-swarm) a cheap, novel, genuinely publishable experiment on hardware they already own.

Five VL53L1X ≈ 100 mW ≈ **1.3% of hover power** — the existing ranging stack is effectively free in mass and energy.

---

## Complementary sensors, judged against 15 g / 7.9 W

**Power budget rule:** 250 mAh at 3.7 V over 7 min ⇒ ~7.9 W average. A 2 W sensor cuts endurance to ~5.6 min; a 0.1 W sensor costs essentially nothing.

| Sensor | Mass | Power | Flies on a Crazyflie? |
| --- | --- | --- | --- |
| **FLIR Lepton 3.5** (LWIR 160×120, <50 mK) | **~1 g** | **140 mW** | ✅ **Yes — see correction below** |
| **Prophesee GenX320** event sensor (320×320) | ~mm-scale | **3 mW** | ✅ Yes (bare sensor) |
| Loco/UWB deck (DWM1000) | 3.3 g | 150 mA | ✅ Supported deck; 7→6 min |
| Flow deck v2 | 1.6 g | low | ✅ Supported deck |
| AI-deck 1.1 | 4.4 g | up to 300 mA | ✅ but see [F07](F07_edge_ml.md) UART conflict |
| **TI IWR6843** mmWave radar | tens of g | **1.75–2 W (~25% of hover)** | ❌ — **ground robot only** |
| **Polarization camera** (IMX250MZR) | **>100 g** (GigE body) | — | ❌ — ground or fixed mount |
| Ultrasonic (HC-SR04, MB1043) | 4.3–8.5 g | low | ✅ but **strictly inferior to the VL53L1X already owned** |
| **GPR** | **0.9–1.2 kg** | — | ❌ — 60–80× the entire payload budget |

> ⚠ **Correction to [C-01](../02_constraints.md#c-01--physical--payload).** That constraint says thermal imaging is ruled out by mass. **It is not.** The FLIR Lepton 3.5 is ~1 g and 140 mW — about 1.8% of hover power, well inside 15 g. Thermal's real limits are different: it does not range, is 160×120, is **defeated by glass (opaque in LWIR)**, and needs periodic flat-field **shutter events that blank the image** — a real-time control hazard belonging in the risk register if adopted.

### mmWave radar — and why heterogeneity makes it feasible

4 GHz sweep bandwidth gives range resolution c/2B = **3.75 cm, comparable to or better than most lidar.** **Radar's weakness is angular, not radial** — stating that stops the team dismissing radar as simply low-resolution.

| | IWR6843ISK | Ouster OS0-64 |
| --- | --- | --- |
| Azimuth resolution | ~15° | 0.35° |
| Cross-range smear at 5 m | **1.31 m** | 3.1 cm |

**~43× worse in angle — raw radar cannot resolve two drones 1 m apart at 5 m.**

**Why it sees through obscurants, derived rather than asserted:** scattering by micron droplets is Rayleigh at 5 mm wavelength but Mie at 940 nm; the wavelength ratio (~5300) to the fourth power makes per-droplet scattering roughly **8×10¹⁴ times weaker at 60 GHz.** One-line derivation, defensible in a design review. (The 60 GHz oxygen absorption peak of ~15 dB/km costs only **0.15 dB over a 10 m indoor path** — pre-empting the obvious objection to 60 over 77 GHz indoors.)

**The supervision trick has a published precedent.** RadarHD (ICRA 2023) co-mounted a TI AWR1843 (15° azimuth) with an Ouster OS0-64 (0.35°) and **used the lidar cloud as training ground truth** — then demonstrated usable point clouds under **heavy smoke**, driving Cartographer for odometry.

- Scale: ~200,000 raw I/Q radar-lidar pairs over 5147 m². **A deliberate data-collection campaign, not an afternoon.**
- Result: **24 cm** point-cloud error vs lidar; 3.5× better than CFAR on modified Hausdorff, 2.7× on Chamfer.
- ⚠ **Generalization caveat for the risk section:** in unseen environments median error degrades to **0.75 m Hausdorff / 0.36 m Chamfer — roughly 3× worse.** A demo that only works in its training room is a known failure mode of this method.

**The scoping insight:** the trick needs both sensors rigidly co-mounted during clear-air training. At ~2 W and tens of grams that cannot fly on a Crazyflie — but **fits comfortably on the ground robots.** The heterogeneous architecture is what makes the radar idea feasible at all.

### Polarization — genuine disjoint complementarity

**Lidar gets a return from glass only at small incidence angles (near-normal); the degree of polarization of light reflected from glass *rises* with incidence up to Brewster's angle (~56° for n=1.5).** The two sensors cover **disjoint angular regimes** rather than voting on the same evidence — that is the precise complementarity.

⚠ But DoP peaks at Brewster and *decreases* beyond, so a DoP-thresholded detector has a **blind band at both near-normal and grazing incidence.** State it as a limitation rather than discover it.

Industrial polarization cameras are >100 g GigE bodies — ground or fixed mount only. A **Crazyflie-compatible approximation**: a fixed linear polarizer over the AI-deck's HM01B0 plus commanded yaw, trading single-shot capture for a rotating-analyser measurement across frames. Near-zero cost, stretch item only.

### Event cameras

>120 dB dynamic range (up to 143) vs ~60 dB for conventional CMOS, µs temporal resolution, sub-ms latency — exactly the properties that fail on a conventional camera during aggressive manoeuvres in a dim lab. **The GenX320 at 3 mW and a few mm² is the one exotic modality unambiguously inside the Crazyflie budget**, making it the most interesting stretch entry.

⚠ But event cameras **produce no output from a static scene viewed by a stationary camera** and yield no absolute intensity — so they **cannot read an ArUco tag from rest.** Since the ground robots are ArUco-localized, this is an addition, never a replacement. Published event-based teach-and-repeat achieved <24 cm ATE over thousands of metres at ~3.3 ms latency — but with an EVK4 HD sensor far heavier than a GenX320.

> ⚠ **No off-the-shelf Crazyflie deck carries an event sensor, radar, or thermal imager.** Any of these means a **custom PCB design and bring-up** — an apparently simple sensor swap becomes a schedule risk against a short first semester.

### UWB — the lowest-risk addition

The Loco deck is the one advanced modality already available as a **supported, flight-proven deck**: ±10 cm at a **500 Hz aggregate ranging rate shared across anchors** (≈80 Hz per anchor with six), max tested range 10 m.

**Two distinct roles, and only one is infrastructure-independent:** anchor-referenced positioning (TWR/TDoA against fixed anchors), versus **direct agent-to-agent ranging**. The second **measures formation error directly in a single frame — sidestepping the two-frame systematic bias that is [C-05](../02_constraints.md#c-05--technical--two-frames-one-formation) and [IR-03](../01_idea_register.md#ir-03--unified-coordinate-frame-across-two-localization-systems).** That is a genuinely attractive option.

The shared-rate structure is the same bandwidth-division problem as [C-06](../02_constraints.md#c-06--technical--radio-bandwidth-ceiling), so UWB scaling must be budgeted the same way. And **NLOS propagation biases range *long*, not zero-mean** — systematic like frame misalignment, so it won't average out; published learned bias-correction models exist for Crazyflie-class UWB.

### Terminology correction

**The Flow deck is optical flow, not VIO.** It measures body-frame velocity over a textured floor at known height, yielding position only by integration — so it drifts without bound and fails over featureless or specular floors. **Calling it VIO in the proposal is a technical error a reviewer would catch.**

### Why airborne sonar is a category error — the one-sentence version

> Achieving 1° bearing resolution at 40 kHz requires an aperture of about **505 mm — roughly five times the Crazyflie's 92 mm motor-to-motor span.**

Supporting facts: at 40 kHz in 20 °C air, λ = 8.57 mm, giving a 24 mm piston a ~21° −3 dB beamwidth. A single ping returns **one range — the first strong echo anywhere in a 20–30° cone** — so an object reported at 2 m may lie anywhere on a spherical cap 0.7–1 m across. It is a collision-avoidance trigger; treating returns as map points injects metre-scale false geometry.

Worse, most indoor walls are acoustically smooth relative to 8.57 mm, so they reflect **specularly** — a surface tilted more than about half a beamwidth from normal **returns nothing at all**, making walls intermittently vanish. (Documented since Kuc & Siegel 1987, Leonard & Durrant-Whyte 1991.)

**Rebutting "submarines map with sonar, why can't the drone":** water's 1500 m/s at 100 kHz–1 MHz gives 1.5–15 mm wavelengths against ship-scale arrays *hundreds of wavelengths* wide; an air-coupled 40 kHz transducer is **two or three wavelengths across.**

And air-to-concrete acoustic impedance mismatch (413 vs 8.4×10⁶ rayl) gives **99.98% reflection, 0.02% transmission** — killing any through-wall or subsurface notion in air.

*(Even the one thing it does well drifts: 0.177%/°C, so an uncompensated 10 °C change gives ~3.5 cm error at 2 m.)*

### GPR — closed on mass alone

Minimum viable drone GPR payload is **0.9–1.2 kg (0.8 kg controller + 0.1–0.4 kg antenna), about 60–80× the Crazyflie's entire budget**, on DJI M300/M350-class airframes.

**The physics fights the platform:** penetration trades against resolution *and* antenna size — 100 MHz reaches 15–20 m from the ground but only 7–10 m from a drone in dry sand, while 500 MHz–1 GHz stops at 50–60 cm in wet clay. **The lightweight high-frequency antennas a drone can lift are precisely the ones with least penetration.** Airborne systems also lose signal to the air-ground interface reflection, achieving roughly half the depth of the same antenna on the ground.

And beyond physics: **the lab is an indoor flight volume with a floor — there is no subsurface to map** and no realistic test target without building a sand box with buried calibrated targets. Correctly recorded as future work, not stretch.

---

## Open

- **Are the lab's ArUco tags printed on ordinary paper or retroreflective sheeting?** Paper is harmless to lidar; retroreflective sheeting would be a blooming source. Confirm with the lab.
- **Does the Lighthouse system itself have analogous optical failure modes** — occlusion, inter-base-station interference, retroreflective surfaces in the flight volume? Outside this pass's scope, and it is the system the team actually depends on. Worth its own look.
- Dust lofted by Crazyflie downwash indoors is physically plausible as a ToF noise source, but no measurement was found at that scale. A short experiment would settle it.
- Ouster's v1.12 note doesn't say which sensor models had the 20–40 cm retroreflector bias.
- The glare paper gives no pixel-count or angular extent for glare spread beyond a "six-row band" on its test sensor.
- ⚠ A claim that 20/106 PillarNet and 33/332 Aerial-PointPillars false positives were crosstalk-attributable **could not be verified — do not cite without checking arXiv:2512.08557 directly.**

---

## References

1. Velodyne, *VLP-16 User Manual* 63-9243 Rev. F — Tables F-1, F-2; Dual Return Mode. **Corrected divergence and spot size.**
2. J. P. Godbaz, A. A. Dorrington, M. J. Cree, "Understanding and Ameliorating Mixed Pixels and Multipath Interference in AMCW Lidar," in *TOF Range-Imaging Cameras*, Springer 2013, 91–116.
3. P. Tang et al., "Development of a mixed pixel filter…," *ISPRS J. Photogramm.*, 2016.
4. Chain Link Fence Manufacturers Institute, *CLFMI Product Manual* CLF-PM0610, 2015.
5. A. J. Moore et al., "Lidar-derived Navigational Geofences for Low Altitude Flight Operations," *AIAA Aviation* 2020-2908.
6. J.-S. Yun, J.-Y. Sim, "Detection and Utilization of Reflection in 3D Lidar Scans," arXiv:1909.12483. — **the four-outcome glass model**
7. P. Foster, B. Kuipers, "The Reflectance Field Map," *IEEE ICRA* 2023.
8. "GRASS: Glass Reflection Artifact Suppression…," *Remote Sensing* 18(2):332.
9. A. Gump, C. Henley, S. Cheong, A. Prabhakara, M. Gupta, "Ghosts in the Point Clouds: De-glaring LiDAR in the Transient Domain," *CVPR* 2026, arXiv:2605.24753.
10. Ouster, *Lidar Firmware v1.12* release note. — 20–40 cm retroreflector bias
11. C. Hopkinson et al., "Errors in LiDAR ground elevation and wetland vegetation height estimates," *ISPRS Archives* XXXVI-8/W2. — **the per-class bias table**
12. M. E. Hodgson, P. Bresnahan, "Accuracy of Airborne Lidar-Derived Elevation," *PE&RS* 70(3):331–339, 2004. — *RMSE, not bias*
13. X. Zhu et al., "An Integrated Approach to Generating Accurate DTM from Airborne Full-Waveform LiDAR Data," *Remote Sens.* 9(8):871, 2017.
14. A. L. Diehm, M. Hammer, M. Hebel, M. Arens, "Mitigation of crosstalk effects in multi-LiDAR configurations," *Proc. SPIE* 10796:1079604, 2018. — **crosstalk rates and the UAV-deletion finding**
15. "Mutual Interferences of a True-Random LiDAR With Other LiDAR Signals," *IEEE Access*, 2020.
16. STMicroelectronics, *VL53L1X Datasheet* DocID031281 Rev 2, Tables 6–7. — **the range-collapse table**
17. M. Kutila et al., "Automotive LiDAR performance verification in fog and rain," *IEEE ITSC* 2018.
18. J. Wojtanowski et al., "Comparison of 905 nm and 1550 nm semiconductor laser rangefinders…," *Opto-Electronics Review* 22(3), 2014.
19. "Assessing the Robustness of LiDAR, Radar and Depth Cameras Against Ill-Reflecting Surfaces," arXiv:2309.10504.
20. A. Prabhakara et al., "High Resolution Point Clouds from mmWave Radar" (RadarHD), *IEEE ICRA* 2023.
21. Texas Instruments, *IWR6843 Datasheet*; *IWR6843ISK* tool page.
22. Sony Semiconductor, *IMX250MZR* polarization sensor flyer; Yamaguchi et al., REM 2020.
23. Prophesee, *GenX320* event sensor; G. Gallego et al., "Event-based Vision: A Survey," arXiv:1904.08405.
24. Teledyne FLIR, *Lepton 3.5* product documentation.
25. Bitcraze AB, *Multi-ranger*, *Loco*, *Flow deck v2*, *AI-deck 1.1* datasheets.
26. J. J. Leonard, H. F. Durrant-Whyte, *Directed Sonar Sensing for Mobile Robot Navigation*, 1992.
27. SPH Engineering, *GPR integrated systems* and depth documentation.
28. "MirrorDrift: Actuated Mirror-Based Attacks on LiDAR SLAM," arXiv:2603.11364.

---

**Related:** [`F01_crazyflie_platform.md`](F01_crazyflie_platform.md) · [`F07_edge_ml.md`](F07_edge_ml.md) · [`../01_idea_register.md`](../01_idea_register.md) · [`../../INDEX.md`](../../INDEX.md)
