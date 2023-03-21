#Characters
define terumi = Character(_("Terumi"), color="#8aa38b")
define you = Character(_("You"), color="#1166ff")

#Images
image questboard = "no_image.png"
image rosette_pattern = "no_image.png"
image rosette_flower = "no_image.png"

label start:

label intro:
    #[Black Screen]
    scene bg black
    "Being an adventurer isn't a particularly glamorous job."
    "Despite what one might think it's not always glory and treasure, that's reserved for the truly powerful."
    
    #[Some generic locale BG]
    scene bg locale
    "Some of us are simple men and women who want to make a living doing what we do best."
    "Just like any other occupation."
    "And with any other occupation, you have co-workers."
    "Unlike my previous job…" #(Maybe just this kind of line can hint at kois also being isekai'd but we can keep them out if we don't want that)
    "We not only rely on each other to get work done, we literally leave our lives to one another."
    "But if there's one co-worker that I appreciate above everyone else."
    "It's not those who fight alongside me, it's not those who taught me my skills."
    "I am grateful for them yes..."
    "But..."

    scene bg black
    #[Black Screen]
    "It's the woman behind the desk that gives me direction."
    "From the first day I found myself having to fight for my life." # (Again, isekai hint, could be excluded)
    "To every day where I continue to live this new life."
    "She has always been there."
    #[Some Teru CG Where she's not looking at us, probably working]
    show terumi busy
    "Her name is Terumi."
    "She's been working hard as a guild receptionist ever since I met her."
    "The type of girl to spend more time than needed to ensure everyone is safe and happy."
    "For me she was a light in the dark."
    "Whenever I didn't know what to do, she gave me direction."
    "Quest or not."
    "So recently, I've been saving money in order to pay her back."
    "In my own little way."
    #[Guild Hall BG]
label intro_guild_hall:

    scene bg guild_hall
    "It’s a simple, sunny morning as I start my day."
    "And the guild hall is warm as always."
    "A gentle feeling of comfort washes over me despite the sounds shuffling footsteps, ringing bells and stamps on parchment."
    "It's simply a place where I feel safe."
    "I walk past many other adventurers towards the quest board to see what I can do for this day."
    #[Maybe an image of said board here]
    hide terumi
    show questboard:
        xalign 0.5
        yalign 0.5

    "Reading through the many posted notices, one catches my attention."
    "A small infestation of gelatinous cubes at a nearby forest needs to be driven off."
    "I think that'll do."
    "Taking the flyer, I make my way to the desk."
    #[Guild Hall CG]
    hide questboard
    "Just as I arrive, Terumi walks in."
    show terumi normal with move
    "With gentleness and grace, she sits down. Every movement flowing like the leaves caught in a river’s current."
    #[Terumi CG – Smiling]
    show terumi smile
    terumi "You're here early again, how diligent of you."
    you "The early bird gets the worm as they say"
    "I wish I could’ve said something less cliché."
    you "I’d like to take this quest please."
    terumi "Alright."
    "She sets down her bag onto the table and starts unpacking her things."
    #[Possibly a CG here that foreshadows a future plot point, the bag with either a rosette pattern on it or a rosette charm hanging off of it]
    show rosette_pattern:
        xalign 0.7
        yalign 0.5

    terumi "Adventurer registration please."
    "Despite saying only these professional words, I feel a warmth to them."
    "Even though they’re standard phrases said to everybody, it feels special."
    "It stirs something deep in my heart."
    "I hand over my papers and wait."
    #[Stamps and scribbling sfx]
    #play sound "stamps_and_scribbling.mp3"
    "After a few more moments of stamping and signing, Terumi places the completed forms down."
    terumi "Here you go, please be careful out there."
    "With those reassuring words, I take me leave."
    #[Teru Smile]
    show terumi smile
    "Not wanting to stare at her too much."
    #[Forest-y BG, maybe a ‘Later…’ text too]
    hide terumi

label intro_forest:
    scene bg forest
    "Later..."
    "Alright… that should be the last of them…"
    "It took longer than expected, but I finish my quest."
    "I feel satisfied and excited. Not only have I finished today’s work but I get to see her again."
    "But before that… maybe a little rest…"
    "Around here should be a nice little clearing…"
    #[shuffling sfx and transition to the eventual date spot]
    #play sound "shuffling.mp3"
    scene bg date_spot with dissolve
    "Ah, here it is."
    "I take a seat under the tree and watch the soft orange sunlight flicker and dance as it makes its way through the forest canopy."
    "My eyes subconsciously follow a particular flash of light lands upon an unfamiliar image."
    "A single almost golden flower dappled by sunset’s fleeting rays."
    "One I haven’t seen before but…"
    "It seemed familiar."
    "I fish around my knapsack for my Adventurer’s Handbook."
    "Leafing through the pages gives a satisfying sound until I reach the ‘plants’ section."
    #[CG of the flower up close]
    show rosette_flower:
        xalign 0.5
        yalign 0.5

    "Checking the characteristics of the flower and comparing it to the examples in the book, I finally discover what it is."
    "An “Eastern Gold Rose”."
    "Described as ‘A gentle and fragile type of rose that is said to be from a distant land yet to be explored.’"
    "‘The petals resemble a pin of honor bestowed upon those one finds important.’"

    return
