# Puzzles

## Disclaimer about the code in this repo
Just in case you came to this repo in a context where you would have to make an opinion on the code that I produce:  
Please consider that this is code that I initially wrote for myself, to solve specific puzzles. Any code you find here is both a good indication of my ability to problem-solve, and absolutely not representative neither of the kind of code I write when in a team nor of the practices I enforce to ensure quality.  

And I kinda went for the easy solution for some of those, not sure it would work for your inputs, but whatever.

## Why I think those puzzles matter
I enjoyed all kind of puzzles when I was far younger, but as I grew up I decided that my time was too valuable and I needed to focus on real problems. In retrospect, that was a huge mistake. Doing your job is not enough for getting better at doing your job.

You sometimes need to focus on some skills that you don't use that much, but matter a lot when you use them. You sometimes need to build a good intuition on how things work one or two layers under the one you are working on to build something efficient.

You can never be sure of how transferable all of those skills are, but if learning a new language can improve your memory, maybe even the weirdest puzzles provide some form of general improvement of your cognitive capabilities.

For the coding puzzles, it is even more straightforward : for example, I only did the 2023 edition of the Advent of Code for now, months late, so I can't talk about any other edition, but most of the second parts were there for you to find the tricks that will bring you huge performance gains.

Maybe those are not as complex as the real world problems, but it's still a good way to build intuition. Maybe you just need the simplest recursive implementation and a cache, be it Python's `dict` in your solution, or Redis in the real world. Maybe that's not enough, maybe you need to fully reconsider the way your functions pass data to each other. Maybe you can find a cycle somewhere and get a decent estimation of a future value. That's the kind of thinking involved with software engineering, and that you don't necessarily train enough while actually doing software engineering, as you're supposed to have meetings, backlog refinements, pipeline runnings, all those things that need to be combined with your problem-solving abilities for you to provide value for a company.

Now, it could be worse, but I do regret that I didn't train as much as I should have through puzzles like those.

## How do I solve?
This is the hardest question. It's really hard to introspect and give a definitive answer on how you managed to pull out the correct intuition at some point. Actually, I think it's about asking yourself the right questions, whether consciously or not.
So, this is a short list of the kind of questions I ask myself, not exhaustive, but I may try to complete it someday.

- Can I cache some results?
  - If so, what will be the memory cost?
  - Are the cached values redundant enough to not waste too much memory?
  - Could I actually just reorganize my code so that the same computations aren't done so many times?
- Is there some form of cycle / pattern in the processing of the data?
  - Can I automatically identify those patterns and make assumptions on final values?
- Can I use the divide and conquer strategy on something?
- Can I use specific data structures to gain efficiency? (Python's `dict` and `set` are awesome, it feels so good to use a hash table with just 2 chars)
- Can I introduce a slight variation to a known algorithm? (I may or may not allow myself to re-read about those to verify my assumptions, but I think going to harder problems and checking solutions may be a great way to find out about the ones you don't know)
- Can I go further by mixing the answers to some of the above questions in some way?

Now, I look at the solutions after solving the puzzle by myself (I still do it after I solve the puzzle as I may found other interesting performance / concision tradeoffs), but maybe going for the solution half the time when you are beginning is good to build intuition.

## Resources that may help you problem-solve
### [Computer, Enhance!](https://www.computerenhance.com/p/table-of-contents) by [Casey Muratori](https://caseymuratori.com/about)
While showing you some low-level tricks that don't apply to everyone anymore, everything in here is still an interesting read, whether it applies to your current profile or not. Special mention for his [1994 Internship Interview Series](https://www.computerenhance.com/i/99218768/internship-interview-series) where he breaks down solving the questions he was asked during his Microsoft interview.

## Puzzles I enjoyed and I'd recommend but still didn't publish
### [Daily Coding Problem ](https://www.dailycodingproblem.com/)
I did nearly all of those on a work laptop, and wiped it when I left, so I'll have to start again to publish solutions.
But I'd recommend doing those, even if you may not be sure if your answers are correct.

### [CodeSignal](https://codesignal.com/)
Had to grind a bit to get Python fluency again, I really enjoyed that one for the questions and the "half the tests you have to pass are shown, half the tests you have to pass are covering edge cases you have to think about" philosophy. You have to use their online IDE though.

### [Exercism](exercism.org)
Not really puzzles, more like easy exercises to help you get fluent with your language of choice. At least can be done locally, and may provide the best difficulty curve for beginners.

## Other recommendations if you enjoy those coding puzzles
May seem weird for me to link this here, but [those are the games and puzzles I would like to find out if I didn't know about](https://github.com/c4ffein/writings/blob/main/s/puzzles/puzzles.md), and I guess if you read this you may enjoy those too.
