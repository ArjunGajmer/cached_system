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
freq-1:[2, 3]
freq-2:[1]
***************

Inserting: key 2 with value: 122

Item in Cache:
***************
freq-1:[3]
freq-2:[1, 2]
***************

Inserting: key 7 with value: 177

Item in Cache:
***************
freq-1:[3, 7]
freq-2:[1, 2]
***************

Inserting: key 4 with value: 148

Item in Cache:
***************
freq-1:[3, 4]
freq-2:[1, 2]
***************

Fetching value from cache with key 4: 148

Item in Cache:
***************
freq-1:[3]
freq-2:[1, 2, 4]
***************

Fetching value from cache with key 1: 117
Fetching value from cache with key 2: 122
Fetching value from cache with key 4: 148

Item in Cache:
***************
freq-1:[3]
freq-3:[1, 2, 4]
***************

Inserting: key 10 with value: 1107
Fetching value from cache with key 10: 1107

Item in Cache:
***************
freq-3:[1, 2, 4]
freq-2:[10]
***************

Inserting: key 11 with value: 1117

Item in Cache:
***************
freq-3:[1, 2, 4]
freq-1:[11]
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
1->101, Exp:1.998896
2->201, Exp:1.998832
3->301, Exp:1.998864
4->400, Exp:1.998892
***************


After 3 second

Inserting: key 5 with value: 500

Items in Cache:
***************
5->500, Exp:1.999876
***************


After 1 second

Inserting: key 6 with value: 600

Items in Cache:
***************
5->500, Exp:0.994391
6->600, Exp:1.999945
***************


After 1 second

Inserting: key 7 with value: 700

Items in Cache:
***************
5->500, Exp:-0.01154
6->600, Exp:0.994006
7->700, Exp:1.999851
***************


After 1 second

Inserting: key 8 with value: 800

Items in Cache:
***************
5->500, Exp:-1.016841
6->600, Exp:-0.011292
7->700, Exp:0.994553
8->800, Exp:1.999862
***************


After 1 second

Fetching value from cache with key 5: 500

Items in Cache:
***************
5->500, Exp:1.999455
6->600, Exp:-1.013568
7->700, Exp:-0.00772
8->800, Exp:0.997589
***************


After 1 second

Inserting: key 1 with value: 10

Items in Cache:
***************
5->500, Exp:0.995869
1->10, Exp:1.999887
***************

Inserting: key 11 with value: 10
Inserting: key 12 with value: 10

Items in Cache:
***************
5->500, Exp:0.995553
1->10, Exp:1.999585
11->10, Exp:1.999855
12->10, Exp:1.999938
***************

Inserting: key 13 with value: 10


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
