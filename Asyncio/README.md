# 🚗 Process & Thread

Imagine a car: every part of this car, such as the engine, rings, lights, and so on, are Threads 🧵, but the car itself is a Process 🚗. Similarly, a browser is a process, and each tab and different parts of it are threads.

## Synchronous

Sending a request to a server and waiting until the server gives a response. 🕰️

## Asynchronous

Sending a request to a server and doing other things until the server returns a response. 🏃‍♂️

### Types:
- **Concurrent** 🌀
- **Parallel** 🚀

### Different Types of Tasks:
- **I/O Bound**: Input/Output 📥📤
- **CPU Bound**: Processor Intensive 🧠

# Asynchronous in Python

### 🖥️ Multiprocessing
- Multiple Processes, High CPU utilization
- We have ten kitchens, ten chefs, and ten dishes to cook. (CPU Bound) 👨‍🍳👨‍🍳👨‍🍳...👨‍🍳

### 🍜 Threading
- Single Process, Multiple threads, pre-emptive multitasking, OS decides task switching.
- We have one kitchen, ten chefs, and ten dishes to cook; the kitchen is crowded when the ten chefs are present together. (Fast I/O Bound) 👨‍🍳👨‍🍳...👨‍🍳

### 🥣 AsyncIO
- Single Process, Single Thread, Cooperative Multitasking, tasks cooperatively decide switching.
- We have one kitchen, one chef, and ten dishes to cook. (Slow I/O Bound) 👨‍🍳

