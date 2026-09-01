ok so i want to start some ideas about a senior captone project. these two pdfs explain the projects we are interested in. i added the proposal template as well so that you can also have an idea what the project needs to be. we want to eventually be able to have a pie in the sky idea is to have a drone that can use lidar, photogrammetry, potentially sonar to do topographical mapping and using sensor fusion with accelerometer and GPS and possibly more to help project the images on to landscpae, and then also think about having where the drone is flying a waypoint mission above the ground, so technically it is moving in a 2D plane, but then things like taking photos in houses for real estate, we might need a camera on the top, bottom, and right, and left, all overlapping their neighbors in FOV. i understand there are many more variables and parameters, but this is to coneptualize moving in 3D to then make a 4D map. this can be used for subterrainian mapping, and also we can do normal cameras, or thermal/ir camerais. etc... make sense? the machine learning would be for assiting with denoising ambiguous objects/phenomena in the lidar data, then we could have a different ML model for help with sonar data? then we could have an ML model for image based slam as well - wehre you take google maps about 10 km square area, compress them all, then the drone flies around and takes pictures facing down so then it tries to understand where it is at. make sens? so image based SLAM could use some ML. there is ways to find ML applications, but of course we don't want to overdo it, and then aslo there should be adequate denoising algorithms but we could also make our own, we need minimalism - actally i wont go into planning the implementation we are on project ideas for now but we want to pick apart the grand vision. because also there is a difference between a drone swarm flying above treeline and fliyin in the forest, machine learning would help with keeping positions of drones for communications and movement for forward progress of the mission (doesn't always have to be covering the most distance, it could be sensor arrays doing surveys) make sense? there is more ideas i am not giving you right now i just need you to start processing everything



Yes, it makes sense. Let me give you the honest structural read first, then break the vision into pieces you can actually pick from.

## What you've described is a research program, not a capstone

Topographic mapping + sensor fusion + photogrammetry + subterranean SLAM + cross-view geolocalization + swarm coordination under canopy is roughly five to seven separate capstones. That's not a criticism of the vision. It's the reason the proposal rubric has a line asking "what is out of scope" worth part of the 45%. The grand vision is your *problem statement* and your *future work*; one thin vertical slice is your *proposed solution*.

## The vision decomposes into six layers

Worth naming them explicitly because they're separable, and each one is where a different team's contribution would live:

1. **Platform and mobility** — flying a lawnmower pattern at fixed altitude (2.5D) is a genuinely different problem from traversing a house or a tunnel (true 3D). You correctly spotted this with the multi-camera rig comment.
2. **Sensing** — what physically goes on the airframe.
3. **State estimation** — fusing IMU/GPS/vision into a pose. This is where SLAM lives.
4. **Reconstruction** — point cloud → mesh → textured, georeferenced model.
5. **Perception ML** — denoising, disambiguation, place recognition.
6. **Multi-agent** — formation, comms-aware positioning, coverage planning.
7. (The "4D" part is really layer 4 repeated over time, which makes it a *change detection* problem. Say that out loud in the proposal and it stops sounding vague.)

## Three constraints that will decide everything

**Payload.** A Crazyflie 2.x is about 27g with roughly 15g of useful payload. That gets you the Multi-ranger ToF deck, the Flow deck, or the AI-deck (a tiny grayscale camera with a GAP8). It does not get you a lidar, a thermal camera, GPS, or a photogrammetry-grade sensor. If the mapping vision is the goal, you need a different airframe entirely, which means procurement, budget, and a semester of bring-up before you write a line of interesting code.

**Localization regime.** The lab's existing infrastructure is indoor and external: Lighthouse base stations for the drones, an overhead camera with ArUco tags for the ground robots. Neither works outdoors. GPS doesn't work indoors or underground. Your subterranean and under-canopy ideas are specifically the *GPS-denied* case, which is the hardest one and also the most interesting one. Pick the regime deliberately, because it changes the entire sensor stack.

**Sonar, specifically.** In air, "sonar" means an ultrasonic rangefinder: a few meters of range, a wide cone, essentially no bearing resolution. It's an altimeter, not a mapping sensor. Real sonar mapping (side-scan, multibeam) means an underwater vehicle and a five-figure sensor. If what you actually want is *seeing through dirt*, the sensor is ground-penetrating radar, and that's its own project. I'd cut sonar from the proposal or demote it to future work.

## Where ML actually earns its place

Ranked by how defensible each is in a two-semester project:

