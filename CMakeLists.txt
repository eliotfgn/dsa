cmake_minimum_required(VERSION 3.24)
project(dsa)

set(CMAKE_CXX_STANDARD 14)

add_executable(dsa
        data-structures/challenges/graphs/flood_fill.py
        data-structures/challenges/heaps/closest_points_to_origin.py
        data-structures/challenges/linked_list/add_two_numbers.py
        data-structures/challenges/linked_list/linked_list.cpp
        data-structures/challenges/linked_list/linked_list.py
        data-structures/challenges/linked_list/merge_k_sorted_list.cpp
        data-structures/challenges/linked_list/merge_two_sorted_lists.py
        data-structures/challenges/linked_list/middle_of_the_linked_list.py
        data-structures/lessons/heap_implementation/minheap.py)
