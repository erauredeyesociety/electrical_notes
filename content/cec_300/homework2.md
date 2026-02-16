# DeepSeek Conversation

## User Message 1

please show all work for homework 2 and provide references to lecture material.  i can provide clarity for images like the VOR indicator. 

for the VOR indicator....

we see FR. N for north is at the very top of the indicator.... i belive it is the track or something... the CDI line goes from being at the top at North and then comes downward to the left side towards the number 22 line.... or between the second and third DOT from the left. make sense?

### DeepSeek Response

# CEC 300 - Module 2 Homework Solutions

## Problem 1: DME Pulse Analysis

### Understanding the DME System (from Module 2a - Navigation Systems)

Based on the lecture material, DME (Distance Measurement Equipment) operates as follows:

- Frequencies: Airborne: 1025-1150 MHz; Ground: ±63 MHz from transmit frequency
- Pulse pair spacings (from Module 2a, slide 30):

Frequencies: Airborne: 1025-1150 MHz; Ground: ±63 MHz from transmit frequency

Pulse pair spacings (from Module 2a, slide 30):

Key concepts from lecture:

- Radar mile: 12.36 μs per nautical mile (round trip) (Module 2a, slide 32)
- FRUIT: Friendly Replies Unsynchronized in Time - replies meant for other aircraft (slide 34)
- GARBLE: When interference scrambles signals preventing correct output (slide 35)
- Maximum range: 200 nmi per FARs (slide 33)
- No reply condition: When measured time exceeds 200 nmi (slide 33)

Radar mile: 12.36 μs per nautical mile (round trip) (Module 2a, slide 32)

FRUIT: Friendly Replies Unsynchronized in Time - replies meant for other aircraft (slide 34)

GARBLE: When interference scrambles signals preventing correct output (slide 35)

Maximum range: 200 nmi per FARs (slide 33)

No reply condition: When measured time exceeds 200 nmi (slide 33)

### Distance Calculation Formula

From Module 2a, slide 33:

```text
Distance (nmi) = (time_between_first_pulses - ground_delay) / 12.36
```

Where:

- time_between_first_pulses = response_first_pulse - transmit_first_pulse
- Ground delay: 50 μs for both X and Y channels

time_between_first_pulses = response_first_pulse - transmit_first_pulse

`time_between_first_pulses = response_first_pulse - transmit_first_pulse` Ground delay: 50 μs for both X and Y channels

### Python Implementation

