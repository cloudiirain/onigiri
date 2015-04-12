project onigiri
===============

A modern API/UI-centric aggregator site for light novel fan translations. The mission of this project is to make 
light novel translations more accessible on mobile platforms. It can be thought of as a fusion between Mangafox,
Baka-Tsuki, and Wordpress.

![Landing Page](http://i.imgur.com/NxIxbXR.png)

![Volume Detail Page](http://i.imgur.com/VGUupTf.png)

Key Features:
-------------
* English-only support

* A directory of light novel series, built in Django
    * Popularity rankings and ratings of light novel series
    * Category tags and searching
    * Chapter-by-chapter translations, either:
        * Links to external translations
        * Physically hosted translations
            * Translators have control over who has access to their scripts. They can opt to have them editable 
              to the world (like Baka-Tsuki), to specific friends (their editors), or private to themselves.
        * Note: Model needs to be able to resolve abnormal yet common situations, such as: 
            * Multiple versions of the same chapter translated by differen translators exist
            * Some translators translate by parts, not chapters (or put multiple chapters in one page)
    * Recent updates and RSS

* A hosting workspace for collaborating translators and editors (think google docs), built in Javascript
    * Translators have control over who has access to their scripts. They can opt to have them editable to the 
      world (like Baka-Tsuki), to specific friends (their editors), or private to themselves.
        * Translators should be able to control the visibility of their scripts (ie: private when it is a WIP and still
          being edited by their editor)
        * A "permit/licensing" system should be developed and clearly marked like it is on GitHub:
            * Open-source translations should be marked as such (free to distribute, change, and edit by anyone).
            * Whether other translators of other languages can use your translations to translate.
            * Whether a fan translation has all rights reserved (no derivative works, etc).
    * A sophisticated commenting system like that in google docs
        * Editors definitely need a good commenting system
        * It would be nice if readers could highlight a typo/error and submit a suggestion ticket to the translator
    * A sophisticated editor markup system like Microsoft Word's track changes. 
    * Currently deliberating: Real-time collaboration, translator-specific features like marking sentences for help.
    * Currently considering: [Etherpad](https://beta.etherpad.org/), [NYTimes-ICE](http://nytimes.github.io/ice/demo/) 

* An API for other developers to extend on:
    * Applications:
        * Android App, iOS, EPUB, MOBI, tablet, etc.
    * There should be no need to parse HTML
    * API will make it easy to determine when volumes or chapters are completed
    * API will make it easy to get the next chapter
        * Needs to be able to handle the situation where multiple versions of the same chapter are present

Dream Features (what I'd like to do):
-------------------------------------
* Multilingual support
* Fancy UI and user-friendliness
    * User-customizable backgrounds, fonts, styles, for online reading
    * Bookmarking for users
* Series-specific forums (Not pHpBB; integrated into web app)
* Translator/Translation Group-Oriented Features:
    * Customizable Translation Group Pages (like tumblr styling)
    * Journals/Blogs for translation groups
    * Private/Public forums for translation groups and their members
    * Statistics
* In short, the entire "community" section:
    * How can translators better help each other?
    * How can translators find editors more easily?
    * How can we make the fan translating community more effective and connected, but in a good way?

Why Am I Making an Aggregator?
==============================
I strongly believe that aggregators are the best way to spread the popularity of light novels
(and fan translations) in the English-speaking West. My mission statement, so to speak, is to
popularize light novels yet do it in an ethical, noncommercial, and responsible way.

There are three major features that I think are most important: 

1). The ability for readers to easily find new novels to read. Aggregators are best at this because
They keep rankings of what others find interesting, and have ways for readers to search based on 
certain categories. This is the most important role I'd like for an aggregator like this to fill.

2). Convenience. Users don't really like to travel across multiple links and be forced to read using
the UI chosen by each translation group (or be exposed to ads or distractions). Users should be able 
to read using the fonts that are easy on their eyes and with backgrounds they like.

3). HUGE: Portability. In my opinion the future of light novel translations will be for smartphones.
People *want* to download and read light novels on the bus, train, or airplane--when they're traveling
and don't necessarily have WI-FI or internet connection. The Baka-Reader app is one step in this
direction, but its selection is limited to only Baka-Tsuki projects. The goal for onigiri is to 
produce a (secure) environment that more translators would be willing to be post their translations to
without worrying about anons or other random individuals editing their manuscripts. 
Combined with an effective API, it's possible for us as a community to make portable fan-translations
possible.

What Do I Need to Make this Possible?
=====================================
* Developers willing to work with me (please contact me!). So far I've gotten interest from:
    * Lord-Simon
    * GJdan
    * Given Zane
* Someone willing to host the web application
    * Temporarily, I'll be able to put things on Heroku, but only while things stay small and not very noticeable  
* Someone willing to administrate it (b/c I'm just a developer here!). So far I've gotten interest from:
    * Frog-kun








