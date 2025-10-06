This documentation outlines the core theoretical concepts relevant to Assignments 1 and 2, based on the course description and included materials. The purpose of this course is two-fold: to provide an understanding of the concepts and design of operating systems (OS), and to examine implementation details of OSs like UNIX and Windows.

***

## Operating Systems Theory Outline

### I. Functions of an Operating System

An operating system acts as an intermediary program between a user and the computer hardware.

**Primary Goals and Roles (Describe the functions of an operating system):**

1.  **Execute user programs** and make solving user problems easier.
2.  **Make the computer system convenient to use**.
3.  **Use the computer hardware efficiently**.
4.  **Resource Allocator:** The OS manages all resources and decides between conflicting requests to ensure efficient and fair resource use.
5.  **Control Program:** The OS controls the execution of programs to prevent errors and improper use of the computer.

**Key Operating System Services:**

*   **User Interface (UI):** Nearly all OSs provide a user interface, which can be Command-Line (CLI), Graphics User Interface (GUI), or Batch.
*   **Program Execution:** The system must load a program into memory, run it, and handle termination (normal or error).
*   **I/O Operations:** Managing I/O requests, which may involve files or I/O devices.
*   **File-System Manipulation:** Programs need to read, write, create, delete, search files and directories, list information, and manage permissions.
*   **Communications (IPC):** Processes exchange information either on the same computer or over a network, potentially using **shared memory** or **message passing**.
*   **Error Detection:** The OS must constantly be aware of errors in the CPU, memory, I/O devices, or user programs, and take appropriate action to ensure consistent computing.
*   **Resource Allocation:** When multiple jobs run concurrently, the OS allocates resources such as CPU cycles, main memory, file storage, and I/O devices.
*   **Protection and Security:** Protection ensures access to system resources is controlled, while security defends the system (and user information) from external invalid access attempts.

***

### II. Interrupt Handling (Describe the events that follow the occurrence of an interrupt)

The operating system is fundamentally **interrupt driven**.

1.  **Interrupt Trigger:** An I/O device controller informs the CPU that it has finished an operation by causing a hardware interrupt. Alternatively, a **trap** or **exception** is a software-generated interrupt caused by an error (e.g., division by zero) or a user request (e.g., a system call).
2.  **Control Transfer:** The interrupt transfers control to the **interrupt service routine**. This transfer is generally achieved through the **interrupt vector**, which contains the memory addresses of all the service routines.
3.  **State Preservation:** The interrupt architecture must save the address of the interrupted instruction so the system can resume execution later. User program registers and process state are saved.
4.  **Kernel Mode Entry:** If the interrupt is a request for an OS service (a system call), the mode bit is changed to **kernel mode** (or supervisor mode), allowing privileged instructions to execute.
5.  **Service Routine Execution:** The CPU executes the relevant service routine based on the interrupt type.
6.  **Return to User:** After the interrupt is handled, the system call changes the mode back to user mode, and execution resumes from the saved instruction address.

A **timer** can be set by the operating system (a privileged instruction) to interrupt the computer after a certain period, ensuring the OS regains control and preventing a single process from hogging resources.

***

### III. Process and Thread Management Schemes

**A. Process Management (Describe and Assess)**

A **process** is defined as a program in execution and is the unit of work within the system; a program is merely a passive entity.

| Component | Description |
| :--- | :--- |
| **Process State** | Changes as the process executes: *new*, *running*, *waiting* (for an event), *ready* (waiting for a processor), or *terminated*. |
| **Process Control Block (PCB)** | Information associated with each process, including state, program counter, CPU registers, scheduling information, memory management data, accounting info, and I/O status. |
| **Process Creation** | Parent processes create children processes, forming a tree. The UNIX `fork()` system call creates a new process, and `exec()` replaces the child process's memory space with a new program. |
| **Interprocess Communication (IPC)** | Cooperating processes need mechanisms to share information, achieve computation speedup, or maintain modularity. This is achieved via **shared memory** or **message passing**. |

**B. Thread Management (Describe and Assess)**

A thread is a fundamental unit of CPU utilization. A multithreaded process has one program counter per thread, allowing multiple locations to execute at once.

