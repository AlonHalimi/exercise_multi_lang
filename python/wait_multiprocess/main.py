#!/usr/bin/env python3
"""
Python multiprocessing translation of wait.go.
This demonstrates Python multiprocessing best practices for CPU-bound tasks.
"""

import multiprocessing
import sys
from typing import List


def worker_process(worker_id: int) -> None:
    """
    Worker process function that simulates the Go goroutine.
    This function runs in a separate process.
    
    Args:
        worker_id: The ID of the worker process
    """
    print(f"go routine {worker_id}", end="", flush=True)


def main() -> None:
    """
    Main function that creates and waits for all worker processes.
    This is equivalent to the Go main function with WaitGroup.
    """
    # Create a list to store process objects
    processes: List[multiprocessing.Process] = []
    
    # Create 5 processes (equivalent to Go goroutines)
    for i in range(5):
        process = multiprocessing.Process(target=worker_process, args=(i,))
        processes.append(process)
        process.start()
    
    # Wait for all processes to complete (equivalent to vg.Wait())
    for process in processes:
        process.join()


if __name__ == "__main__":
    # Ensure proper multiprocessing setup on all platforms
    multiprocessing.set_start_method('spawn', force=True)
    main()