```python
def DME(t1, t2, t3, t4):
    """
    Analyze DME pulses and determine channel, distance, or error conditions.
    
    Parameters:
    t1, t2: times of leading edges of transmitted pulses (μs)
    t3, t4: times of leading edges of received response pulses (μs)
    """
    
    # Calculate pulse pair spacings
    tx_spacing = t2 - t1
    rx_spacing = t4 - t3
    
    # Calculate time between first pulses of sent and received signals
    time_between_first = t3 - t1
    
    # Channel X characteristics (from Module 2a, slide 30)
    X_TX_SPACING = 12  # μs
    X_RX_SPACING = 12  # μs
    X_DELAY = 50       # μs
    
    # Channel Y characteristics (from Module 2a, slide 30)
    Y_TX_SPACING = 36  # μs
    Y_RX_SPACING = 30  # μs
    Y_DELAY = 50       # μs
    
    # Constants
    RADAR_MILE = 12.36  # μs per nautical mile (Module 2a, slide 32)
    MAX_RANGE = 200     # nautical miles (Module 2a, slide 33)
    
    # Check if pulse spacings are valid for any channel
    tx_x_valid = abs(tx_spacing - X_TX_SPACING) < 0.5  # Allow small floating point tolerance
    rx_x_valid = abs(rx_spacing - X_RX_SPACING) < 0.5
    tx_y_valid = abs(tx_spacing - Y_TX_SPACING) < 0.5
    rx_y_valid = abs(rx_spacing - Y_RX_SPACING) < 0.5
    
    # Check for garbled signals (invalid spacings or arrival before ground delay)
    # Ground stations add fixed delay before retransmitting (Module 2a, slide 33)
    if time_between_first < X_DELAY or time_between_first < Y_DELAY:
        print("Signal Garbled.")
        return
    
    # Check for valid channel X
    if tx_x_valid and rx_x_valid:
        channel = "X"
        ground_delay = X_DELAY
        # Check if this is FRUIT (valid X spacing but wrong channel)
        # Not applicable since we're checking both TX and RX for X
    # Check for valid channel Y
    elif tx_y_valid and rx_y_valid:
        channel = "Y"
        ground_delay = Y_DELAY
    else:
        # Check for FRUIT (valid pulse spacing for one channel when transmitting on another)
        # From Module 2a, slide 34-35: FRUIT occurs when we receive pulses meant for other aircraft
        if (tx_x_valid and rx_y_valid) or (tx_y_valid and rx_x_valid):
            print("FRUIT detected.")
            return
        else:
            print("Signal Garbled.")
            return
    
    # Calculate distance
    # Distance formula from Module 2a, slide 33
    distance = (time_between_first - ground_delay) / RADAR_MILE
    
    # Check for no reply condition (exceeds 200 nmi)
    # Module 2a, slide 33: "The maximum range allowed for use in FARs is 200nm"
    if distance > MAX_RANGE:
        print(f"Channel is {channel}, no reply.")
        return
    
    # Print result with one decimal place as specified
    print(f"Channel is {channel}, distance is {distance:.1f} nm.")

# Test cases from homework
if __name__ == "__main__":
    test_cases = [
        (572, 584, 772, 784),      # Example from prompt: should be X, 12.1 nm
        (1011, 1047, 1361, 1391),   # Test case 2
        (1671, 1683, 2081, 2117),   # Test case 3
        (2307, 2319, 2337, 2349),   # Test case 4
        (5181, 5217, 7767, 7797),   # Test case 5
        (8011, 8047, 8300, 8322)    # Test case 6
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: DME{test}")
        DME(*test)
```

### Verification of Example

For the example DME(572,584,772,784):

`DME(572,584,772,784)` - TX spacing = 584 - 572 = 12 μs ✓ (Channel X)
- RX spacing = 784 - 772 = 12 μs ✓ (Channel X)
- Time between first pulses = 772 - 572 = 200 μs
- Distance = (200 - 50) / 12.36 = 150 / 12.36 = 12.14 nm ✓

TX spacing = 584 - 572 = 12 μs ✓ (Channel X)

RX spacing = 784 - 772 = 12 μs ✓ (Channel X)

Time between first pulses = 772 - 572 = 200 μs

Distance = (200 - 50) / 12.36 = 150 / 12.36 = 12.14 nm ✓

### References to Lecture Material

- Module 2a, Slide 30: DME channel pulse pair spacings table
- Module 2a, Slide 32: Definition of radar mile (12.36 μs)
- Module 2a, Slide 33: Distance formula and 50 μs ground delay for X channel
- Module 2a, Slide 33: Maximum range of 200 nmi per FARs
- Module 2a, Slide 34: FRUIT definition (Friendly Replies Unsynchronized in Time)
- Module 2a, Slide 35: GARBLE definition (scrambled signals)

Module 2a, Slide 30: DME channel pulse pair spacings table

Module 2a, Slide 32: Definition of radar mile (12.36 μs)

Module 2a, Slide 33: Distance formula and 50 μs ground delay for X channel

Module 2a, Slide 33: Maximum range of 200 nmi per FARs

Module 2a, Slide 34: FRUIT definition (Friendly Replies Unsynchronized in Time)

Module 2a, Slide 35: GARBLE definition (scrambled signals)

## Problem 2: VOR Indicator Analysis

Based on the description: "FR. N for north is at the very top... the CDI line goes from being at the top at North and then comes downward to the left side towards the number 22 line... between the second and third DOT from the left"

### Understanding VOR Operation (from Module 2a)

From Module 2a, slides 19-22:

- VOR indicates which radial the aircraft is on relative to the station
- The phase angle between reference and variable signals determines the bearing
- The Course Deviation Indicator (CDI) shows deviation from the selected radial

