# Review Analysis — 1,802 Google Photos reviews

Full labels for every review, with a one-line reason each, are in `reviews_classified_claude.csv`.

---

## How this was done

- Every review read and labelled individually: 1,000 Play Store, 802 Reddit.
- **Step 1, relevance:** is this review about finding photos at all? Everything below is reported as a share of the relevant ones, not of all 1,802.
- **Step 2, your 8 questions**, answered only when the review actually says it. "Not stated" was allowed and used heavily.
- **Step 3, my own classification**, built from what reviewers actually complained about, then checked against the research.
- **Rule for Q5 vs Q6:** "I don't know what to type" = Q5. "I typed a reasonable description and got nothing useful" = Q6. Unclear cases were marked unclear.

---

## 1. Relevance

| | Count | Share |
|---|---|---|
| **Retrieval difficulty** | **1,001** | 56% |
| Not about retrieval | 646 | 36% |
| Positive / suggestion | 86 | 5% |
| Technical (photos lost, app won't open) | 69 | 4% |

Play Store: 787 of 1,000 are retrieval difficulties. Reddit: only 214 of 802, because most Reddit rows are short thread replies ("same here", tips, jokes).

**All numbers below are out of the 1,001 retrieval-difficulty reviews.**

---

## 2. The most important finding: your 8 questions only cover a third of the problem

Questions 4–8 assume the user **searched**. Most didn't.

| How the user was trying to find the photo | Count | Share |
|---|---|---|
| Browsing people, albums, folders, places | 389 | 39% |
| Search box | 355 | 35% |
| Scrolling the timeline | 185 | 18% |
| Mixed | 30 | 3% |
| Memories | 18 | 2% |
| Not stated | 24 | 2% |

**57% of retrieval complaints are about navigating, not searching.** The search journey is real and badly broken, but it's the minority case. Your research already pointed here (people navigate even when search is better); the reviews confirm it in your own users' words.

---

## 3. Your 8 questions

### Q1. What kinds of old photos do users struggle to retrieve?

A specific type was named in 515 reviews (51%).

| Photo type | Count |
|---|---|
| People | 174 |
| Albums / folders (the container itself) | 103 |
| Old or previous-phone photos | 79 |
| Screenshots / documents | 70 |
| Received / downloaded / shared | 63 |
| Objects / things | 52 |
| Trips / places | 39 |
| Videos | 18 |
| Events / occasions | 11 |

Note that "the album itself" is the second most common thing people can't find.

### Q2. What information do people actually remember?

Stated in only 390 reviews (39%). Reviews say what people *tried*, not everything they remembered.

| Cue | Count |
|---|---|
| Person | 152 |
| Object | 59 |
| Specific date | 49 |
| Own caption / tag they wrote | 39 |
| Named place | 38 |
| Text in the image | 34 |
| Filename | 33 |
| Year | 21 |
| Month | 14 |
| Event / occasion | 9 |
| Scene / what was happening | 8 |
| Type of place | 4 |
| Season | 1 |
| Time of day | 0 |

### Q3. What information have they forgotten?

**Only 4 reviews say explicitly what they forgot.** Reviews simply don't carry this. Two worth quoting:

> "we cannot regularly keep on remembering date or event" — P516
>
> "I cannot find a single photo, except by accident, unless I happen to remember WHEN it was modified" — P562

### Q4. How do users formulate searches when memory is incomplete?

Method stated in 573 reviews.

| Method | Count |
|---|---|
| Browsed people / albums / folders / places | 225 |
| Scrolled the timeline | 111 |
| Keyword | 101 |
| Own caption / tag | 35 |
| Date | 31 |
| Person's name | 31 |
| Text in image | 29 |
| Filename | 25 |
| Place | 20 |
| Natural description | 12 |

Two recurring patterns:
- **Falling back to time.** When search fails, people scroll to roughly when they think it was. *"If I want to find a photo… I have to remember the date I took it and scroll back"* (R458).
- **Workarounds that prove the intent.** Typing keywords into the description field so they can find photos later, putting text in quotes, typing "03-15" instead of "March 15", pinching to reveal hidden dates.

### Q5–Q8. The search journey, step by step

Out of the 385 reviews where the user searched:

| Step | Failed here | Share |
|---|---|---|
| **Q5.** Couldn't express what they remember | **0** | 0% |
| **Q6.** App didn't understand the clue | **314** | 82% |
| **Q7.** Results hard to judge | 50 | 13% |
| **Q8.** Couldn't fix a failed search | 37 | 10% |

**Read Q5 carefully.** Zero doesn't mean people can always articulate. In 129 of these reviews the person stated a perfectly clear query ("dog", "Halloween 2024", "museum") and the app failed it. Reviewers blame the app, not their own memory, and someone who can't put a memory into words doesn't experience that as a product failure worth reviewing. **Q5 can only be tested by watching someone search in an interview.**

**Q6 dominates.** Typical examples:
- *"museum"* now returns one museum from 2018 (R001)
- *"when I was wearing the yellow dress"* (P219)
- *"me climbing a mountain"*, *"me holding a snake"* (R175)
- *"autumn [city name] 2022"* returns zero results (R182)
- *"painting of a woman in a blue dress"*, *"green pancakes in Japan"* used to work, now return nothing (R033)

**Q8 is small but vivid:**
> "I have to attempt 3-4 different searches for other things that might be in the picture I'm looking for according to my memory" — R060

---

## 4. My own classification: what people actually complain about

| Problem | Reviews | Share | Play Store | Reddit |
|---|---|---|---|---|
| Search got worse, or AI search | 340 | 34% | 31% | 44% |
| **Photos scattered across folders, sources, device vs cloud** | **268** | **27%** | **34%** | 2% |
| Timeline hard to navigate (layout, scrolling, date breaks) | 229 | 23% | 23% | 23% |
| Albums hard to find or manage | 157 | 16% | 19% | 4% |
| Face grouping wrong or impossible to correct | 145 | 15% | 13% | 21% |
| Wants more control (sort, filter, select) | 81 | 8% | 9% | 6% |
| Clutter: duplicates, screenshots, stacking | 73 | 7% | 8% | 4% |
| Memories / resurfacing | 36 | 4% | 5% | 0% |
| Knows it exists, or needed it urgently | 28 | 3% | 3% | 4% |
| Lost context after finding a photo | 17 | 2% | 1% | 3% |
| Asks for "find similar" | 4 | 0.4% | | |

A review can have several, so shares add to more than 100%.

**The two sources tell different stories.** Play Store users mostly can't find *where* photos went (folders, downloads, device vs cloud). Reddit users mostly complain that *search got worse*. Worth keeping separate on the slide.

---

## 5. How this lines up with the research

### Strongly confirmed

**Auto-collections fail silently and can't be corrected.** 145 face-grouping complaints, plus dozens of Reddit replies. The same people split into many; different people merged into one (a man with a child, a friend with a dog); and the one that hurts most: *manual corrections get undone.*
> "Does not respect 'merging' two people into one… Weeks later it will yet again split those photos out… Lather rinse repeat, for eternity." — R331

**Albums become their own retrieval problem.** 157 complaints. The album list can't be searched or sorted when adding a photo, so people scroll through dozens or hundreds of albums. One user has 75,000 photos going back to 1910 (P741).

**Date breaks are the landmarks people navigate by.** A long Reddit thread erupted when Google removed the gaps between days and made random thumbnails bigger.
> "I need that white spaces back. Those helped to search for photos faster" — R569
>
> "In the old UI, the scroller wheel directed the user to the Month and Year titles, moving through them like checkpoints" — R589

**Locate-on-timeline, the feature you marked "GOLD".** Small numbers, but people asked for exactly this, unprompted and in detail, 11 times, plus 6 more posts trading workarounds for its absence.
> "Let's say I searched for a particular photo and found it. Now I want to see the other photos I've taken at that event… The only way I can see to do it is to note the day… then scroll down to the date." — R112
>
> "It's baffling that it doesn't exist… for any photo, say 'show in photostream' (or whatever Google calls it). To see it in context of where it sits in the gallery." — R119

**Context cues fail.** Every "Q6" example above is a description of a scene, a season, a person doing something. Exactly the kind of cue your central finding says systems can't use.

**Screenshots and documents are a separate, urgent use.** 70 reviews name them; text-in-image search failures appear in 36. The stakes are practical and immediate: a ticket at a counter, a passport, a Global Entry number.
> "Not being able to find things quickly this way has added hours of labour to my day to day life." — R197

**Combining cues is what people need.** "Sue" plus "2021" for a gift book (R094), a person plus their dog (R745), several named friends together (P205). When it works, people love it: *"person A and person B with a dog and BOOM it found it"* (P525). *"Searching 'christmas' will bring forth every christmas photo taken since 2014"* (P944).

**Stacking hid what people needed.** *"I couldn't find the picture I just took… it was stacked and needed to be unstacked. That was a mean trick."* (P606). Stacking also hid a user's folders (P764).

**Resurfacing can't hand off to locating.** Several people can only reach old photos when a Memory happens to show them, and can't get from that Memory back to the photo in their library.
> "I know they are there though, because when it prompts 'memories' I suddenly can access everything." — P462
>
> "Memories… can usually only see one pic… And can't find these specific pics, videos in history." — P675

### New, not in the research

**Fragmentation is the biggest problem on the Play Store (34%).** Downloads, WhatsApp images, screenshots, edited copies and freed-up backups each land somewhere different, and other apps can't see them. The research mentioned fragmentation in passing; the reviews say it's the single largest source of "I can't find my photo."

**Every update resets people's mental map.** 124 layout complaints. The research argued that being shown "you are here" builds a map of your library over time. The reviews show the reverse: each redesign erases it, and people have to relearn where everything is.

**Dates people rely on are often wrong.** 44 complaints: photos re-dated after a phone transfer, backup or move. The research flagged date hygiene as a risk; here it's actively breaking navigation.

**People want to teach the AI, and want it to remember.** "Let us help the AI" (P247). "Surely if you've manually chosen a person that should override the algorithm?" (R276). Directly relevant to an AI-native solution: correction has to stick.

### Not supported, or can't be tested here

**Can't express the memory (Q5): no evidence either way.** Reviews can't show this. Interviews must.

**"Find similar" has little pull.** Only 4 reviews ask for it. That's not demand, but it's also not evidence against: people rarely ask for features they've never seen.

**Time-scale memory (season, time of day): untestable.** 1 mention of season, 0 of time of day. Reviews only show that when people use time, they try exact dates, and that breaks.

**AI search is mixed, not simply bad.** 74 complaints, but also genuine successes: a restaurant in Udaipur found through Ask Photos (P964), descriptive adjectives working (R061), a competitor's AI finding *"elderly holding baby"* (R178).

---

## 6. Comparison with the existing model labels

- **The file holds one set of labels, not separate Luna and Astra columns**, so I couldn't compare the two models against each other.
- **Relevance agreement: 84%.** I counted 197 more reviews as retrieval problems, mostly ones the model filed as "technical only" where the photos exist but the user can't locate them (device vs cloud, folders, faces). From the user's side, that is a retrieval failure.
- **The model's Q5–Q8 answers can't be counted.** It wrote free-text observations and never answered yes, with over 500 distinct wordings per question. My labels give a countable Yes / No / Not stated.
- **Q6 agreement is reasonable:** the model flagged a matching problem in 321 reviews, I flagged 382, and 239 overlap.
- **We agree reviews say almost nothing about what people forgot.**

---

## 7. What reviews can't tell you → interview priorities

1. **Can people put the memory into words?** Q5 is invisible in reviews. Test it with a live search task.
2. **What do they remember and forget?** Reviews show only what people typed. Ask them to describe a photo before searching.
3. **Season and time-of-day memory.** Untested here; the survey and a verified-date task in interviews are the only sources.
4. **Why browse instead of search?** 57% of complaints are navigation. Find out what makes someone choose to scroll.
5. **Would "show me where this sits in my library" get used?** Strong, specific but small signal. Watch whether people try to do it during the task.
6. **Memories vs utility photos.** Screenshots and documents behave differently and carry urgency. Probe both.

---

## 8. Quotes worth putting on slides

> "it took me FOUR HOURS yesterday afternoon, to find a set of two pictures adjacent to each other." — P511

> "Not being able to find things quickly this way has added hours of labour to my day to day life." — R197

> "I have to attempt 3-4 different searches for other things that might be in the picture I'm looking for according to my memory." — R060

> "It's baffling that it doesn't exist… 'show in photostream' (or whatever Google calls it). To see it in context of where it sits in the gallery." — R119

> "We cannot regularly keep on remembering date or event." — P516

> "I know they are there though, because when it prompts 'memories' I suddenly can access everything." — P462

> "My mother died recently, and Im trying to gather up her photos and google has them […] all over the place." — R456

> "cant remember when you were in Thailand, just search Thailand and every photo you've taken will show in the results." — P715 (what success looks like)

---

## Caveats

- **App reviews skew negative and recent.** Most were written right after an update broke something, so "worse after update" is inflated.
- **Reddit rows are mostly thread replies**, which is why only a quarter are retrieval complaints. The substantive Reddit posts are rich but few.
- **One person labelled all of this (me), in one pass.** The reason column lets you spot-check any label.

---

## 9. What the Luna/Astra analysis caught that this one missed

Logged after comparing against the Luna/Astra report. These are gaps in this analysis, not in theirs.

**1. People who can't express a combination in the search box's language (Q5).**
R091, R094 and R095 knew exactly what they wanted, such as "Sue" plus 2021 minus one album, but couldn't write it in the search syntax. I filed these under "wants more control". They belong with Q5 as a narrower finding: people can tell a person what they want but can't tell the system. That is the "formalized vs compromised" stage from Wilson's model in the tip-of-the-tongue research.

**2. Two explicit cases of forgotten details (Q3).**
- **P964:** remembered Udaipur and last winter, forgot the restaurant's name; Ask Photos found it. The closest thing to a true tip-of-the-tongue case in the dataset, and it was an AI success.
- **P722:** forgot which app or location a photo was saved from.
With these, explicit forgetting rises from 4 reviews to 6.

**3. Question 6 measures what users report, not what actually went wrong.** Reviews can't tell whether a failure came from matching, indexing, missing files or wrong metadata. Describe Q6 as "user-reported failures to match a clue", not "the app didn't understand".

**4. Counts are not prevalence.** These are counts from a selected set of reviews. They don't estimate how common a problem is among users, and one person can appear several times in a Reddit thread.

**5. Tip-of-the-tongue: neither established nor ruled out.** The reviews don't show it as a commonly reported state. That is a limit of the medium, not evidence against it.

**6. P516 is a feature request, not a failed search.** It still works as a quote about memory, but shouldn't be counted as a retrieval failure.

**7. Question 7 was defined too narrowly.** I only counted search results that were hard to judge (13% of searchers). Their broader reading includes inspecting any candidate set: wrong face groups, missing thumbnails, photos spread across folders. On that definition, inspection burden is larger than my number suggests.

**8. The problem isn't limited to old photos.** Recent downloads and photos taken minutes earlier also go missing. My fragmentation theme captures the cases, but I didn't state it as a finding under Q1.

**9. Utility retrieval starts from purpose or file type.** Their Q1/Q2 reading notes that utility images are recalled by why or how they were saved and by which app they came from, while memory photos start from a person, event, place or time. That matches the two-corpora research and should be stated from the reviews directly.

**10. Relevance should be shown as a range.** Their stricter filter gives 905 retrieval-relevant reviews; mine gives 1,001. The gap is mostly photos that exist but can't be located because of folders or backup state. Present it as 905–1,001 and say what the difference is.