**Strong: image-based localization against pre-cached satellite tiles.** This is a real, named research area (cross-view geo-localization), it has public datasets and published baselines, and critically you can validate the core contribution *entirely offline* on recorded imagery. No flight hours required to prove it works. That's an enormous de-risking property for a capstone, and it's a direct continuation of the GPS-denied survey thinking you were doing on the rover side.

**Medium: learned components inside a SLAM front end** — loop closure, place recognition, descriptor matching. Real, but you're competing with well-tuned classical methods, so the evaluation has to be careful.

**Weak: lidar denoising.** Statistical and radius outlier removal, voxel filtering, and intensity gating handle most of it. A learned denoiser needs labeled ground truth you won't have, and the honest baseline comparison will probably show the classical filter is fine. Good instinct to flag "we don't want to overdo it" — this is the place where that instinct applies hardest.

**Weak for now: ML for swarm position keeping.** Multi-agent RL for formation under comms constraints is a legitimate research direction and also a notorious time sink. Consensus and virtual-structure controllers are what the Calderon project already points at, and they're provable.

## How this maps onto the two offered projects

The Calderon swarm project is indoor, formation-focused, and hands you working infrastructure. Your mapping vision doesn't fit it directly, but a **cooperative coverage/survey mission** does: two swarms maintaining geometry while sweeping a sensor field, with formation error and coverage completeness as your metrics. That's a legitimate extension of their slide 8 mission sequence.

The Akbas RL project is the better bridge to your vision than it first appears, for one reason: Isaac Sim does high-fidelity simulated lidar and depth sensing. You could train and evaluate a policy for traversing cluttered space with simulated range sensing, then transfer to a Crazyflie with the Multi-ranger deck. The sim-to-real gap analysis they're asking for is the deliverable, and your sensing interests ride along inside it.

One correction for that slide, and it's a good thing to raise with Dr. Akbas: Isaac Gym is deprecated legacy software, superseded by Isaac Lab built on Isaac Sim. The Isaac Gym Preview Release, OmniIsaacGymEnvs, and Orbit are all deprecated in favor of Isaac Lab. Knowing that before you start saves you weeks of following dead tutorials.

## What the rubric is actually forcing

The template splits into Semester 1 and Semester 2 deliverables and asks for standards (Part 107 is your obvious one if anything flies outdoors, plus FCC for the radio links and possibly ASPRS/ASTM for mapping accuracy). It also asks for stakeholders, which for you is probably search-and-rescue teams, surveyors, or mine inspectors depending on which slice you take. And the budget section: if you use existing lab hardware, you write "$0" and the 10% redistributes into the sections you care about. If you want lidar and a real airframe, you're writing a low-four-figure build, and you should price that before you commit to it.

The one thing I'd want to know before going further: **are you choosing between the two offered projects, or proposing your own to one of these mentors?** That changes the advice completely. Picking an offered project means you inherit a working stack and spend the year on algorithms. Proposing your own means Semester 1 is procurement and bring-up, and the interesting work compresses into Semester 2.

Send me the rest of the ideas when you're ready.


also for the reinforcement learning, could we use blender, unreal engine, and cascadure or something to help use generate 3D realistic maps for simulation? then we could spawn drones and simulate sensors so that we could do ML training, we have access to an HPC vega with 8x H100 gpus, across 2 nodes - 1 node has 4 GPUs. we might not want to make it that big, but again jsut ideas that we need on a list for now because that is for the navigational machine learning. for the lidar machine learning we might not need entire forests spans randomly generated like minecraft or something, but we would need different 3d scenarios like chain link fences and glass or offices or oudoor pieces of environemtns jsut to encpomass the drone/lidar or something, or we could get measurements in real life for the lidar, but we cannot get everyting, ideally we would not need to do simulation, we could get data flying wayponit missions next to chain link fences and feed that data into the ML make sens? and then also flying next to buildings where there is glass, but then we would have to map out where the glass is. again all ideas and machine leraning demands data that might be tough to figure out, so any ideas you come up with for machine learning you also need to figure out what exactly is the data it needs to train on then how we could get that data. then why simulation would be used versus real life and things


Good questions, and the data audit you're asking for is exactly the right discipline. Two corrections first, one of which will save you real pain.

## Cascadeur is the wrong tool

It's a character animation package for humanoids and creatures. Nothing in it applies here. Drop it from the list.

## Your H100s cannot run Isaac Sim

