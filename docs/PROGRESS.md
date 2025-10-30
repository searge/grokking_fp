# Learning Progress

Progress log for "Grokking Functional Programming" by Michał Płachta.

## Chapter 1: Introduction to Functional Programming

**Status:** Completed

**Python:** [ch01_intro.py](../src/main/ch01_intro.py)

**Scala:** [Ch01Intro.scala](../src/scala/Ch01Intro.scala)

**Topics Covered:**

- Imperative vs declarative programming styles
- Understanding the difference between telling the computer what to do vs how to do it
- Word scoring example with different approaches

**Coffee Break Exercises:**

- Implemented character filtering in word scoring
- Compared imperative loop-based approach with declarative string operations
- Created reusable function for character removal

## Chapter 2: Pure Functions and Immutability

**Status:** Completed

### Exercise: Shopping Cart Discounts

**Python:** [ch02_shopping_cart_discounts.py](../src/main/ch02_shopping_cart_discounts.py)

**Scala:** Not implemented

**Topics Covered:**

- Problems with mutable state and side effects
- Evolution from stateful to stateless design
- Pure functions and their benefits

**Implementations:**

1. **ShoppingCartBad** - Demonstrates problems with tracking state
   - Uses `book_added` flag that doesn't reflect current cart state
   - Shows issues when items are removed

2. **ShoppingCartRecalculating** - Improved approach
   - Recalculates discount based on current items
   - Better handling of add/remove operations

3. **ShoppingCartStatic** - Static method approach
   - Moves toward functional style
   - Method doesn't depend on instance state

4. **get_discount_percentage** - Pure function
   - Completely stateless
   - Takes input, returns output
   - No side effects

5. **create_discount_calculator** - Higher-order function
   - Returns customized discount calculator functions
   - Demonstrates functional composition
   - Allows flexible discount rules

### Exercise: Tip Calculator

**Python:** [ch02_tip_calculation.py](../src/main/ch02_tip_calculation.py)

**Scala:** Not implemented

**Topics Covered:**

- Comparing imperative and functional approaches
- Static methods as transition to pure functions
- State management in different paradigms

**Implementations:**

1. **TipCalculator** - Imperative approach
   - Maintains mutable state (names list, tip percentage)
   - Updates state through method calls
   - Tip percentage changes based on group size

2. **TipCalculatorStatic** - Functional approach
   - Uses static method with no instance state
   - Pure function: same input always produces same output
   - Group size determines tip percentage (10% or 20%)

## Summary

**Python Progress:**

- Chapter 1: Complete
- Chapter 2: Complete

**Scala Progress:**

- Chapter 1: Complete
- Chapter 2: Not started

**Key Concepts Learned:**

- Pure functions are predictable and testable
- Immutability prevents bugs from unexpected state changes
- Static methods and standalone functions separate data from behavior
- Higher-order functions enable code reuse and composition

**Next Steps:**

- Begin Chapter 3
- Consider implementing Chapter 2 exercises in Scala for language comparison
