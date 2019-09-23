# Fibonacci API
A simple Python Flask application to return individual, sequential values from the Fibonacci sequence using three distinct endpoints. Implemented by [Brady Mathieson](http://github.com/bradymathieson).

## What is the Fibonacci sequence?
The Fibonacci sequence is a sequence of numbers, calculated recursively by adding the last two values in the sequence. Thus,

![alt text](https://latex.codecogs.com/gif.latex?F_{n}%20=%20F_{n-1}%20+%20F_{n-2} "Fibonacci formula")

...with the first two values in the sequence ![alt text](https://latex.codecogs.com/gif.latex?F_0%20=%200 "Base 0") and ![alt text](https://latex.codecogs.com/gif.latex?F_1%20=%201 "Base 1"). With this, the first values of the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, and so on.

More information on this sequence can be found [here](https://www.mathsisfun.com/numbers/fibonacci-sequence.html) and [here](https://www.youtube.com/watch?v=SjSHVDfXHQ4).

## Instructions

1. Clone repository to your local machine.
2. Navigate to the cloned folder and run `python run.py`.

## Available Endpoints
|Route|Function|
|--|--|
|`/current`|Returns the current value in the Fibonacci sequence, along with the current index|
|`/next`|Returns the next value in the Fibonacci sequence, along with the next index, and updates the current value to reflect this increase|
|`/previous`|Returns the previous value in the Fibonacci sequence, along with the previous index, and updates the current value to reflect this decrease|
|`/clear`|Clears the current position in the sequence and cached Fibonacci values|

## Example Session

Initial `\current` response:
```
{
  "index": 0,
  "value": 0
}
```

After calling `\next` 10 times...
```
{
  "index": 10, 
  "value": 55
}
```

...then requesting `previous`...
```
{
  "index": 9, 
  "value": 34
}
```

...and then, finally, calling `\clear`.
```
{
  "index": 0, 
  "value": 0
}
```