This is the important one. NVIDIA's Isaac Sim requirements state plainly that GPUs without RT Cores, naming A100 and H100 specifically, are not supported. The listed minimum, good, and ideal configurations are all RTX-class consumer or workstation cards. Hopper dropped ray-tracing hardware because it's a compute part, and Isaac Sim's renderer, including its lidar and depth sensor simulation, depends on hardware RT.

This isn't fatal, but it forces an architecture decision you should make deliberately:

**Split rendering from training.** Anything that needs pixels or simulated lidar gets generated on an RTX workstation (or an L40S/RTX PRO node if your HPC has one) and cached to disk. The H100s then do what they're actually excellent at: training on that cached data, and running physics-only RL where the policy input is state vectors and range readings rather than images.

That split has a happy consequence. A Crazyflie with a Multi-ranger deck gives you maybe six ToF range measurements. A policy over that observation space needs no rendering at all, trains absurdly fast, and runs beautifully on H100s in Isaac Lab. If you're doing the Akbas project, **start there** and only add vision if the range-only policy proves insufficient. Check what else Vega has before assuming, though. Many university clusters have a visualization partition with RTX cards precisely for this.

## The pipeline, if you go this route

Blender → USD → Isaac Sim is the sane path. Blender is genuinely useful upstream: Geometry Nodes will do your procedural forest generation, and it exports USD natively, which is Isaac Sim's scene format. Unreal is a second photoreal renderer with a separate asset pipeline and an awkward RL loop; adding it means maintaining two of everything for a marginal fidelity gain you probably can't measure.

Also, don't build a drone simulator from scratch. Look at **Aerial Gym Simulator** (built for quadrotors on the Isaac stack, includes depth and lidar rendering), **Pegasus Simulator** (Isaac Sim, PX4-in-the-loop), and **Colosseum** (the community fork of Microsoft's archived AirSim, Unreal-based). One of these is probably 70% of what you'd otherwise spend a semester writing. Also flag: authoring an asset pipeline is a full semester of work containing zero machine learning. That's a real cost to weigh.

## The data audit

Here's the framework, then each candidate against it. For every model, four questions: what's the input, what is a *label*, where do labels come from, and does sim or reality produce them more cheaply.

**Navigation policy (RL).** Input is sensor readings plus goal; output is velocity commands. There are no labels at all, only a reward function and experience. Simulation isn't a convenience here, it's mandatory, because the training signal comes from millions of collisions you cannot afford in hardware. This is the single cleanest sim justification in your whole vision, and it's why the Akbas project is structured the way it is. Your design artifacts are the reward function and the randomization ranges (obstacle density, sensor noise, latency, mass, thrust, wind).

**Cross-view geo-localization (down-camera → position).** Input is a downward image; output is position within your pre-cached tile set. **The label is the GPS coordinate of the capture, which means labels are free.** You fly with GPS, log it, train on it, then deploy in the GPS-denied case. Better still, you can build a large training set with no flying at all: public orthoimagery (NAIP in the US is free and public domain) sampled at two resolutions gives you "drone view" and "map view" pairs. Public benchmarks exist too (CVUSA, CVACT, University-1652, VIGOR) so you have baselines to compare against, which the rubric's evaluation section will want. Simulation adds nothing here. Reality is cheaper *and* better.

**Lidar disambiguation.** This is the hard one, and you already found the crux: to label glass, you have to know where the glass is. Two things worth separating, because you've been treating them as one problem:

- **Chain-link fence** is a sparse-aperture problem. The beam partially passes through, so you get returns from both the wire and whatever is behind it, mixed in the same neighborhood.
- **Glass** is a specular problem. You get either no return at all (pass-through) or a mirror ghost: a reflected copy of the scene appearing at roughly twice the true distance, geometrically plausible and completely wrong.

Different physics, different failure signatures, probably different training data.

The labeling trick that makes real-world collection tractable: **get ground truth from a modality that doesn't fail the same way.** Measure the fence plane or glass facade with a tape measure and a few control points, fit the plane, and now every point in your cloud has a known signed distance to the true surface. Points behind the glass plane at ~2× range are ghosts. Points scattered around the fence plane are wire returns. That auto-labels an entire scan from about twenty minutes of manual survey work. It scales to a handful of controlled scenes, which is a fine capstone scope. It does not scale to forests, which is why "randomly generated forest spans" is the wrong ambition for this particular model.

And a caution on simulating this: simulated lidar tends to be **too clean**, and glass multipath in particular is poorly modeled by most sensor sims. A denoiser trained on synthetic noise learns to remove synthetic noise. For this model, your instinct to collect real data is correct, and the reason is that the phenomenon you're modeling is precisely the one simulation gets wrong.

