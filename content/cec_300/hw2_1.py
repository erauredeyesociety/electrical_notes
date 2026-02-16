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