VOR indicates which radial the aircraft is on relative to the station

The phase angle between reference and variable signals determines the bearing

The Course Deviation Indicator (CDI) shows deviation from the selected radial

### Analysis

a. What radial is the VOR set to?

The OBS (Omni Bearing Selector) is set to the radial displayed at the top of the indicator. With North at the top, the selected radial is 360° (or 0°).

b. Does the indicator show that we must turn left or right?

The CDI needle is deflected to the left of center. Standard VOR interpretation: "Fly toward the needle." Since the needle is left of center, the aircraft must turn left to intercept the selected radial.

c. What degree of heading change is needed approximately?

The CDI is deflected approximately 2-3 dots from center. On a standard VOR indicator, full scale deflection is typically 10-12° per side, with each dot representing 2°.

- Deflection: between 2nd and 3rd dot = approximately 4-5° left
- Therefore, a heading change of approximately 4-5° to the left is needed

Deflection: between 2nd and 3rd dot = approximately 4-5° left

Therefore, a heading change of approximately 4-5° to the left is needed

How determined: The number of dots of deflection multiplied by the standard 2° per dot gives the angular deviation from the selected radial. The pilot must turn toward the needle by approximately this amount.

### References to Lecture Material

- Module 2a, Slide 19: VOR indicates which radial the aircraft is on; TO/FROM flag interpretation
- Module 2a, Slide 21-22: Phase angle between reference and variable signals determines bearing
- Module 2a, Slide 23: Basic VOR indicator components and CDI operation

Module 2a, Slide 19: VOR indicates which radial the aircraft is on; TO/FROM flag interpretation

Module 2a, Slide 21-22: Phase angle between reference and variable signals determines bearing

Module 2a, Slide 23: Basic VOR indicator components and CDI operation

## Problem 2a: ILS Localizer Signal Characteristics

From Module 2a, slides 44-51 on Instrument Landing System:

### Signal Characteristics When Left of Runway Centerline

When aircraft is left of runway centerline:

- Localizer signals: The 90 Hz modulation dominates over 150 Hz modulation
- CDI indication: Needle deflects to the right (indicating "fly right" to intercept centerline)
- This is because the 90 Hz modulated signal is transmitted with a pattern that points to the left side of the runway (Module 2a, slide 50)

Localizer signals: The 90 Hz modulation dominates over 150 Hz modulation

CDI indication: Needle deflects to the right (indicating "fly right" to intercept centerline)

This is because the 90 Hz modulated signal is transmitted with a pattern that points to the left side of the runway (Module 2a, slide 50)

### Signal Characteristics When Right of Runway Centerline

When aircraft is right of runway centerline:

- Localizer signals: The 150 Hz modulation dominates over 90 Hz modulation
- CDI indication: Needle deflects to the left (indicating "fly left" to intercept centerline)

Localizer signals: The 150 Hz modulation dominates over 90 Hz modulation

CDI indication: Needle deflects to the left (indicating "fly left" to intercept centerline)

### Technical Explanation

From Module 2a, slides 46-48:

- The localizer uses two types of modulation: 90 Hz (left side) and 150 Hz (right side)
- Space modulation creates overlapping signal patterns
- The receiver compares the depth of modulation of the two signals
- When equally balanced, the aircraft is on the centerline

The localizer uses two types of modulation: 90 Hz (left side) and 150 Hz (right side)

Space modulation creates overlapping signal patterns

The receiver compares the depth of modulation of the two signals

When equally balanced, the aircraft is on the centerline

### References to Lecture Material

- Module 2a, Slide 44-45: Localizer provides alignment with runway centerline
- Module 2a, Slide 46: Two types of modulation (90 Hz and 150 Hz)
- Module 2a, Slide 48: Space modulation concept
- Module 2a, Slide 50: 90 Hz modulation pointing left, 150 Hz pointing right

Module 2a, Slide 44-45: Localizer provides alignment with runway centerline

Module 2a, Slide 46: Two types of modulation (90 Hz and 150 Hz)

Module 2a, Slide 48: Space modulation concept

Module 2a, Slide 50: 90 Hz modulation pointing left, 150 Hz pointing right

