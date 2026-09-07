# Go Fundamentals — Days 1–5

## 0. How the concepts connect

A useful order for reviewing the first five days is:

1. Go program structure
2. Variables, constants, and basic types
3. Conditions: `if` and `switch`
4. Arrays and slices
5. Maps
6. Loops and `range`
7. Functions, parameters, return values, and scope
8. Structs and custom types
9. Pointers
10. Methods and receivers

The important connections are:

- Variables store values.
- Types describe what kind of value a variable stores.
- Arrays and slices store multiple values of the same type.
- Maps store values using keys.
- Structs create a custom type that groups related values.
- Functions contain reusable logic.
- Pointers let us work with the original value through its memory address.
- Methods are functions attached to a type.
- Pointer receivers use pointers so a method can modify the original value.

---

# 1. Go Program Structure

A basic Go program starts with a package and usually imports the libraries it needs.

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello")
}
```

`package main` means this file belongs to the `main` package.

`import "fmt"` imports the `fmt` package so we can use functions such as `fmt.Println`.

`func main()` is the entry point of an executable Go program.

---

# 2. Variables and Basic Types

A variable stores a value.

## 2.1 Two common ways to declare a variable

```go
var name string = "Tom"

name := "Tom"
```

The first form uses `var`.

```go
var name string = "Tom"
```

`var` can be used for variables declared at package level or inside functions/blocks.

The second form uses the short variable declaration:

```go
name := "Tom"
```

`:=` can only be used inside functions.

Go can infer the type from the value:

```go
age := 27
name := "Tom"
isStudent := true
```

The equivalent explicit declarations are:

```go
var age int = 27
var name string = "Tom"
var isStudent bool = true
```

### Important distinction

`:=` is not another type of variable. It is a shorter way to declare and initialize a local variable.

---

## 2.2 Printing values with `fmt.Println`

Use the `fmt` package to print values.

```go
fmt.Println("He is", name, ". He is", height, "meters tall and he is", age, "years old. Is he a student?", isStudent, ".")
```

`fmt.Println` accepts multiple arguments and prints them separated by spaces.

A more natural example is:

```go
fmt.Println("Name:", name)
fmt.Println("Age:", age)
```

---

# 3. Conditions

Conditions allow a program to choose different paths.

## 3.1 `if`, `else if`, and `else`

```go
if age >= 18 {
    fmt.Println("He is an adult.")
} else if age >= 13 {
    fmt.Println("He is a teenager.")
} else {
    fmt.Println("He is a child.")
}
```

The logic is:

- If `age >= 18`, execute the first block.
- Otherwise, if `age >= 13`, execute the second block.
- Otherwise, execute the `else` block.

Go does not require parentheses around the condition.

```go
if age >= 18 {
```

not:

```go
if (age >= 18) {
```

---

## 3.2 `switch`

Use `switch` when you want to choose between multiple possible values.

```go
color := "yellow"

switch color {
case "red":
    fmt.Println("The color is red.")
case "blue":
    fmt.Println("The color is blue.")
case "green":
    fmt.Println("The color is green.")
default:
    fmt.Println("The color is not red, blue, or green.")
}
```

Go automatically stops after a matching case, so `break` is normally not needed.

A useful way to remember the difference:

- `if` is useful when checking conditions such as `age >= 18`.
- `switch` is useful when comparing one value against several possible values.

---

# 4. Arrays and Slices

This is an important distinction in Go.

## 4.1 Array

An array has a fixed length.

```go
var numbers [5]int = [5]int{1, 2, 3, 4, 5}
```

The `[5]` means the array always contains exactly 5 elements.

Another example:

```go
names := [3]string{"Tom", "Alex", "David"}
```

The type of this variable is `[3]string`.

The length is part of the array's type.

---

## 4.2 Slice

A slice is a dynamically sized view over an array.

A common way to create a slice is:

```go
var numbers []int = []int{1, 2, 3, 4, 5}
```

or:

```go
numbers := []int{1, 2, 3, 4, 5}
```

The type is `[]int`, which means a slice of `int`.

Example:

```go
weapons := []string{"Sword", "Bow", "Axe"}
```

Unlike an array, a slice can grow.

```go
weapons = append(weapons, "Wand")
```

`append` returns a slice containing the new element, so we normally assign the result back to the variable.

```go
weapons = append(weapons, "Wand")
```

---

## 4.3 `len`

Use `len()` to get the number of elements in an array or slice.

```go
fmt.Println(len(weapons))
```

For an array, the length is fixed.

For a slice, the length can change.

---

## 4.4 Array vs slice

| Array | Slice |
|---|---|
| Fixed length | Can grow or shrink |
| Type includes length, e.g. `[5]int` | Type does not include length, e.g. `[]int` |
| Less commonly used for flexible collections | Commonly used for collections |
| Example: `[5]int{1, 2, 3, 4, 5}` | Example: `[]int{1, 2, 3, 4, 5}` |

### Key memory point

`[5]int` and `[]int` are different types.

---

# 5. Maps

A map stores key-value pairs.

```go
people := map[string]int{
    "Tina": 22,
    "John": 26,
    "Mike": 30,
}
```

Here:

- `string` is the key type.
- `int` is the value type.
- `"Tina"` is a key.
- `22` is the value associated with `"Tina"`.

Each key in a map is unique.

A map does not guarantee a specific iteration order.

---

## 5.1 Access a value

```go
fmt.Println(people["Tina"])
```

Output:

```text
22
```

---

## 5.2 Change a value

```go
people["Tina"] = 23
```

Now:

```go
fmt.Println(people["Tina"])
```

prints:

```text
23
```

---

## 5.3 Add a new key-value pair

```go
people["Sara"] = 28
```

The map now contains Sara as well.

---

## 5.4 Delete a key-value pair

Use `delete()`:

```go
delete(people, "Mike")
```

This removes the key `"Mike"` and its associated value.

---

# 6. Loops and `range`

Go has one main looping keyword: `for`.

## 6.1 Traditional `for` loop

```go
for i := 0; i < 5; i++ {
    fmt.Println(numbers[i])
}
```

The three parts are:

```text
initialization; condition; post statement
```

In this example:

```go
i := 0
```

starts the counter.

```go
i < 5
```

is the condition.

```go
i++
```

increases the counter after each iteration.

---

## 6.2 `range`

`range` is useful when iterating over arrays, slices, and maps.

For a slice:

```go
for index, value := range numbers {
    fmt.Println(index, value)
}
```

For each iteration, `range` provides the index and the value.

If the index is not needed, use `_`:

```go
for _, value := range numbers {
    fmt.Println(value)
}
```

The `_` is called the blank identifier. It means that we intentionally ignore that returned value.

---

## 6.3 `range` with maps

For a map:

```go
for name, age := range people {
    fmt.Println(name, age)
}
```

Here `range` provides:

```text
key -> name
value -> age
```

The order is not guaranteed because maps are unordered collections.

### Important distinction

For arrays and slices:

```go
for index, value := range numbers
```

For maps:

```go
for key, value := range people
```

The first returned value is the index for arrays/slices and the key for maps.

---

# 7. Functions

A function is a reusable block of code.

## 7.1 Define and call a function

Define:

```go
func sayHello() {
    fmt.Println("Hello")
}
```

Call:

```go
sayHello()
```

The basic structure is:

```go
func functionName() {
    ...
}
```

---

## 7.2 Function parameters

A function can receive values through parameters.

```go
func printName(name string) {
    fmt.Println(name)
}
```

Call it with:

```go
printName("Alex")
```

Here:

```text
name
```

is the parameter.

```text
"Alex"
```

is the argument passed to the function.

---

## 7.3 Return values

A function can return a value.

```go
func add(a int, b int) int {
    return a + b
}
```

The final `int` before `{` is the return type.

Call the function and store the returned value:

```go
result := add(3, 5)
```

Now `result` contains `8`.

---

## 7.4 Multiple return values

A Go function can return multiple values.

```go
func getNumbers(a int, b int) (int, int) {
    return a, b
}
```

Receive them with multiple variables:

```go
result1, result2 := getNumbers(1, 2)
```

The order matters.

The first returned value goes into `result1`.

The second returned value goes into `result2`.

This feature is especially important later because Go commonly returns a value together with an error:

```go
value, err := someFunction()
```

---

# 8. Scope

Scope determines where a variable can be used.

A variable declared inside a function is local to that function.

```go
func main() {
    age := 27
    fmt.Println(age)
}
```

`age` cannot be used outside `main`.

Variables declared inside an `if`, `for`, or another inner block are also limited to that block.

```go
if age >= 18 {
    message := "Adult"
    fmt.Println(message)
}
```

`message` cannot be used after the `if` block.

A variable declared at package level can be used by functions in the same package, subject to Go's normal visibility rules.

---

# 9. Structs

A struct is a custom type that groups related data together.

## 9.1 Define a struct

```go
type Person struct {
    name    string
    age     int
    isAlive bool
}
```

Here:

```text
Person
```

is the struct type.

The variables inside the struct are called fields.

Each field has:

- a name
- a type

For example:

```text
name -> string
age -> int
isAlive -> bool
```

---

## 9.2 Create a struct

A struct can be created using positional values:

```go
person := Person{"Alex", 27, false}
```

It can also be created using field names:

```go
person := Person{
    name:    "Alex",
    age:     27,
    isAlive: false,
}
```

Using field names is usually easier to read and safer when a struct has several fields.

---

## 9.3 Access a field

Use `.`:

```go
fmt.Println(person.name)
fmt.Println(person.age)
```

---

## 9.4 Modify a field

Assign a new value:

```go
person.age = 28
```

The original struct is now changed.

---

## 9.5 Structs with slices

A slice can contain multiple structs of the same type:

```go
people := []Person{
    {name: "Alex", age: 27, isAlive: false},
    {name: "Tina", age: 22, isAlive: true},
}
```

This is useful when we need a collection of structured objects.

---

## 9.6 Structs with maps

A map can use a struct as its value type:

```go
people := map[string]Person{
    "Person1": {
        name:    "Alex",
        age:     27,
        isAlive: false,
    },
    "Person2": {
        name:    "Tina",
        age:     22,
        isAlive: true,
    },
}
```

Access the map value and then the struct field:

```go
fmt.Println(people["Person2"].age)
```

---

# 10. Pointers

A pointer stores the memory address of another variable.

## 10.1 Get an address with `&`

```go
age := 27

p := &age
```

Here:

```text
age -> stores the value 27
p   -> stores the address of age
```

So `p` is a pointer to `age`.

---

## 10.2 Get the value through a pointer with `*`

```go
fmt.Println(*p)
```

`*p` means:

> Go to the address stored in `p` and get the value there.

So if `age` is `27`:

```go
fmt.Println(*p)
```

prints:

```text
27
```

---

## 10.3 Change the original value through a pointer

```go
*p = 30
```

Now `age` is also `30`.

```go
fmt.Println(age)
```

prints:

```text
30
```

The important idea is:

```text
&age -> get the address of age
p    -> stores that address
*p   -> access the value at that address
```

---

# 11. Methods

A method is a function associated with a specific type.

A method has a receiver.

## 11.1 Basic method syntax

```go
func (receiverName receiverType) methodName() {
    ...
}
```

Example:

```go
type Person struct {
    name string
    age  int
}

func (p Person) introduce() {
    fmt.Println("My name is", p.name)
}
```

The receiver is:

```go
p Person
```

It connects the `introduce` method to the `Person` type.

Call the method with `.`:

```go
person.introduce()
```

---

# 12. Value Receivers and Pointer Receivers

This is one of the most important connections between structs and pointers.

## 12.1 Value receiver

```go
func (p Person) haveBirthday() {
    p.age++
}
```

`p` is a copy of the original `Person`.

Therefore, changing `p.age` changes only the copy.

The original struct is not changed.

Think:

```text
original Person
      ↓ copy
receiver p
      ↓
method changes the copy
```

---

## 12.2 Pointer receiver

```go
func (p *Person) haveBirthday() {
    p.age++
}
```

Here `p` is a pointer to the original `Person`.

Therefore, changing `p.age` changes the original struct.

Think:

```text
original Person
      ↑
pointer p
      ↓
method changes the original value
```

Example:

```go
person := Person{
    name: "Alex",
    age: 27,
}

person.haveBirthday()
```

With a pointer receiver, `person.age` becomes `28`.

---

## 12.3 Main difference

```text
Value receiver
    -> receives a copy
    -> changes affect the copy

Pointer receiver
    -> receives a pointer to the original value
    -> changes can affect the original value
```

This is why pointer receivers are useful when a method needs to modify a struct.