## The decision rule, compressed

Simulate when labels are physically impossible to obtain, when the process is destructive, or when you need volume. Use real data when a second sensor hands you labels for free, or when the phenomenon is exactly the thing physics engines model badly. Do both when the sim-real gap is itself your research contribution, which is literally the Akbas deliverable.

Applied to your list: **navigation → sim. Geo-localization → real, and cheap. Lidar disambiguation → real, scoped to two or three controlled scenes.** That's a coherent answer, and notably it means the giant Blender/Unreal world-generation pipeline is only justified for one of the three.

Keep the ideas coming when you have them.





then also we could do both the machine learning and drone swarm - that is the ml enhanced navigation of a single drone, but we could then add a drone swarm, so two different ml models at different levels among the swarm. i already have alot of researh for how ml models at the edge would work and using ai and ml for denoising sensors or data make sense? ok and then also please let me know, the HPC is linux and we can run applications that can be installed to user's local bin or something on the hpc and coordinate using resources just fine i have plenty of notes about it but won't share them here, so don't jsut discount things yet just becuase you think we can or cannot run them on the HPC, again this list of ideas really should not have any ideas removed from it unless it is not within the preferences of the humans, but we do wnat to keep track of the ideas for proejcts we don't want to do and why make sense? that way we don't get confused in the future


Fair correction on the framing, and let me narrow my claim rather than retract it, because the two things are different.

What I asserted was a hardware feature gap: NVIDIA's own docs say Isaac Sim's **RTX renderer** requires RT cores and names H100 as unsupported. That's about silicon, not about permissions or userspace installs, and it doesn't generalize to "simulation on Vega." I stated it too broadly. Here's the accurate scope, which is much narrower and mostly good news:

- **Isaac Lab physics-only training** (state and range observations, no cameras) runs on PhysX without touching the ray tracer. Should be fine on H100.
- **MuJoCo/MJX or Genesis** are pure-physics GPU simulators with no RT dependency at all, and MuJoCo has built-in rangefinder sensors. Excellent H100 fit.
- **NVIDIA Warp** does GPU mesh raycasting against its own BVH. You can generate simulated lidar returns at scale on H100s without RTX hardware if you're willing to write the sensor model yourself. Worth verifying against current Warp docs, but this is the route that keeps lidar sim on your cluster.
- **Blender Cycles** renders on the CUDA backend without RT cores. Slower than OptiX, but for offline dataset generation you don't care.
- What's genuinely off the table on those nodes is Isaac Sim's photoreal RTX path and its built-in RTX lidar. That's one component, not the whole plan.

## The two-level ML idea

This is a good structure and it's the standard hierarchical decomposition, so you'd be on solid literature. The thing that decides whether it works isn't the models, it's **the interface between them**. Pick that early: does the swarm layer output formation slot assignments, virtual-leader poses, or goal waypoints per agent? Whatever you choose becomes the action space above and the goal input below, and changing it later invalidates both models.

Two design points that will save you a semester:

**Train the levels separately, not jointly.** Get the single-agent policy working, freeze it, then treat it as part of the environment while training the swarm layer on top. Joint end-to-end training of a hierarchy is a research problem with a bad debugging story. Separated, each level has its own metric and its own failure mode.

**Centralized training, decentralized execution** is the paradigm you want to name in the proposal, and it maps cleanly onto your setup: train with global state on the HPC, deploy with only local observations and neighbor messages. Your edge-ML research plugs in right there.

On edge specifically, the concrete ceiling: the Crazyflie AI-deck's GAP8 can run genuinely tiny CNNs onboard. **PULP-DroNet** is the canonical published example and a good citation for you. Anything larger runs on the ground station and streams commands over the radio, which is what the Calderon stack already does. So "ML at the edge" is real but the edge is very small, and that's a design constraint worth writing down rather than discovering later.

## The register

Built the tracking document you asked for, with a status taxonomy that includes parked and rejected entries plus the reason, so nothing gets silently dropped or re-litigated later.Everything from the last three messages is in there, including the things I'd argued against, with the reasoning attached rather than just the verdict. A few structural notes on how I filled it out:

I split "learned lidar denoising" (rejected) from "glass/fence disambiguation" (parked) because they're genuinely different problems and only one has a workable labeling strategy. Sonar is the only hard rejection on physics grounds, and I noted what you'd actually want instead if the real goal was seeing through dirt.

