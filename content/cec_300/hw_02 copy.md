## Problem 1: DME Pulse Simulation in Python

```python
def DME(pulse1, pulse2, pulse3, pulse4):
    """
    Simulate DME pulse analysis
    
    Parameters:
    pulse1, pulse2: transmitted pulses from aircraft to DME station
    pulse3, pulse4: response pulses received by aircraft
    """
    
    # Calculate pulse pair spacings
    tx_spacing = pulse2 - pulse1
    rx_spacing = pulse4 - pulse3
    
    # Calculate time between first pulses (round trip time)
    round_trip_time = pulse3 - pulse1
    
    # Channel definitions
    X_SPACING = 12  # microseconds
    Y_SPACING = 30  # microseconds
    X_DELAY = 50    # microseconds
    Y_DELAY = 56    # microseconds
    CONVERSION_FACTOR = 12.36  # microseconds per nautical mile
    
    # Check for garbled signals (invalid pulse spacings)
    valid_x_spacing = (tx_spacing == X_SPACING and rx_spacing == X_SPACING)
    valid_y_spacing = (tx_spacing == Y_SPACING and rx_spacing == Y_SPACING)
    
    if not (valid_x_spacing or valid_y_spacing):
        print("Signal Garbled.")
        return
    
    # Check for FRUIT (mismatched channels)
    if (tx_spacing == X_SPACING and rx_spacing == Y_SPACING) or \
       (tx_spacing == Y_SPACING and rx_spacing == X_SPACING):
        print("FRUIT detected.")
        return
    
    # Determine channel
    if valid_x_spacing:
        channel = "X"
        ground_delay = X_DELAY
    else:  # valid_y_spacing
        channel = "Y"
        ground_delay = Y_DELAY
    
    # Check if received signals arrive in less than built-in delay
    if round_trip_time < ground_delay:
        print("Signal Garbled.")
        return
    
    # Calculate distance
    propagation_time = round_trip_time - ground_delay
    distance_nm = propagation_time / CONVERSION_FACTOR
    
    # Check for no reply condition (exceeding 200 nmi)
    if distance_nm > 200:
        print(f"Channel is {channel}, no reply.")
        return
    
    # Print result
    print(f"Channel is {channel}, distance is {distance_nm:.2f} nm.")


# Test cases
if __name__ == "__main__":
    print("Testing DME function with provided examples:")
    print("-" * 50)
    
    test_cases = [
        (572, 584, 772, 784),      # Should be Channel X
        (1011, 1047, 1361, 1391),  # Should be Channel Y (30µs spacing)
        (1671, 1683, 2081, 2117),  # Mixed spacing? (12 and 36)
        (2307, 2319, 2337, 2349),  # Very short round trip
        (5181, 5217, 7767, 7797),  # Long range
        (8011, 8047, 8300, 8322)   # Another test
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: DME{test}")
        DME(*test)
        print()
    
    # Additional test cases for edge conditions
    print("Additional edge case tests:")
    print("-" * 50)
    
    # Test FRUIT detection
    print("FRUIT test (X transmit, Y receive):")
    DME(572, 584, 772, 802)  # 12µs transmit, 30µs receive
    
    # Test no reply condition (>200 nmi)
    print("\nNo reply test (>200 nmi):")
    DME(572, 584, 3072, 3084)  # ~2500µs round trip = ~200 nmi
    
    # Test garbled signal
    print("\nGarbled signal test (invalid spacing):")
    DME(572, 585, 772, 784)  # 13µs transmit spacing
    
    # Test signal arriving before ground delay
    print("\nGarbled signal test (arrives before ground delay):")
    DME(572, 584, 590, 602)  # 18µs round trip (<50µs)
```

## Problem 2: VOR Indicator

a. 220° radial

b. Right turn needed

c. Approximately 7° heading change to the right (determined by the 3.5 dots of deflection at 2° per dot)

## Problem 3: ILS Questions

a. Aircraft left/right of runway centerline before landing:

If the aircraft is left of the runway centerline:

- The localizer signal would indicate the aircraft is to the left
- The CDI would show deflection to the right
- The aircraft would need to turn right to intercept the centerline

If the aircraft is right of the runway centerline:

- The localizer signal would indicate the aircraft is to the right
- The CDI would show deflection to the left
- The aircraft would need to turn left to intercept the centerline

b. ILS category for transport jet with 950 feet visibility:

A transport category jet with 950 feet runway visibility would be operating under CAT II minimums.

## Problem 4: GPS Essay

GPS determines your location using trilateration, which relies on timing signals from multiple satellites. Each satellite continuously broadcasts its exact position and the precise time the signal was sent. A GPS receiver measures how long each signal took to arrive and multiplies that travel time by the speed of light to calculate its distance from the satellite.

Each distance measurement forms a sphere around a satellite, and the receiver’s position is the point where those spheres intersect. Signals from three satellites can determine latitude and longitude, but a fourth satellite is needed to correct small clock errors in the receiver and calculate altitude. By solving four equations simultaneously, the receiver determines its x, y, z position and corrects its internal clock offset. 

GPS accuracy can be affected by atmospheric delays in the ionosphere and troposphere, small satellite clock or orbital errors, and signal reflections from buildings or terrain (multipath). Accuracy also depends on satellite geometry. Widely spaced satellites provide better precision than clustered ones. Modern systems reduce these errors using correction methods such as Differential GPS (DGPS) and the Wide Area Augmentation System (WAAS), often achieving accuracy within about a meter.

## Problem 5: Satellite Sensors and Actuators

a. Reaction Wheels vs. Magnetorquers

Reaction wheels are internal flywheels that spin to create torque; by conservation of angular momentum, the spacecraft rotates in the opposite direction. They provide highly precise, continuous control and are ideal for fine pointing tasks such as aiming cameras or antennas. However, they can “saturate” when they reach maximum speed, require periodic desaturation, consume moderate power, and contain moving parts that can wear out over time.

Magnetorquers, in contrast, use electromagnets to interact with Earth’s magnetic field and generate torque. They have no moving parts, making them lightweight and highly reliable, and they consume relatively little power. Their main limitations are lower torque output and reduced precision. They also only function effectively in the presence of a planetary magnetic field, such as in low Earth orbit.

Together, these systems create a balanced attitude control strategy. Reaction wheels handle precise pointing and smooth control, while magnetorquers provide coarse adjustments and, importantly, desaturate the reaction wheels by bleeding off stored angular momentum. This combination improves both pointing accuracy and long-term system reliability, allowing spacecraft to maintain precision without overloading mechanical components.


b. Fiber-Optic Gyroscopes and the Sagnac Effect

Fiber-optic gyroscopes (FOGs) measure angular rate using the Sagnac effect. A laser beam is split and sent in opposite directions through a coil of optical fiber. When the gyroscope rotates, the beam traveling in the direction of rotation takes slightly longer to complete the path than the beam traveling opposite to rotation. This creates a phase difference between the two beams when they recombine. By measuring this phase difference, the system can determine the angular rotation rate about the axis perpendicular to the coil. The Sagnac effect is purely relativistic, occurring because light travels at a constant speed regardless of the observer's motion.

c. Deep Space Network (DSN) Role

The DSN's global network of large antennas ensures continuous coverage as Earth rotates, critical for spacecraft operating at extreme distances where signal strength is minimal.