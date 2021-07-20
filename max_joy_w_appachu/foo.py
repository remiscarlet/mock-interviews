"""
===
Written in an editor with no code interpretter/running.
===

The vacation consists of N days.
For each day you will choose one of the following activities and gain the corresponding points of happiness.

    A: Swim in the sea. Gain a points of happiness.
    B: Catch bugs in the mountains. Gain b points of happiness.
    C: Do homework at home. Gain c points of happiness.

You cannot do the same activities for two or more consecutive days.
Find the maximum possible total points of happiness.



Input:
N = 3
A = [10, 20, 30]
B = [40, 50, 60]
C = [70, 80, 90]

Output:
210


C, B, C -> 70+50+90=210 points of happiness.

Example1:
most_joyous = [(40, 70), (50, 80), (60,90)]
most_joyous_idx = [1, 0, 1] (or [0, 1, 0])

Example2:
N = 3
A = [10, 60, 30]
B = [60, 20, 100]
C = [50, 70, 20]

potential_joy_on_given_day = [(10, 60, 50), (60, 20, 70), (30, 100, 20)]

Tracing:
n = 1, a=[10], b=[60], c=[50]
max_happiness(0)
    -> n=0, prev_day = None
       todays_score = 10|60|50
       return => 60

n=2, a=[10,60], b=[60, 20], c=[50, 70]
max_happiness(0)
    -> n=0, prev_day = None
       if todays_score = 10
           max_happiness(1, 0)
           -> n=1, prev_day=0
              if activity_idx=0: continue
              if activity_idx=1: todays_score = 20
              if activity_idx=2: todays_score = 70
              return => 70
           score = 70 + 10
       if todays_Score = 60:
           max_happiness(1, 1)
           -> n=1, prev_day=1
              if activity_idx=0: todays_score=60
              if activity_idx=1: continue
              if activity_idx=2: todays_score=70
              return => 70
          score = 70 + 60
      if todays_score = 50:
           
        
"""

from typing import List, Optional

def main(n: int, a: List[int], b: List[int], c: List[int]) -> int:
    #joy_options_per_day = zip(a, b, c)
    assert(n == len(a))
    joy_options_per_day = [(a[i], b[i], c[i]) for i in range(n)]
    
    def max_happiness_from_day(day_num: int, prev_days_activity: Optional[int] = None) -> int:
        if day_num >= n: return 0
        
        max_score = 0
        for activity_idx in range(3):
            if activity_idx == prev_days_activity: continue
            todays_score = joy_options_per_day[day_num][activity_idx]
            future_score = max_happiness_from_day(day_num+1, activity_idx)
            score = todays_score + future_score
            
            if score > max_score:
                max_score = score
        
        return max_score
                
            
    return max_happiness_from_day(0)
    
print(main(3, [10,20,30], [40,50,60], [70,80,90]))
    
    
    
def main_cached(n: int, a: List[int], b: List[int], c: List[int]) -> int:
    #joy_options_per_day = zip(a, b, c)
    assert(n == len(a))
    joy_options_per_day = [(a[i], b[i], c[i]) for i in range(n)]
    
    cache = {}
    def max_happiness_from_day(day_num: int, prev_days_activity: Optional[int] = None) -> int:
        if day_num >= n: return 0
        cache_key = (day_num, prev_days_activity)
        if cache_key in cache:
            return cache[cache_key]
        
        max_score = 0
        for activity_idx in range(3):
            if activity_idx == prev_days_activity: continue
            todays_score = joy_options_per_day[day_num][activity_idx]
            future_score = max_happiness_from_day(day_num+1, activity_idx)
            score = todays_score + future_score
            
            if score > max_score:
                max_score = score
        
        cache[cache_key] = max_score
        return max_score
                
            
    return max_happiness_from_day(0)

print(main_cached(3, [10,20,30], [40,50,60], [70,80,90]))