## Problem 2b: ILS Category for 950 ft Runway Visibility

From Module 2a, slides 55-59 on ILS Categories:

### ILS Category Requirements

### Analysis

Given runway visibility of 950 feet:

- Convert to meters: 950 ft × 0.3048 = approximately 290 m
- Compare with CAT II requirement: > 200 m (700 ft) ✓
- Compare with CAT IIIA: 150-700 ft (50-200 m) - 950 ft exceeds this range

Convert to meters: 950 ft × 0.3048 = approximately 290 m

Compare with CAT II requirement: > 200 m (700 ft) ✓

Compare with CAT IIIA: 150-700 ft (50-200 m) - 950 ft exceeds this range

Answer: A transport category jet with 950 feet runway visibility would be operating under CAT II minimums.

### References to Lecture Material

- Module 2a, Slide 55: ILS Category table with RVR requirements
- Module 2a, Slide 56-59: Detailed category breakdowns

Module 2a, Slide 55: ILS Category table with RVR requirements

Module 2a, Slide 56-59: Detailed category breakdowns

## Problem 3: GPS 3D Position Determination and Error Sources

### How GPS Determines 3D Position

Based on Module 2b (Satellite Navigation: GPS) slides 32-37:

Basic Principle: GPS uses trilateration - determining position by measuring distances to multiple satellites with known positions.

Step 1: Time-of-Flight MeasurementEach GPS satellite broadcasts a Pseudorandom Noise (PRN) code at a precise time (Module 2b, slide 32). The receiver generates the same code locally and compares the phase shift between the received and generated codes. This phase shift represents the signal travel time.

Step 2: Range CalculationThe distance (pseudorange) to each satellite is calculated as:

```text
pseudorange = speed of light × time delay
```

However, this is called "pseudo" range because it includes the receiver's clock error (Module 2b, slide 35).

Step 3: Solving for PositionWith one satellite, the receiver's position lies on a sphere centered at that satellite. With two satellites, the intersection is a circle. With three satellites, two possible points exist (one usually impossible). Four satellites are needed to solve for x, y, z, and time simultaneously (Module 2b, slide 34-35).

The fundamental equation:

```text
ρᵢ = √[(xᵢ - x)² + (yᵢ - y)² + (zᵢ - z)²] + c·Δt
```

where:

- ρᵢ = pseudorange to satellite i
- (xᵢ, yᵢ, zᵢ) = position of satellite i (from ephemeris data)
- (x, y, z) = receiver position (unknown)
- c = speed of light
- Δt = receiver clock error (unknown)

ρᵢ = pseudorange to satellite i

(xᵢ, yᵢ, zᵢ) = position of satellite i (from ephemeris data)

(x, y, z) = receiver position (unknown)

c = speed of light

Δt = receiver clock error (unknown)

With four satellites, we have four equations and four unknowns, solvable through iterative methods like least squares estimation.

Step 4: Navigation Message DecodingThe receiver demodulates the navigation message from each satellite (Module 2b, slide 47), which contains:

- Ephemeris parameters (satellite orbit information) (slide 77)
- Almanac data (approximate orbits of all satellites)
- Clock correction parameters
- Ionospheric correction models

Ephemeris parameters (satellite orbit information) (slide 77)

Almanac data (approximate orbits of all satellites)

Clock correction parameters

Ionospheric correction models

### Sources of GPS Error

From Module 2b, slide 88 (Table 8.2):

Additional Considerations:

Geometric Dilution of Precision (GDOP) (Module 2b, slides 82-84):

- PDOP (Position DOP): Quality metric based on satellite geometry
- HDOP (Horizontal DOP): Error in horizontal position
- VDOP (Vertical DOP): Error in vertical position (typically larger)
- Values 1-2 = Excellent, 3-5 = Good/Moderate, 6+ = Poor

PDOP (Position DOP): Quality metric based on satellite geometry

HDOP (Horizontal DOP): Error in horizontal position

VDOP (Vertical DOP): Error in vertical position (typically larger)

Values 1-2 = Excellent, 3-5 = Good/Moderate, 6+ = Poor