| Benefit | Description / Assessment |
| :--- | :--- |
| **Responsiveness** | Allows continued execution if part of the process is blocked (important for UIs). |
| **Resource Sharing** | Threads automatically share the resources of the parent process, which is easier than implementing shared memory or message passing between separate processes. |
| **Economy** | Thread creation is "light-weight" and cheaper than "heavy-weight" process creation; thread switching has lower overhead than context switching. |
| **Scalability** | A process can take advantage of multiprocessor architectures (parallelism). |

**Multithreading Models (Explain the major alternatives for process/thread management):**

| Model | Description | Assessment / Usage |
| :--- | :--- | :--- |
| **User Threads** | Management done by user-level thread libraries (e.g., POSIX Pthreads, Windows threads, Java threads). | Kernel is unaware of them. |
| **Kernel Threads** | Supported directly by the operating system kernel (e.g., Windows, Linux, Solaris). | |
| **Many-to-One** | Many user threads mapped to a single kernel thread. | Low concurrency; if one thread blocks, all block. Few systems use this. |
| **One-to-One** | Each user thread maps to a separate kernel thread. | Higher concurrency, commonly used (e.g., Windows, Linux). Overhead may restrict the total number of threads. |
| **Many-to-Many** | Many user threads mapped to a smaller or equal number of kernel threads. | Allows the OS to create a sufficient number of kernel threads for optimal execution. |

***

### IV. Concurrency Mechanisms (Use semaphores and other mechanisms to solve standard concurrency problems)

**Concurrency** supports more than one task making progress, typically achieved by multiplexing CPUs among processes/threads. **Parallelism** implies a system can perform more than one task simultaneously, requiring multi-core hardware.

**Race Condition:** Occurs when several processes concurrently access and manipulate the same data, and the final outcome depends on the particular order in which the access takes place. Maintaining data consistency requires orderly execution of cooperating processes.

**Critical Section (CS) Requirements:** Any solution designed to solve the critical-section problem must satisfy three requirements:
1.  **Mutual Exclusion:** If process $P_i$ is executing in its critical section, no other process can be executing in their critical sections.
2.  **Progress:** If no process is in the CS, and some wish to enter, the selection of the next process cannot be postponed indefinitely.
3.  **Bounded Waiting:** A limit must exist on the number of times other processes can enter their CS after a process requests entry, but before that request is granted.

**Synchronization Tools (Describe and Assess):**

| Mechanism | Description | Assessment / Usage |
| :--- | :--- | :--- |
| **Mutex Locks** | Simplest software tool. Protects a CS by requiring a process to `acquire()` a lock before entering and `release()` the lock upon exiting. | Requires busy waiting (spinlock). Calls to `acquire()` and `release()` must be atomic. |
| **Semaphores** | An integer variable, $S$, accessed only via atomic `wait()` (decrement) and `signal()` (increment) operations. | **Counting Semaphores** range over an unrestricted domain and can control access to a resource with a finite number of instances. **Binary Semaphores** are equivalent to mutex locks (range 0 or 1). Can be implemented without busy waiting using a waiting queue. |
| **Monitors** | A high-level abstraction (Abstract Data Type) ensuring that only one process may be active within the monitor procedures at a time. | Uses **condition variables** (`x.wait()`, `x.signal()`) to suspend and resume processes within the monitor structure. |

**Standard Concurrency Problem: Bounded-Buffer**

The classic Producer-Consumer problem using a bounded buffer can be solved using three semaphores:
1.  `mutex`: Initialized to 1, ensuring mutual exclusion for buffer access.
2.  `full`: Initialized to 0, counting the number of full buffers.
3.  `empty`: Initialized to $n$ (buffer size), counting the number of empty buffers.

The **Producer** must `wait(empty)` (wait if buffer is full) before adding an item, and the **Consumer** must `wait(full)` (wait if buffer is empty) before removing an item. Both use `wait(mutex)` and `signal(mutex)` around buffer access (the critical section). (Assignment 1 requires implementing the bounded buffer producer/consumer using shared memory and managing the buffer pointers `in` and `out` to detect full/empty conditions.)

**Deadlock Characterization:** Deadlock can arise if four conditions hold simultaneously:
1.  **Mutual Exclusion:** Only one process can use a resource at a time.
2.  **Hold and Wait:** A process holding at least one resource is waiting to acquire additional resources held by other processes.
3.  **No Preemption:** Resources can only be released voluntarily by the holding process after completion.
4.  **Circular Wait:** A closed chain of waiting processes exists, where each process waits for a resource held by the next process in the chain.

***

### V. CPU Scheduling Algorithms (Describe and Assess)

