# Cache System

## Description

This project implements a versatile **Cache System** that supports multiple eviction strategies, including:

- **LRU (Least Recently Used) Eviction**
- **LFU (Least Frequently Used) Eviction**
- **TTL (Time-to-Live) Eviction**
- **Non-Eviction**


## UML Diagram
The system's architecture is represented in the UML diagram below:
![UML](static/uml.svg)


## Examples Ran From Simulation
****The logs are stored on [logs](logs/) file****

***LRU (Least Recently Used) Eviction***
```plaintext
Cache Capacity:4

Inserting: key 1 with value: 117
Inserting: key 2 with value: 127
Inserting: key 3 with value: 137
Fetching value from cache with key 1: 117

Item in Cache:
***************
1->117
2->127
3->137
***************

Inserting: key 2 with value: 122

Item in Cache:
***************
1->117
2->122
3->137
***************

Inserting: key 7 with value: 177

Item in Cache:
***************
1->117
2->122
3->137
7->177
***************

Inserting: key 4 with value: 148

Item in Cache:
***************
1->117
2->122
7->177
4->148
***************

Fetching value from cache with key 4: 148

Item in Cache:
***************
1->117
2->122
7->177
4->148
***************

Fetching value from cache with key 1: 117

Item in Cache:
***************
1->117
2->122
7->177
4->148
***************

Inserting: key 10 with value: 1107
Fetching value from cache with key 10: 1107

Item in Cache:
***************
1->117
7->177
4->148
10->1107
***************

Inserting: key 11 with value: 1117

Item in Cache:
***************
1->117
4->148
10->1107
11->1117
***************
```

**LFU (Least Frequently Used) Eviction**
```plaintext
Cache Capacity:4

Inserting: key 1 with value: 117
Inserting: key 2 with value: 127
Inserting: key 3 with value: 137
Fetching value from cache with key 1: 117

Item in Cache:
***************
freq-1:[(2, 127), (3, 137)]
freq-2:[(1, 117)]
***************

Inserting: key 2 with value: 122

Item in Cache:
***************
freq-1:[(3, 137)]
freq-2:[(1, 117), (2, 122)]
***************

Inserting: key 7 with value: 177

Item in Cache:
***************
freq-1:[(3, 137), (7, 177)]
freq-2:[(1, 117), (2, 122)]
***************

Inserting: key 4 with value: 148

Item in Cache:
***************
freq-1:[(3, 137), (4, 148)]
freq-2:[(1, 117), (2, 122)]
***************

Fetching value from cache with key 4: 148

Item in Cache:
***************
freq-1:[(3, 137)]
freq-2:[(1, 117), (2, 122), (4, 148)]
***************

Fetching value from cache with key 1: 117
Fetching value from cache with key 2: 122
Fetching value from cache with key 4: 148

Item in Cache:
***************
freq-1:[(3, 137)]
freq-3:[(1, 117), (2, 122), (4, 148)]
***************

Inserting: key 10 with value: 1107
Fetching value from cache with key 10: 1107

Item in Cache:
***************
freq-3:[(1, 117), (2, 122), (4, 148)]
freq-2:[(10, 1107)]
***************

Inserting: key 11 with value: 1117

Item in Cache:
***************
freq-3:[(1, 117), (2, 122), (4, 148)]
freq-1:[(11, 1117)]
***************
```

**TTL (Time-to-Live) Eviction**
```plaintext
Cache Capacity:4 and ttl: 2

Inserting: key 1 with value: 101
Inserting: key 2 with value: 201
Inserting: key 3 with value: 301
Inserting: key 4 with value: 400

Items in Cache:
***************
1->101, Exp:1.999844
2->201, Exp:1.999515
3->301, Exp:1.999545
4->400, Exp:1.999573
***************


After 1 second

Fetching value from cache with key 2: 201

Items in Cache:
***************
1->101, Exp:-1.007617
2->201, Exp:1.99815
3->301, Exp:-1.007566
4->400, Exp:-1.007548
***************


After 3 second

Inserting: key 5 with value: 500

Items in Cache:
***************
5->500, Exp:1.999948
***************


After 1 second

Inserting: key 6 with value: 600

Items in Cache:
***************
5->500, Exp:0.994295
6->600, Exp:1.999895
***************


After 1 second

Inserting: key 7 with value: 700

Items in Cache:
***************
6->600, Exp:0.996137
7->700, Exp:1.999938
***************


After 1 second

Inserting: key 8 with value: 800

Items in Cache:
***************
7->700, Exp:0.993956
8->800, Exp:1.999871
***************


After 1 second


Items in Cache:
***************
7->700, Exp:-0.00722
8->800, Exp:0.998698
***************


After 1 second

Inserting: key 1 with value: 10

Items in Cache:
***************
1->10, Exp:1.999948
***************

Inserting: key 11 with value: 10
Inserting: key 12 with value: 10

Items in Cache:
***************
1->10, Exp:1.999736
11->10, Exp:1.999904
12->10, Exp:1.999963
***************

Inserting: key 13 with value: 10
Inserting: key 14 with value: 10


**************************************************

		Cache is Full ATM
```

**Non-Eviction**
```
Cache Capacity:4

Inserting: key 1 with value: 117
Inserting: key 2 with value: 127
Inserting: key 3 with value: 137
Fetching value from cache with key 1: 117

Item in Cache:
***************
1->117
2->127
3->137
***************

Inserting: key 2 with value: 122

Item in Cache:
***************
1->117
2->122
3->137
***************

Inserting: key 7 with value: 177

Item in Cache:
***************
1->117
2->122
3->137
7->177
***************

Inserting: key 4 with value: 148


**************************************************

		Cache is Full.Please flush it.
```

Follow the steps below to run a simulation:

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:ArjunGajmer/cached_system.git
   ```

2. **Set Up the Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   pip install -r requirements.txt
   ```
   
3. **Run the Simulation**
   ```bash
   python examples/lfu_cache.py
   ```
   ```bash
   python examples/lru_cache.py
   ```
   ```bash
   python examples/ttl_cache.py
   ```
   ```bash
   python examples/no_eviction.py
   ```
