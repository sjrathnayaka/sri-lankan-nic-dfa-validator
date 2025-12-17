"""
DFA State Diagram Representation for Sri Lankan NIC Validation
============================================================

This file provides a textual representation of the DFA state diagram
and additional documentation for the automaton theory assignment.

DFA FORMAL DEFINITION:
=====================


M = (Q, Σ, δ, q0, F) where:

Q (States):
- q0: Initial/Start state
- q1: After 1st digit
- q2: After 2nd digit  
- q3: After 3rd digit
- q4: After 4th digit
- q5: After 5th digit
- q6: After 6th digit
- q7: After 7th digit
- q8: After 8th digit
- q9: After 9th digit (CRITICAL BRANCHING STATE)
- q10: Old NIC final state (9 digits + V/X) - ACCEPTING
- q11: After 10th digit (New NIC path)
- q12: After 11th digit (New NIC path)
- q13: New NIC final state (12 digits) - ACCEPTING
- qReject: Dead/Reject state

Σ (Alphabet):
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, V, X}

δ (Transition Function):
State transitions implemented via if-elif statements in the main program.

q0 (Start State):
The initial state of the automaton.

F (Final/Accepting States):
{q10, q13}
- q10: Accepts old NIC format (9 digits + V/X)
- q13: Accepts new NIC format (12 digits)

TEXT-BASED STATE DIAGRAM:
========================

         [0-9]     [0-9]     [0-9]     [0-9]     [0-9]
    q0 --------> q1 -----> q2 -----> q3 -----> q4 ------>
     │            │        │         │         │
     │ [^0-9]     │[^0-9]  │[^0-9]   │[^0-9]   │[^0-9]
     ↓            ↓        ↓         ↓         ↓
  qReject    qReject   qReject   qReject   qReject
                                              
         [0-9]     [0-9]     [0-9]     [0-9]      
    q5 -----> q6 -----> q7 -----> q8 -----> q9
     │        │         │         │        │ │
     │[^0-9]  │[^0-9]   │[^0-9]   │[^0-9]  │ │
     ↓        ↓         ↓         ↓        │ │
  qReject qReject   qReject   qReject      │ │
                                          │ │
                                    [V,X] │ │ [0-9]
                                          ↓ ↓
                                        q10 q11
                                         │   │
                                    ((ACCEPT)) │ [0-9]
                                      OLD NIC  ↓
                                             q12
                                              │
                                              │ [0-9]
                                              ↓
                                             q13
                                              │
                                         ((ACCEPT))
                                          NEW NIC

CRITICAL DESIGN DECISIONS:
========================

1. State q9 is the BRANCHING POINT:
   - If next character is V or X → transition to q10 (Old NIC path)
   - If next character is digit → transition to q11 (New NIC path)
   - Any other character → transition to qReject

2. Dead State (qReject):
   - Once the automaton enters qReject, it stays there
   - Ensures the DFA property (exactly one transition per state-symbol pair)
   - Any invalid character or extra characters lead here

3. No Length Checking:
   - The automaton doesn't explicitly check string length
   - Length validation is implicit through state transitions
   - This satisfies the "no length checks" requirement

4. No Regular Expressions:
   - All pattern matching done through explicit state transitions
   - Character validation using char.isdigit() and direct comparison

COMPLEXITY ANALYSIS:
==================

Time Complexity: O(n) where n is the length of input string
- Each character is processed exactly once
- Each state transition is O(1)

Space Complexity: O(1)
- Only stores current state (constant space)
- No additional data structures needed

AUTOMATA THEORY CONCEPTS DEMONSTRATED:
====================================

1. Deterministic Finite Automaton (DFA):
   - Exactly one transition per (state, input) pair
   - No epsilon transitions
   - Deterministic behavior

2. State Machine Design:
   - Clear state separation
   - Well-defined transitions
   - Dead state for error handling

3. Formal Language Recognition:
   - Recognizes the language L = {Old_NIC ∪ New_NIC}
   - Old_NIC = {d₁d₂...d₉(V|X) | dᵢ ∈ {0-9}}
   - New_NIC = {d₁d₂...d₁₂ | dᵢ ∈ {0-9}}

4. Accepting vs Rejecting States:
   - Clear distinction between accept and reject
   - Multiple accepting states for different formats

EXAMPLE EXECUTIONS:
==================

Example 1: "991234567V" (Old NIC)
q0 →[9] q1 →[9] q2 →[1] q3 →[2] q4 →[3] q5 →[4] q6 →[5] q7 →[6] q8 →[7] q9 →[V] q10
Result: ACCEPT – Old NIC

Example 2: "200012345678" (New NIC)  
q0 →[2] q1 →[0] q2 →[0] q3 →[0] q4 →[1] q5 →[2] q6 →[3] q7 →[4] q8 →[5] q9 →[6] q11 →[7] q12 →[8] q13
Result: ACCEPT – New NIC

Example 3: "99123X4567" (Invalid)
q0 →[9] q1 →[9] q2 →[1] q3 →[2] q4 →[3] q5 →[X] qReject →[4] qReject →[5] qReject →[6] qReject →[7] qReject
Result: REJECT
"""

# Python Implementation with Step-by-Step DFA Execution

def run_dfa_implementation():
    """
    Python Implementation: Implement the automaton fully with step-by-step execution.
    Shows ACCEPT/REJECT outcomes with detailed state transitions.
    """
    # Import the validator function
    import sys
    sys.path.append('.')
    from sri_lankan_nic_dfa import nic_dfa_validator, demonstrate_dfa_step_by_step
    
    print("=" * 60)
    print("3. Python Implementation - DFA Automaton with Step-by-Step Execution")
    print("=" * 60)
    print("Enter NIC numbers to test (or 'quit' to exit)")
    print("Format: Old NIC (9 digits + V/X) | New NIC (12 digits)")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\nEnter NIC: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n🎯 DFA Implementation Complete!")
                break
                
            if user_input == "":
                print("Please enter a valid NIC number.")
                continue
                
            print("\n" + "="*50)
            print(f"Processing Input: '{user_input}'")
            print("="*50)
            
            # Show step-by-step DFA execution
            demonstrate_dfa_step_by_step(user_input)
            
            # Show final ACCEPT/REJECT outcome
            result = nic_dfa_validator(user_input)
            print(f"\n🔹 Final Outcome: {result}")
            print("-" * 50)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Program terminated by user (Ctrl+C)")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_dfa_implementation()