The CPU scheduler is the short-term scheduler that selects the next process residing in the ready queue to execute on the CPU. Scheduling decisions are either **nonpreemptive** (when a process terminates or switches running $\to$ waiting state) or **preemptive** (when a process switches running $\to$ ready or waiting $\to$ ready).

**Scheduling Criteria (Assessment):** The goal is to maximize **CPU utilization** and **throughput**, while minimizing **turnaround time**, **waiting time**, and **response time**.

| Algorithm | Description | Assessment (Advantages/Disadvantages) |
| :--- | :--- | :--- |
| **First-Come, First-Served (FCFS)** | Processes are served in the order they arrive (FIFO queue). Nonpreemptive. | Simple to implement. Can suffer from the **convoy effect** (short processes stuck behind long ones), leading to high average waiting time. |
| **Shortest-Job-First (SJF)** | Schedules the process with the shortest predicted next CPU burst time. Can be estimated using exponential averaging. | **Optimal**: gives the minimum average waiting time for a given set of processes. The main difficulty is predicting the length of the next CPU burst. |
| **Shortest-Remaining-Time-First (SRTF)** | The preemptive version of SJF. | If a new process arrives with a shorter burst time than the currently running process's remaining time, the current process is preempted. |
| **Priority Scheduling (PR)** | The CPU is allocated based on a priority number (smallest integer $\equiv$ highest priority). Can be preemptive or nonpreemptive. | **Problem:** **Starvation** (low-priority processes may never execute). **Solution:** **Aging** (gradually increasing the priority of processes waiting for a long time). |
| **Round Robin (RR)** | Each process receives a small **time quantum** ($q$), typically 10–100 milliseconds. If the quantum expires, the process is preempted and added to the end of the ready queue. | **Good response time**. High overhead if $q$ is too small (relative to context switch time). If $q$ is large, it performs like FCFS. |
| **Multilevel Feedback Queue** | Allows processes to move between different ready queues based on their CPU behavior (e.g., short interactive jobs stay in RR queues with small quanta; CPU-bound jobs drop to FCFS queues). | **Aging** can be easily implemented by moving processes between queues. Highly configurable based on criteria such as the number of queues and scheduling algorithms used for each queue. |

***

### VI. Real and Virtual Memory Management Schemes

**A. Real (Physical) Memory Management**

The objective is to optimize CPU utilization and computer response by deciding what data moves into and out of memory, and allocating/deallocating memory space.

**Memory Allocation Schemes (Describe and Assess):**

*   **Contiguous Allocation:** Each process is contained in a single contiguous section of memory.
    *   *Assessment:* Requires hardware support (Base/Limit registers) for protection. Suffers from **external fragmentation** (total memory space exists, but is scattered/noncontiguous).
*   **Segmentation:** A memory management scheme that supports the user's view of memory, where a program is viewed as a collection of logical units (segments) such as the main program, procedures, stack, and heap.
    *   *Assessment:* Logical addresses are two-dimensional: `<segment-number, offset>`. Still suffers from external fragmentation.
*   **Paging:** The physical address space is noncontiguous, avoiding external fragmentation. Physical memory is divided into fixed-size blocks called **frames**, and logical memory is divided into same-sized blocks called **pages**.
    *   *Assessment:* Logical addresses are translated using a page table which maps page numbers ($p$) to physical frame addresses. This scheme suffers from **internal fragmentation** (allocated memory slightly larger than requested). Hardware support often includes a Translation Look-aside Buffer (TLB) to speed up address translation, as the page table is usually kept in main memory.

**B. Virtual Memory Management (Describe and Assess)**

**Virtual memory** separates user logical memory from physical memory, allowing the logical address space to be much larger than the physical address space. This allows more programs to run concurrently and requires less I/O for loading programs.

**Demand Paging:** The implementation method where a page is brought into memory only when it is actually needed (referenced).

*   *Assessment:* Reduces I/O and memory needed, leading to faster response. Requires hardware support, including a page table with a **valid–invalid bit** (used to detect a **page fault**).
*   **Effective Access Time (EAT):** Performance is sensitive to the **page fault rate** ($p$) because page fault service time (involving disk I/O) is extremely slow. $EAT = (1-p) \times (memory\ access\ time) + p \times (page\ fault\ time)$. To maintain reasonable performance, $p$ must be very small.