Selective Availability (historical):

- Turned off by presidential order in 2000
- Previously introduced intentional errors for non-military users

Turned off by presidential order in 2000

Previously introduced intentional errors for non-military users

### References to Lecture Material

- Module 2b, Slide 32-34: Trilateration concept with spheres
- Module 2b, Slide 35: Importance of atomic clock synchronization
- Module 2b, Slide 45: Pseudorange calculation via autocorrelation
- Module 2b, Slide 47: Navigation message structure
- Module 2b, Slide 77: Ephemeris parameters
- Module 2b, Slide 82-84: Dilution of Precision concepts
- Module 2b, Slide 88: Comprehensive error source table

Module 2b, Slide 32-34: Trilateration concept with spheres

Module 2b, Slide 35: Importance of atomic clock synchronization

Module 2b, Slide 45: Pseudorange calculation via autocorrelation

Module 2b, Slide 47: Navigation message structure

Module 2b, Slide 77: Ephemeris parameters

Module 2b, Slide 82-84: Dilution of Precision concepts

Module 2b, Slide 88: Comprehensive error source table

## Problem 4: Satellite Sensors and Actuators

### 4a. Reaction Wheels vs. Magnetorquers

From Module 2c (Spacecraft GNC Elements), slides 7-9:

Reaction Wheels (Module 2c, slide 7):

- Principle: Store angular momentum through spinning mass; conservation of momentum causes spacecraft to counter-rotate
- Configuration: Typically 3 orthogonal wheels for 3-axis control, often with 4th for redundancy
- Advantages: High precision pointing, smooth control, no fuel consumption
- Disadvantages: Can become saturated (reach maximum speed), mechanical complexity, failure prone

Principle: Store angular momentum through spinning mass; conservation of momentum causes spacecraft to counter-rotate

Configuration: Typically 3 orthogonal wheels for 3-axis control, often with 4th for redundancy

Advantages: High precision pointing, smooth control, no fuel consumption

Disadvantages: Can become saturated (reach maximum speed), mechanical complexity, failure prone

Magnetorquers (Module 2c, slide 9):

- Principle: Create magnetic dipole that interacts with Earth's magnetic field to generate torque: T = M × B
- Configuration: Three orthogonal coils or torquer bars
- Advantages: No moving parts (high reliability), low mass, no consumables
- Disadvantages: Limited to planets with magnetic fields, lower torque, slow response

Principle: Create magnetic dipole that interacts with Earth's magnetic field to generate torque: T = M × B

Configuration: Three orthogonal coils or torquer bars

Advantages: No moving parts (high reliability), low mass, no consumables

Disadvantages: Limited to planets with magnetic fields, lower torque, slow response

How They Complement Each Other:

- Reaction wheels provide precise, rapid attitude control but can saturate
- Magnetorquers are used to "desaturate" reaction wheels by applying external torque to slow the wheels back to nominal speed (Module 2c, slide 7)
- Magnetorquers handle coarse attitude control and momentum management while reaction wheels handle fine pointing

Reaction wheels provide precise, rapid attitude control but can saturate

Magnetorquers are used to "desaturate" reaction wheels by applying external torque to slow the wheels back to nominal speed (Module 2c, slide 7)

Magnetorquers handle coarse attitude control and momentum management while reaction wheels handle fine pointing

### 4b. Fiber-Optic Gyroscopes and the Sagnac Effect

From Module 2c, slide 19:

Fiber-Optic Gyroscope (FOG) Operation:A FOG measures angular rate by splitting a laser beam and sending the two beams in opposite directions through a long coil of optical fiber. When the coil rotates, the beam traveling in the direction of rotation travels a slightly longer path than the counter-rotating beam.

The Sagnac Effect:When two light beams travel in opposite directions around a rotating closed loop, they experience a phase difference proportional to the rotation rate. This phase shift Δφ is given by:

```text
Δφ = (8π·A·Ω)/(λ·c)
```

where:

- A = area enclosed by the optical path
- Ω = angular rotation rate
- λ = wavelength of light
- c = speed of light

A = area enclosed by the optical path

