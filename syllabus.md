#JOUR491 An Introduction to Storybots#
**Fall 2014**  
**T/Th 2:30 p.m. - 3:45 p.m.**  
**228 Andersen Hall**  

Matt Waite, instructor
Email: mwaite3@unl.edu   
Twitter: @mattwaite   
IM: matt.waite on Gtalk, mdwnlz on Yahoo   
Phones: (402) 802-5202 cell, (402) 472-5840 office   
Office: 318 Andersen   

**Course description:**

On the morning of March 14, Ken Schwencke rolled out of bed, logged into the LA Times content management system and published a story about an earthquake that happened three minutes prior. 

This is interesting only in the particulars: Schwencke didn't write a word of the story - no human did. The story was written by a bot. Specifically, a bot programmed by Schwencke to write a story about earthquakes minutes after they happen, so the LA Times can have something on its website about it first, and faster than any human can do the job. All Schwencke had to do was check the story to see if the bot did its job and hit publish.

Welcome to the dawning days of storybots: programs that write stories so humans don't have to. Bots now write simple stories about softball games, corporate earnings reports, the weather and, yes, earthquakes. Some of them are extraordinarily simple -- basic programming knowledge is all that's required. Others are quite sophisticated -- they rely on more complex tools to arrive at a simple story. 

This course is going to take your journalism education and combine it with some programming knowledge to produce storybots. We'll discuss the ethics, the practicality, the limits, the nature of what it means to be human and we'll make a few storybots of our own. And then we're going to evaluate their performance. 

**Course goals:**

1. Explore how oft-derided formulaic writing can be exploited to create storybots.
2. Understand the true value of what it means to bring a human touch to stories.
3. Learn basic programming techniques to create your first storybots.
4. Run and evaluate your storybot on real world data.
5. Increase the complexity and develop a second storybot.
6. Deploy said storybots into the real world and evaluate its performance.
7. Have fun.

**Open lab hours:**

Each Friday throughout the semester, I run something called Maker Hours. It’s an open learning time where anyone who wants to learn about some digital tool or technology can come in and I’ll help. It’s in Room 27 from 1-5. You’re welcome to come learn something new outside of class, or bring your class stuff with you to get questions answered. 

**Required materials:**

* Assigned readings from the internet.
* A GitHub account.
* A laptop computer that you bring with you to class.
* Administrative rights to install software.
* An abundant sense of curiosity and no fear of failure.
* A sense of humor. 

**Grading:**

* Showing up. It’s mandatory and not only that, it’s a really good idea. We’re going to be moving very, very fast. Miss a class, get left behind.
* Participating. A lot of this class is going to be discussion. I want you to argue. I want you to tell me I’m full of it. Debate forms better ideas. Non-participation will be graded poorly.
* Doing. We’re going to build storybots. Plural. Getting your hands dirty reflects well on you. Avoiding work does not.

Do your work, hit your deadlines, mix it up in class and you’re probably going to get a good grade. Simple.

**Notes on attendance:**

Yes, we all get sick. Yes, things happen. I don’t want you to be sick in my class any more than you want to be sick. You’ve got no fewer than five ways to get ahold of me. If you are going to miss class, tell me before class. We’ll work it out. But you have to tell me before class for me to help you.

This said: this class builds each class onto the next one. Miss a class, especially a code class, and you are behind. You’re going to be covering a lot of new material in this class. Miss one at your own peril.

**The short version on policies regarding academic integrity, diversity and students with disabilities:**

You cheat, you fail, no exceptions. 

If I’m doing something that’s keeping you from learning, tell me. Tell the Dean. Tell someone, because that’s not cool. I won’t tolerate it from myself and you shouldn’t either.

Now, the longer versions:

**Academic integrity:**