**Page Replacement (Describe and Assess):** Required when a page fault occurs and no free frames are available. A **modify (dirty) bit** reduces overhead by indicating whether a victim page needs to be written back to disk.

| Algorithm | Description | Assessment (Pros/Cons) |
| :--- | :--- | :--- |
| **First-In-First-Out (FIFO)** | Replaces the page that has been in memory the longest (oldest). | Simple. Suffers from **Belady’s Anomaly**, where increasing the number of allocated frames can sometimes increase the page fault rate. |
| **Optimal (OPT)** | Replaces the page that will not be used for the longest period of time in the future. | Impossible to implement since it requires predicting the future. Used solely as a standard for comparison. |
| **Least Recently Used (LRU)** | Replaces the page that has not been used for the longest time in the past. | Generally a good algorithm that does not suffer from Belady's Anomaly. Implementation requires expensive hardware support (counters or stacks) to track usage time. |
| **LRU Approximation (e.g., Second-Chance)** | Uses a reference bit; pages are replaced if the reference bit is 0. If 1, the bit is cleared and the process checks the next oldest page. | An efficient attempt to approximate LRU behavior without complex hardware. |

**Thrashing:** A state where a process is busy swapping pages in and out because it does not have enough frames allocated to hold its current working set (locality). This results in low CPU utilization. Limiting the effects of thrashing requires using local or priority page replacement policies.

***

### VII. Assignment-Specific and Course Relevant Topics

**Assignment 1 Specifics: Shared Memory and Multi-Tasking**

Assignment 1 involves writing producer and consumer programs that communicate via a **bounded buffer in shared memory**.

*   The Producer (parent) uses `fork()` to create the Consumer (child) and loads the consumer executable using `exec()`.
*   A fixed-size shared memory block (4K) is created by the producer using `InitShm()`. This block contains a header with: `bufSize` (buffer capacity), `itemCnt` (items to produce/consume), `in` (index of next item to produce), and `out` (index of next item to consume).
*   The producer must **wait** if the bounded buffer is full. The consumer must **wait** if the bounded buffer is empty.
*   Synchronization must be maintained by using specified functions to read/write the shared `in` and `out` variables (`GetIn/Out()`, `SetIn/Out()`) and to access the buffer contents (`ReadAtBufIndex()`, `WriteAtBufIndex()`).

**Assignment 2 Specifics: CPU Scheduling Algorithms**

Assignment 2 focuses on simulating four CPU scheduling algorithms, assuming a single CPU:
1.  **Round Robin (RR):** Processes are added to a FIFO queue based on arrival time. The time quantum is a parameter. If the quantum expires, the process goes to the end of the queue.
2.  **Shortest Job First (SJF) (Non-preemptive):** Scheduling decisions occur only when the current process terminates. The next process chosen is the one that has arrived and has the shortest CPU burst length. Ties are broken by arrival time (FCFS).
3.  **Priority Scheduling without Preemption (PR noPREMP):** Scheduling decisions occur only upon termination. The process with the highest priority (smallest number) is chosen. Ties are broken arbitrarily.
4.  **Priority Scheduling with Preemption (PR withPREMP):** Scheduling decisions occur upon termination OR when a higher priority process arrives. If a higher priority process arrives, the current CPU-holding process is preempted and added back to the priority queue.

**OS Design and Implementation:**

A crucial design principle is separating **Policy** (what will be done?) from **Mechanism** (how to do it?). Mechanisms determine *how* to accomplish a task, while policies decide *what* needs to be done. Separating them allows policy changes without changing underlying mechanisms.

OS structures vary widely:
*   **Simple Structure (MS-DOS):** Not divided into modules, interfaces and functionality poorly separated.
*   **Traditional UNIX:** Limited structuring, consists of systems programs and the kernel (everything below the system-call interface).
*   **Microkernel:** Moves as much functionality as possible from the kernel into user space, communicating via message passing. Benefits include being easier to extend/port, more reliable, and more secure; the detriment is performance overhead due to communication.
*   **Hybrid Systems:** Most modern OSs combine multiple approaches (e.g., Linux/Solaris are monolithic plus modular; Mac OS X uses a Mach microkernel base combined with BSD UNIX parts).

***

## Summary of Questions from Source Materials

The following is a condensed list of all multiple-choice and essay questions found in the provided slides, categorized by relevant topic:

### Functions of an Operating System & OS Structure

