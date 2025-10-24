#!/usr/bin/env python3
"""
Python translation of wait.go using asyncio for concurrency.
This demonstrates Python concurrency best practices with async/await.
"""

import asyncio
import sys
from typing import List


async def worker_routine(worker_id: int) -> None:
    """
    Async worker function that simulates the Go goroutine.
    
    Args:
        worker_id: The ID of the worker routine
    """
    print(f"go routine {worker_id}", end="", flush=True)


async def main() -> None:
    """
    Main async function that creates and waits for all worker routines.
    This is equivalent to the Go main function with WaitGroup.
    """
    # Create a list of coroutines (equivalent to Go goroutines)
    tasks: List[asyncio.Task] = []
    
    # Create 5 async tasks (equivalent to Go goroutines)
    for i in range(5):
        task = asyncio.create_task(worker_routine(i))
        tasks.append(task)
    
    # Wait for all tasks to complete (equivalent to vg.Wait())
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
