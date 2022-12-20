def solve(original_order) -> int:
    # index_tracker = {idx: idx for idx, _ in enumerate(original_order)}
    tracker = [(val, idx) for idx, val in enumerate(original_order)]
    list_len = len(original_order)
    
    for i in range(list_len):
        to_move_idx = tracker[i][1]
        n = tracker[i][0]
        new_idx = (to_move_idx + n) % list_len
        
        # move everything above its new position up 1
        for val, current_idx in tracker:
            # current_idx != i ensures we don't move the element we're moving
            if current_idx > new_idx and current_idx != i:
                

    # for i in range(list_len):
    #     print()
    #     to_move_idx = index_tracker[i]
    #     n = original_order[i]
    #     new_idx = (to_move_idx + n) % list_len
    #     print(f"Moving {n} to {new_idx}")
    # 
    #     for original_idx, current_idx in index_tracker.items():
    #         if current_idx > new_idx and current_idx != i:
    #             index_tracker[original_idx] = index_tracker[original_idx] + 1
    #         if current_idx == new_idx and current_idx != i:
    #             index_tracker[original_idx] = index_tracker[original_idx] - 1
    #     print(f"new_idx = {new_idx}")
    #     print("", end="")
    #     index_tracker[i] = new_idx
    #     for original_idx, current_idx in index_tracker.items():
    #         if current_idx > to_move_idx and original_idx != i:
    #             index_tracker[original_idx] = (index_tracker[original_idx] - 1) % list_len
    # 
    #     print_list(index_tracker, original_order)
    # return -1


def print_list(index_tracker, original_order):
    print()
    for v in index_tracker.values():
        print(original_order[v], end=", ")
