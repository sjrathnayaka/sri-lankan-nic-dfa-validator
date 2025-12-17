"""
Deterministic Finite Automaton (DFA) for Sri Lankan NIC Validation
================================================================

This program implements a DFA to validate Sri Lankan National Identity Card numbers.

Automata Theory Concepts:
- Alphabet (Σ): {0,1,2,3,4,5,6,7,8,9,V,X}
- States: q0 (start), q1-q9 (digit counting), q10 (old NIC final), 
          q11-q12 (new NIC continuation), q13 (new NIC final), qReject (dead state)
- Accepting States: q10 (old NIC), q13 (new NIC)

Author: Automata Theory Assignment
Date: December 2025
"""

def nic_dfa_validator(nic: str) -> str:
    """
    Validates Sri Lankan NIC numbers using DFA implementation.
    
    Args:
        nic (str): The NIC string to validate
        
    Returns:
        str: "ACCEPT – Old NIC", "ACCEPT – New NIC", or "REJECT"
        
    DFA States:
    - q0: Initial state
    - q1-q9: Counting first 9 digits (for old NIC format)
    - q10: Old NIC accepting state (after 9 digits + V/X)
    - q11-q12: Continuing digit count for new NIC (10th, 11th, 12th digits)
    - q13: New NIC accepting state (after 12 digits)
    - qReject: Dead/reject state
    """
    
    # Initialize DFA state
    current_state = "q0"
    
    # Process each character in the input string
    for char in nic:
        # State transition logic using if-elif statements (no regex, no length checks)
        if current_state == "q0":
            # Start state - expecting first digit
            if char.isdigit():
                current_state = "q1"
            else:
                current_state = "qReject"
                
        elif current_state == "q1":
            # After 1st digit - expecting 2nd digit
            if char.isdigit():
                current_state = "q2"
            else:
                current_state = "qReject"
                
        elif current_state == "q2":
            # After 2nd digit - expecting 3rd digit
            if char.isdigit():
                current_state = "q3"
            else:
                current_state = "qReject"
                
        elif current_state == "q3":
            # After 3rd digit - expecting 4th digit
            if char.isdigit():
                current_state = "q4"
            else:
                current_state = "qReject"
                
        elif current_state == "q4":
            # After 4th digit - expecting 5th digit
            if char.isdigit():
                current_state = "q5"
            else:
                current_state = "qReject"
                
        elif current_state == "q5":
            # After 5th digit - expecting 6th digit
            if char.isdigit():
                current_state = "q6"
            else:
                current_state = "qReject"
                
        elif current_state == "q6":
            # After 6th digit - expecting 7th digit
            if char.isdigit():
                current_state = "q7"
            else:
                current_state = "qReject"
                
        elif current_state == "q7":
            # After 7th digit - expecting 8th digit
            if char.isdigit():
                current_state = "q8"
            else:
                current_state = "qReject"
                
        elif current_state == "q8":
            # After 8th digit - expecting 9th digit
            if char.isdigit():
                current_state = "q9"
            else:
                current_state = "qReject"
                
        elif current_state == "q9":
            # After 9th digit - CRITICAL BRANCHING POINT
            # Can be V/X (old NIC path) or digit (new NIC path)
            if char in ['V', 'X']:
                current_state = "q10"  # Old NIC path - accepting state
            elif char.isdigit():
                current_state = "q11"  # New NIC path (10th digit)
            else:
                current_state = "qReject"
                
        elif current_state == "q10":
            # Old NIC completed (9 digits + V/X) - any additional character is invalid
            current_state = "qReject"
            
        elif current_state == "q11":
            # After 10th digit in new NIC - expecting 11th digit
            if char.isdigit():
                current_state = "q12"
            else:
                current_state = "qReject"
                
        elif current_state == "q12":
            # After 11th digit in new NIC - expecting 12th digit
            if char.isdigit():
                current_state = "q13"  # New NIC accepting state
            else:
                current_state = "qReject"
                
        elif current_state == "q13":
            # New NIC completed (12 digits) - any additional character is invalid
            current_state = "qReject"
            
        else:  # current_state == "qReject"
            # Dead state - once in reject, always reject
            current_state = "qReject"
    
    # Determine final result based on final state (accepting vs rejecting)
    if current_state == "q10":
        return "ACCEPT – Old NIC"
    elif current_state == "q13":
        return "ACCEPT – New NIC"
    else:
        return "REJECT"


def demonstrate_dfa_step_by_step(nic: str):
    """
    Demonstrates the DFA state transitions step by step for educational purposes.
    Shows how the automaton processes each character.
    """
    print(f"\nStep-by-step DFA execution for input: '{nic}'")
    print("-" * 50)
    
    current_state = "q0"
    print(f"Initial state: {current_state}")
    
    for i, char in enumerate(nic):
        old_state = current_state
        
        # Apply the same transition logic as in the main function
        if current_state == "q0":
            if char.isdigit():
                current_state = "q1"
            else:
                current_state = "qReject"
        elif current_state in ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]:
            if char.isdigit():
                state_num = int(current_state[1:])
                current_state = f"q{state_num + 1}"
            else:
                current_state = "qReject"
        elif current_state == "q9":
            if char in ['V', 'X']:
                current_state = "q10"
            elif char.isdigit():
                current_state = "q11"
            else:
                current_state = "qReject"
        elif current_state == "q10":
            current_state = "qReject"
        elif current_state == "q11":
            if char.isdigit():
                current_state = "q12"
            else:
                current_state = "qReject"
        elif current_state == "q12":
            if char.isdigit():
                current_state = "q13"
            else:
                current_state = "qReject"
        elif current_state == "q13":
            current_state = "qReject"
        else:
            current_state = "qReject"
            
        print(f"Character '{char}': {old_state} → {current_state}")
    
    # Final result
    result = nic_dfa_validator(nic)
    print(f"Final result: {result}")
    return result


