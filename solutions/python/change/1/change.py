from collections import deque

def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """
    Calculate the fewest number of coins required to make a exact change for a target amount.
    """
    if target < 0:
        raise ValueError("target can't be negative")

    # Queue stores tuples of (current_sum, list_of_coins)
    queue: deque[tuple[int, list[int]]] = deque([(0, [])])
    seen: set[int] = {0}

    while queue:
        current_sum, current_coins = queue.popleft()

        # If we hit the target, this is guaranteed to be the shortest path
        if current_sum == target:
            return sorted(current_coins)

        for coin in coins:
            new_sum = current_sum + coin
            
            # Only proceed if we haven't exceeded the target and haven't seen this sum yet
            if new_sum <= target and new_sum not in seen:
                seen.add(new_sum)
                queue.append((new_sum, current_coins + [coin]))

    # If the queue empties and we haven't returned, it's impossible
    raise ValueError("can't make target with given coins")