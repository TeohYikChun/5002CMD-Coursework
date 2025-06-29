import threading
import random
import time


def generate_numbers():
    return [random.randint(0, 10000) for _ in range(100)]


def test_experiment(use_threads, rounds=10):
    results = []

    for _ in range(rounds):
        start_time = time.time_ns()

        if use_threads:
            threads = []
            for _ in range(3):
                t = threading.Thread(target=generate_numbers)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        else:
            for _ in range(3):
                generate_numbers()

        end_time = time.time_ns()
        results.append(end_time - start_time)

    return results


# Run experiments
thread_results = test_experiment(True)
seq_results = test_experiment(False)

# Calculate metrics
thread_total = sum(thread_results)
seq_total = sum(seq_results)
thread_avg = thread_total / 10
seq_avg = seq_total / 10

# Format output to match sample
print("+-------+--------------------------+------------------------------+-----------------+")
print("| Round | Multithreading Time (ns) | Non-Multithreading Time (ns) | Difference (ns) |")
print("+-------+--------------------------+------------------------------+-----------------+")

for i in range(10):
    diff = seq_results[i] - thread_results[i]
    print(f"| {i + 1:<4} | {thread_results[i]:<25} | {seq_results[i]:<28} | {diff:<15} |")

print("+------+---------------------------+------------------------------+-----------------+")

print("\n### Summary of Results:")
print("+------------------+----------------------+-------------------------+-----------------+")
print("| Metric           | Multithreading (ns)  | Non-Multithreading (ns) | Difference (ns) |")
print("+------------------+----------------------+-------------------------+-----------------+")
print(f"| Total Time       | {thread_total:<20} | {seq_total:<23} | {seq_total - thread_total:<14}  |")
print(f"| Average Time     | {thread_avg:<20.1f} | {seq_avg:<23.1f} | {seq_avg - thread_avg:<14.1f}  |")
print("+------------------+----------------------+-------------------------+-----------------+")