Section 7 is the constraints, not ideas — the things that are true regardless of what we pick. I rewrote the H100 entry as a scoped checklist rather than a blocker.

Section 10 is empty and waiting for the rest of your ideas.



also there are other reasons why chainlink fence and glass and grass and more are hard on lidar so don't just make lots of assumptions, i am just sharing scenarios of problems and why our project would be working to solve it, i just want to know what the requirements are and how we would proceed about solving the problem, you don't have to reserach every little detail but do research all that you can to fill in as many gaps, these ideas all overlap in scope so that is why just researhing as much as you can in general wlll help out, and don't plan out the entire project yet, just keep in mind all the requirements for the project based on the idea, so your list of ideas shoud include teh projec, problem, why it is a problem, then don't propose an outright solution that might immediately change, but list concepts involved with the solution and who knows maybe there are other sensors that can help. make sense? do not include cost, an you can see some other items involved with what we need for a project idea



Good push. Let me actually research the sensor physics rather than reason from first principles, since that's where the requirements come from.


sorry to interrupt, but i just wanted to clarify - so yes take the documetn you made about the idea register and just make it "meta idea register" so it about how the register is built, then make a separate documetn that is teh actual idea register. make sense? ok please continue all your research and make sure to document your findings, you can make multiple findings documents and organize them however is needed, they don't need to be discriminated based on "the probelm being solved" it could be able about system capabilities nad how it ties to other systems and stuff, and please incldue file references for cross referencing the files amke sens? okay otherwise continue


No problem — that's a cleaner structure. Let me finish the research pass first, then rebuild the file set that way.Research pass done. Rebuilding the file set with the split you asked for.Eight files, cross-referenced through `INDEX.md`. Cost removed everywhere. Register entries now use the problem/why-it's-a-problem/concepts-involved shape with no committed solution.

The research changed several things I'd told you earlier, and you were right to push:

**Chain-link and glass aren't the same category of problem, and neither is what I said.** The fence issue is primarily geometric: the beam is a diverging cone, so a Velodyne VLP-16 with 0.17°×0.09° divergence has a spot roughly 40mm×25mm at 10m, and when that footprint hits a small structure or an edge the computed range can be an average of multiple observations — a "mixed pixel". Filtering by return type helps but the false measurement persists when the return is counted as a single one. That's a much better-specified problem than "the beam passes through the mesh."

For glass, detection depends on the angle of inclination, the material, and the thickness, and there's a newer failure mode I didn't know about: as lidar shifts to compact solid-state arrays, internal-multipath glare appears — light from a bright or retroreflective surface scatters inside the sensor and spreads across the pixel array, creating phantom objects and obscuring real ones. That's a sensor-architecture problem, not a scene problem.

**Grass is a different failure again**, and I'd have gotten it wrong: low vegetation produces a systematic positive height shift during terrain model generation, and when the shift is small it's difficult to separate from random measurement noise. Systematic, so averaging won't fix it. The fix is sensor-side — full-waveform data lets you detect weak returns backscattered by bare terrain under canopy.

**Two sensors you should have on the list that weren't.** Polarization imaging pairs with lidar in a specifically useful way: lidar detects glass at low incidence angles and the polarization camera detects it at large incidence angles, and public annotated datasets already exist. And mmWave radar, where the trade is stark — fog and smoke have negligible effect on millimeter waves due to the size disparity between particles and wavelength, while they have the largest impact on lidar, but single-chip radars achieve angular resolution two orders of magnitude worse than lidar. That gap is itself an ML opportunity with a free labelling scheme: supervise radar with co-mounted lidar in clear air, deploy in smoke.

**"4D mapping" now has real substance.** M3C2 is the standard method, but it assumes planar surfaces and uniform registration error, and on natural surfaces that overestimates the level of detection. The error-propagation variant matters for you specifically because it allows combining datasets with different accuracies — multiple scan positions, different sensors, different platforms — without degrading the resulting level of detection. That's exactly the heterogeneous-swarm case.

**Your comms intuition was better-founded than I gave credit for.** Dense-forest networks are limited by signal attenuation as a first-order problem, and UAV-relayed measurements show link quality varying with height as well as distance. Above-canopy relay and below-canopy sensing have incompatible position requirements, which is a much stronger argument for heterogeneity than "air and ground are complementary."

One thing that surfaced and isn't in any entry yet: multiple lidars in the same volume can trigger on each other's pulses. If a lidar-carrying swarm stays on the table, that needs its own entry.