Ω = angular rotation rate

λ = wavelength of light

c = speed of light

Determining Angular Rate:The phase difference is measured by interfering the two returning beams. The interference pattern shifts proportionally to the rotation rate. By measuring this shift, the angular velocity about the sensor's axis is determined. Integration of this rate over time yields the angular position.

### 4c. Deep Space Network (DSN) for Guidance and Control

From Module 2c, slide 21 and Module 7 concepts:

DSN Components:

- Three ground complexes spaced approximately 120° apart (Goldstone, CA; Madrid, Spain; Canberra, Australia)
- Large parabolic antennas (34m and 70m dishes)
- Atomic clock timing synchronization

Three ground complexes spaced approximately 120° apart (Goldstone, CA; Madrid, Spain; Canberra, Australia)

Large parabolic antennas (34m and 70m dishes)

Atomic clock timing synchronization

Guidance and Control Functions:

- Two-Way Ranging: DSN transmits signal to spacecraft; spacecraft returns signal; round-trip time gives distance (range) measurement
- Doppler Tracking: Frequency shift of received signal provides line-of-sight velocity
- Delta-Differential One-Way Ranging (ΔDOR): Using multiple DSN sites to determine angular position with high precision
- Command Upload: DSN transmits navigation commands, trajectory correction maneuvers, and software updates
- Telemetry Reception: Spacecraft transmits health data, attitude information, and scientific data back through DSN
- Orbit Determination: Ground-based computers process ranging and Doppler data to determine precise orbit and generate ephemeris predictions

Two-Way Ranging: DSN transmits signal to spacecraft; spacecraft returns signal; round-trip time gives distance (range) measurement

Doppler Tracking: Frequency shift of received signal provides line-of-sight velocity

Delta-Differential One-Way Ranging (ΔDOR): Using multiple DSN sites to determine angular position with high precision

Command Upload: DSN transmits navigation commands, trajectory correction maneuvers, and software updates

Telemetry Reception: Spacecraft transmits health data, attitude information, and scientific data back through DSN

Orbit Determination: Ground-based computers process ranging and Doppler data to determine precise orbit and generate ephemeris predictions

Key Challenge: Beyond cislunar space, communication delays become significant (minutes to hours). This requires onboard autonomy between DSN contacts, with DSN providing periodic updates and corrections.

### References to Lecture Material

- Module 2c, Slide 7: Reaction wheel operation and desaturation
- Module 2c, Slide 9: Magnetorquer physics and applications
- Module 2c, Slide 19: Fiber-optic gyroscope and Sagnac effect
- Module 2c, Slide 21: Deep Space Network and transponders

Module 2c, Slide 7: Reaction wheel operation and desaturation

Module 2c, Slide 9: Magnetorquer physics and applications

Module 2c, Slide 19: Fiber-optic gyroscope and Sagnac effect

Module 2c, Slide 21: Deep Space Network and transponders

## References Summary

Module 2a - Navigation Systems:

- Slides 30-35: DME operation, channels, FRUIT, GARBLE, distance calculation
- Slides 44-51: ILS localizer principles and modulation
- Slides 55-59: ILS categories and minima
- Slides 19-23: VOR operation and interpretation

Slides 30-35: DME operation, channels, FRUIT, GARBLE, distance calculation

Slides 44-51: ILS localizer principles and modulation

Slides 55-59: ILS categories and minima

Slides 19-23: VOR operation and interpretation

Module 2b - Satellite Navigation (GNSS):

- Slides 32-37: GPS trilateration principles
- Slide 88: GPS error sources table
- Slides 82-84: Dilution of Precision concepts

Slides 32-37: GPS trilateration principles

Slide 88: GPS error sources table

Slides 82-84: Dilution of Precision concepts

Module 2c - Spacecraft GNC Elements:

- Slides 7-9: Reaction wheels vs. magnetorquers
- Slide 19: Fiber-optic gyroscopes and Sagnac effect
- Slide 21: Deep Space Network applications

Slides 7-9: Reaction wheels vs. magnetorquers

Slide 19: Fiber-optic gyroscopes and Sagnac effect