This topic covers the definition and goals of an OS, its components, and system architecture.
Questions include: How an operating system is like a government (it creates an environment for other programs to do work); what program runs all the time on the computer (the kernel); describing the four components of computer systems; describing OS design goals (convenience, reliability, safety, speed, ease of design/maintenance); and determining which statement relating to OS services, resource management, interfaces, protection, and security is incorrect. It also asks how microkernels handle communication (message passing), and defines the relationship between an API, the system-call interface, and the operating system.

### Interrupts, Bootstrapping, and System Calls

This covers how the OS starts and how user programs request services.
Questions address: Which stage triggers the CPU switch from user program to interrupt processing; what a bootstrap program is and where it is stored (ROM/EPROM/firmware); the three general methods used to pass parameters during system calls (registers, block/table in memory, or pushed onto the stack); which mechanism provides the interface to OS services (system calls); and why clustered systems provide high-availability service.

### Process and Thread Management

This section addresses the definition, states, creation, and advantages of processes and threads.
Questions cover: What area contains dynamically allocated data during runtime (heap section); which process state is switched to from 'running' when an I/O event occurs (waiting); scenarios that force a process off the CPU (I/O request, fork, interrupt/time slice expired); defining and describing the different process states; explaining why Google Chrome uses multiple processes; discussing the consequences of calling `exec()` before `fork()`; identifying items shared across threads of the same process (code, data, files); explaining why a web server shouldn't be single-threaded; listing and explaining the four major benefits of multithreaded programming (Responsiveness, Resource Sharing, Economy, Scalability); and defining and justifying the use of a thread pool.

### CPU Scheduling

This includes scheduling algorithms, criteria, and related concepts like latency.
Questions focus on: Which criterion is most important for an interactive system (response time); which circumstance cooperative scheduling can take place (running to waiting state switch); which algorithm must be nonpreemptive (FCFS); defining the role of the dispatcher; explaining starvation and how aging prevents it; identifying the two types of latency affecting real-time systems (interrupt latency, dispatch latency); and which term describes the capability for multiple tasks to make progress on a single processor system (concurrency).

### Concurrency and Synchronization

This section includes race conditions, critical section solutions, and classic synchronization problems.
Questions require: Explaining race conditions (concurrent access leading to outcome dependent on access order); assessing the relationship between the three critical section requirements (Mutual Exclusion, Progress, Bounded Waiting); discussing whether counting semaphores can be used to control access to resources with a finite number of instances (Yes); contrasting semaphores and mutex locks; detailing approaches to handle critical sections in OSs; analyzing structural changes in the bounded buffer producer process and the resulting blocking; describing scenarios for when using a reader–writer lock is preferable to a semaphore; explaining the difference between the first and second readers-writers problems; and describing a starvation scenario in the monitor solution for the dining philosophers problem.

### Deadlocks

This covers the characterization and handling of deadlocks.
Questions address: The necessary condition for deadlock stating a resource must be nonsharable (mutual exclusion); whether an unsafe state necessarily leads to a deadlocked state (it may lead to it); explaining the four necessary conditions for deadlock (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait); listing the three general ways deadlocks are handled (prevention, avoidance, recovery/ignoring); and describing protocols to prevent the hold-and-wait condition.

### Memory Management (Real and Virtual)

This topic covers address binding, allocation methods, fragmentation, paging, and demand paging.
Questions include: Identifying the binding method used by most general-purpose OSs (execution time binding); calculating the page number from a given logical address and page size (requires calculation); distinguishing between internal and external fragmentation; describing how a TLB assists address translation; calculating context switch time associated with swapping (requires calculation based on transfer rate/latency); explaining the distinction between demand paging and paging with swapping; explaining how Effective Access Time is computed for demand paging; explaining why a local replacement algorithm doesn't entirely solve thrashing; identifying when a page is loaded in demand paging (only when needed during execution); and identifying what the dirty (modify) bit signals (the page has been modified since loading).

### Storage and File System Implementation (General Course Relevance)

Questions address: The two components of positioning time (seek time + rotational latency); which disk scheduling algorithm ignores the current head position (FCFS); describing a disadvantage of FCFS disk scheduling (long waits); listing the factors influencing disk-scheduling algorithm selection; which structure reads and writes physical blocks (basic file system); what structures implement a file system (boot control block, volume control block, directory structure); and explaining why the entire block is unavailable to a user when linked allocation is employed.