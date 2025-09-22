// Comparison Operators
console.log(x == y);   // true  (loose equality → value only)
console.log(x === y);  // false (strict equality → value + type)
console.log(x != y);   // false (loose inequality)
console.log(x !== y);  // true  (strict inequality)
console.log(x > 3);    // true
console.log(x < 3);    // false
console.log(x >= 5);   // true
console.log(x <= 4);   // false

// Arithmetic Operators
console.log(a + b);  // 13
console.log(a - b);  // 7
console.log(a * b);  // 30
console.log(a / b);  // 3.333...
console.log(a % b);  // 1
console.log(a ** b); // 1000 (Exponentiation)
console.log(a++);    // 10 (post-increment → then a=11)
console.log(b--);    // 3 (post-decrement → then b=2)

// Logical Operators
console.log(a && b); // false (AND)
console.log(a || b); // true  (OR)
console.log(!a);     // false (NOT)


// Assignment Operators
n += 5;  // n = 15
n -= 3;  // n = 12
n *= 2;  // n = 24
n /= 4;  // n = 6
n %= 5;  // n = 1
n **= 3; // n = 1 (1^3)

// Ternary Operator (shorthand for if/else)
let age = 18;
let result = (age >= 18) ? "Adult" : "Minor";
console.log(result); // Result will come Adult ...
