# F09 · Simulation and HPC Compute

What simulation is worth setting up, and what the 8× H100 allocation can honestly be claimed to do. Verified against current vendor documentation, with two corrections to earlier assumptions.

Related: [C-09](../02_constraints.md#c-09--compute--hpc-gpus-are-not-rendering-gpus) · [DR-02](../03_decision_record.md#dr-02--semester-1-favors-real-hardware-over-simulation) · [DR-05](../03_decision_record.md#dr-05--benchmarking-is-measurement-not-simulation) · [IR-08](../01_idea_register.md#ir-08--ml-enhanced-single-drone-navigation-the-original-preference)

---

## The verdict, in four tiers

| Tier | Tool | When |
| --- | --- | --- |
| **1 — do this** | **Crazyswarm2 `backend:=sim`** | Semester 1. ~one afternoon. Reuses the real flight scripts. |
| **2 — if needed** | **Crazyflow** (JAX/MJX) | Semester 2 only, and only if learned policies at scale enter scope |
| **3 — scope out** | Isaac Sim, Isaac Lab 2.3.x, Pegasus, Aerial Gym | Cannot run on the H100s, or built on deprecated products |
| **4 — the honest HPC claim** | PyTorch/JAX training, MJX/MuJoCo-Warp rollouts, Warp raycast sensors, Genesis, headless Blender Cycles | Everything **except** the Omniverse RTX renderer |

**Tier 1 is the proposal's simulation answer**: it costs an afternoon, reuses real flight scripts unchanged, and is a pre-flight safety check rather than a research artifact. It satisfies [SLO 6](../04_course_requirements.md#student-learning-outcomes-map-deliverables-to-these) without contradicting the stated hardware-first preference.

---

## The strongest argument for hardware-first

> **No surveyed simulator ships an out-of-the-box model of Lighthouse base-station positioning or of overhead-camera ArUco localization.** The team's actual localization stack — and its latency and dropout characteristics — is precisely the part that cannot be simulated off the shelf.

That belongs close to verbatim in the proposal's risk or approach section. It converts "we prefer hardware" from a preference into a technical finding.

---

## The H100 question — corrected

**The earlier claim was directionally right but stated too absolutely.** Both halves matter:

**Confirmed:** Isaac Sim 5.1.0 and 6.0.0 requirements pages both state verbatim — *"GPUs without RT Cores (A100, H100) are not supported."* Any proposal text promising Isaac Sim on the HPC cluster is wrong.

**But it is a support boundary, not a hardware lockout.** The Omniverse Kit technical-requirements page (Kit 109.0, updated 2026-08-28) enumerates **Hopper H100/H200/H800 at compute capability 9.0** in its RTX Renderer feature table. NVIDIA staff describe the minimum spec as *"defined by the lowest spec GPU tested,"* a *"supported/testing boundary as opposed to a hard technical limitation,"* and *"not an 'all or nothing' situation."*

**The honest answer is therefore "unsupported and degraded," not "impossible."** What degrades, per NVIDIA's own feature table on Hopper:

| Feature | Hopper |
| --- | --- |
| OptiX Denoiser | ✅ |
| DLSS Ray Reconstruction | ❌ |
| DLSS Frame Generation | ❌ |
| Shader Execution Reordering | ❌ |
| Opacity Micro-Map | ❌ |
| **Motion BVH** | **❌** |

Two consequences that are disqualifying for a sensing project:

- Without DLSS Ray Reconstruction, *"images appear significantly noisy when using the RTX Real-Time render mode"* — any camera-based perception data generated on H100 would be **visibly noisier than on an RTX workstation, contaminating sim-to-real transfer.**
- Motion BVH *"must be enabled for RTX Lidar motion compensation to work correctly"* and *"for the Doppler effect, and therefore RTX Radar entirely, to be modeled correctly."* Since Motion BVH is ❌ on Hopper, **RTX-rendered lidar/radar on H100 would be not just slow but physically wrong.**

NVIDIA states running Omniverse SDKs on non-RTX GPUs is *"provided without any support guarantees,"* and **no NVIDIA statement blesses a physics-only Isaac Sim mode on H100** — so the team cannot cite one.

**If Isaac Sim ever is needed**, the workstation spec is: minimum RTX 4080/16 GB, good RTX 5080/16 GB, ideal RTX PRO 6000 Blackwell/48 GB, Linux driver 580.65.06+, 32 GB RAM. (Omniverse Kit alone has a lower bar — RTX 3070 — so a lab RTX 30-series machine enables Kit-level work even below Isaac Sim's minimum.) Isaac Sim also ships **PhysX** sensors — Generic, Lidar, Lightbeam, Contact, Effort, IMU, Proximity — that use raycasting rather than the renderer and don't need RT cores, though they ignore materials and transparency.

### The roadmap, worth knowing

Isaac Lab's maintainer wrote in January 2026 that *"by decoupling from RTX rendering requirements, you will be able to run Isaac Lab on a mix of the latest NVIDIA compute GPUs (ex: L40s/H100/H200/B200)."* The Isaac Lab 3.0 Beta (Newton) install page lists Isaac Sim as *"[Optional] … not required if the Omniverse visualizer is not used"* — **documentary proof that a Kit-less, RTX-free install exists today.**

**But it has zero drone environments.** The Newton integration docs state *"many features are not yet supported, and only a limited set of classic RL and flat terrain locomotion … examples are included,"* and the supported-task list is cartpole, ant, humanoid, quadruped locomotion, arm reach and cube manipulation — **no multirotor task.** So the RTX-free Isaac path cannot serve this project in Semester 1.

Newton itself is a Linux Foundation project built on NVIDIA Warp with MuJoCo Warp as its primary backend (NVIDIA + Google DeepMind + Disney Research). **The H100 path and the MuJoCo path are converging on the same GPU kernels — so learning MuJoCo/Warp now is not wasted effort.**

### Ecosystem status, settled

| Product | Status |
| --- | --- |
| **Isaac Gym Preview** | **Deprecated.** NVIDIA's page reads *"Isaac Gym — Now Deprecated,"* legacy, *"no longer supported."* |
| IsaacGymEnvs, OmniIsaacGymEnvs, Orbit | Superseded by Isaac Lab |
| **Isaac Lab** | The single robot-learning framework as of 2026. Pin **v2.3.2** (2026-02-02) — the last stable main-branch release; 3.0 is beta |

Note: v2.3.2's release notes say *"this will be the final release from the current main branch"* — **bug fixes land only on a beta branch during the capstone year.** v2.3.2 did add the first first-party multirotor actuator and drone task (contributed by the Aerial Gym authors), but it is immature.

---

## What the H100s *can* do

Warp's compatibility page sets the minimum at compute capability **5.2** (CUDA 12.x) or 7.5 (CUDA 13.x) and **never mentions RT cores**. H100 is sm_90 — so Warp, and therefore Warp-based raycasting, Newton and MuJoCo Warp, run on the cluster without qualification.

Warp exposes `wp.mesh_query_ray`, `mesh_query_ray_anyhit`, `bvh_query_ray` and `tile_bvh_query_ray` as built-in BVH primitives. **A hand-rolled Multi-ranger or 2D-lidar model is roughly a hundred lines of Warp kernel and runs at full speed on H100.**

**MuJoCo/MJX has rangefinder sensors** — MJX-JAX lists RANGEFINDER as supported and MJX-Warp supports *"all except PLUGIN."* So a Multi-ranger deck can be modelled natively in GPU-batched MuJoCo. **Target the MJX-Warp backend, not the older JAX one:** ray casting is *"All, BVH for meshes, hfield, and flex"* on Warp versus *"slow for meshes, hfield and flex unimplemented"* on JAX.

MuJoCo also renders headless via **EGL** — hardware-accelerated, no ray-tracing hardware, works over SSH on an H100 node, which Isaac Sim cannot do in a supported way.

**`mujoco_menagerie` ships an official `bitcraze_crazyflie_2` model**, and Bitcraze links MuJoCo on its own external-projects page — removing the biggest asset-authoring cost of a MuJoCo route.

**Blender Cycles renders on CUDA without RT cores** (compute capability 5.0+, which includes H100 at 9.0). The OptiX backend also requires only 5.0 and merely *"takes advantage of"* RT hardware for speed. **Neither Cycles path is blocked by the absence of RT cores** — the H100s can batch-render training imagery or presentation visuals.

---

## Drone simulators surveyed

| Tool | Status | Verdict |
| --- | --- | --- |
| **Crazyswarm2 `backend:=sim`** | Active (pushed 2026-08-21) | **Tier 1.** Firmware SITL, identical ROS 2 API and Python scripts as hardware |
| **Crazyflow** | Active (pushed 2026-08-31), arXiv:2606.01478 | **Tier 2.** JAX/MJX, Crazyflie-specific, batched over n_worlds × n_drones, differentiable, *"up to 914 M steps/s on an RTX 4090"*; **Bitcraze-recommended** |
| CrazySim | ICRA 2024, active | Credible high-fidelity firmware SITL against Gazebo; speaks cflib so Crazyswarm2 can use it as a backend |
| Bitcraze Webots | Vendor calls it *"not realistic, feature-rich, or actively maintained"* | Only Bitcraze-supported path simulating the Multi-ranger; Gazebo folder *"still underdeveloped"* |
| gym-pybullet-drones | Active | Lowest friction, installs in minutes — but **CPU-only, uses no H100** |
| Genesis | Active, v1.3.3 | Non-RT GPU, batched LBVH lidar; multi-physics breadth far beyond need |
| Aerial Gym | **Isaac Gym Preview 4, Python 3.8, CUDA 11.7** | Toolchain predates H100 (sm_90 needs CUDA 11.8+); sensing layer is good Warp prior art |
| Pegasus | Requires Isaac Sim 5.1.0 *exactly* | Inherits full RTX requirement; targets PX4 airframes the team doesn't own |
| **Colosseum** | **ARCHIVED, read-only** | Drop it — any proposal naming it as the AirSim successor is out of date |
| AirSim | Last binary release **2022-07-18**; commits since are README edits | Related work only, never a tool to build on |
| Flightmare | Last substantive commit 2021-04 | Unmaintained; split physics/Unity design can't run headless on H100 |
| Brax | Active | Rigid-body JAX, **no rangefinder or camera** — name and dismiss in one line |

**Crazyflow is the one option that converts the 8× H100 allocation into capstone value without an unsupported-hardware fight.**

Note PX4 SITL is irrelevant here — **Crazyflies run `crazyflie-firmware`, not PX4.** Bitcraze states full SITL is *"not officially supported yet for Crazyflies because it requires a large overhaul of the firmware to compile on a desktop machine"* — which is itself evidence for the minimal-simulation plan.

---

## Blender → USD pipeline, if an arena digital twin is ever wanted

**It's real and free.** Blender's USD exporter is built in and exports meshes, cameras, curves, lights, hair, point clouds, volumes and armatures.

Two caveats:

- **Materials barely survive.** Only *"simple node trees containing Diffuse BSDF, Principled BSDF, Image Textures, UVMap, and Separate RGB nodes"* export to UsdPreviewSurface. Fine for an arena mockup, **not fine for photorealistic perception training.** Layers and variants are unsupported.
- **No physics transfers.** In Isaac Sim the team must additionally apply `UsdPhysics` RigidBodyAPI and CollisionAPI and choose a collision approximation for every prim. **Geometry transfer is an afternoon; physics authoring and tuning is the multi-week part.** That is the hidden cost.

Isaac Sim's Asset Importer also handles `.fbx`, `.obj`, `.gltf`, so Blender USD is one of several equivalent entry points if it proves lossy.

---

## Open — one is a 30-minute test, not more reading

1. **Does Isaac Lab 2.3.x actually start and train physics-only, headless, rendering disabled, on an H100?** NVIDIA documents no supported physics-only mode and the only forum thread on it is poster speculation. **This needs a 30-minute empirical test on one HPC node**, not more research.
2. **Do the ERAU HPC nodes permit the workload shape these simulators need** — long-lived interactive sessions, X/EGL display access, container privileges, Vulkan ICD availability, per-user GPU-hour quotas? A question for the **cluster administrator**, not the mentor.
3. **Are the H100s MIG-partitioned, and at what slice size?** Materially changes achievable environment counts for MJX and Crazyflow.
4. Which GPUs do the lab workstations contain? Whether any single machine meets RTX 4080/16 GB decides Isaac Sim availability independent of the H100 question.
5. Does Isaac Lab 3.0 / Newton get a multirotor task before Spring 2027? Unpublished — ask the mentor or track the `develop` branch.
6. Does the lab's ArUco ground-robot stack have any existing simulation or replay harness, or prior code from the mentor's group? **This is the piece no off-the-shelf simulator provides.**
7. **Can the Crazyradio link's throughput and latency — the team's stated core difficulty — be modelled in any of these at all?** A network simulator (ns-3, Mininet-WiFi) coupled to a physics simulator may be a separate research question worth scoping with the mentor. See [F04](F04_network_and_latency.md).
8. Whether Isaac Gym Preview 4 binaries execute on sm_90 at all is unresolved — would need a direct trial if Aerial Gym is seriously considered.

---

## References

1. NVIDIA, *Isaac Sim Requirements*, 5.1.0 and 6.0.0. — the verbatim RT-core exclusion
2. NVIDIA, *Technical Requirements*, Omniverse Kit 109.0 Developer Guide (28 Aug 2026). — **the Hopper feature table**
3. NVIDIA, *RTX Sensors*, Isaac Sim 5.1.0. — Motion BVH dependency of RTX Lidar/Radar
4. NVIDIA, *Isaac Gym — Now Deprecated*. <https://developer.nvidia.com/isaac-gym>
5. R. Thaker (NVIDIA), *Isaac Lab Development Update*, IsaacLab Discussion #4339, 6 Jan 2026. — the L40s/H100/H200/B200 roadmap
6. NVIDIA, *Newton Physics Integration — Installation / Training Environments*, Isaac Lab docs.
7. Newton Physics Project (Linux Foundation). <https://github.com/newton-physics/newton>
8. NVIDIA, *Warp — Compatibility & Support* and *Built-ins Reference*. — sm_52 minimum; BVH ray primitives
9. Google DeepMind, *MuJoCo XLA (MJX)* documentation. — MJX-Warp vs MJX-JAX parity, RANGEFINDER
10. Google DeepMind, *MuJoCo Visualization* — EGL headless rendering
11. Google DeepMind, `mujoco_menagerie` — `bitcraze_crazyflie_2`
12. W. Hönig et al., *Crazyswarm2 Usage — Simulation*. <https://imrclab.github.io/crazyswarm2/usage.html>
13. C. Llanes, Z. Kakish, K. Williams, S. Coogan, "CrazySim: A Software-in-the-Loop Simulator for the Crazyflie Nano Quadrotor," *IEEE ICRA* 2024, 12248–12254.
14. *Crazyflow: Fast, parallelizable simulations of Crazyflie quadrotors with JAX*, arXiv:2606.01478.
15. M. Kulkarni, W. Rehberg, K. Alexis, "Aerial Gym Simulator," *IEEE RA-L* 10(4):4093–4100, 2025.
16. Bitcraze AB, *Getting Started with Simulation* and *External Projects — Crazyflie Simulators*.
17. Genesis Embodied AI documentation — installation matrix, Raycaster sensor.
18. Blender Foundation, *GPU Rendering* and *Universal Scene Description*, Blender 5.2 LTS Manual.
19. NVIDIA, *Isaac Sim Reference Architecture* — asset import and collision authoring.

---

**Related:** [`F01_crazyflie_platform.md`](F01_crazyflie_platform.md) · [`F04_network_and_latency.md`](F04_network_and_latency.md) · [`F07_edge_ml.md`](F07_edge_ml.md) · [`F10_benchmarking_and_measurement.md`](F10_benchmarking_and_measurement.md) · [`../../INDEX.md`](../../INDEX.md)