def run_comprehensive_tests():
    """
    Run comprehensive test cases to validate the DFA implementation.
    """
    print("=" * 70)
    print("Sri Lankan NIC Validation using Deterministic Finite Automaton")
    print("=" * 70)
    
    # Comprehensive test cases
    test_cases = [
        # Valid Old NIC format (9 digits + V/X)
        ("991234567V", "ACCEPT – Old NIC", "Valid old format"),
        ("123456789X", "ACCEPT – Old NIC", "Valid old format with X"),
        ("987654321V", "ACCEPT – Old NIC", "Valid old format"),
        ("000000000V", "ACCEPT – Old NIC", "Valid old format with zeros"),
        
        # Valid New NIC format (12 digits)
        ("200012345678", "ACCEPT – New NIC", "Valid new format"),
        ("199812345678", "ACCEPT – New NIC", "Valid new format"),
        ("200512345678", "ACCEPT – New NIC", "Valid new format"),
        ("000000000000", "ACCEPT – New NIC", "Valid new format with zeros"),
        
        # Invalid cases
        ("99123X4567", "REJECT", "X in wrong position (should be at end)"),
        ("991234567", "REJECT", "Missing V/X terminator"),
        ("991234567VV", "REJECT", "Extra character after V"),
        ("2000123456789", "REJECT", "13 digits (too long for new format)"),
        ("20001234567", "REJECT", "11 digits (too short for new format)"),
        ("99123456V", "REJECT", "Only 8 digits before V"),
        ("A91234567V", "REJECT", "Letter in digit position"),
        ("9912345678", "REJECT", "10 digits (ambiguous length)"),
        ("", "REJECT", "Empty string"),
        ("ABCDEFGHIJ", "REJECT", "All letters"),
        ("991234567Y", "REJECT", "Invalid letter Y (not V or X)"),
        ("99 1234567V", "REJECT", "Contains space"),
        ("991-234-567V", "REJECT", "Contains hyphens"),
        ("99123456V7", "REJECT", "Digit after V"),
    ]
    
    print("\nTest Results:")
    print("-" * 70)
    print(f"{'#':<3} {'Input':<16} {'Expected':<20} {'Result':<20} {'Status'}")
    print("-" * 70)
    
    passed = 0
    total = len(test_cases)
    
    for i, (test_input, expected, description) in enumerate(test_cases, 1):
        result = nic_dfa_validator(test_input)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
            
        print(f"{i:<3} {test_input:<16} {expected:<20} {result:<20} {status}")
        
        # Show description for failed tests
        if result != expected:
            print(f"    Description: {description}")
    
    print("-" * 70)
    print(f"Test Summary: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("🎉 All tests PASSED! The DFA implementation is correct.")
    else:
        print("❌ Some tests FAILED. Please review the implementation.")
    
    return passed == total


def interactive_demo():
    """
    Interactive demonstration of the DFA.
    """
    print("\n" + "=" * 50)
    print("Interactive DFA Demonstration")
    print("=" * 50)
    
    # Demo with specific examples
    demo_inputs = ["991234567V", "200012345678", "99123X4567"]
    
    for demo_input in demo_inputs:
        demonstrate_dfa_step_by_step(demo_input)
        print()


def interactive_input():
    """
    Interactive input function to test your own NIC numbers.
    """
    print("\n" + "=" * 50)
    print("🔧 Interactive NIC Testing")
    print("=" * 50)
    print("Enter NIC numbers to test (or 'quit' to exit)")
    print("Formats: Old NIC (9 digits + V/X) | New NIC (12 digits)")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nEnter NIC: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("✅ Testing Complete!")
                break
                
            if user_input == "":
                print("Please enter a valid NIC number.")
                continue
                
            # Show step-by-step DFA execution
            demonstrate_dfa_step_by_step(user_input)
            
            # Show final ACCEPT/REJECT outcome
            result = nic_dfa_validator(user_input)
            print(f"\n🔹 Final Outcome: {result}")
            print("-" * 30)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Testing terminated by user (Ctrl+C)")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """
    Main function with menu options.
    """
    print("Sri Lankan NIC DFA Validator")
    print("=" * 40)
    print("Choose an option:")
    print("1. Run comprehensive tests")
    print("2. Test your own NIC numbers")
    print("3. Run both")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == "1":
        run_comprehensive_tests()
        interactive_demo()
    elif choice == "2":
        interactive_input()
    elif choice == "3":
        run_comprehensive_tests()
        interactive_demo()
        interactive_input()
    else:
        print("Invalid choice. Running comprehensive tests...")
        run_comprehensive_tests()
        interactive_demo()
    
    print("\n" + "=" * 50)
    print("DFA Theory Summary")
    print("=" * 50)
    print("Alphabet (Σ): {0,1,2,3,4,5,6,7,8,9,V,X}")
    print("States: q0, q1, q2, ..., q13, qReject")
    print("Start State: q0")
    print("Accepting States: q10 (Old NIC), q13 (New NIC)")
    print("Transition Function: Implemented via if-elif statements")
    print("Dead State: qReject (ensures DFA property)")
    print("\nThe DFA successfully validates both old and new Sri Lankan NIC formats!")


if __name__ == "__main__":
    main()
