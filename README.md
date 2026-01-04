# Advent of Code 2025 Solutions

![AOC Stars](https://img.shields.io/badge/AOC_Stars-24_⭐-gold?style=plastic&logo=python&logoColor=white)

My solutions for [Advent of Code 2025](https://adventofcode.com/2025), a series of programming puzzles released daily during December.

## Overview

Advent of Code is an annual set of Christmas-themed programming challenges that can be solved in any programming language. Each puzzle has two parts, with the second part unlocked after completing the first. Each part solved awards one star ⭐.
I'm happy having completed the whole thing for a second time on a row. The aoc community is really cool and has made me feel excited about continuing to improve in algo and solve interesting problems. It also felt a bit easier than last year, but unlike people saying it got easier, I will choose to believe that I got better. Finally, it being 12 days was not bad, last year I had to struggle with holiday commitments and solving aoc, whereas this year i was mostly done with everything on the 12th and just had to revisit day 9 part 2 to solve it later.

## Implementation Details

All solutions are implemented in Python. Most solutions use only the standard library, but this year i decided to use some more libs for some solutions, in particular numpy, scipy and shapely.

## Learning Journey

### Key Learnings
- Kind of implemented Union-Find (disjoint set) data structure for the problem in day 8, which was cool. Also had to scratch my brain to use numpy to find the shortest edges using matrix operations because i thought it would be faster (maybe i should benchmark haha)
- Day 9 part 2 was interesting, I started by creating the image as an svg which made me think that there should be an easy way of solving (single round shape with a band empty). But I was decided on using some library to make objects and look at intersections in 2D, so I tried Shapely which was rather easy to setup and get working and it did the job fine. I might revisit the problem to make a solution not using this lib.
- Day 10 part 2 was also challenging, I started it doing breadth first with some pruning but some of the problems were making too large of a tree and it was running forever. Then after some thinking i realised that it was a best solution minimizing the number of clicks kind of problem, so I implemented a solution using scipy's linprog and that worked fine. It was cool revisiting some linear programming since i do not do much of it anymore.

### Community Experience
Same as last year, I really like the AOC community, I do not post much but I think it is always nice to see people commenting to help others. And I have a lot of fun going over some out of the box solutions and memes once I'm done with a problem in a day. It was also kind of inspiring to see people that have been going at it and completing it for 10 years.

## Notes
- Input files are not included in the repository as per Advent of Code's request
- Each day's solution is contained in its own directory