Every student must adhere to the policy on academic integrity set forth in the UNL Student Code of Conduct as outlined in the UNL Bulletin. Students who plagiarize may receive a failing grade on an assignment or for an entire course and may be reported to the Student Judicial Review Board. The work a student submits in a class must be the student's own work and must be work completed for that particular class and assignment. Students wishing to build on an old project or work on a similar project in two classes must discuss this with both professors.

Academic dishonesty includes:

* handing in another's work or part of another's work as your own.
* turning in one of your old papers (including something you wrote in high school) for a current class.
* turning in the same or similar paper for two different classes,
using notes or other study aids or otherwise obtaining another's answers for a quiz or an examination.

Anything and everything you include in your papers that comes from another source must be attributed with proper citation. That includes ideas and opinions. 

Plagiarism consists of using phrases, sentences or paragraphs from any source and republishing them without alteration or attribution. The sources include, but are not limited to, books, magazines, newspapers, television or radio reports, Web sites and other students’ papers.

**Students with disabilities:**

Students with disabilities are encouraged to contact the instructor for a confidential discussion of their individual needs for academic accommodation. It is the policy of the University of Nebraska-Lincoln to provide flexible and individualized accommodation to students with documented disabilities that may affect their ability to fully participate in course activities or meet course requirements. To receive accommodation services, students must be registered with the Services for Students with Disabilities (SSD) office, 132 Canfield Administration, 472-3787 voice or TTY.

**Diversity:**

The College of Journalism and Mass Communications values diversity, in the broadest sense of the word – gender, age, race, ethnicity, nationality, income, religion, education, geographic, physical and mental ability or disability, sexual orientation. We recognize that understanding and incorporating diversity in the curriculum enables us to prepare our students for careers as professional communicators in a global society. As communicators, we understand that journalism, advertising and other forms of strategic communication must reflect society in order to be effective and reliable. We fail as journalists if we are not accurate in our written, spoken and visual reports; including diverse voices and perspectives improves our accuracy and truthfulness. In advertising, we cannot succeed if we do not understand the value of or know how to create advertising that reflects a diverse society and, thus, appeals to broader audiences.

##Class Schedule:##

A word of warning: This class is pretty fluid. I will move things up and back, depending on how well you’re getting things. If things change, I will update the syllabus on Blackboard and I will update the class blog.


###Aug. 26, 2014###

**In class:**

Introduction to Storybots

* What are they?
* What aren't they? 
* What are they good for?
* Limitations
* Technologies
* Examples

**Homework:**

Read: Selections from BotWeek:

[How to break news while you sleep.](https://source.opennews.org/en-US/articles/how-break-news-while-you-sleep/)  
[Bots with thought](https://source.opennews.org/en-US/articles/bots-with-thoughts/)  
[Bot or be botted](https://source.opennews.org/en-US/articles/bot-or-be-botted/)

###Aug. 28, 2014###

**In class:**

On the structure of data and journalism

* Data is everywhere.
* Structure in what we do.
* Combined they are powerful.

**Homework:**

Read: [Holovaty](http://www.holovaty.com/writing/fundamental-change/).

###Sept. 2, 2014###

**In class:**

Mad Libs, sentence structure and programming: Your first storybot

* Remember Mad Libs? Aww yeah.
* Introducing Python, the programming language of this course
* Variables and strings

**Homework:**

Write a Python script that creates a variable called "noun" and "verb" and print a sentence to the screen. 

###Sept. 4, 2014###

**In class:**

More Python, more Mad Libs

* Lists, loops and dictionaries
* Indexing in Python is a little weird at first.
* Your first assignment

**Homework:**

Write a Python script that completes the assigned Mad Lib. Due Tuesday.

###Sept. 9, 2014###

**In class:**

Even more Python, even more Mad Libs.

* Using lists to store information
* Random extraction from lists for use in Mad Libs.
* Using lists to generate multiple versions from the same sentence.

**Homework:**

Re-write your homework from over the weekend using lists of words for the nouns and verbs and randomly pull them from your lists. Run your Mad Lib generator three times. Compare each version. Did all of them "work", i.e. did your word choices make sense and did the sentence sound correct?

###Sept. 11, 2014###

**In class:**

Conditional language, conditional logic

* How we change a story based on thresholds
* How those thresholds can be used
* How conditional logic works in programming

**Homework:**

Time for a new Mad Lib. This time, we're going to change it based on conditional logic. Write a Python script that completes the assigned sentence, but changes the wording based on threshold's you decide.

###Sept. 16, 2014###

**In class:**

Case Study: Neighborhood Watch. We'll discuss the project, how it was created and conceived, and we'll critique it. 

**Homework:**

Read about Quakebot.

###Sept. 18, 2014###

**In class:**

Case study: Quakebot. Can we get Ken Schwencke up in this?

**Homework:**

Reaction paper: In 500 words, compare our Mad Lib game with Neighborhood Watch and/or Quakebot. How similar are they? How different? What ideas are opening up in your mind?

###Sept. 23, 2014###

**In class:**

Using a bot to write hundreds of stories, or, Matt is going to swear about crime trend stories.

* An introduction to the FBI's Uniform Crime Reports
* Examples of (bad) stories done using UCR data
* Can this be automated? How, conceptually?

**Homework:**

Write four sentences using data from one city in the UCR. 

###Sept. 25, 2014###

ONA Conference. No class. 

###Sept. 30, 2014###

**In class:**

More UCR story planning.

* We're going to read your four sentences and compare them.
* What is similar? What's different?
* What are the key pieces of information in each sentence?
* How can we bundle this together?

**Homework:**

Write a Python script that uses a list containing your data to complete your four sentences. 

###Oct. 2, 2014###

**In class:**

Write one, write them all. 

* Using loops, we're going to write several hundred stories.
* Combining list indexes, conditional logic and Mad Libs.

**Homework:**

Write your own UCR storybot. The storybot will need to have the data and the script together, because I'm going to run it myself and see if it works. We're going to compare them in class on Thursday.

###Oct. 7, 2014###

**In class:**

Evaluating our Storybots.

* The good, the bad and the ugly.
* What does this accomplish?
* What could go wrong?
* Should these stories be edited by a human before publication?

**Homework:**

Reaction paper: In no more than 500 words, describe what you see as the implications of what you've just done are. Did you just take someone's job? Did you serve the reader? Is this an admission that a lot of journalism is just boilerplate and boring?

###Oct. 9, 2014###

**In class:**

Intro to automated fetching from the internet.

**Homework:**

Your first scrape.

###Oct. 14, 2014###

**In class:**

More scraping

**Homework:**

###Oct. 16, 2014###

**In class:**

Combining scraping with bots: Intro to Twitter Bots

**Homework:**

Start working on your twitter bot over break

###Oct. 21, 2014###

**FALL BREAK: No Class**

###Oct. 23, 2014###

**In class:**

More on Twitter bots: Good and bad.

**Homework:**

Finish twitter bot

###Oct. 28, 2014###

**In class:**

Present our Twitter bots

**Homework:**

###Oct. 30, 2014###

**In class:**

**Homework:**

###Nov. 4, 2014###

**In class:**

**Homework:**

###Nov. 6, 2014###

**In class:**

**Homework:**

###Nov. 11, 2014###

**In class:**

**Homework:**

###Nov. 13, 2014###

**In class:**

**Homework:**

###Nov. 18, 2014###

**In class:**

**Homework:**

###Nov. 20, 2014###

**In class:**

**Homework:**

###Nov. 25, 2014###

**In class:**

**Homework:**

###Nov. 27, 2014###

Thanksgiving. No class.

###Dec. 2, 2014###

**In class:**

**Homework:**

###Dec. 4, 2014###

**In class:**

**Homework:**

###Dec. 9, 2014###

**In class:**

**Homework:**

###Dec. 11, 2014###

**In class:**

**Homework:**
