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

## Other recommendations if you enjoy puzzles
Kinda weird for me to write this here, but those are the games and puzzles I would like to find out if I didn't know about, and I guess if you read this you may enjoy those too.

### [How Would You Move Mount Fuji?](https://www.amazon.fr/How-Would-Move-Mount-Fuji/dp/0316778494)
A book about Microsoft's cult of the puzzle, both a good criticism and a good source for the puzzles they ask to each others and to interviewees.

### [Simon Tatham's Portable Puzzle Collection](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/)
[Simon Tatham](https://en.wikipedia.org/wiki/Simon_Tatham)'s own [puzzle collection](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/), accessible from your browser.

### [Braid](https://store.steampowered.com/app/499180/Braid_Anniversary_Edition/)
Imo, the masterpiece, seems like a nice little platformer with nice graphics and nice music (the [Anniversary Edition](https://store.steampowered.com/app/499180/Braid_Anniversary_Edition/) has to be played on a 4K screen), but there are clever puzzles and it conveys real meaning, if you care. May start too easy (some of the greatest mind of our time may even consider this is [for people who smoke, or people who drink](https://www.youtube.com/watch?v=xSXofLK5hFQ) without going past the first levels) but it does build further with some new mechanics.
And the [Anniversary Edition](https://store.steampowered.com/app/499180/Braid_Anniversary_Edition/) does come with commentaries to convince you that yes, this is a masterpiece.

### [The Talos Principle 2](https://store.steampowered.com/app/835960/The_Talos_Principle_2/)
First person, lasers, colored lasers, tools that do stuff with lasers, teleporters, bumpers...
Very well made, not really hard, I'd really recommend and I still hope for a harder DLC - update, the DLC is really good.
They introduced many game mechanics but didn't mix them as much as they could
(that's what the DLC for the first one did, no new mechanic, but it built far more complex puzzles with what was introduced).

The philosophy in this game is cheap, there is nothing you'll find in it that you can't come up with by yourself.
And the NPCs won't stop talking.
But at least [they're making young engineers think about AI and consciousness](https://www.lesswrong.com/posts/hgpGbepiNzHMBDHcF/the-talos-principle).

Thanks to [Unreal Engine 5](https://www.unrealengine.com/en-US/developer-interviews/inside-croteam-s-transition-from-in-house-tech-to-ue5-for-the-talos-principle-2), it's really beautiful for a 3D puzzle game with that artistic direction, you can't compare with [The Witness](https://store.steampowered.com/app/210970/The_Witness/) (still aesthetically pleasant imo, but it's not like it could compete with a AAA).

### [Portal 2](store.steampowered.com/app/620/Portal_2/)
First person, portals and momentum, dialogues you may find funny, not that hard but you may enjoy the vibe.

### [We Were Here](https://store.steampowered.com/app/582500/We_Were_Here/)
A first person 2 player escape game in which  you have to share information with your pair (away in other rooms) to escape. The [first one](https://store.steampowered.com/app/582500/We_Were_Here/) is really easy (and free), not even really a puzzle game, but still good to introduce you and your pair to the information sharing that is required for all of those. They become better and better.

### [Baba Is You](https://store.steampowered.com/app/736260/Baba_Is_You/)
A [Sokoban](https://en.wikipedia.org/wiki/Sokoban) where you can move words to make new rules. As always, start simple, finish hard.

### [Sedecordle](https://www.sedecordle.com/)
There is still a point playing a [Wordle](https://www.nytimes.com/games/wordle/index.html)-like when you're filling 16 words in 21 tries.

### [Jane Street Puzzles](https://www.janestreet.com/puzzles/)
You can go for the [current one](https://www.janestreet.com/puzzles/current-puzzle/) or just browse [the archive](https://www.janestreet.com/puzzles/archive/index.html).