Slide 21: Deep Space Network applications

```text
Distance (nmi) = (time_between_first_pulses - ground_delay) / 12.36
```

```python
def DME(t1, t2, t3, t4):
    """
    Analyze DME pulses and determine channel, distance, or error conditions.
    
    Parameters:
    t1, t2: times of leading edges of transmitted pulses (μs)
    t3, t4: times of leading edges of received response pulses (μs)
    """
    
    # Calculate pulse pair spacings
    tx_spacing = t2 - t1
    rx_spacing = t4 - t3
    
    # Calculate time between first pulses of sent and received signals
    time_between_first = t3 - t1
    
    # Channel X characteristics (from Module 2a, slide 30)
    X_TX_SPACING = 12  # μs
    X_RX_SPACING = 12  # μs
    X_DELAY = 50       # μs
    
    # Channel Y characteristics (from Module 2a, slide 30)
    Y_TX_SPACING = 36  # μs
    Y_RX_SPACING = 30  # μs
    Y_DELAY = 50       # μs
    
    # Constants
    RADAR_MILE = 12.36  # μs per nautical mile (Module 2a, slide 32)
    MAX_RANGE = 200     # nautical miles (Module 2a, slide 33)
    
    # Check if pulse spacings are valid for any channel
    tx_x_valid = abs(tx_spacing - X_TX_SPACING) < 0.5  # Allow small floating point tolerance
    rx_x_valid = abs(rx_spacing - X_RX_SPACING) < 0.5
    tx_y_valid = abs(tx_spacing - Y_TX_SPACING) < 0.5
    rx_y_valid = abs(rx_spacing - Y_RX_SPACING) < 0.5
    
    # Check for garbled signals (invalid spacings or arrival before ground delay)
    # Ground stations add fixed delay before retransmitting (Module 2a, slide 33)
    if time_between_first < X_DELAY or time_between_first < Y_DELAY:
        print("Signal Garbled.")
        return
    
    # Check for valid channel X
    if tx_x_valid and rx_x_valid:
        channel = "X"
        ground_delay = X_DELAY
        # Check if this is FRUIT (valid X spacing but wrong channel)
        # Not applicable since we're checking both TX and RX for X
    # Check for valid channel Y
    elif tx_y_valid and rx_y_valid:
        channel = "Y"
        ground_delay = Y_DELAY
    else:
        # Check for FRUIT (valid pulse spacing for one channel when transmitting on another)
        # From Module 2a, slide 34-35: FRUIT occurs when we receive pulses meant for other aircraft
        if (tx_x_valid and rx_y_valid) or (tx_y_valid and rx_x_valid):
            print("FRUIT detected.")
            return
        else:
            print("Signal Garbled.")
            return
    
    # Calculate distance
    # Distance formula from Module 2a, slide 33
    distance = (time_between_first - ground_delay) / RADAR_MILE
    
    # Check for no reply condition (exceeds 200 nmi)
    # Module 2a, slide 33: "The maximum range allowed for use in FARs is 200nm"
    if distance > MAX_RANGE:
        print(f"Channel is {channel}, no reply.")
        return
    
    # Print result with one decimal place as specified
    print(f"Channel is {channel}, distance is {distance:.1f} nm.")

# Test cases from homework
if __name__ == "__main__":
    test_cases = [
        (572, 584, 772, 784),      # Example from prompt: should be X, 12.1 nm
        (1011, 1047, 1361, 1391),   # Test case 2
        (1671, 1683, 2081, 2117),   # Test case 3
        (2307, 2319, 2337, 2349),   # Test case 4
        (5181, 5217, 7767, 7797),   # Test case 5
        (8011, 8047, 8300, 8322)    # Test case 6
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest {i}: DME{test}")
        DME(*test)
```

```text
pseudorange = speed of light × time delay
```

```text
ρᵢ = √[(xᵢ - x)² + (yᵢ - y)² + (zᵢ - z)²] + c·Δt
```

```text
Δφ = (8π·A·Ω)/(λ·c)
```

---



---
*Exported on 2/15/2026, 6:54:30 PM*
