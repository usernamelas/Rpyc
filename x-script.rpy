define persistent.dialogueBoxOpacity = 1.0

label splashscreen:
    scene black with dissolve
    pause(0.2)
    $ renpy.sound.set_volume(0.5, channel='movie')
    $ renpy.movie_cutscene("gui/ntr_maniac.webm")

    scene warning with dissolve
    pause
    scene black with dissolve

    return

label start:
    scene black

    $ name = renpy.input("My name is", default = "Jake", length=15)
    $ persistent.name = name

    if name == "":
        $ mc = "Jake"
        $ mct = "Jake Tought"
        menu:
            "Are you sure about Jake?"
            "Yes":
                pause
            "No,Please.":

                pause



    $ fname = renpy.input("My wife's name is", default = "Emily", length=15)
    $ persistent.fname = fname

    if fname == "":
        $ em = "Emily"
        $ emt = "Emily Tought"

    if _in_replay:
        if persistent.name:
            $ mc = persistent.name
        if persistent.fname:
            $ em = persistent.fname


    scene st1 with fade

    pause

    scene st2 with dissolve

    pause

    scene st3 with dissolve

    pause

    scene st4 with dissolve

    pause

    em "I'll never get used to this."

    scene st5 with dissolve

    $ persistent.mc_unlock = True

    mc "I know babe, its really complicated. I can't believe it's been almost 1 year."

    scene st6 with dissolve

    mct "This is my loyal wife, [fname]. We have been married for 5 years. We really love each other. We were happy but after that incident our life became a mess."

    mct "End of 2026 a virus occurred. Every single women are dead due to this virus except [fname] and few ones. Now everyone wants to be with my wife. I can't decide if I'm lucky or unlucky."

    mct "But I know one thing we always love each other whatever happens."

    scene black with dissolve

    pause

    scene hm1 with fade

    mc "Honey, do you want to talk?"

    scene hm2 with dissolve

    pause

    scene hm2 with dissolve

    mc "I think we have to talk now. We cannot delay this conservation anymore."

    scene hm4 with dissolve

    em "I don't know what to do."

    scene hm3 with dissolve

    mc "We tried every single day even though we know the fact Im infertile. Humanity migh be end because of us and I feel guilty. If you try with someon..."

    scene hm4 with dissolve

    em "Babe, I cannot. I love you."

    scene hm5 with dissolve

    pause

    scene hm5 with dissolve

    anc "Only 5 of the 15 women who survived after the virus are able to give birth."

    scene hm6 with dissolve

    anc "Scientists are predicting a significant decline in the human population, which could potentially signal the end of humanity."

    scene hm7 with Dissolve(1.0)

    anc "The good news is that these four women made many sacrifices and became the saviors of humanity."

    scene hm8 with dissolve

    anc "Unfortunately, this is not enough."

    scene hm9 with dissolve

    anc "There is still no news from the women who lives in Knew-York City."

    scene hm10 with dissolve

    em "Honey..."

    scene hm11 with dissolve

    em "I will try. I have to..."

    scene hm12 with dissolve

    mc "We have to. I will never let you alone. I will always be with you."

    scene hm11 with dissolve

    em "Thanks honey. I cannot do this without you, What we gonna do now?"

    scene hm12 with dissolve

    mc "Only one person comes to my mind."

    scene hm11 with dissolve

    em "Who?"

    scene hm13 with dissolve

    mc "Ermm... Well..."

    scene hm14 with dissolve

    em "Spill the beans."

    scene hm15 with dissolve

    mc "Well. Andrew?"

    scene hm16 with dissolve

    em "B-but he is your best friend."

    scene hm15 with dissolve

    mc "That’s why I suggest him, Andrew is my homie who I can trust."

    scene hm17 with dissolve

    em "Well I’m really like Andrew but this is something different. Im not sure.."

    scene hm18 with dissolve

    mc "I know its hard for both of us. But we have to. Don’t worry Im not pushing you anything. We can move step by step until you feel okay."

    scene hm19 with dissolve

    em "Okay."

    scene hm19_5 with dissolve

    mc "Hey Andrew, I need you. Could you come immediately?"

    scene hm19_5 with dissolve

    mc "Yeah yeah, I'll explain when you arrive."

    scene hm20 with dissolve

    pause

    scene hm22 with dissolve

    mct "This is Andrew, my brother. We've been best buddies since we were five years old."

    mct "He's always had my back, especially when it came to dealing with bullies during my childhood. We've shared a strong bond ever since."

    mct "Andrew and [fname] get along pretty well too."

    scene hm21 with dissolve

    aw "What's the issue? Why did I need to come urgently?"

    $ persistent.aw_unlock = True

    scene hm22 with dissolve

    mc "U have to help us."

    scene hm21 with dissolve

    aw "Sure, about whaat?"

    scene hm23 with dissolve

    mc "There's no easy way to say this so I'll just say it directly. Get [fname] pregnant."

    scene hm24 with dissolve

    aw "What the fuuuck? Are you insane??"

    scene hm25 with dissolve

    mc "You know my health condition. We have to do this for sake of humanity."

    scene hm26 with dissolve

    aw "And are you okey with that?"

    scene hm27 with dissolve

    pause(0.5)

    scene hm28 with dissolve

    em "Yes."

    scene hm29 with dissolve

    aw "Dude, I'm not sure about that. I mean [fname] is perfectly perfect. I really want to fuc, Ermm, I mean help you and [fname]."

    aw "Are you sure this won't harm your relationship?"

    scene hm30 with dissolve

    mc "We already talk about that, nothing will effect our marriage. This is our duty, it is what it is. Right babe?"

    scene hm31 with dissolve

    em "Yes dear."

    scene hm32 with dissolve

    mc "So what are you saying dude? Are you in or out?"

    scene hm33 with dissolve

    aw "Im in."

    scene hm34 with dissolve

    em "I don’t wanna rush anything I already feel nervous."

    scene hm35 with dissolve

    mc "Don’t worry honey, I will always be with you."

    jump hj1

label hj1:
    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"






    scene hm36 with dissolve

    $ persistent.a_scene1_unlocked = True

    aw "So when do we do it? "

    menu:
        "Push [fname] to sex":

            $ ntr_point += 1

            scene hm37 with dissolve

            mc "Now... There is no need to wait. There's no point in prolonging it. Just do it."

            scene hm38 with dissolve

            em "Are you serious right now? GOSH! Didn't we talk about this?"

            scene hm39 with dissolve

            aw "Okay chill guys. Why don’t we take it slowly?"

            scene hm40 with dissolve

            aw "Let's get to know each other's bodies for now."

            scene hm41 with dissolve

            em "???"

            scene hm42 with dissolve

            em "How big is that thing?!"

            scene hm43 with dissolve

            mct "I cant imagine [fname] take all of it."

            scene hm44 with dissolve

            mct "Why is my heart beating faster? Why am I getting excited?"

            scene hm45 with dissolve

            pause(0.5)

            scene hm47 with dissolve

            pause(0.5)

            scene hm48 with dissolve

            pause

            scene hm49 with dissolve

            pause

            scene hm51 with dissolve

            em "Should I feel guilty for liking it?"

            scene hm50 with dissolve

            em "It barely fits in my hand."

            scene hm52 with dissolve

            aw "Oh really? You are the first girl who says that. Hahahah!"

            scene hm53 with dissolve

            mct "I can't believe I'm allowing this but we have to endure."

            scene hm53_5 with dissolve

            mct "I wonder how [fname] is feeling right now?"

            scene black with dissolve

            pause(0.01)

            scene hj1 with dissolve

            em "mmmm..."

            aw "Oh-hhh! Your hands are so small and soft."

            scene hj2 with dissolve

            em "hhh..."

            aw "Keep going..."

            scene hm54 with dissolve

            pause

            scene hm55 with dissolve

            mct "Shit!"

            scene hm57 with dissolve

            em "I think we should stop for today. It's a lot to take in."

            scene hm58_b with dissolve

            aw "Come on [fname]..."

            scene hm59_b with dissolve

            aw "We're already in this."

            scene hm60_b with dissolve

            aw "We can't just stop now. Maybe this will get you in the mood."

            scene hm61_b with dissolve

            pause

            scene hm62_b with dissolve

            pause

            scene hm64_b with dissolve

            mct "Holly! He literally put his penis between her legs. How will [fname] react to this?"

            mct "It's so exciting, I feel strange and really want to see what happens next. It looks like that big wet thing is inside [fname]."

            scene hm63_b with dissolve

            emt "He hugged me so tightly. I can't stop him from forcing me against him. There's something big between my legs."

            emt "I can feel its warmth and hardness as if I weren't wearing shorts. What is this wet feeling? Am I wet?"

            emt "Oh no. It's so embarrassing for [name] to see me like this. I don't want to go too fast. I have to stop it."

            em "STOP!!!"

            scene hm65_b with dissolve

            em "Andrew, please understand. This is overwhelming for me. I need time to process everything."

            scene hm66_b with dissolve

            aw "But we can't afford to wait. We have a responsibility here."

            scene hm67_b with dissolve

            em "No, Andrew. I said no."

            scene hm68_b with dissolve

            mc "We will continue however [fname] wants."

            scene hm69_b with dissolve

            aw "Fine, have it your way. But don't forget the purpose here."

            aw "I think I should leave now. I'll give you some space to process everything that's happened. Goodbye."

            $ renpy.end_replay()
        "Encourage [fname]":


            $ nts_point += 1

            scene hm37 with dissolve

            mc "I don't want [fname] to feel bad."

            scene hm38_a with dissolve

            mc "Let's proceed step by step. We have to start somewhere. Are you okay with Andrew being naked?"

            scene hm40 with dissolve

            aw "Why am I the only naked person in the room, [fname] you have to naked too."

            scene hm42_a with dissolve

            em "I don't feel comfortable yet."

            scene hm41_a with dissolve

            aw "Okay, but you gonna be naked eventually..."

            scene hm41 with dissolve

            em "???"

            scene hm42 with dissolve

            em "How big is that thing?!"

            scene hm43 with dissolve

            mct "I cant imagine [fname] take all of it."

            scene hm44 with dissolve

            mct "Why is my heart beating faster? Why am I getting excited?"

            scene hm45 with dissolve

            pause(0.5)

            scene hm47 with dissolve

            pause(0.5)

            scene hm48 with dissolve

            pause

            scene hm49 with dissolve

            pause

            scene hm51 with dissolve

            em "Should I feel guilty for liking it?"

            scene hm50 with dissolve

            em "It barely fits in my hand."

            scene hm52 with dissolve

            aw "Oh really? You are the first girl who says that. Hahahah!"

            scene hm53 with dissolve

            mct "I can't believe I'm allowing this but we have to endure."

            scene hm53_5 with dissolve

            mct "I wonder how [fname] is feeling right now?"

            scene black with dissolve

            pause(0.01)

            scene hj1 with dissolve

            em "mmmm..."

            aw "Oh-hhh! Your hands are so small and soft."

            scene hj2 with dissolve

            em "hhh..."

            aw "Keep going..."

            scene hm54 with dissolve

            pause

            scene hm55 with dissolve

            mct "Shit!"

            scene hm57 with dissolve

            em "I think we should stop for today. It's a lot to take in."

            scene hm67 with dissolve

            aw "Yeah, it's intense. We don't need to rush this."

            scene hm68 with dissolve

            mc "Absolutely, let's take it slow. We're all in this together, there's no need to push ourselves too hard."

            scene hm67_b with dissolve

            em "Thank you. I just need some time to process everything."

            scene hm69 with dissolve

            aw "Of course, [fname]. We'll go at your pace. "

            scene hm70 with dissolve

            mc "Let's sit and talk for a bit. We can figure out the best way to handle this moving forward."

            scene hm71 with dissolve

            aw "I think it's best if I leave now. I'll give you some space to process what happened. You should sit and talk. Goodbye."

            scene hm67_b with dissolve

            em "Wait before you go…"

            scene hm73 with dissolve

            pause

            aw "Oh!"

            scene hm74 with dissolve

            pause

            scene hm75 with dissolve

            pause

            aw "Damn!!!"

            scene hm72 with dissolve

            em "You can say a thank you kiss or next time gift... Goodbye."

            scene hm71 with dissolve

            aw "Okay… I- I guess now that I've got my gift, I should get going."

            $ renpy.end_replay()


    scene hm76 with fade

    mc "That was... intense."

    scene hm77 with dissolve

    em "Yeah, I can't believe we actually went through with it."

    scene hm76 with dissolve

    mc "I know. It's so surreal. I feel like we're in some kind of bizarre nightmare."

    scene hm78 with dissolve

    em "Do you think we did the right thing?"

    scene hm76 with dissolve

    mc "I don't know. But what choice do we have? It's not just about us anymore. It's about humanity."

    scene hm79 with dissolve

    em "I get that, but... it still feels so wrong. I mean, we love each other, and now we're involving someone else in something so personal."

    scene hm76 with dissolve

    mc "I feel the same way. It's humiliating, but... we have to try, right?"

    scene hm77 with dissolve

    em "Yeah, I guess so. I just never imagined our life would turn out like this."

    scene hm76 with dissolve

    mc "Neither did I. But whatever happens, we'll face it together. You're not alone in this."

    scene hm80 with dissolve

    em "Thank you. I really need that right now. It's just so overwhelming."

    scene hm81 with dissolve

    mc "I know, babe. We'll get through this."

    scene hm80 with dissolve

    em "You're right. We'll get through this. Together."

    scene hm81 with dissolve

    mc "Together..."

    scene hm82 with dissolve

    mct "As I hold her close, a familiar scent hits me. Semen."

    mct "The remnants of what just happened. To my surprise, it arouses me."

    mct "My body responds despite my mind's confusion and guilt."

    scene hm83 with dissolve

    mct "Oh no, not now. I can't let her notice."

    scene hm84 with dissolve

    em "I feel so ashamed and guilty for saying this, but... I'm really horny right now. Can we go to our bedroom?"

    scene hm85 with dissolve

    mc "Really? I mean, I - sure, if that's what you want."

    scene hm86 with dissolve

    mct "So, [fname] was affected by what just happened too. After all, she's a woman."

    scene hm87 with dissolve

    mc "Hey, it's okay. We can go to the bedroom. There's nothing to be ashamed of. We're in this together, remember?"

    scene hm84 with dissolve

    em "Thank you. I just need to feel close to you right now."

    scene hm85 with dissolve

    mc "I know babe but how about this? There's an erotic cinema I remember from back in the day. It could be a fun distraction and help us shake off the weirdness from earlier. What do you think?"

    scene hm88 with dissolve

    em "Really? That sounds... interesting. Let's do it!"

    scene hm89 with dissolve

    mc "Alright then, let's hurry up and go before the cinema closes."

    scene hm90 with dissolve

    pause

    scene cs1 with dissolve

    em "I've thought about it again. Are you sure the cinema is safe for me? I'm a bit concerned."

    scene cs2 with dissolve

    mc "Don’t worry, babe. I know the owner and we have a good history. We can trust him to give us a nice, private place."

    scene cs3 with dissolve

    mc "Besides we have them to protect us."

    scene cs3_5 with dissolve

    pause

    scene cs4 with dissolve

    em "I sometimes forget they're around, but I don't trust them. Do you think they'll treat us the same way when our government agreement ends?"

    scene cs5 with dissolve

    mc "Can you please stop!"

    scene cs6 with dissolve

    mc "Sorry, [fname]. We don’t need to worry about that right now. Let’s just have a good time."

    scene cs7 with dissolve

    em "Right. There's no point in thinking about this right now. We're here to relax, so let’s head inside."

    scene ch1 with fade

    $ persistent.jm_unlock = True

    jm "Hey, buddy. Welcome! I’ve been expecting you."

    scene ch2 with dissolve

    mc "Hey. Thanks for setting up the room for us so quickly. Sorry for calling at the last minute."

    scene ch3 with dissolve

    jm "No worries, man. I always have a room for you, anytime. Just give me a call, and I’ll make sure to have a spot ready for you."

    jm "If needed, I’ll even close down one of my salons so you two can have some privacy."

    scene ch4 with dissolve

    mct "This is James, the owner of the adult theater. Years ago, Andrew and I used to come here. Sometimes, he’d set up a private room just for us and our girlfriends."

    mct "James has looked out for us more times than I can count. He’d even loan us money when we were short."

    mct "But over time, we lost touch. The last time we saw each other was when we went to offer our condolences after he lost his wife."

    scene ch5 with dissolve

    mc "Thanks, James."

    scene ch6 with dissolve

    jm "It's an honor to meet your wife. I must say, you have a very beautiful and elegant lady."

    scene ch7 with dissolve

    em "Thank you so much, James. It’s a pleasure to meet you too."

    scene ch8 with dissolve

    jm "Well then, go on inside and make yourselves at home. Enjoy!"

    scene ch9 with dissolve

    mc "Thanks, James."

    em "Thanks"

    scene cs7_1 with fade

    pause

    scene cs7_2 with dissolve

    em "Wow. This place is much cleaner and… nicer than I expected!"

    scene cs7_3 with dissolve

    mc "Premium quality."

    scene cs7_4 with dissolve

    mc "Let’s take a seat."

    scene cs7_5 with dissolve

    em "I want to get this off."

    scene cs8 with dissolve

    pause

    scene cs8_5 with dissolve

    em "Mmm..."

    scene cs9 with dissolve

    em "Hhh..."

    scene cs10 with dissolve

    mct "She’s so wet, and I haven’t even started yet. I know what happened at home turns [fname] on even more, but it’s weird that she is still in the mood."

    mct "I like this version of [fname], but I can’t help wondering if it's Andrew's influence."

    scene cs11 with dissolve

    em "Calm down, horny boy."

    scene cs12 with dissolve

    em "If we were gonna move this fast, we could've just stayed home."

    scene cs12_5 with dissolve

    mc "I know doing it in public turns you on even more."

    scene cs12_6 with dissolve

    mc "Come here."

    scene cs13 with dissolve

    em "Someone knows how to please his wife. Good boy."

    mc "It’s my duty and the duty calls me."

    scene cs13_1 with dissolve

    em "Lie."

    em "Down."

    scene cs13_2 with dissolve

    mc "Yes, ma’am."

    scene cs13_3 with dissolve

    pause

    jump cinema

label cinema:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"

    $ persistent.b_scene1_unlocked = True

    scene black with dissolve

    pause(0.01)

    scene rc1 with dissolve

    mc "You are so wet."

    em "Because of your dick, handsome."

    scene rc2 with dissolve

    mc "You are getting tighter..."

    em "Ahhh...."

    scene cs14 with dissolve

    jmt "I need to get closer."

    scene cs15 with dissolve

    jmt "What a pink hole."

    jmt "I want to lick it."

    scene cs16_5 with dissolve

    jm "*Slurp*"

    scene cs16 with dissolve

    jmt "Let's see if you can take the tip of my finger."

    scene cs17 with dissolve

    pause

    scene cs18 with dissolve

    pause

    scene cs19 with dissolve

    em "Mmm.. Ah!!"

    scene cs20 with dissolve

    em "Oh!! Honey That’s new."

    mct "I don’t know what she is talking about, but I don’t want to ruin the mood by asking questions."

    scene cs21 with dissolve

    jmt "Now, let's see if we can widen your hole a bit."

    scene cs22 with dissolve

    em "Ahh, that hurts!"

    scene cs23 with dissolve

    em "Mmm,harder!"

    scene cs23_5 with dissolve

    em "[name], do it harder!"

    scene hm44 with eye_shut

    mct "What's this now? I don't want to remember this right now."

    scene hm48 with dissolve

    mct "Shit! I can't control my thoughts. Remembering these things feels really…"

    mct "really different..."

    scene cs23 with eye_open

    em "Mmm..."

    scene hm51 with eye_shut

    emt "It was…"

    emt "Huge."

    emt "It felt like it was from another world."

    scene hm52 with dissolve

    emt "If it were inside me right now, it would have shattered me. I think I can only take the tip of it."

    emt "Ahhh… Shit. Don’t think about this right now, don’t think about this right now, [fname]!"

    scene cs24 with eye_open

    em "Hhh.."

    scene cs25 with dissolve

    "*Sniff*-*Sniff*"

    scene cs26 with dissolve

    jmt "I have to leave for now."

    scene cs27 with dissolve

    jmt "But soon, the thing that goes in there will be my tongue."

    scene black with dissolve

    pause(0.01)

    scene rc2 with dissolve

    em "*Heavily Breathing* Ahhh... *Heavily Breathing*"

    mc "*Heavily Breathing* I am gonna cum. *Heavily Breathing*"

    em "*Heavily Breathing* Cum inside me. *Heavily Breathing*"

    scene cs28 with dissolve

    em "*(Screams)*Ahh!!"

    scene cs29 with dissolve

    mc "*Ohh-hhh!!!*"

    scene cs30 with dissolve

    pause

    scene cs13_1 with dissolve

    em "[name]. This was so... so good. Ahh… *Heavily Breathing*"

    scene cs13_2 with dissolve

    mc "I love your warm and tight pussy. Ohh. *Heavily Breathing*"

    scene cs13_3 with dissolve

    pause

    scene cs13_5 with dissolve

    em "I am so tired, I need to recharge for tomorrow. Let's go home, babe."

    scene cs13_2 with dissolve

    mc "Okay, baby."

    $ renpy.end_replay()

    scene ch10 with fade

    jm "Hello, our lovely young couple!"

    scene ch11 with dissolve

    mc "Thanks for everything James."

    scene ch12 with dissolve

    jm "No need to thank me; after all, I’m serving humanity. I’ll always be here for you guys."

    jm "Next week, a new movie is coming out. And guess who the star is? You’ll never guess."

    scene ch13 with dissolve

    jm "Sharlet Moansson!"

    scene ch14 with dissolve

    em "Is she alive??"

    mc "Really?! Is she still alive and starring in adult films?"

    scene ch15 with dissolve

    jm "Hahahah. You wish. I mean we all wish."

    jm "This movie is made with AI, I mean, only the parts with her are animated. Everyone else is real, except her."

    scene ch16 with dissolve

    em "[name]! We need to go next week. I really want to see what she looks like."

    scene ch17 with dissolve

    jm "Even if [name] can't make it, I'll definitely be waiting for you!"

    scene ch18 with dissolve

    mc "Don’t worry, I’ll be coming with her too. Anyway, we have to go now. See you."

    em "Bye, James..."

    scene ch19 with dissolve

    pause

    scene ch20 with dissolve

    jm "*Sniff*"

    scene ch21 with dissolve

    jm "Hmm..."

    scene ch22 with dissolve

    jm "Delicious."

    scene cs4 with fade

    em "Darling, there’s something bothering me."

    scene cs4_5 with dissolve

    mc "Did something happen?"

    scene cs4_6 with dissolve

    em "Don’t you think James' attitude changed after the movie?"

    scene cs4_5 with dissolve

    mc "What do you mean?"

    scene cs4_6 with dissolve

    em "I don’t know, it’s like the way he looked at me was different. Like he was eyeing me up."

    scene cs4_5 with dissolve

    mc "Yeah, you might be right. You’re the only woman he’s seen in a long time, so he might have acted a bit strange."

    mc "But James is a good guy. And besides, I’m here with you."

    scene cs4_6 with dissolve

    em "Even if that’s not the case, I’ve decided I don’t want to think about it right now. We have work tomorrow; we need to get ready. Let’s just get home, take a shower, and sleep."

    scene cs4_5 with fade

    mc "I really need that too."

    scene pass1 with dissolve

    pause

    scene hd1 with dissolve

    mc "Still not dressed?"

    scene hd2 with dissolve

    em "I am dressed already."

    scene hd3 with dissolve

    mc "Isn't Theo coming today?"

    scene hd2 with dissolve

    em "Yes, he is."

    scene hd1_5 with fade:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.0

    pause

    scene hd3 with dissolve

    mc "Isn't your outfit a bit revealing?"

    scene hd4 with dissolve

    em "Hahahahah."

    scene hd4_5 with dissolve

    em "He’s just a kid."

    scene hd5 with dissolve

    mc "Kid?! He’s 18, and you know what boys that age are like."

    mc "Their hormones are through the roof, and you’re the only woman he sees."

    scene hd7 with dissolve

    "KNOCK!KNOCK!KNOCK!"

    scene hd6 with dissolve

    em "Act normal, please."

    scene hd8 with dissolve

    pause

    scene hd9 with fade:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.0

    pause

    scene hd10 with dissolve

    $ persistent.th_unlock = True

    em "Welcome Theo!"

    scene hd11 with dissolve

    th "Hey, [fname]."

    scene hd12 with dissolve

    mc "Whats up buddy?"

    scene hd13 with dissolve

    th "Im good Mr…"

    scene hd14 with dissolve

    mc "Just call me [name]."

    scene hd15 with dissolve

    th "Okay. Thanks [name]!"

    scene hd16 with dissolve

    em "Alright, enough talking. Let's get started."

    scene hd17 with dissolve

    em "Let’s see what we’re working on today!"

    scene hd18 with dissolve

    th "Derivative..."

    scene hd19 with dissolve

    em "Again?!"

    scene hd20 with dissolve

    th "Yes."

    scene hd21 with dissolve

    em "Oh honey, Im sorry. We can handle it. Don’t worry."

    scene hd21_5 with dissolve

    pause

    scene hd22 with dissolve

    mct "Kid huh?"



    menu:
        "Stop Theo":

            $ stp_th += 1

            $ nts_point += 1

            scene hd23_a with dissolve

            mc "Hey Theo!"

            scene hd24_a with dissolve

            th "Hhh-uhh?"

            scene hd25_a with dissolve

            mc "I don’t remember ever seeing you this focused."

            scene hd26_a with dissolve

            th "Well-Y-Yess... I have to pass."

            scene hd27_a with dissolve

            mc "I'm running late for work. I need to leave now. Good luck with your studying!"

            scene hd28_a with dissolve

            mc "Bye honey, bye Theo."

            em "Bye, babe."

            th "Bye, [name]."

            scene pass2 with dissolve

            pause

            jump path_a
        "Let Him Enjoy The View":


            $ ntr_point += 1

            scene hd23_b with dissolve

            mct "He's going to pass out from staring."

            mct "Who wouldn’t stare if they were in his place?"

            mct "I’m curious, will [fname] notice too?"

            scene hd27_a with dissolve

            mc "I'm running late for work. I need to leave now. Good luck with your studying!"

            scene hd28_a with dissolve

            mc "Bye honey, bye Theo."

            em "Bye, babe."

            th "Bye, [name]."

            scene pass2 with dissolve

            pause

            jump path_b



label path_a:

    scene r1 with fade

    mc "I’m so tired today. It’s nice to finally be home with you."

    mc "How was your study?"

    scene r2 with dissolve

    em "It was good. I love teaching Theo."

    em "It reminds me of the days when I was a teacher, so I feel so happy when he comes over."

    scene r3 with dissolve

    mc "I love seeing you happy."

    scene r4 with dissolve

    em "Aww, you are cutie."

    em "Oh, did I mention that Theo will be coming more often now? He’s still struggling a bit."

    scene r5_a with dissolve

    mc "I can guess the reason. His focus definitely wasn’t on his studies."

    scene r6_a with dissolve

    em "What do you mean?"

    scene r7_a with dissolve

    mc "It seemed like he was more interested in your boobs than the lesson."

    scene r8_a with dissolve

    em "Really?? I didn’t realize."

    scene r9_a with dissolve

    mc "Well, he’s not a kid anymore. He’s young and healthy."

    mc "If the world were as it used to be, he could even have a child."

    scene r10_a with dissolve

    mc "I was thinking--"

    scene r11_a with dissolve

    em "Yes?"

    scene r10_a with dissolve

    mc "Should we have a backup plan besides Andrew?"

    scene r12_a with dissolve

    em "With Theo?!"

    scene r13_a with dissolve

    mc "He's young, and his sperm should be healthy. Our chances of success could be high."

    scene r14_a with dissolve

    em "You have a point, but... I don’t know babe."

    em "Actually, it does make me a bit sad that he'll never be with women. Maybe this way, I can ease my conscience as well."

    scene r15_a with dissolve

    mc "I don't like it either, but once we have a baby, we’ll be free."

    jump dream

label path_b:

    scene r1 with fade

    mc "I’m so tired today. It’s nice to finally be home with you."

    mc "How was your study?"

    scene r2 with dissolve

    em "It was good. I love teaching Theo."

    em "It reminds me of the days when I was a teacher, so I feel so happy when he comes over."

    scene r3 with dissolve

    mc "I love seeing you happy."

    scene r4 with dissolve

    em "Aww, you are cutie."

    em "Oh, did I mention that Theo will be coming more often now? He’s still struggling a bit."

    scene r5_a with dissolve

    mc "I can guess the reason. His focus definitely wasn’t on his studies."

    scene r6_a with dissolve

    em "I guess it’s because of me. You were right."

    scene r7_a with dissolve

    mc "I told you he’s not a child."

    scene r8_b with dissolve

    mc "You’re like the naughty teachers in porn with that kind of theme."

    scene r8_b1 with dissolve

    em "Hahahahah"

    scene r8_a with dissolve

    em "Actually, when I saw Theo watching me today, I felt sorry for him..."

    em "and kept thinking about it throughout the lesson."

    scene r9_a with dissolve

    mc "What did you think about?"

    scene r11_a with dissolve

    em "About the baby situation. I mean..."

    em "I know we’re going to try with Andrew, but having a backup plan would be good."

    scene r8_a with dissolve

    mct "Hearing this from [fname] surprised me."

    mct "It seems like she’s becoming more and more comfortable with it."

    mct "I know she’s suggesting this for our future, but still..."

    scene r12_a with dissolve

    em "So..What do you think about this?"

    scene r13_a with dissolve

    mc "As long as you’re okay with it, I have no problem."

    mc "I know you’re suggesting this for our future. I trust you and love you."

    scene r13_b with dissolve

    em "Me too babe."

    scene r16_a with dissolve

    pause

    jump dream

label dream:

    $ persistent.d_scene1_unlock = True

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"


    scene dr1 with fade

    pause

    scene dr2 with dissolve

    unk "*(Moans)*"

    scene dr3 with dissolve

    mct "What are those noises?"

    scene dr4 with dissolve

    unk2 "You’re the best teacher in the world. I no longer have any issues with derivatives."

    unk "Mmm... *Slurp* *-Lurp* *Rp*"

    unk "I’m ready to do whatever you need to help you focus."

    scene dr5 with dissolve

    mct "WTF?? I must be misunderstanding this."

    scene black with dissolve

    pause(0.01)

    scene bj1 with dissolve

    pause

    scene dr7 with dissolve

    em "Mmmmm...."

    mc "What the fuck?!"

    scene dr8 with dissolve

    em "Don't worry, honey. I'm just helping him with derivatives."

    scene dr9 with fade

    th "I need to get inside you, I can't hold back any longer."

    scene dr10 with dissolve

    em "Come on, take my derivative already."

    menu:
        "Just Watch":

            $ nts_point += 1

            scene dr11 with dissolve

            mct "It was going to happen sooner or later anyway. I might as well enjoy it."

            scene dr11_a with dissolve

            em "Mmm... Please put it in slowly, Theo."

            mct "Holly..."
        "Try to Stop":


            $ ntr_point += 1

            scene dr11 with dissolve

            mct "Okay, it was going to happen sooner or later, but I didn’t want it to be done behind my back like this."

            scene dr11_b with dissolve

            mc "WTF?! [fname]! STOP THIS!"


    scene black with dissolve

    "KNOCK!KNOCK!KNOCK!"

    scene dr12 with dissolve

    pause

    scene dr13 with dissolve

    mc "Gosh! This was so real."

    $ renpy.end_replay()

    scene black with dissolve

    pause

    scene nm1 with dissolve

    unk2 "Hey [fname]... Ops.. Did I come early?"

    scene nm1 with dissolve

    em "No, no, come in. I just got back from tennis and was doing some relaxation exercises. Just give me 5 minutes, okay?"

    scene nm1 with dissolve

    unk "Okay..."

    scene nm2 with dissolve

    mc "Who is this?"

    mc "Oh… Theo was supposed to come over today. I don’t have any work, so I can hang out with them. Let get dressed and head over."

    scene nm3 with dissolve

    em "Why are you standing? Have a sit, honey."

    scene nm4 with dissolve

    th "I'm good, thanks."

    scene nm5 with dissolve

    em "Oh, you’re awake, baby. Is something wrong? Are you feeling sick?"

    scene nm6 with dissolve

    mc "Hey! Yeah, I’m Okay. I had a dream, and I think I’m still affected by it."

    scene nm7 with dissolve

    em "Was it a bad dream?"

    menu:
        "Yes":


            $ ntr_point += 1

            scene nm8 with dissolve

            mc "I think it was... Do you have study today?"

            jump theo_cm
        "No":


            $ nts_point += 1

            scene nm8 with dissolve

            mc "To be honest, it was an exciting dream. Do you have study today?"

            jump theo_cm

label theo_cm:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"

    $ persistent.d_scene2_unlock = True

    scene nm9 with dissolve

    em "Yeah, silly, I told you that yesterday. Did you forget? Anyway, don’t distract me; I need to finish these exercises."

    scene nm10 with dissolve

    pause

    scene nm11 with dissolve

    pause

    scene nm12 with dissolve

    pause

    if stp_th == 1:

        scene nm12 with dissolve

        mct "Am I seeing this wrong, or is [fname] intentionally teasing Theo? It seems that she has accepted what I suggested yesterday."
    else:


        scene nm12 with dissolve

        mct "Is [fname] already putting the plan she suggested to me yesterday into action? I'm surprised by how eager she is."

    scene nm13 with dissolve

    em "I can't stretch enough. I need help."

    menu:
        "Offer your help.":

            $ ofr_mc += 1

            $ ntr_point += 1

            scene nm14_a with dissolve

            mc "Let me help you, love."

            scene nm15_a with dissolve

            em "I'm not sure you can do it exactly right."

            scene nm16_a with dissolve

            em "Theo! You are into sports,right? Can you help me?"

            mc "I know we have a plan with Theo, but did she really need to say I couldn't manage it."

            scene nm15_b with dissolve

            th "Oh.. Okay.. Are you sure?"

            scene nm16_b with dissolve

            em "After all, you've been playing basketball since you were a kid. You must know some tricks."

            scene nm17_b with dissolve

            mct "I think [fname] wants to make this process enjoyable and include me in the game. I'm getting excited..."

            scene nm18_b with dissolve

            pause

            scene nm19_b with dissolve

            em "Come on, Theo, aren’t you going to help?"

            th "O-Okay. I-I’ll do it..."

            scene nm20_b with dissolve

            pause

            scene nm21 with dissolve

            tht "Oh! Shit. I have a boner. I hope [fname] doesn't notice this."

            scene nm22 with dissolve

            emt "What?"

            emt "How did he get hard already? I haven’t even done anything yet!"

            scene nm23 with dissolve

            emt "Well.. He managed to rub it right in the spot."

            scene nm24 with dissolve

            mct "There's no doubt this is more than just helping with stretching exercises."

            scene nm25 with dissolve

            em "I feel much better now! Thanks for your help. Let’s crush these derivatives."

            scene nm26 with dissolve

            th "O-Okay…"

            scene nm25 with dissolve

            mct "Well, well... looks like someone has a boner."

            $ renpy.end_replay()
        "Suggest Theo to help.":



            $ nts_point += 1

            $ sgt_th += 1

            scene nm14_b with dissolve

            mc "Theo, why aren’t you helping?"

            scene nm15_b with dissolve

            th "Oh.. Okay.. Are you sure?"

            scene nm16_b with dissolve

            em "After all, you've been playing basketball since you were a kid. You must know some tricks."

            scene nm17_b with dissolve

            mct "I think [fname] wants to make this process enjoyable and include me in the game. I'm getting excited..."

            scene nm18_a with dissolve

            pause 

            scene nm19_b with dissolve

            em "Come on, Theo, aren’t you going to help?"

            th "O-Okay. I-I’ll do it..."

            scene nm20_b with dissolve

            pause

            scene nm21 with dissolve

            tht "Oh! Shit. I have a boner. I hope [fname] doesn't notice this."

            scene nm22 with dissolve

            emt "What?"

            emt "How did he get hard already? I haven’t even done anything yet!"

            scene nm23 with dissolve

            emt "Well.. He managed to rub it right in the spot."

            scene nm24 with dissolve

            mct "There's no doubt this is more than just helping with stretching exercises."

            scene nm25 with dissolve

            em "I feel much better now! Thanks for your help. Let’s crush these derivatives."

            scene nm26 with dissolve

            th "O-Okay…"

            scene nm25 with dissolve

            mct "Well, well... looks like someone has a boner."

            $ renpy.end_replay()

    scene nm27 with fade

    th "I am done with assignments you gave me yesterday!"

    scene nm28 with dissolve

    pause

    scene nm29 with dissolve

    em "I think…"

    scene nm30 with eye_open

    em "I’ll reward you for that."

    scene nm31 with eye_shut

    pause (2.0)

    scene nm32 with eye_open

    th "Tha..Thanks. You don’t need to get me a gift. "

    scene nm33 with dissolve

    pause

    scene chl with dissolve

    pause



    if sgt_th == 1:

        scene a1 with dissolve

        mc "You're not mad that I brought up the idea about Theo right away, are you?"

        scene a2 with dissolve

        em "No! Actually, it was really fun. I felt super hot teasing him like that."

        scene a3 with dissolve

        mc "Hahaha. Seeing you like that was kinda weird, but... I guess I liked it"

        scene a4 with dissolve

        em "This is something new for our relationship... I have to admit, I liked it too. But I still feel weird, babe."

        em "When all of this started, I thought everything would be so hard, but with you, everything feels easier. I love you, babe."

        scene a6 with dissolve

        mc "I love you too, more than you could ever know."

    if ofr_mc == 1:


        scene a2 with dissolve

        em "I have to admit, this was a really different experience. I felt super hot teasing him like that."

        em "Theo got an erection without me doing anything. It amused me to put him in an awkward position."

        scene a1 with dissolve

        mc "Seeing you like that excited me, but you really didn’t have to do that."

        scene a4 with dissolve

        em "What are you talking about?"

        scene a1 with dissolve

        mc "I'm talking about you saying I wouldn't be able to do it."

        scene a4 with dissolve

        em "I was putting the plan we talked about yesterday into action. We made a decision, and I just did it to get things started."

        em "You know I love you, [name]. I thought you wanted this too."

        scene a1 with dissolve

        mc "I want to..."

        mc "I just..."

        mc "I guess you're right. It was our mutual decision. You just caught me off guard."

        scene a6 with dissolve

        mc "And I love you too, honey."

    scene 5m with dissolve

    pause

    scene at1 with dissolve

    "*-RING!! RING!! RING!!-"

    scene at2 with dissolve

    pause

    scene at2 with dissolve

    mct "Oh. It's Andrew."

    scene at3 with dissolve

    aw "Hey, how’s it going? We haven’t talked since that day."

    aw "I don’t want to make things awkward, but I gotta ask—have you decided to back out?"

    scene at4 with dissolve

    mc "No, we haven't backed out; we were just processing what happened. Actually, I was going to call you today. Are you down for another the next step?"

    scene at3 with dissolve

    aw "I am busy a bit right now, but... Okay, I'm on my way!"

    scene at4 with dissolve

    mc "Okay,dude."

    scene at5 with dissolve

    mc "He is coming."

    scene at6 with dissolve

    em "Having a few days go by has been good. I feel a lot more relaxed now."

    scene at5 with dissolve

    mc "I can see that you're more relaxed now, and that..."

    menu:
        "Worries me":

            $ ntr_point += 1

            scene at6_a with dissolve

            mc "I can't help but worry—what if this affects our relationship? What if you start developing feelings for Andrew?"

            scene at7_a with dissolve

            em "Don’t be silly! I love you. None of this is going to change anything between us"
        "Comforts me":


            $ nts_point += 1

            scene at6_b with dissolve

            mc "I know the situation is weird, but I’m happy that I don’t see you stressed anymore."

            scene at7_b with dissolve

            em "I believe in our love. No matter what happens, we’re in this together."

    scene at8 with dissolve

    em "I'm gonna have a glass or two of wine before Andrew gets here. Do you want too?"

    scene at9 with dissolve

    mc "No, thanks honey."

    scene at9_5 with dissolve

    pause

    scene oneh with dissolve

    pause

    scene rt1 with dissolve

    aw "Hey, dude! Ready for round two?"

    scene rt2 with dissolve

    pause

    scene rt3 with dissolve

    aw "Just a joke, man. Chill."

    scene rt4 with dissolve

    mc "We’re doing this for a reason, remember?"

    scene rt5 with dissolve

    aw "Okay,okay... Let's not keep [fname] waiting."

    scene rt6 with dissolve

    aw "Whoa, you look amazing today!"

    scene rt7 with dissolve

    em "Hey, Andrew!"

    scene rt8 with dissolve

    em "Just today?"

    scene rt9 with dissolve

    aw "Hahaha. I thought you’d be as tense as last time."

    scene rt10 with dissolve

    em "I'm getting used to it."

    scene rt11 with dissolve

    aw "So, are you ready for the next step?"

    mct "I think it might be better if I stay a bit quiet, that way the atmosphere won't be so awkward."

    scene rt12 with dissolve

    em "I guess..."

    mct "Yeah, we guess..."

    scene rt13 with dissolve

    aw "Are you gonna take your clothes off this time?"

    scene rt14 with dissolve

    em "Well, not so fast. I can touch you like last time."

    scene rt15 with dissolve

    aw "Oh man... Okay, then."

    scene rt16 with dissolve

    aw "You are the boss."

    scene rt17 with dissolve

    mct "I wonder what [fname] thinks right now. "

    mct "This time, I’ll step back a bit. Let’s see how things progress."

    scene rt18 with dissolve

    pause

    scene rt19 with dissolve

    aw "Wait."

    scene rt20 with dissolve

    aw "Now… Better. Let’s move on [fname]."

    scene rt21 with dissolve

    emt "I said I was getting used to it, but when I saw that huge thing, I changed my mind. How could any woman get used to this?"

    scene rt22 with dissolve

    emt "I can feel its weight in my hand. It’s getting harder and harder in my hands."

    scene black with dissolve

    pause(0.01)

    scene hj3_s with dissolve

    emt "Andrew's penis has a different smell. It's a stronger scent. I can't quite describe it, but it's different from the [name]'s."

    scene black with dissolve

    pause(0.01)

    scene hj3_f with dissolve

    pause

    scene rt23 with dissolve

    awt "She smells like perfume and wine. This time, I’m not gonna let you finish that quickly. Little guy isn’t just going to settle for your hand this time."

    scene black with dissolve

    pause(0.01)

    scene hj_s with dissolve

    pause

    scene hj_f with dissolve

    emt "Am i doing wrong? It doesn’t seem like he's going to cum anytime soon."

    scene rt24 with dissolve

    em "Ugh. I’m getting tired. Why can’t you finish yet? Did you take something or what?"

    scene rt25 with dissolve

    aw "Whaaa… What? I didn’t take pills or anything. This is just how I am. No one’s ever been able to make me cum with just their hand."

    scene rt26 with dissolve

    em "Really?! So, what do I need to do?"

    scene rt25 with dissolve

    aw "I think you’re ready for the sex. Just let yourself go with me. I promise you’ll feel good."

    scene rt27 with dissolve

    em "No way! It's way too early for that!"

    scene rt28 with dissolve

    aw "Oh.. Okay, boss. Then at least let me use your mouth."

    scene rt29 with dissolve

    em "Well..."

    scene rt30 with dissolve

    pause 

    jump aw_scnd

label aw_scnd:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"

    $ persistent.b_scene1_unlocked = True


    $ persistent.a_scene2_unlocked = True

    scene rt31 with dissolve

    mct "I don't know if I want her to do this with someone else since she's rejected me about it so many times before."

    mct "I know we need to move forward. I’m not sure if I want her to do something with someone else that she doesn't want to do with me."

    menu:
        "Insist on sex":

            $ ntr_point += 2

            scene rt32 with dissolve

            mc "Honey... You're going to have sex eventually. I think you're ready for it today"

            scene rt33 with dissolve

            em "Really? I told you I wasn’t ready! I cannot believe you. I’m gonna go with Andrew’s suggestion."

            em "Andrew can you move like this?"

            scene rt34 with dissolve

            aw "Okay… I'll stand wherever you want me to right now."

            scene rt35_a with dissolve

            mct "[fname] is really mad at me. I felt inadequate and ended up ignoring her feelings. I’m not sure if she’s punishing me or if she just doesn’t care."

            mct "She’s acting like I’m not even in the room."
        "Support the blowjob idea":


            $ nts_point += 2

            scene rt32 with dissolve

            mc "It's okay honey. I know you are not ready for the sex."

            scene rt29 with dissolve

            em "I guess I should do that. I'm not ready to take that thing in my..."

            em "Anywways. Andrew, can you move over there?"

            scene rt34 with dissolve

            aw "Okay… I'll stand wherever you want me to right now."

            scene rt35 with dissolve

            mct "Is [fname] trying to tease me? If so, it’s definitely working."

            scene rt36 with dissolve

            mct "She looks super sexy right now. It feels like me and [fname] are playing a game—a naughty game."

    scene rt37 with dissolve

    awt "Her mouth is so small and tight… It feels like I’m inside [fname] pussy."

    em "Mmm...mmm."

    scene rt38 with dissolve

    awt "It doesn’t seem like it’s her first time."

    aw "Hhh… [fname] y-you..."

    aw "Hhh.. You are so perfect."

    scene rt39 with dissolve

    em "Slurp..SluRP…SLURP."

    aw "That feels nice."

    scene black with dissolve

    pause(0.01)

    scene bj2 with dissolve

    aw "[fname], you have to stop! I am gonna.. CUM!!"

    scene rt40 with dissolve

    aw "OH!!!"

    scene rt41 with dissolve

    em "Wha…"

    scene rt42 with dissolve

    mc "Wait..."

    scene rt43 with dissolve

    aw "Im sorry [fname], it was an accident. I couldn’t hold back anymore."

    scene rt44 with dissolve

    mc "DUDE!"

    em "What the he..."

    scene rt45 with dissolve

    aw "Oh, I totally forgot! I’ve got something to do. I gotta go. Bye!"

    scene rt46 with dissolve

    em "What was that?? UGH... I'm gonna go clean up. "

    scene rt47 with dissolve

    mc "Okay..."

    $ renpy.end_replay()

    scene rt48 with dissolve

    pause

    scene rt49 with dissolve

    em "I definitely wasn’t expecting that to happen."

    scene rt50 with dissolve

    mc "Same here, that was so weird."

    scene rt51 with dissolve

    mct "She smells really strong... semen…"

    scene rt52 with dissolve

    em "I was about to yell at him."

    scene rt53 with dissolve

    em "But when I saw him running away like that, I had to really hold back my laughter."

    scene rt54 with dissolve

    em "I think we handled today pretty well, aside from the last bit."

    scene rt51 with dissolve

    mc "I think so too."

    mc "So I was thinking..."

    scene rt55 with dissolve

    pause

    scene rt56 with dissolve

    em "Not really in the mood for that, babe."

    scene rt57 with dissolve

    mc "Ohh. Okay. Sorry honey."

    scene rt58 with dissolve

    mc "Oh! This is Andrew's phone! He must've dropped it. I should take it to him."

    scene rt59 with dissolve

    pause

    scene rt60 with dissolve

    em "Right now?"

    scene rt61 with dissolve

    mc "Yeah, I'll be right back."

    scene rt60 with dissolve

    em "Okay, babe. Drive safe."

    scene rt62 with dissolve

    pause

    scene rt63 with dissolve

    mc "Hey! Honey… I am home."

    scene rt64 with dissolve

    mct "Oh…"

    mct "Is that a remote controller?"

    scene black with dissolve

    pause

    jump expose




label halloween_event_label:

    $ disable_saving = True

    scene inf with dissolve

    pause

    scene black

    $ name = renpy.input("My name is", default = "Jake", length=15)
    $ persistent.name = name

    if name == "":
        $ mc = "Jake"
        $ mct = "Jake Tought"
        menu:
            "Are you sure about Jake?"
            "Yes":
                pause
            "No,Please.":

                pause



    $ fname = renpy.input("My wife's name is", default = "Emily", length=15)
    $ persistent.fname = fname

    if fname == "":
        $ em = "Emily"
        $ emt = "Emily Tought"

    if _in_replay:
        if persistent.name:
            $ mc = persistent.name
        if persistent.fname:
            $ em = persistent.fname


    scene h0 with dissolve

    mct "Women... She said she'd be ready in 10 minutes an hour ago, and she's still not ready."

    scene h1 with dissolve

    mc "Are you still not ready, [fname]?"

    scene h2 with dissolve

    em "Alright, alright! Five more minutes. Don't rush me."

    scene h1 with dissolve

    mc "So... that means you’ll be ready in half an hour?"

    scene h2 with dissolve

    em "Haha, you’re so cute. Trust me, I’ll be worth the wait."

    scene h2 with dissolve

    em "Oh, by the way, honey, did you get the wine I asked for?"

    scene h2_5 with dissolve

    mct "Oh, crap. How did I forget that? If I tell [fname], she’ll kill me."

    scene h2_5 with dissolve

    mc "Uh... Yeah, of course! I even dropped it off at Andrew’s already."

    scene h2_6 with dissolve

    em "Oh, you’re amazing!"

    scene h2_7 with dissolve

    mct "James is the only one who can handle this quickly. Better text him now."

    scene 30m with dissolve

    pause

    scene h2_8 with fade

    em "I’m ready."

    scene h3 with fade:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.0

    mc "Wow!"

    scene h4 with dissolve

    em "Speechless?"

    scene h4 with dissolve

    mc "Hmm… Honey?"

    menu:
        "Warn her about the dress showing too much":

            scene h4_1 with dissolve
            mc "Don’t you think the front of your dress is… well, a little too low?"

            scene h4_2 with dissolve
            em "Oh, really? You think so?"

            scene h4_3 with dissolve
            mc "I mean, if you’re not careful, I might just get a peek at... well, you know."

            scene h4_4 with dissolve
            em "Guess I’d better be extra careful, then."

            scene h4_4 with dissolve
            mc "Haha."

            $ persistent.warn_1 = False
        "Don't warn her":


            scene h4_1 with dissolve
            mc "Your beauty just left me speechless for a second there."

            scene h4_1 with dissolve
            mc "You look absolutely stunning."

            scene h4_2 with dissolve
            em "Ohh... thank you, sweetheart."

            $ persistent.warn_1 = True

    scene h4_1 with dissolve

    mc "Let's...."

    scene h4_9 with dissolve

    em "Mwah!"

    scene h4_5 with fade

    mc "Wow! What was that for?"

    em "This was just an apology kiss for keeping you waiting. Come on, we’re running late—let’s go!"

    scene 30m with dissolve

    pause

    scene h4_6 with dissolve

    mc "Wow! Andrew's really getting into the Halloween spirit!"

    em "Yeah, I didn’t expect him to go to all this trouble."

    em "Wait wait wait!"

    scene h4_7 with dissolve

    em "Do I look spooky and sexy?"

    mc "You always do, babe."

    scene h4_8 with dissolve

    em "Hey?!"

    scene h4_8_2 with dissolve

    aw "What are you guys doing out here?"

    aw "Not planning to come inside?"

    scene h4_8_3 with dissolve

    aw "Anyway, never mind. I worked hard on my welcome, so here goes!"

    scene h5 with dissolve

    aw "Welcome to Andrew's Legendary Halloween Party!"

    mc "Bro! You scared the shit out of me!"

    em "Ahhhh! Oh my God!"

    scene h5_5 with dissolve

    aw "Sorry! I thought it would make an impressive 'welcome.'"

    em "You scared me half to death with that welcome! But since it’s Halloween, I’ll let it slide this time."

    mc "Yeah, man…"

    scene h6 with dissolve

    aw "Hey, where have you guys been? I was starting to think you had given up on coming."

    mc "We're late. You can guess why."

    scene h7 with dissolve

    aw "Let me guess. It was all your fault."

    mc "Hahaha."

    scene h8 with dissolve

    em "Hey! Stop messing with me."

    aw "Sure…"

    mc "Of course, honey!"

    em "Come on, let's head inside."

    scene h9 with dissolve

    aw "Psst, hey man, can we talk for a sec?"

    mc "Yeah, what's up, man? Is something wrong?"

    scene h10 with dissolve

    aw "The kid you invited showed up, but are you sure he's 18?"

    mc "Yeah, yeah. He just looks a little younger, but there's no problem."

    scene h11 with dissolve

    aw "If you say so..."

    aw "He seems a bit... odd. And that costume...?"

    mc "What's wrong with his costume?"

    aw "You'll see. Come on, let’s head inside."

    scene h12 with fade

    pause

    scene h13 with Dissolve(3.5)

    unk2 "Aaaaargh..."

    scene h14 with Dissolve(1.5)

    unk2 "Hahaha!"

    scene h15 with Dissolve(1.5)

    unk2 "Let's have fun."

    scene h12 with Dissolve(3.5)

    pause

    scene h16 with fade

    jm "Would you mind if I check the fabric of your dress, [fname]?"

    em "Huh?"

    th "Yes, please, can I feel it too?"

    scene h17 with dissolve

    jm "Hey! Welcome, [name]."

    mc "Thanks."

    th "Welcome, [name]."

    mc "Thanks, buddy."

    mc "I honestly didn’t expect you to put this much effort in costumes. It looks so realistic."

    scene h18 with dissolve

    jm "Yeah. My wife and I used to go to a costume party every year, and there were... various fantas... ahem. Anyway, thanks."

    scene h17 with dissolve

    th "Yeah, it is really important to me. It’s my first time attending a Halloween party."

    mc "That’s good. But Theo, it seems like you forgot to dress up, buddy. What’s with the costume?"

    scene h19 with dissolve

    th "This is Bonecrusher costume! This is how he dresses. Actually, he's a bad guy too, but he crushes other bad guys. He's a solid character."

    scene h20 with dissolve

    emt "Wow. I guess it’s time I accept that Theo is starting to grow up. It looks like he’s shoved something huge into his underwear, and his underwear is about to burst."

    scene h19 with dissolve

    mc "Do I see this right, or is [fname] looking at Theo’s penis?"

    mc "Is it the size that caught her attention? Could she have liked it?"

    mc "The woman I love is looking at another young guy’s big cock. Shit. I don’t even know how to feel."

    mc "I shouldn’t be thinking about this right now, or I’ll end up getting hard."

    scene h21 with dissolve

    jm "Alright, settle down. Let me get you guys something to drink. You need to loosen up a bit!"

    scene h22 with dissolve

    "Yeah!"

    scene h22_5 with dissolve

    jmt "Now…"

    scene h23 with dissolve

    jmt "Let’s add some of Uncle James’s special mix and…"

    scene h23_5 with dissolve

    jmt "Let the party get even more exciting."

    scene h24 with dissolve

    em "...it was a staple of our college parties..."

    scene h25 with dissolve

    jm "Who wants some wine? It’s a really fine one—aged to perfection."

    scene h26 with dissolve

    jmt "Wow! What a sight. One day, I’m going to bite those nipples of yours, [fname]."

    scene h27 with dissolve

    em "Are you kidding me? I’ve been waiting for this all week!"

    scene h27 with dissolve

    mc "Same here."

    th "I want it too!"

    aw "Count me in! I’m not missing out on that."

    scene h28 with dissolve

    em "So, Andrew, is this the infamous Halloween party you’ve been hyping up?"

    aw "Oh, you bet! Later tonight, I’ve arranged for Bloody Horny Mary’s ghost to show up. She’s going to take the party to the next level!"

    th "Why do they call her *Horny* Mary?"

    em "Trust me, Theo. You don’t want to know."

    mc "Come on, don’t fill his head with this nonsense."

    jm "Hehehe..."

    scene h28 with dissolve

    aw "Bloody Horny Mary is a legend. They say she appears in mirrors, takes over women’s bodies, and gives men the time of their lives..."

    aw "Until she drains their dicks dry of every last drop of blood. She doesn’t stop until there’s absolutely nothing left!"

    th "Whoa."

    em "Haha..."

    scene h29 with dissolve

    mct "Is this old bastard staring at [fname]’s breasts?"

    if persistent.warn_1 == True:

        scene h29 with dissolve

        mct "He hasn’t even joined the conversation or moved his head at all."

        mct "It’s hard to tell exactly where he’s looking with that mask. The mask covers his eyes."

        scene h31 with dissolve

        mct "Wtf? Is he... stroking himself?"

        mct "I should’ve warned [fname]. He’s masturbating right in front of me while staring at her breasts."

        scene h30 with dissolve

        mct "He’s so close. Just a little more, and he could rub himself on her shoulder. Or even across her face."

        mct "Shit. Thinking about this is making me hard. The thought of Old James rubbing his dick on my beautiful wife’s face is insanely arousing. Is it the alcohol?"

        mct "Anyway, he’s not really hurting anyone. Stay calm, [name]. Just enjoy the moment."
    else:


        scene h30_5 with dissolve

        mct "Haha... Looks like [fname] noticed too. She must’ve remembered the warning I gave her at home."

        scene h31_5 with dissolve

        jm "Grrr..."

        mct "Later, Old James, but I’ve gotta hand it to you for the effort."


    scene h33 with dissolve

    em "Honey, where did you even find this wine? Vino Rouge D’Argent... It’s been years since I last had some."

    scene h32 with dissolve

    mc "A magician never reveals his secrets."

    jm "Hahaha!"

    scene h33 with dissolve

    em "Maybe the magician who found this wine deserves a reward. At the end of the night..."

    scene h32 with dissolve

    jm "Hmm..."

    mct "Shit."

    mc "Yeah, honey. You definitely should reward him."

    scene h33 with dissolve

    em "Haha... I wish you could see the look on your face. You’re blushing, aren’t you? So cute."

    mct "If you knew I just heard you say you wanted to reward James in bed, you’d understand why my face looks like this."

    scene h34 with Dissolve(3.5)

    unk2 "Ah, what a lively group."

    scene h35 with Dissolve(2.0)

    unk2 "Let me…"

    scene h36 with Dissolve(2.0)

    unk2 "stir things up a bit."

    scene h37 with Dissolve(2.0)

    unk2 "Such beauty... It deserves to be appreciated by all."

    scene h38 with Dissolve(2.0)

    unk2 "Did we also play with the nipples a little? Then it’s perfect. Have fun, beauty..."

    scene h39 with Dissolve(3.5)

    em "Anyway... Thanks for finding this wine, baby."

    scene h40 with dissolve

    em "That... was so weird. I felt a chill for a moment there."

    em "Why is everyone staring at me like that?"

    mc "Uh... [fname]..."

    scene h41 with dissolve

    th "I... I think your dress is..."

    aw "Open. It's... open."

    em "What?"

    scene h42 with dissolve

    em "Oh my God!"

    em "How did this even happen?!"

    scene h43 with dissolve

    mc "Honey, are you okay?"

    em "No, I’m not okay! This is humiliating!"

    em "They saw everything!"

    scene h44 with dissolve

    jm "Hey, uh, maybe it’s the wine? It’s been a strange evening already..."

    th "Yeah, yeah and no one saw anything! I swear!"

    aw "Theo, we all saw everything."

    em "Andrew! Not helping!"

    scene h45 with dissolve

    mc "[fname], let’s step outside for a second. Take a breather, okay?"

    em "...Fine. Just... give me a moment."

    em "I think I need to be alone for a bit... Where’s the bathroom?"

    aw "It’s upstairs, on the right."

    scene h46 with dissolve

    jm "Well... that was... unexpected."

    aw "So, uh, who wants more wine?"

    scene h47 with fade

    em "Oh my God... They all saw me."

    em "Andrew, James, even Theo! They were all staring at me like—"

    em "How could I not notice my dress? God, that was so embarrassing..."

    em "They were looking at me like they wanted to devour me... And I was standing there, showing everything with [name] right next to me."

    scene h48 with dissolve

    em "They were looking at me like they wanted to devour me... And I was standing there, showing everything with [name] right next to me."

    scene h48 with dissolve

    em "Thinking about them while they stared, with [name] by my side... It felt so…"

    scene h49 with dissolve

    unk2 "What a beautiful sight you were... All their eyes were on you, drinking in every inch."

    scene h49 with dissolve

    unk2 "That dress... hugging you so perfectly. And then, the way it opened, revealing your secrets. Such a tease... even if you didn’t mean to be."

    scene h50 with dissolve

    unk2 "I could feel their desire filling the room, just like they want to fill you. Couldn’t you?"

    scene h50 with dissolve

    unk2 "This body... so warm, so soft. It’s mine now."

    scene h50 with dissolve

    unk2 "Let me show you what they were all imagining. Let me help you embrace this pleasure you've kept buried."

    scene h50 with dissolve

    unk2 "Mmm... Yes. This is what you deserve... to feel adored, worshiped, wanted."

    scene h51 with dissolve

    pause

    scene h52 with dissolve

    pause

    scene h53 with dissolve

    unk2 "Hmm…"

    scene h54 with dissolve

    jm "Alright, folks, I’m officially at my limit. I’m too old for this much wine. Nature’s calling, and it’s urgent!"

    scene h54 with dissolve

    jm "Is there another bathroom around here? Looks like [fname]’s using the one upstairs."

    scene h55 with dissolve

    aw "Yeah, there’s another one in my room. Head upstairs, and it’s the door to the left."

    scene h56 with dissolve

    jm "Got it, thanks."

    scene h56_5 with dissolve

    pause

    scene h57 with dissolve

    jmt "Wait... is [fname]?"

    scene h57_5 with dissolve

    jmt "Holy—what is she...?"

    scene h58 with fade:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.0

    jmt "What the hell is this? Is she... is this some kind of prank?"

    jmt "Did she leave the door open on purpose? Maybe [name] and [fname] are into something kinky, and I’ve just stumbled upon it..."

    scene h59 with dissolve

    em "James... I know you’re there. Come closer."

    scene h59 with dissolve

    jm "[fname], is this... is this a joke? Are you and [name] testing me or something?"

    scene h60 with dissolve

    em "Does this look like a joke to you?"

    scene h60 with dissolve

    jmt "Goddamn... this can’t be real. Is she really... inviting me?"

    scene h60 with dissolve

    jm "[fname], I... Look, if you’re serious about this, I’m not one to say no, but this has to be between us. You know [name] can’t find out."

    scene h60 with dissolve

    em "[name]? Oh, James... Forget about him. Right now, it’s just you and me."

    scene h60 with dissolve

    em "Now, James... Why don’t you show me what you’ve been thinking about all night?"

    scene h61 with dissolve

    jm "Don’t mind if I do, sweetheart."

    scene h62 with dissolve

    em "So, tell me, James..."

    scene h62 with dissolve

    em "What would you do with this body? I mean... What are you going to do to me?"

    scene h62 with dissolve

    jm "Ermm... I want to smell your pussy. And then taste it."

    scene h62 with dissolve

    em "You’re going to smell and taste the pussy of a woman whose husband is downstairs enjoying the party? My husband hasn’t even smelled my pussy."

    scene h62 with dissolve

    jm "Then let me succeed where your husband failed. Let my tongue explore inside."

    scene h63 with dissolve

    jmt "Ahh…"

    scene h63 with dissolve

    jmt "Mmm..."

    scene h63 with dissolve

    jmt "That smell. Like a wildflower drenched in sin. So raw, so filthy... God, it’s driving me insane."

    scene h64 with dissolve

    em "Did you like it?"

    scene h64 with dissolve

    jm "Such young, smooth skin... For a man my age, this is beyond a dream."

    scene h64 with dissolve

    em "Ahh..."

    scene h64 with dissolve

    jm "I can’t believe your husband is downstairs while you’re letting me sniff your pussy here."

    scene h64 with dissolve

    em "I only wish he could watch what you’re about to do to me. You can do whatever you want to my pussy James."

    scene h65 with dissolve

    jm "Then lie down over there."

    scene h65 with dissolve

    em "But I should warn you. You don’t have much time. You can only fulfill one desire for now."

    scene h65 with dissolve

    jm "My only desire is to taste your honey pot."

    scene h66 with dissolve

    em "Hmm..."

    scene h66 with dissolve

    em "Then?"

    scene h67 with dissolve

    jm "Haha."

    scene h68 with dissolve

    pause

    scene h69 with dissolve

    pause

    scene h70 with dissolve

    pause

    scene h71 with dissolve

    pause

    scene h72 with dissolve

    em "Ahh…"

    scene h72 with dissolve

    em "Run your tongue inside me."

    scene h73 with dissolve

    jm "*Slurp*"

    scene h73 with dissolve

    em "Ahhh… Ah…"

    scene h73 with dissolve

    jm "Mmmm…"

    scene h73 with dissolve

    em "I'm cumming."

    scene h74 with dissolve

    em "That felt so good. I’m sure you’ve completely consumed [fname] while savoring her essence."

    scene h74 with dissolve

    jm "[fname], what do you mean?"

    scene h74 with dissolve

    em "Never mind, that’s none of your business, old bastard."

    scene h74 with dissolve

    jm "O-o-okay… You’re getting a bit harsh all of a sudden."

    scene h74 with dissolve

    em "For someone licking a married woman’s pussy, you’re surprisingly polite. Hah! Now, go back downstairs already."

    scene h75 with dissolve

    em "But wait… Before you leave, let me give you a little gift."

    scene h76 with dissolve

    em "Take this. It’s all yours. I won’t need it anymore tonight."

    scene h76 with dissolve

    jm "Are you sure?"

    scene h76 with dissolve

    em "Yes. Just take it."

    scene h76 with dissolve

    jm "See you downstairs."

    scene h76 with dissolve

    em "Bye…"

    scene h77 with dissolve

    em "Alright, [fname]."

    scene h77 with dissolve

    em "I’m letting you go for now. Go downstairs and let’s have some fun together."

    scene h78 with dissolve

    pause

    scene h47 with dissolve

    pause

    scene h79 with dissolve

    em "…strange. Huh? What?"

    scene h79 with dissolve

    em "It feels like a chill again. It sent a shiver down my spine."

    scene h79 with dissolve

    em "What? There’s really a chill. I can feel it under my skirt."

    scene h80 with dissolve

    em "Hick? What... What is this?!"

    scene h81 with dissolve

    em "Oh my God, where are my panties?! What happened?!"

    scene h81 with dissolve

    em "Did I... never wear them? I remember putting them on when I left the house."

    scene h81 with dissolve

    em "Shit, shit, shit. Am I losing my mind?"

    scene h80 with dissolve

    em "What is this wetness?"

    scene h80 with dissolve

    em "I swear I didn't feel like this just a moment ago."

    scene h80 with dissolve

    em "This is so scary. I don’t want to be alone anymore."

    scene h82 with fade

    emt "If I’m not careful, they might see something they shouldn’t."

    scene h82 with dissolve

    emt "I need to tell [name] about this strange thing that happened, but without drawing too much attention."

    scene h83 with dissolve

    em "Honey"

    scene h83 with dissolve

    em "Are you kidding me?! Hey, wake up. Come on, don’t fall asleep here."

    scene h83 with dissolve

    aw "Good luck with that, [fname]. He’s out cold. Guess the wine hit him harder than he thought."

    scene h84 with dissolve

    em "Not right now…."

    scene h85 with fade

    unk2 "Wakey, wakey, sweetie..."

    scene h86 with dissolve

    mc "Huh? Who’s—?"

    scene h88 with dissolve

    unk2 "Shh… Don’t struggle. You’re not waking up from this, not yet."

    scene h89 with dissolve

    mc "What the…? Where am I? Who are you?"

    scene h89 with dissolve

    mc "Just a moment ago I... What’s happening?"

    scene h89 with dissolve

    mc "Where is [fname]?"

    scene h88 with dissolve

    unk2 "You’ll find out soon enough. Let’s just say… I’m here to play. And [fname] Oh, she’s part of the game now."

    scene h90 with dissolve

    mc "What are you?!"

    scene h90 with dissolve

    mc "Leave her out of this!"

    scene h88 with dissolve

    unk2 "But where’s the fun in that? You’ll answer my questions, sweetheart. Get them right, and maybe—just maybe—I’ll spare her."

    scene h88 with dissolve

    unk2 "But every wrong answer… Well, let’s just say, [fname] won’t enjoy it as much as I will."

    scene h91 with dissolve

    unk2 "Oh, maybe she will too..."

    scene h91 with dissolve

    unk2 "Well then, let’s begin with the first question... Relationship-testing questions... Let’s see if you’re really such a good husband."

    scene h91 with dissolve

    unk2 "Here’s the first one. What’s [fname]’s favorite wine?"

    menu:
        "Vino Rouge D’or":

            scene h92 with dissolve

            mc "Vi-Vino Rouge D’or?"

            scene h93 with dissolve

            unk2 "Hahaha. You lie to [fname], pretending you were the one who got the wine, yet you can’t even remember its name properly."

            scene h93 with dissolve

            unk2 "You truly are a terrible husband, and for that, we must punish [fname] right before your eyes."

            scene h90 with dissolve

            mc "Shit. What you are gonna do to her?"

            scene h93 with dissolve

            unk2 "I won't do anything. Just sit back and watch."

            scene h94_5 with dissolve

            unk2 "Ah, [fname]... looks like you’ve joined the party too. You must be confused, huh? Well, let me fill you in—this is all part of the game. The game where things get a little... complicated."

            scene h95 with dissolve

            pause 0.5

            scene h96 with dissolve

            em "W-What’s happening? Why are you here... and why is this happening to me?"

            scene h94_5 with dissolve

            unk2 "Oh, [fname]... You’ve been part of this game since the moment you entered Andrew's house. It’s a little test, a little challenge for your husband. All I want is to see how far he’ll go, and whether he’ll pass or fail."

            scene h97 with dissolve

            em "A game? What do you mean? What game are you talking about? This isn’t fun, this isn’t right—"

            scene h94_5 with dissolve

            unk2 "Oh, it’s all part of the fun, my dear. The rules are simple: Your husband answers my questions, and every wrong answer leads to something... "

            scene h94_5 with dissolve

            unk2 "unpleasant for you. And, of course, every right answer keeps you safe... but not always."

            scene h98 with dissolve

            mc "Don’t worry, honey. I’m going to get you out of this. I’ll stop her, I swear it."

            scene h99 with dissolve

            em "W-What? You’ll stop him? But how? We’re trapped here…"

            scene h94_5 with dissolve

            unk2 "He might try to save you, but remember, every mistake he makes will cost you. Let’s see if he’s strong enough to handle what’s coming."

            scene h100 with dissolve

            unk2 "Come on, [name]... Let’s bring the punishment here."

            scene h101 with dissolve

            em "What's going on. [name] what's that?"

            mc "STOP IT!"

            scene h102 with dissolve

            unk2 "Let’s get her wet first, right? Jumping straight in might not be the best idea."

            scene black with dissolve

            pause(0.01)

            scene td with dissolve

            em "I can’t move my body. Ahh..."

            em "The ridges are hurting me, and it’s so cold."

            unk2 "Don't worry. You'll warm it up with your honey pot in a bit."

            unk2 "So... how’s the view from there, [name]?"

            scene h90 with dissolve

            mc "Go to hell!"

            scene black with dissolve

            pause(0.01)

            scene td2 with dissolve

            unk2 "Hahaha. I’m already coming from there."

            unk2 "Since you're wet enough you are ready to take that."

            em "Ahhh…. Hhhh…."

            em "Stop!"

            unk2 "I can't help but make you pay your punishment, sorry."

            mc "Shit!"

            em "It's too big… It h… Hurts…"

            scene h103 with dissolve

            unk2 "I think we can move on to the next question now…"

            scene h104 with dissolve

            unk2 "Let’s move her like this so you can see our sex toy more clearly."

            em "Hhhh…"

            mct "She’s really holding [fname] like a lifeless plastic sex toy."

            unk2 "I guess you enjoyed the view."

            unk2 "Sorry to pull you away from it, but we need to move on."
        "Vino Rouge D’Argent":


            scene h90 with dissolve

            mc "Of course I know this. Vino Rouge D'argent."

            scene h93 with dissolve

            unk2 "Well well... You’re too lazy to buy your wife’s favorite wine, but you still know which one it is."

            unk2 "Even though you got the answer right, because of your little deception, you still deserve a small punishment."

            scene h90 with dissolve

            mc "No! I got it right. Stick to your word."

            scene h94 with dissolve

            unk2 "Quiet! and try not to make me angry."

            scene h95 with dissolve

            unk2 "Ah, [fname]... looks like you’ve joined the party too. You must be confused, huh? Well, let me fill you in—this is all part of the game. The game where things get a little... complicated."

            scene h96 with dissolve

            em "W-What’s happening? Why are you here... and why is this happening to me?"

            scene h94_5 with dissolve

            unk2 "[fname]... You’ve been part of this game since the moment you entered Andrew's house. It’s a little test, a little challenge for your husband."

            unk2 "All I want is to see how far he’ll go, and whether he’ll pass or fail."

            scene h97 with dissolve

            em "A game? What do you mean? What game are you talking about? This isn’t fun, this isn’t right—"

            scene h94_5 with dissolve

            unk2 "Oh, it’s all part of the fun, my dear. The rules are simple: Your husband answers my questions, and every wrong answer leads to something... "

            unk2 "unpleasant for you. And, of course, every right answer keeps you safe... but not always."

            scene h98 with dissolve

            mc "Don’t worry, honey. I’m going to get you out of this. I’ll stop her, I swear it."

            scene h99 with dissolve

            em "W-What? You’ll stop him? But how? We’re trapped here…"

            scene h94_5 with dissolve

            unk2 "He might try to save you, but remember, every mistake he makes will cost you. Let’s see if he’s strong enough to handle what’s coming."

            scene h93 with dissolve

            unk2 "Come on, [name]... Let’s bring along the magician who figured out our wine."

            scene h105 with dissolve

            unk2 "Let's take James here. As a result of the answer you just gave, we can say that you prevented the entry of something thicker, but still James's dirty and old fingers have to taste your wife's pussy. Come on James..."

            mc "James! Help!"

            scene h106 with dissolve

            unk2 "Don’t bother struggling. James is under my control now— just like everything else here… You are all my little puppets!"

            scene h107 with dissolve

            em "It cant be!…"

            unk2 "Ah... Yes, good of you to remind me of your presence."

            scene h108 with dissolve

            unk "Let’s get you into a nice, comfortable position. What do you say?"

            scene h109 with dissolve

            em "I can’t move my body. [name] help!"

            mc "Dammit! I can't move either."

            unk2 "Come on, magician, let's see your show."

            scene h110 with dissolve

            jm "Grrr…."

            em "[name], he is toucing me."

            mc "I can't do anyting! Shit!"

            mc "My whole body is paralyzed, except for one part. Why the hell does the thought of this monstrous thing touching [fname]'s private parts turn me on?"

            mc "Deep down, I knew I enjoyed imagining [fname] with others, but... this..-"

            scene h111 with dissolve

            em "[name]! He is getting closer!"

            em "Hhh... James, wake up!"

            unk2 "Hahaha. Trust me, you don’t want him to wake up right now. If you knew the things he wants to do to you, you’d never go near him again."

            em "[name], he’s touching my..."

            scene h112 with dissolve

            jm "Hmm..."

            em "Get your filthy hands off me… Ahhh!"

            scene h113 with dissolve

            mc "The woman I love… She’s about to be fingered, and I can’t do a damn thing about it!"

            scene h114 with dissolve

            em "He... he is moving..-"

            scene h113 with dissolve

            em "his finger inside my pussy!"

            scene h114 with dissolve

            mc "Finish this punishment! Please!"

            unk2 "We’ve just got a couple more things to do with James."

            scene h115 with dissolve

            jm "Hahaha…"

            scene h116 with dissolve

            em "*Hick*!!"

            scene h117 with dissolve

            em "Hhh..."

            scene h118 with dissolve

            em "Ahh!"

            scene h120 with dissolve

            em "He’s pushing it in..."

            scene h119 with dissolve

            em "So deep..!"

            scene h89 with dissolve

            mc "Is this a nightmare?"

            scene h119 with dissolve

            em "Mmm…"

            scene h120 with dissolve

            pause

            scene h119 with dissolve

            em "If he keeps going like this…"

            scene h120 with dissolve

            em "Mmm… I can't hold on."

            scene h119 with dissolve

            em "Mmm…"

            scene h120 with dissolve

            pause

            scene h119 with dissolve

            em "Hhhh…"

            scene h120 with dissolve

            em "Ahh..."

            scene h94_5 with dissolve

            unk2 "I think we can move on to the next question."

            unk2 "Well...Your punishment has been sufficient."

            scene h108 with dissolve

            unk2 "You're free now, James... You can go."

    scene h91 with dissolve

    unk2 "Now, let’s move on to the second and final question."

    unk2 "I’d suggest you answer this wisely. This time the wrong answer you give may not have a remedy."



    menu:
        unk2 "Does the thought of someone screwing your wife turn you on?"
        "Yes":

            scene h90 with dissolve

            mc "Yes! Damn it, yes. I like it. I'm telling the truth, now leave her alone!"

            scene h121 with dissolve

            em "Honey... Are you sure?"

            scene h125 with dissolve

            mc "[fname]? But you... You can move..."

            scene h122 with dissolve

            em "Yes. I could all along."

            scene h125 with dissolve

            mc "You mean… was everything that just happened your own choice? Were you acting?"

            scene h123 with dissolve

            mc "How is this possible? Your eyes... it can't be real."

            scene h122 with dissolve

            em "What if we focus on making your desires come true?"

            scene h126 with dissolve

            mc "I... I'm not sure."

            scene h122 with dissolve

            em "We'll take our time and ensure you enjoy it, but in the end, I will be fucked by someone. Be prepared for that."

            scene h127 with dissolve

            mc "O-Okay, my love."

            scene h124 with dissolve

            em "Is it okay if I want Andrew?"

            mc "Okay..."

            scene h128 with dissolve

            aw "Hey there buddy. I think someone needs me."

            scene h129 with dissolve

            em "Welcome. Yes, I really need you, but I will only do this so that [name]'s desires are fulfilled. Know this."

            aw "Okay. As you say..."

            aw "So, can I use all of you?"

            em "I don't know, we need to get [name]'s permission."



            menu:
                em "What do you say, honey?"
                "Use Her Pussy":

                    scene h129 with dissolve

                    mc "You can use her pussy."

                    scene h130 with dissolve

                    em "Are you sure babe?"

                    em "Right now?"

                    mc "Yes, I don't want to wait any longer."

                    scene h134 with dissolve

                    em "Oh.."

                    mc "What happened?"

                    scene h132 with dissolve

                    em "Nothing I just…"

                    scene h133 with dissolve

                    aw "Yeah buddy… Nothing is happening…"

                    scene h132 with dissolve

                    em "*Whispers*How can it be this big? It feels like a massive tree branch sliding between my cheeks.*Whispers*"

                    scene h135 with dissolve

                    mc "What did you say honey?"

                    scene h132 with dissolve

                    pause

                    scene h133 with dissolve

                    pause

                    scene h136 with dissolve

                    em "Hhh…Nothing babe…"

                    scene h145 with dissolve

                    aw "Dude, I should thank you for sharing your precious wife with me."

                    scene h132 with dissolve

                    pause

                    scene h133 with dissolve

                    pause

                    scene h145 with dissolve

                    em "Mmm…"

                    scene h146 with dissolve

                    mc "What are you doing to her?"

                    scene h146 with dissolve

                    aw "Me..? Nothing… Just hanging around."

                    scene h146 with dissolve

                    aw "Let's do something right?"

                    scene h148 with dissolve

                    em "What? Honey?"

                    scene h149 with fade:
                        subpixel True
                        yalign 0.0
                        pause 1.5
                        linear 7.0 yalign 1.0

                    mc "What? What? [fname]?"

                    scene h147 with dissolve

                    mc "MotherF…"

                    scene h147 with dissolve

                    aw "Didn’t I promise you guys it would be an impressive party?"

                    scene h147 with dissolve

                    em "I can't say I’m not impressed."

                    scene black with dissolve

                    pause(0.01)

                    scene hrub with dissolve

                    aw "Then let’s slide a bit on it."

                    em "Ahhh... So close to the hole."

                    em "[name], it’s almost going in."

                    em "So slippery. I think it’s going to slide in."

                    aw "Isn’t it time to put it in already?"

                    aw "Let’s stretch you out a bit."

                    scene h150 with dissolve

                    aw "Here it comes…"

                    scene h125 with dissolve

                    mc "No, not yet, stop!"

                    mc "Noooooo!"

                    scene h154 with fade

                    mc "Nooo!"

                    scene h155 with dissolve

                    mc "Oh. It must be a nightmare."

                    em "What happened, honey? You woke me up."

                    mc "Nothing. It's just a nightmare."

                    em "Okay. Goodnight, honey."

                    mc "Goodnight, my babygirl."

                    scene h156 with dissolve

                    em "Hhh... Honey?"

                    mc "Yes."

                    em "How did we get home? I don't remember."

                    em "And I feel pain between my legs."

                    scene h154 with dissolve

                    mc "You said what!?"

                    scene h94 with fade

                    pause

                    scene inf2 with dissolve

                    pause
                "Use Her Mouth":


                    scene h129 with dissolve

                    mc "You can use her mouth"

                    scene h131 with dissolve

                    em "I don't know how it will fit in my mouth, but I'll try it, just for you."

                    aw "Don't worry, I'm sure you can take it all."

                    em "Then…"

                    scene h137 with dissolve

                    em "Mmm…"

                    scene h138 with dissolve

                    em "*Muck* Mmmm… Can't I just kiss it?"

                    em "[name], Honey... It barely fits in my hand... How am I supposed to put it in my mouth?"

                    mc "Wow [fname], please... I want to see you try."

                    scene h139 with dissolve

                    em "Mmm… Muck"

                    em "Since that's what you want..."

                    scene h142 with dissolve

                    em "Mmm…"

                    scene h141 with dissolve

                    em "**Gag**Gag**"

                    scene h143 with dissolve

                    em "Enormous…"

                    em "[name], this is almost twice the size of yours."

                    mct "I've been hard for a while now. I'm about to tear my pants."

                    scene black with dissolve

                    pause(0.01)

                    scene hbj with dissolve

                    em "Mmmm… mmm…"

                    em "*Slurp*"

                    mc "Huge! How can she take it all? It must be down her throat."

                    aw "Such a tight mouth."

                    aw "Take it all the way."

                    aw "Thank you for letting me use your wife's mouth, [name]."

                    mc "Honey, you can stop anytime you want."

                    em "Mmm… Mmm…"

                    mct "The way she looks into my eyes turns me on so much."

                    aw "I think I'm cumming!"

                    scene h151 with dissolve

                    em "Mmm..."

                    aw "Opss..."

                    scene h152 with dissolve

                    em "Mmmwa…"

                    aw "You need to swallow."

                    em "Hhh... Cwame... in... my... mwouth..."

                    scene h153 with dissolve

                    em "*Gulp*"

                    em "Sorry, darling. I accidentally swallowed while trying to talk."

                    mc "But... But... You’ve never swallowed mine before."

                    em "I’m sorry, sweetheart."

                    scene h89 with dissolve

                    mc "Noooooo!"

                    scene h154 with fade

                    mc "Nooo!"

                    scene h155 with dissolve

                    mc "Oh. It must be a nightmare."

                    em "What happened, honey? You woke me up."

                    mc "Nothing. It's just a nightmare."

                    em "Okay. Goodnight, honey."

                    mc "Goodnight, my babygirl."

                    scene h156 with dissolve

                    em "Hhh... Honey?"

                    mc "Yes."

                    em "How did we get home? I don't remember."

                    em "And I feel pain between my legs."

                    scene h154 with dissolve

                    mc "You said what!?"

                    scene h94 with fade

                    pause

                    scene inf2 with dissolve

                    pause
                "Use Both":


                    scene h129 with dissolve

                    mc "You can use whatever part of her you want."

                    scene h130 with dissolve

                    em "Are you sure, babe?"

                    em "Does he have permission to use everything?"

                    mc "Yes. I’m giving permission."

                    em "Right now?"

                    mc "Yes, I don’t want to wait any longer."

                    em "I can’t take it inside me right now, so I’ll need to wet it first."

                    mc "Hmm..."

                    aw "I liked that idea."

                    scene h137 with fade

                    em "Mmm…"

                    scene h138 with dissolve

                    em "*Muck* Mmmm… Can't I just kiss it?"

                    em "[name], Honey... It barely fits in my hand... How am I supposed to put it in my mouth?"

                    mc "Wow [fname], please... I want to see you try."

                    scene h139 with dissolve

                    em "Mmm… Muck"

                    em "Since that's what you want..."

                    scene h142 with dissolve

                    em "Mmm…"

                    scene h141 with dissolve

                    em "**Gag**Gag**"

                    scene h143 with dissolve

                    em "Enormous…"

                    em "[name], this is almost twice the size of yours."

                    mct "I've been hard for a while now. I'm about to tear my pants."

                    scene black with dissolve

                    pause(0.01)

                    scene hbj with dissolve

                    em "Mmmm… mmm…"

                    em "*Slurp*"

                    mc "Huge! How can she take it all? It must be down her throat."

                    aw "Such a tight mouth."

                    aw "Take it all the way."

                    aw "Thank you for letting me use your wife's mouth, [name]."

                    mc "Honey, you can stop anytime you want."

                    em "Mmm… Mmm…"

                    mct "The way she looks into my eyes turns me on so much."

                    scene h143 with dissolve

                    em "It’s slippery enough now."

                    scene h134 with dissolve

                    em "Oh.."

                    scene h132 with dissolve

                    em "I just…"

                    scene h133 with dissolve

                    aw "Do you feel that [fname]?"

                    scene h132 with dissolve

                    em "*Whispers*How can it be this big? It feels like a massive tree branch sliding between my cheeks.*Whispers*"

                    scene h135 with dissolve

                    mc "What did you say, honey?"

                    scene h136 with dissolve

                    em "Hhh… Nothing, babe…"

                    scene h145 with dissolve

                    aw "Dude, I should thank you for sharing your precious wife with me."

                    scene h132 with dissolve

                    pause

                    scene h133 with dissolve

                    pause

                    scene h145 with dissolve

                    em "Mmm… Honey, I wanna..."

                    scene h146 with dissolve

                    em "Andrew is rubbing against my hips, and I..."

                    mc "Do you like it?"

                    scene h146 with dissolve

                    aw "Yes, she likes it."

                    scene h146 with dissolve

                    aw "So... let's do something, right?"

                    scene h148 with dissolve

                    em "What? Honey?"

                    scene h149 with fade:
                        subpixel True
                        yalign 0.0
                        pause 1.5
                        linear 7.0 yalign 1.0

                    mc "What? What? [fname]?"

                    scene h147 with dissolve

                    mc "MotherF…"

                    scene h147 with dissolve

                    aw "Didn’t I promise you guys it would be an impressive party?"

                    scene h147 with dissolve

                    em "I can't say I’m not impressed."

                    scene black with dissolve

                    pause(0.01)

                    scene hrub with dissolve

                    aw "Then let’s slide a bit on it."

                    em "Ahhh... So close to the hole."

                    em "[name], it’s almost going in."

                    em "So slippery. I think it’s going to slide in."

                    aw "Isn’t it time to put it in already?"

                    aw "Let’s stretch you out a bit."

                    scene h150 with dissolve

                    aw "Here it comes…"

                    scene h125 with dissolve

                    mc "No, I'm not ready to do this, stop!"

                    scene h154 with fade

                    mc "Nooo!"

                    scene h155 with dissolve

                    mc "Oh. It must be a nightmare."

                    em "What happened, honey? You woke me up."

                    mc "Nothing. It's just a nightmare."

                    em "Okay. Goodnight, honey."

                    mc "Goodnight, my babygirl."

                    scene h156 with dissolve

                    em "Hhh... Honey?"

                    mc "Yes."

                    em "How did we get home? I don't remember."

                    em "And I feel pain between my legs."

                    scene h154 with dissolve

                    mc "You said what!?"

                    scene h94 with fade

                    pause

                    scene inf2 with dissolve

                    pause
        "No":




            scene h157 with fade

            mc "Nooo!"

            scene h158 with dissolve

            mc "Oh. It must be a nightmare."

            scene h159 with dissolve

            mc "Hey. Where is [fname]?"

            scene h91 with fade

            unk2 "Now, let’s move on to the second and final question."

            unk2 "I’d suggest you answer this wisely. This time the wrong answer you give may not have a remedy."

            scene h157 with dissolve

            mc "Nooo!"

            scene h94 with fade

            pause

            scene inf2 with dissolve

            pause



    jump return_main_menu

label return_main_menu:

    $ disable_saving = False

    return

label expose:

    scene vt1 with dissolve

    em "Mmm..."

    mct "She's so into it, she didn’t even hear me come in. She looks really horny."

    scene vt2 with dissolve

    mct "Should I leave her alone, or should I join in?"

    scene vt3 with dissolve

    mct "I don’t even know what to think."

    menu:
        "Keep Watching":

            scene vt4 with dissolve

            mct "I shouldn’t be watching this… but I can’t take my eyes off her."

            mct "She looks so beautiful like this… so vulnerable, so lost in herself."

            scene vt3 with dissolve

            mct "What does this mean for us? For me? God, I shouldn’t feel this turned on, should I?"

            scene vt11 with dissolve

            mct "I'm secretly watching my wife and touching myself."

            scene vt13_5 with dissolve

            mct "How did we get to this point?"

            mct "Have I completely lost myself to lust?"

            scene vt12 with dissolve

            pause 

            scene vt13 with dissolve

            em "Huh?"

            scene vt17 with dissolve

            em "Oh my God! What the hell are you doing?!"

            scene vt18 with dissolve

            mc "[fname], I—uh—"

            scene vt19 with dissolve

            em "Were you just standing there… watching me?!"

            em "And what’s that? Were you… touching yourself?!"

            scene vt20 with dissolve

            mc "[fname], I— I couldn’t help it… You were just…"

            scene vt21 with dissolve

            em "Oh my God! What the hell is wrong with you?!"

            scene vt22 with dissolve

            emt "I can’t believe this is happening! But… maybe the reason I’m so furious isn’t just because of him watching me… It’s because of Andrew. What we did…"

            emt "It’s made me feel so guilty and so… turned on at the same time. God, what is wrong with me? Maybe yelling at him is the only way I can get through this embarrassment."

            scene vt23 with dissolve

            mct "I know I shouldn’t have watched… but seeing her like that, I just couldn’t stop myself. God, I’ve messed up big time."

            mc "Honey, [fname]… I’m sorry. I shouldn’t have… done that. It was wrong, and I crossed a line. I wasn’t thinking."

            scene vt24 with dissolve

            em "You’re damn right you crossed a line!"

            scene vt25 with dissolve

            emt "I’m yelling at him, but… is it really him I’m mad at? Or is it me? Everything feels so out of control since Andrew. And now this… but maybe I went too far."

            scene vt26 with dissolve

            em "I… I’m sorry too. I shouldn’t have screamed like that. This whole thing is just… so overwhelming."

            scene vt27 with dissolve

            mc "No, you’re right to be upset. I invaded your privacy, and I shouldn’t have. It’s my fault."

            em "Maybe… but I’m not exactly innocent here either. There’s so much guilt I’ve been carrying lately, and it’s just… hard to handle."

            scene vt28 with dissolve

            mc "Maybe we can… talk about it? Together? I hate seeing you like this, and I don’t want to make things worse."

            scene vt29 with dissolve

            em "Yeah… maybe we should. We can’t keep going like this. It’s not good for either of us."

            scene vt28 with dissolve

            mc "I just want us to figure this out, [fname]. I love you, no matter what."

            scene vt30 with dissolve

            em "I love you too. Even if you’re an idiot sometimes."

            scene vt31 with dissolve

            mc "You know… maybe it’s time we talk to someone about all of this. I don’t want to keep pushing things down."

            mc "We’ve been through a lot, and maybe we could use some help to make sense of it."

            scene vt32 with dissolve

            em "A therapist? Are you serious?"

            scene vt33 with dissolve

            mc "I don’t know… I think it could help us. I mean, everything we’re dealing with—me, you, Andrew… there’s so much going on."

            mc "Maybe we need someone to guide us through this."

            scene vt34 with dissolve

            em "I guess… it wouldn’t hurt. I’ve been feeling so lost lately. But… what if it makes everything worse? And I don’t know, I feel like I’m changing. I don’t even recognize myself anymore."

            scene vt33 with dissolve

            mc "I get it. But that’s exactly why we need help. We can’t do this alone, and we don’t have to."

            scene vt35 with dissolve

            em "Yeah, I’ve been holding all this in for so long, and I just… I don’t know who I’m becoming. It’s scary."

            scene vt36 with dissolve

            mc "I understand, [fname]. But whatever happens, we’ll go through it together. We’ll figure it out. I’m here for you."

            scene vt35 with dissolve

            em "Okay… I trust you. Let’s try it. Let’s talk to someone."

            scene vt36 with dissolve

            mc "Then I'll book an appointment with the therapist the government has arranged for you as soon as possible."

            scene vt37 with dissolve

            em "Okay."
        "Interrupt Her":


            scene vt4 with dissolve

            mc "[fname]?"

            scene vt5 with dissolve

            pause

            scene vt6 with dissolve

            mc "What are you doing?"

            scene vt17 with dissolve

            em "Oh my God! I didn’t think you’d be back so soon!"

            scene vt18 with dissolve

            mc "Yeah, I just dropped Andrew’s phone off and came straight home. But… um, I guess I interrupted something."

            scene vt20_b with dissolve

            em "No! I mean… yes… I mean… Oh God, this is so embarrassing!"

            scene vt21_b with dissolve

            mc "Hey, hey, it’s okay. Really. We all have needs, you know? There’s nothing to be ashamed of."

            scene vt20 with dissolve

            em "But this… this feels different. It feels… wrong somehow. After Andrew, I… I shouldn’t feel like this."

            scene vt25 with dissolve

            mc "Look, [fname], maybe we need to talk about this. These feelings you’re having, this guilt… It’s eating you up, and I hate seeing that."

            scene vt26 with dissolve

            em "Do I… do I turn to someone else or... Gosh! I'm a horrible person. Why have you been so kind to me?"

            scene vt28 with dissolve

            mc "No, no, don’t think that way. You’re not horrible. Something’s going on with us, and maybe… maybe we need someone to help us figure it out. Together."

            scene vt29 with dissolve

            em "Are you saying… a therapist?"

            scene vt28 with dissolve

            mc "Yeah. Feeling guilty is natural, but we shouldn’t let it take over. And to be honest… I’m trying to figure out my own feelings too. This situation… it’s affecting me in ways I didn’t expect."

            scene vt29 with dissolve

            em "What do you mean? Are you saying that what happened with Andrew and me doesn’t… bother you?"

            scene vt29_b with dissolve

            mct "The little games she played with Theo, the way she took Andrew in her mouth—just thinking about it gets me rock hard."

            mct "I can’t admit that to her right now, but maybe a therapist can help me figure out why this turns me on so much."

            scene vt28 with dissolve

            mc "I wouldn’t say it doesn’t bother me. But at the same time… It’s like it affects me in a different way. Almost like… I don’t know, like I’m okay with it. Maybe even… I don't know…"

            scene vt32 with dissolve

            em "Are you serious?"

            scene vt33 with dissolve

            mc "Yeah, I think so. But that’s something I need to figure out too. That’s why I think seeing someone could help us. Both of us."

            scene vt29 with dissolve

            em "Okay. Maybe you’re right. It’s worth a try."

            scene vt28 with dissolve

            mc "We’ll get through this. Together. I promise."

            scene vt30 with dissolve

            em "Okay honey, I trust you."

            scene vt31 with dissolve

            mc "Then I'll book an appointment with the therapist the government has arranged for you as soon as possible."

            scene vt30 with dissolve

            em "Okay."

    scene vt38 with dissolve

    em "I don’t know why, but I’m suddenly so nervous."

    scene vt39 with dissolve

    mc "Really? You seemed fine all the way here."

    scene vt40 with dissolve

    em "I was, but now… the idea of sitting there, opening up to some guy I don’t even know, it just feels so… intimidating."

    scene vt41 with dissolve

    mc "Hey, he’s not just ‘some guy.’ He’s a professional, [fname]. This is his whole thing—helping people feel better."

    scene vt42 with dissolve

    em "I know, but… it’s more than that. Sometimes I feel like I shouldn’t even need this. Like, out of everyone, I should be able to handle it."

    em "I mean, I’m one of the few women left in the world not affected by that virus. And instead of feeling… special or grateful, I feel lost. Like I’m failing."

    scene vt43 with dissolve

    mc "[fname], you’re not failing. No one is expecting you to carry the weight of the world just because of this. You’re human, and it’s okay to need help."

    scene vt44 with dissolve

    em "It’s hard to explain. I feel like I’m not just letting myself down but… everyone else, too."

    scene vt45 with dissolve

    mc "You’re not letting anyone down. You’re here, you’re trying, and that’s more than most people would do. You’re allowed to have bad days."

    mc "That doesn’t make you weak, [fname]. It makes you human."

    scene vt44 with dissolve

    em "I guess that’s why I’m here, right? To figure all this out."

    scene vt45 with dissolve

    mc "Exactly. And look, you’re not alone in this. I’ll be right here, every step of the way."

    scene vt44 with dissolve

    em "You’re really good at this pep talk thing, you know that?"

    scene vt45 with dissolve

    mc "It’s a gift. Now, let’s get in there before you decide to bolt. We’ve got this."

    scene vt46 with dissolve

    em "Alright. But if this goes horribly, you owe me dinner… Dessert…. a back massage…. and cleaning the house and…"

    scene vt47 with dissolve

    mc "Wow, you’re really upping the stakes here. What’s next? Washing your car too?"

    scene vt48 with dissolve

    em "Actually, that’s not a bad idea."

    scene vt49 with dissolve

    mc "Don’t push it."

    scene vt50 with dissolve

    em "Hey, I’m just saying, motivation is important."

    scene vt51 with dissolve

    mc "Fine, but only if you survive the session without running out the door screaming."

    scene vt52 with dissolve

    em "Deal is deal. But don’t think I won’t hold you to all of it."

    scene vt53 with dissolve

    mc "Noted. Now, let’s go before this list gets any longer."

    scene vt54 with fade

    psy "Welcome, please, take a seat. I’m glad you both could make it today."

    psy "Let’s start with introductions. I'm Dr. Matt Wise, and I’m here to help with whatever challenges you might be facing."

    psy "I must say, it’s not every day I get to meet someone like you, [fname]. You’re truly one of the rare ones. It’s an honor to have you here."

    scene vt55 with dissolve

    psy "It’s a safe space, so feel free to express whatever’s on your mind."

    scene vt56 with dissolve

    mc "We’ve been going through some things lately... It’s hard to explain, but it’s... It’s affecting our relationship."

    scene vt57 with dissolve

    psy "That’s perfectly alright. Relationships can be complex. What kind of challenges are you facing?"

    scene vt58 with dissolve

    em "Well, it's... I’ve been feeling a lot of guilt and confusion, especially with everything that’s happened."

    em "It’s like I’m torn between what I feel and what’s expected of me."

    em "and I guess, we’re here because we don’t know how to deal with all of this. it’s... It's messing with both of our heads."

    scene vt59 with dissolve

    mc "Yeah, I mean, it’s just... I’m trying to understand my own feelings too. It’s a lot of pressure, and I don’t want things to get worse between us."

    mc "We came because... I think we need help navigating this, you know?"

    scene vt57 with dissolve

    psy "It’s good that you’re both here together. Relationships can go through tough spots,"

    psy "but with the right tools and understanding, things can be worked through. I'm here to guide you through that."

    psy "Before we proceed, I need to run a quick test with [name] to better understand the confusion you’re both facing."

    scene vt60 with dissolve

    mc "Wait, what? me? You’re doing a test on me? I thought we were here [fname]..."

    scene vt61 with dissolve

    psy "Yes, of course. but to understand everything fully, it’s important to start by focusing on you."

    psy "It’s part of the process to see how you’re both feeling individually."

    scene vt62 with dissolve

    mc "Well, okay... I guess that makes sense."

    scene vt63 with dissolve

    psy "We’ll get to both of you, don't worry. But first, understanding where you're coming from is crucial. We’ll take it one step at a time."

    scene vt64 with dissolve

    em "Looks like he's starting with you, babe."

    scene vt63 with dissolve


    menu:
        psy "Let's say you're a farmer, and this year's seeds aren't yielding the results you expected. How would you approach this situation?"
        "Look better seeds":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "I would look for better quality seeds and try again."
        "Leave the field empty":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "I would leave the season empty and wait for a luckier next year."

    scene vt66 with dissolve

    psy "Hmm..."

    scene vt63 with dissolve


    menu:
        psy "You're going on a journey with someone by your side, and suddenly, someone else joins you. How do you feel in that moment?"
        "Feel excited":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "I feel excited, like a fresh start with a new companion."
        "Feel uneasy":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "I feel uneasy, as the presence of someone else disrupts the balance."

    scene vt66 with dissolve

    psy "I see..."

    scene vt63 with dissolve


    menu:
        psy "In a garden, two flowers are growing side by side. When you notice that one is slightly larger and more attention-grabbing than the other, how do you feel?"
        "It feels balanced":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "It feels like a natural balance, and I sense that they complement each other."
        "My focus shifts":


            $ ntr_point += 1

            mc "My focus is disrupted, and I feel uncomfortable."

    scene vt66 with dissolve

    psy "Interesting...You’ve almost completed the test, just a few more questions left."

    scene vt63 with dissolve

    psy "When you were a kid, did you ever wish you had a sibling?"

    scene vt65 with dissolve

    mc "What does this have to do with anything? I don't get the connection."

    scene vt67 with dissolve

    psy "Please, just answer as honestly as possible. This is my professional field, and I won't be commenting on the interpretation of the results just yet."

    scene vt60 with dissolve

    mc "Sorry, you're right. Let's continue."

    scene vt63 with dissolve


    menu:
        psy "Not a problem! Then… When you were a kid, did you ever wish you had a sibling?"
        "Yes":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "I've always wanted a sibling."
        "No":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "No, I've always wanted to be an only child."

    scene vt66 with dissolve

    psy "Hmm..."

    scene vt63 with dissolve


    menu:
        psy "Are you a cat person or a dog person?"
        "Dog":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "I'm a dog person. I love the loyalty and companionship."
        "Cat":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "I'm a cat person. I enjoy the independence and mystery."

    scene vt66 with dissolve

    psy "Hmm... Noted."

    psy "The questions are done."

    scene vt63 with dissolve

    psy "Thank you for answering. Now, we’ll continue alone with [fname] for a bit. You can wait outside."

    scene vt68 with dissolve

    mc "Thanks, doc. I’ll be waiting for you right outside the door, honey."

    scene vt64 with dissolve

    em "Okay, babe."

    scene vt63 with dissolve

    psy "Yes... Now that we’re alone... What brought you here today [fname]? Please tell me your feelings and thoughts, in all their nakedness."

    scene vt70 with dissolve

    em "Where should I start?"

    em "First, let me tell you about what we’ve been through so far."

    scene vt71 with dissolve

    pause (1.0)

    scene vt72 with dissolve

    pause (1.0)

    scene vt73 with dissolve

    pause (0.5)

    scene vt75 with dissolve

    pause 

    scene vt76 with dissolve

    pause 

    scene vt75_5 with dissolve

    pause

    scene vt77 with dissolve

    pause

    scene vt75 with dissolve

    pause

    scene vt76 with dissolve

    pause

    scene vt74 with dissolve

    em "Also, Andrew's was literally thicker and longer than my arm."

    em "I don’t even know how it fit in my mouth. I could feel it filling my throat and this didn't disgust me at all."

    scene vt70 with dissolve

    em "Normally, I wouldn’t do this with [name]. I’d be disgusted, but in that moment, taking Andrew in my mouth actually aroused me."

    em "I'm feeling such mixed emotions. If I let myself go, it feels like a horrible person will come out. I don’t want [name] to be upset, but what I’m experiencing excites me."

    em "On the other hand, I love [name], and somehow these things don't feel right. I don't know how to explain it. It's hard to put into words."

    em "I know I love him so much... I'm afraid it will harm our relationship."

    scene vt73 with dissolve

    em "I'm sorry, I think I spoke a little too openly."

    scene vt76 with dissolve

    psy "No, no. What I want here is exactly this—being transparent with me. If you can manage to be transparent with me, you might also hear the voices you've been trying to silence inside."

    psy "I understand that you're currently caught between your id and superego."

    psy "To put it simply, your personality is composed of three parts: the id, the ego, and the superego."

    psy "Right now, you’re functioning through your ego, but your superego is repressing your id, specifically your sexual desires."

    psy "This creates a feeling of being stuck. The more you repress, the more intense your guilt becomes. This could be the reason for your outbursts."

    psy "You need to allow yourself freedom—connect with your id again. Break the taboos. By doing so, you'll find a sense of balance."

    scene vt72 with dissolve

    em "That makes sense… but it’s hard. I’ve always been taught to keep everything in check."

    em "It feels like if I let go, things could spiral out of control. I don't know if I can trust myself to let go that much."

    scene vt76 with dissolve

    psy "It’s understandable that you're hesitant. The process of breaking free from what you’ve been taught can be overwhelming, but it’s a necessary step for finding personal peace."

    psy "It’s not about abandoning control, but about finding a healthier balance. Do you think you might be ready to explore this?"

    scene vt70 with dissolve

    em "I will try."

    scene vt77 with dissolve

    psy "Our session is almost over, but before you go, let’s do a quick practice."

    scene vt70 with dissolve

    em "Okay."

    scene vt76 with dissolve

    psy "Now, with this technique, let’s bring out your psychic energy."

    scene vt75 with dissolve

    em "What do I need to do?"

    scene vt76 with dissolve

    psy "Now get up, go behind the couch, hug yourself like this with your hands, and close your eyes."

    scene vt78 with dissolve

    em "Like this? Should I hug myself like this?"

    scene vt77 with dissolve

    psy "No, not quite like that. Let me help you until you get the hang of it."

    scene vt79 with dissolve

    psy "Lift your arms, and I’ll guide you—think of me as your arms for now."

    em "Okay, Doctor Wise."

    psy "There, just like that. Relax, take deep breaths, and..."

    scene vt79_5 with dissolve

    psy "Feel the energy shift within you. Let go of any tension—trust the process."

    scene vt80 with dissolve

    em "Uh... are you sure this is how it’s supposed to be done?"

    scene vt81 with dissolve

    psy "Absolutely. Trust me. This technique is highly effective when done properly. Just focus on your breathing and allow yourself to feel the release."

    scene vt82 with dissolve

    em "I... I don’t know if this feels right. Are you sure this is part of the technique?"

    scene vt83 with dissolve

    psy "You came here for my help, and this is a technique designed to release the energy within your psyche."

    psy "If I weren’t highly skilled at my job, the state wouldn’t have entrusted me with working with someone like you."

    psy "Please, take deep breaths and imagine your energy flowing outward from your body as I guide it with my touch."

    em "Hhh…"

    scene vt84 with dissolve

    psy "I can feel the sweat on your chest and your heart beating faster. Has my technique excited you?"

    em "What? Exciting me? No, it’s just... it feels like the room is getting a bit warmer, that’s all."

    scene vt83 with dissolve

    psy "Oh, I see. Well, our session is almost over. Now, for the final exercise..."

    psy "I’d like you to close your eyes again and imagine this: all the things holding you back, chaining you..."

    psy "and keeping you restrained are being sucked out through your nipples and flowing outward."

    emt "Is it whispering in my ear? I-I fe-..."

    scene vt79 with dissolve

    psy "Good. Now, take deep breaths and feel the energy within you. Let go of the tension. Trust yourself."

    em "It’s... it’s strange. I feel... calmer, but also a little exposed."

    psy "That’s completely normal. It’s a process. This technique helps to release built-up stress and anxiety, allowing you to reconnect with your inner self."

    scene vt85 with dissolve

    em "I think I can feel that. It’s... uncomfortable, but in a good way, I guess."

    scene vt86 with dissolve

    psy "That’s progress. Remember, you don’t have to have all the answers right now. It’s okay to be uncertain."

    psy "This technique is quite powerful. I developed it drawing inspiration from Freud’s work. It helps release built-up tension and brings about catharsis, which is the first step in a deeper process."

    psy "As we continue, we’ll move through the subsequent stages."

    psy "That's enough for today. Let's bring your spouse in as well."

    if ntr_point >= nts_point:

        scene vt87_5 with fade

        mc "Hey, is your session over?"

        scene vt88_5 with dissolve

        psy "Yes, we can wrap things up for today."

        scene vt89_5 with dissolve

        mc "So, how did it go without me? Were you able to let it all out?"

        scene vt90_5 with dissolve

        em "Erm… Haha… I just talked about everything we’ve been going through lately, honey."

        scene vt91_5 with dissolve

        psy "[fname] was very open during our session."

        scene vt92_5 with dissolve

        psy "It’s always refreshing when someone can truly bare themselves—emotionally, of course. It allows us to explore those hidden depths more effectively."

        scene vt93_5 with dissolve

        em "Yes. I feel like I've broken free from my chains. I think some of my confusion has been cleared up."

        scene vt94_5 with dissolve

        mc "What chains? Wow, even a single session seems to have had a big impact on you. You look more confident."

        scene vt95_5 with dissolve

        em "I guess Dr. Wise is really good at what he does."

        scene vt96_5 with dissolve

        psy "Hahaha. Thank you, but I didn’t do anything. Everything achieved here is thanks to the effort and willingness of my clients."

        scene vt98_5 with dissolve

        psy "My next session is about to start. I'll be expecting you again next week. See you then."

        scene vt99_5 with dissolve

        em "Goodbye, Dr. Wise."

        scene vt100_5 with dissolve

        mc "Thanks, Dr. Wise."

        jump first_ntr
    else:


        scene vt87 with fade

        mc "Hey, is your session over?"

        scene vt88 with dissolve

        psy "Yes, we can wrap things up for today."

        scene vt89 with dissolve

        mc "So, how did it go without me? Were you able to let it all out?"

        scene vt90 with dissolve

        em "Erm… Haha… I just talked about everything we’ve been going through lately, honey."

        scene vt91 with dissolve

        psy "[fname] was very open during our session."

        scene vt92 with dissolve

        psy "It’s always refreshing when someone can truly bare themselves—emotionally, of course. It allows us to explore those hidden depths more effectively."

        scene vt93 with dissolve

        em "Uh… yeah, it was… insightful."

        scene vt94 with dissolve

        mc "[fname], is everything okay? Your cheeks are all red, and you seem like you’re breathing a little faster... Are you alright?"

        scene vt95 with dissolve

        em "What? No, no, nothing like that happened! I mean, everything’s fine! It was just... you know, talking. That's all."

        scene vt96 with dissolve

        psy "It’s normal to feel a little off after such an honest session. But don’t worry, [fname], you handled it very well."

        scene vt97 with dissolve

        em "Yeah, really! Nothing to worry about... Right?"

        scene vt98 with dissolve

        psy "Well then, I'll see you again next week. Take care."

        scene vt99 with dissolve

        em "Goodbye, Dr. Wise."

        scene vt100 with dissolve

        mc "Thanks, Dr. Wise."

        jump first_nts

label first_ntr:

    scene vt101 with fade

    mc "Come on... Just one bite. You won't die from sharing."

    scene vt102 with dissolve

    em "Nope. Not happening... I earned this ice cream fair and square."

    scene vt101 with dissolve

    mc "But I really want some now."

    scene vt103 with dissolve

    em "Well, you should have gotten your own. When I asked, you said you weren’t in the mood."

    scene vt104 with dissolve

    mc "That was then! Things change, especially when I see you enjoying it so much."

    scene vt105 with dissolve

    em "Too bad. The early bird gets the worm—or in this case, the ice cream."

    scene vt106 with dissolve

    mc "Come on, just one bite. You won’t die... though if it were Andrew, you'd probably let him lick the ice cream, huh?"

    scene vt107 with dissolve

    em "Andrew? Where did he come from?"

    scene vt108 with dissolve

    em "Oh... you mean the blowjob thing."

    scene vt108_5 with dissolve

    em "You’re joking, right? You don’t seem too bothered by what you saw."

    scene vt106_5 with dissolve

    mc "Last time, you gave him a blowjob. I thought you didn’t like that kind of thing. Honestly, I wasn’t really bothered by what I saw."

    scene vt109 with dissolve

    em "What do you mean? If I went over to that guy right now and gave him a blowjob, wouldn’t that bother you?"

    scene vt110 with dissolve

    mc "I don’t know..."

    scene vt111 with dissolve

    em "After talking to the therapist, I feel a little different. I think some boundaries need to be pushed if we’re going to save the world."

    scene vt112 with dissolve

    mc "What kind of boundaries, for example?"

    scene vt113 with dissolve

    em "When I asked you if you’d be bothered if I took that guy in my mouth, you said you didn’t know. I guess there’s a way to find out."

    scene vt114 with dissolve

    em "Can you hold my ice cream? If you want, you can take a bite, babe."

    mc "Hey [fname]!"

    scene vt115 with dissolve

    mc "Are you serious?"

    scene vt116 with dissolve

    em "Hey! I noticed you've been watching me lick the ice cream since I got here."

    scene vt117 with dissolve

    em "You were looking at me like you wanted to eat me. Do you want me to lick your ice cream?"

    scene vt118 with dissolve

    unk "S-Sure..."

    scene vt119 with dissolve

    unk "Wtf? Did I die or something? Am I in heaven?"

    em "Wow... Why is everyone’s so big?"

    scene vt120 with dissolve

    unk "Hahaha."

    scene vt121 with dissolve

    unk "Isn’t that your husband over there? What’s going on between you two?"

    em "You really want to talk about my husband right now?"

    scene vt122 with dissolve

    unk "Okay... Okay… Keep going please."

    scene vt123 with dissolve

    mct "I can’t believe [fname] changed this much after just one session. Are they talking about me?"

    scene vt124 with dissolve

    mct "Is this how my life is going to be from now on?"

    mct "She used to say she didn’t like taking mine in her mouth."

    mct "Now, she’s taking an old man’s without hesitation, even going all the way. As much as I hate to admit it, seeing [fname] like this fucking turns me on."

    scene black with dissolve

    pause (0.01)

    scene p_bj with dissolve

    pause

    scene vt126 with dissolve

    mct "Shit… I guess it's over now."

    scene vt127 with dissolve

    mc "Honey. Your mouth…"

    scene vt128 with dissolve

    em "Thanks, honey. I’m feeling tired, can we go home?"

    scene vt129 with dissolve

    em "I think there are some things we need to talk about afterward."

    scene vt130 with dissolve

    mc "O-Okay... Sure, sweetheart."

    scene black with dissolve

    pause

    jump ntr_path_cont

label first_nts:

    scene vt101 with fade

    mc "Come on... Just one bite. You won't die from sharing."

    scene vt102 with dissolve

    em "Nope. Not happening... I earned this ice cream fair and square."

    scene vt101 with dissolve

    mc "But I really want some now."

    scene vt103 with dissolve

    em "Well, you should have gotten your own. When I asked, you said you weren’t in the mood."

    scene vt104 with dissolve

    mc "That was then! Things change, especially when I see you enjoying it so much."

    scene vt105 with dissolve

    em "Too bad. The early bird gets the worm—or in this case, the ice cream."

    scene vt106 with dissolve

    mc "Come on, just one bite. You won’t die... though if it were Andrew, you'd probably let him lick the ice cream, huh?"

    scene vt107 with dissolve

    em "Andrew? Where did he come from?"

    scene vt108 with dissolve

    em "Oh... you mean the blowjob thing."

    scene vt108_5 with dissolve

    em "You’re joking, right? You don’t seem too bothered by what you saw."

    scene vt106_5 with dissolve

    mc "Last time, you gave him a blowjob. I thought you didn’t like that kind of thing. Honestly, I wasn’t really bothered by what I saw."

    scene vt111 with dissolve

    em "Are you really okay with everything? With how things have been lately?"

    scene vt112 with dissolve

    mc "I’m fine. It’s just... different, but it’s not a bad different. I guess I’ve come to terms with it."

    scene vt131 with dissolve

    em "Good to hear. Honey, can we take a seat and talk for a bit?"

    scene vt132 with dissolve

    em "I’ve been thinking a lot about what the therapist said. Maybe we’ve been holding back too much. There are things we could try to make things even better."

    scene vt133 with dissolve

    mc "What kind of things?"

    scene vt132 with dissolve

    em "Well, it’s about pushing boundaries. Not in a bad way, just... testing limits. Finding out what works for both of us."

    scene vt133 with dissolve

    mc "Boundaries, huh? I guess there’s no harm in exploring, as long as we’re both comfortable."

    scene vt134 with dissolve

    em "Exactly. It’s about communication, trust... And you know, maybe having a little fun while we’re at it."

    scene vt135 with dissolve

    em "We could even turn this into a game, if you’re up for it. A challenge. To see just how far we’re willing to go for each other."

    scene vt136 with dissolve

    mc "A challenge, huh? I’m intrigued. What kind of game are we talking about?"

    scene vt137 with dissolve

    em "Well, you see that guy standing over there?"

    em "He’s been staring at me ever since I sat down. I can feel his eyes on me. It’s kind of... interesting."

    scene vt138 with dissolve

    mc "Really? Are you sure?"

    scene vt139 with dissolve

    em "Oh, I’m sure. I’ve noticed the way he looks at me. It’s almost like he’s imagining doing something to me. But, I wonder... What do you think about it?"

    scene vt138 with dissolve

    mc "I guess I can’t blame him. You do look good today."

    scene vt140 with dissolve

    em "Hmm, maybe. But I think there’s more to it than just that. What if we made this a game? Let’s see how far we can take this."

    mc "A game, huh? What’s the point?"

    scene vt141 with dissolve

    em "The point is to see how comfortable we can get with things we wouldn’t normally try. Let’s see if you can handle it."

    em "If I let him know I’m aware of him watching, will you get jealous, or will you enjoy watching me play along?"

    scene vt142 with dissolve

    mc "You’re not serious, right? You want to flirt with him, in front of me?"

    scene vt143 with dissolve

    em "Let’s not call it flirting exactly, but maybe we let him watch from a distance, what do you think?"

    scene vt144 with dissolve

    em "You said you were fine with exploring things... let’s see if you really mean it."

    scene vt145 with dissolve

    em "Look honey…."

    scene vt146 with dissolve

    mc "Wow… Can I suck?"

    em "Haha… Not now. We're just playing a game right now."

    scene vt147 with dissolve

    mc "Looks like someone is a bit too eager to join the game."

    em "You’re getting a bit too excited, aren’t you?"

    scene vt146 with dissolve

    mc "Can you blame me? You’re teasing me like crazy right now."

    scene vt148 with dissolve

    em "Hmm, maybe I should turn around and let him see everything?"

    scene vt149 with dissolve

    mc "I don’t know if I can handle much more, but I’m definitely not saying no."

    scene vt148 with dissolve

    em "Alright, let’s raise the stakes a bit."

    scene vt149 with dissolve

    em "There. How’s that for a little thrill?"

    scene vt148 with dissolve

    mc "You’re really playing with fire here… but I love it."

    scene vt149 with dissolve

    em "Good. Now, what if I let him see just a little bit more?"

    scene vt150 with dissolve

    mc "You’re serious? You’d do that?"

    em "Why not? It’s just a game, right? Let’s see how bold we can get."

    scene vt148 with dissolve

    em "Good. Let’s keep it going for a little while longer. But remember, this is our game. We control how far it goes."

    scene vt149 with dissolve

    mc "Absolutely."

    scene vt147 with dissolve

    em "Maybe I should let him touch me? Or perhaps I should show him even more? What do you think?"

    mc "Ohh…"

    scene vt151 with dissolve

    em "I think it's time for me to turn around."

    em "He seems speechless. Should I go over and let him kiss my breast just once?"

    mc "O-okay."

    scene vt152 with dissolve

    em "Hahaha. Looks like you're getting really into the game too."

    em "Besides, if we unlock all the achievements at once, wouldn’t the game get boring?"

    mc "Haha, you're right, it would."

    scene vt153 with dissolve

    em "Oh no…"

    scene vt154 with dissolve

    em "I think he wants to take things even further."

    mc "Oh shit!"

    scene vt155 with dissolve

    em "Come on... I'm unbelievably turned on, we need to go home and have sex right now."

    scene vt156 with dissolve

    mc "O-Okay... Sure, sweetheart."

    jump second_nts

label ntr_path_cont:

    scene int1 with fade

    mct "[fname] has changed. It started with her hair—she was at the salon almost every other day. Then came the wardrobe makeover."

    mct "Every new outfit she picked seemed designed to show off her confidence, her allure. And I have to admit… she looks incredible."

    mct "But it’s not just the way she looks. The way she acts around me… that’s changed too."

    scene int4 with dissolve

    mct "I can still feel her love, but her gaze… it’s different now. There’s something in her eyes, something I can’t quite figure out. And then there’s that day at the park…"

    mct "I can’t shake it. Watching her with that total stranger, that old man… I didn’t know what to think. It was thrilling, sure, but at the same time, deeply unsettling."

    scene int1 with dissolve

    mct "Since that day, there have been times when she just disappears—quick trips, her phone off, completely unreachable. I can’t help but worry. Is she safe? Is she still the same [fname] I know?"

    scene int3 with dissolve

    mct "The choices I’ve made recently have led us here. I can’t help but wonder… what should I have done differently?"

    scene hm48_2 with fade

    mct "Maybe I pushed her into this too fast."

    scene hm52_2 with dissolve

    mct "God… The first time she touched Andrew’s massive cock… I can’t get it out of my head. It didn’t even fit in her hand."

    scene hd20_2 with dissolve

    mct "I remember the way he looked at [fname]… and the way she met his gaze, unflinching. Back then, I didn’t fully grasp it. But now? Now, everything is crystal clear."

    scene nm8_2 with dissolve

    mct "God… my heart is pounding. I know exactly where this is leading, and yet… I don’t stop it. Because deep down… I want this."

    scene nm20_b_2 with dissolve

    mct "I couldn’t look away… [fname]’s hips pressing against Theo’s bulge… And in that moment…"

    scene rt32_2 with dissolve

    mct "That look in [fname]’s eyes… burning, intense, completely unguarded. It wasn’t just desire—it was permission."

    mct " A silent invitation. And instead of resisting… I found myself wanting to see just how far she’d go."

    scene rt42_2 with dissolve

    mct "God… For the first time, someone else came on [fname]’s face. I had fantasized about it before, imagined the scenario in my mind."

    mct "But watching it unfold, watching her accept it… it hits different."

    mct "It happened so suddenly… Even now, I don’t know what I’m supposed to feel. Should I be angry? Should I stop this? Or… should I just embrace it?"

    scene vt115_2 with dissolve

    mct "[fname] handed me her ice cream, no words, just a soft, knowing smile before she turned and walked away. And in that moment, something deep inside me stirred."

    scene vt118_2 with dissolve

    mct "I saw her approach an old man sitting on a bench. My chest tightened, my pulse spiked. What was she doing?"

    mct "I didn’t need to hear their conversation—I already knew. God… it was happening. Right there, right in front of me. A fantasy I had played in my head so many times… but now it was real."

    scene vt123_2 with dissolve

    mct "When the old man unzipped his pants, I caught the look on [fname]’s face. Not a single trace of hesitation. No second thoughts. As if… as if she had been waiting for this."

    scene vt124_2 with dissolve

    mct "The lips I kiss every day were now wrapped around an old man's cock."

    mct "Is this a dream? Or have I finally brought my fantasies to life? It feels surreal, almost impossible… and yet, the thrill running through me is undeniable."

    scene int4 with fade

    mct "I wonder if taking her to that psychologist was a mistake. Did I start something I can’t control? Am I losing her? The thought eats away at me."

    scene int1 with dissolve

    mct "I can’t deny how happy she seems now. And I just can’t bring myself to take that away from her. If this new path excites her, then I’ll find a way to adapt."

    scene int4 with dissolve

    mct "I’ll give her space, support her—whatever this is. I don’t want to lose her. If this is what keeps her by my side, then I’ll endure it. Because despite everything… I still love her."

    scene black with dissolve

    pause (0.5)

    jump home_nmorning

label home_nmorning:

    scene nm1 with dissolve

    mct "I hear sounds coming from inside again. But… the voice isn’t familiar."

    scene nm2 with dissolve

    mc "Ahh… I should hurry up and get dressed. I’m already running late for work."

    scene nr1 with fade

    mct "Who is this guy? And how are they so caught up in their conversation that they don’t even notice I’m right here?"

    scene nr2 with dissolve

    mc "What's going on here?"

    scene nr3 with dissolve

    em "Oh, good morning! This is Taylor—the student I told you about, the one I met at the store. We got to talking, and he asked if I could tutor him. So, here we are."

    $ persistent.ty_unlock = True

    scene nr4 with dissolve

    ty "Yo, what’s up, man? Just grabbing some coffee. [fname]’s gonna help me out with numbers."

    scene nr5 with dissolve

    mc "Math, huh? And you’re just... here?"

    scene nr6 with dissolve

    em "Yeah, like I said, I’m tutoring him. Thought it’d be good to chat a little first, get to know him better before jumping into math."

    scene nr5 with dissolve

    mc "I see… But, [fname], you never mentioned tutoring anyone else besides Theo."

    scene nr6 with dissolve

    em "I didn’t think it was worth mentioning. Taylor needed help, so I offered. It’s really not a big deal."

    scene nr4 with dissolve

    ty "Yeah, man, just tryna get my numbers right. [fname]'s been mad patient with me."

    scene nr5 with dissolve

    mc "Right... Wasn’t expecting this. Uh, Taylor, just… make sure you don’t give [fname] a hard time, alright? You should be grateful she’s even helping you."

    scene nr7 with dissolve

    ty "Chill, man, I got it. We’re just vibin’—math and coffee, no drama. I appreciate it, for real. [fname]’s got skills, and I’m just here to learn."

    scene nr8 with dissolve

    em "Oh, please, you make it sound like I’m teaching you the secrets of the universe. It’s just math."

    scene nr9 with dissolve

    mc "Yeah, whatever. I’ve got work, so I’ll leave you two to it. Just… keep things cool, alright?"

    mc "We’ll talk later."

    scene nr10 with dissolve

    ty "For sure, man. We’re fine. No need to stress. And hey, take care of yourself, old man. We’ll hold down the fort here."

    scene nr11 with dissolve

    mct "Honestly, I don’t feel comfortable leaving [fname] alone with him in the house."

    scene nr12 with dissolve

    em "Sweetheart, don’t forget—we’re going to the movies tonight. You remembered, right?"

    scene nr13 with dissolve

    mc "Of course, I’ll be there. I talked to my boss, and I’ll leave work an hour early to meet you at the theater."

    scene nr12 with dissolve

    em "Alright, I’ll be waiting for you there. Don’t keep me waiting too long."

    scene nr14 with dissolve

    mc "Got it, babe. See you later."

    em "See you."

    ty "Bye-bye, daddy-o!"

    scene nr15 with dissolve

    mct "What an annoying guy."

    scene nr16 with fade

    ty "Alright, [fname], now that [name]’s outta the picture, we can get back to our convo."

    scene nr17 with dissolve

    em "Yes, where were we?"

    scene nr18 with dissolve

    ty "Oh yeah—so what’s the deal with you and math? You always been into numbers and all that?"

    scene nr19 with dissolve

    em "It’s always been a passion. I love the logic and structure. It’s like solving a puzzle."

    scene nr18 with dissolve

    ty "Man, puzzles? I’m trash at those. But hey, I got a knack for figuring people out. Like, I can already tell—you got crazy patience."

    scene nr20 with dissolve

    em "Well, patience is important, especially when teaching."

    scene nr21 with dissolve

    ty "Yeah, you’re like the queen of chill. I bet nothing ever gets to you."

    scene nr22 with dissolve

    em "I try to stay calm. It makes teaching easier."

    scene nr23 with dissolve

    ty "Yo, for real though, if I was a teacher, I’d lose my mind. Kids these days are wild."

    scene nr22 with dissolve

    em "It can be challenging, but also rewarding. Seeing someone finally understand something is a great feeling."

    scene nr24 with dissolve

    ty "That’s deep. You ever think about doing something else? Like, I dunno, rapping or something? You got that cool vibe."

    scene nr25 with dissolve

    em "Rapping?"

    scene nr26 with dissolve

    em "Hahaha."

    scene nr20 with dissolve

    em "That’s… an interesting idea. I don’t think I have the talent for that."

    scene nr27 with dissolve

    ty "Nah, you’d kill it. You got the presence. And, let’s be real, you’d look fire in a music video."

    scene nr28 with dissolve

    em "Well, thanks for the confidence boost, but I think I’ll stick to teaching."

    scene nr29 with dissolve

    ty "Fair enough. But if you ever wanna try, I’m your hype man."

    scene nr30 with dissolve

    em "I’ll keep that in mind."

    scene nr31 with dissolve

    ty "So, what do you do for fun? You seem like you’ve got some hidden hobbies."

    scene nr32 with dissolve

    em "Hmm..."

    scene nr33 with dissolve

    em "I enjoy reading, yoga, and sometimes painting."

    scene nr34 with dissolve

    ty "Yo, painting? That’s dope. I bet you’re good at it. You got that creative energy."

    scene nr35 with dissolve

    em "It’s just a hobby. Something to relax with."

    scene nr36 with dissolve

    ty "Man, you’re like a total package. Smart, creative, and chill. You’re like a dream teacher."

    scene nr37 with dissolve

    pause

    scene nr37_5 with dissolve

    em "You’re flattering me, Taylor."

    scene nr38 with dissolve

    ty "Nah, I’m just keepin’ it real, teach. Just speakin’ facts."

    scene nr37 with dissolve

    emt "He talks a lot of nonsense, but somehow, it’s entertaining. And, I have to admit… his physique is impressive. If the world wasn’t such a mess, I doubt he’d have any trouble keeping the girls away."

    scene nr38_5 with dissolve

    ty "Hey! what’s up? You got real quiet all of a sudden. What’s on your mind?"

    scene nr39 with dissolve

    em "Oh, nothing. Just thinking about what you said."

    scene nr40 with dissolve

    ty "Haha, so I got you thinkin’, huh? Maybe I’m more impressive than I thought."

    scene nr39 with dissolve

    em "Confidence isn’t necessarily a bad thing."

    scene nr34 with dissolve

    ty "Exactly. You can’t get anywhere without it, right?"

    scene nr41 with dissolve

    em "True, but too much confidence can sometimes get you into trouble."

    scene nr38 with dissolve

    ty "Hey, I like taking risks. That’s where the fun starts."

    scene nr46 with dissolve

    em "Taking risks, huh? You are an interesting one."

    scene nr40 with dissolve

    ty "Thanks, teach. And you’re more fun than I expected."

    scene nr48 with dissolve

    em "Seems like we’re surprising each other."

    scene nr49 with dissolve

    ty "Yeah? Well, I like surprises."

    ty "Makes things… more exciting."

    scene nr50 with dissolve

    em "Careful now, Taylor. Some surprises come with consequences."

    scene nr49 with dissolve

    ty "Oh, I can handle a little trouble. Question is… can you?"

    scene nr52 with dissolve

    em "Hmm… speaking of trouble, I think your ‘math lesson’ is over for today."

    scene nr49 with dissolve

    ty "Damn, just when it was gettin’ good. Guess I’ll have to wait for the next class."

    scene nr51 with dissolve

    em "Patience, Taylor. Maybe next time, you’ll actually learn something."

    scene nr49 with dissolve

    ty "Oh, I’m learnin’ plenty already, teach. You just don’t know it yet."

    ty "Damn, guess I should bounce then. But don’t worry, teach—I’ll be back. You know I ain’t the type to skip class."

    scene nr48 with dissolve

    em "It was a good chat, Taylor. Unexpected, but… interesting."

    jump ty_hug

label ty_hug:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"







    $ persistent.ty_scene1_unlocked = True

    scene nr34 with dissolve

    ty "Yeah? Then how ‘bout a proper goodbye? No handshake kinda thing—I'm talkin’ real warm, real close. A little farewell hug, teach?"

    scene nr53 with dissolve

    em "Of course, come here."

    scene nr54 with dissolve

    ty "Mmm, now that’s what I call a real goodbye. You smell good, teach. Damn."

    scene nr55 with dissolve

    em "Wow… that was a little warmer than I expected. Any tighter, and I might start thinking you don’t wanna leave."

    ty "Shit! I could stay if you ask me to."

    scene nr56 with dissolve

    em "That was a joke, Taylor."

    scene nr57 with dissolve

    ty "Aight, aight. But you playin’ with fire, teach. You lucky I got self-control."

    scene nr58 with dissolve

    emt "Is he… trying to kiss my chest? What?"

    scene nr59 with dissolve

    tyt "Damn, her tits smell sweet as hell. Like some warm vanilla or somethin'. If I nudge my face just a lil’ closer… I swear I’d be kissin’ them nipples already."

    tyt "Man, this fool [name] don’t even know how lucky he is. Got me feelin’ all kinds of jealous. Straight up blessed, that dude."

    emt "If I don’t stop him now, he’s gonna start wanting even more…"

    scene nr60 with dissolve

    em "Hmm, we’ll see about that next time. I expect you to be on time for our next session. And I promise… our conversation will be even more interesting."

    scene nr61 with dissolve

    ty "Oh, now you really got me hyped. You sayin’ I got another lesson comin’?"

    scene nr62 with dissolve

    em "Let’s just say… I’ll be giving you a few more lessons on what it means to be a man."

    scene nr65 with dissolve

    ty "Shit, you already my favorite teacher."

    scene nr64 with dissolve

    em "See you next week, Taylor."

    scene nr65 with dissolve

    ty "Yeah, yeah. But don't make me wait too long, teach. A dude’s gotta stay sharp."

    $ renpy.end_replay()

    scene cm1 with fade

    em "Ahh… Why weren’t you answering your phone?"

    scene cm2 with dissolve

    em "I’ve been stuck out here at night, not even sure if I should go in or not."

    scene cm3 with dissolve

    em "You are so dead, [name]!"

    scene cm4 with dissolve

    em "Huh."

    scene cm5 with dissolve

    em "Finally!"

    em "Where the hell have you been? I’ve been waiting outside for half an hour!"

    scene cm6 with dissolve

    mc "I’m so sorry, honey. An emergency meeting came up. The company’s in crisis, they’ve basically declared a state of emergency. I might even lose my job."

    scene cm7 with dissolve

    em "Wait, what?!"

    scene cm8 with dissolve

    em "Oh no… I’m so sorry, baby."

    scene cm9 with dissolve

    mc "No, no. I should be the one apologizing. I shouldn’t have left you waiting outside this long. Let’s just call it off this time. You should head home."

    scene cm10 with dissolve

    em "Seriously? I waited this long, I might as well have just gone in and watched the damn movie."

    scene cm11 with dissolve

    mc "And what would you even do at the movie without me?"

    scene cm12 with dissolve

    em "Don’t overthink it. I was mostly here for Scarlett Johansson anyway."

    scene cm13 with dissolve

    mc "Of course you were."

    scene cm14 with dissolve

    em "Besides, couldn’t you just ask James to set up a private screening for me? Please, please, please..."

    scene cm15 with dissolve

    mc "...Fine. I’ll call James. Just go inside already, don’t stand out here any longer. I’ll come pick you up after the movie."

    scene cm16 with dissolve

    em "Yes! Deal. You’re the best. Thank you, babe. Love you!"

    scene cm17 with dissolve

    mc "Love you too."

    scene cm18 with dissolve

    pause (0.2)

    scene cm19 with dissolve

    pause (0.2)

    scene cm20 with fade

    jm "[fname]! What a pleasant surprise to see you here tonight. Always a pleasure to welcome my favorite customer."

    scene cm21 with dissolve

    em "Hi, James. Thanks for setting up the private screening for me. [name] couldn’t make it, but I didn’t want to miss this. You know how curious I was about this film."

    scene cm22 with dissolve

    jm "Ah, [name]—always buried in work. Shame he couldn’t join you, but hey, that’s where I come in. I’ve got everything set up for you, no worries."

    scene cm23 with dissolve

    em "I appreciate that. It’s not every day you get to see something like this, and I wanted the full experience."

    scene cm24 with dissolve

    jm "And you’ll get it. The private room is all set—no interruptions, perfect sound, the best seat in the house. You’ll have the place all to yourself."

    scene cm25 with dissolve

    jmt "Damn, just look at those legs… smooth, tight, just beggin’ to be tasted. If I had my way, I’d run my tongue up every inch, slow and deep, till she’s shivering."

    jmt "I wonder… since [name] ain't around, maybe she’d let me hit it from the back just this once?"

    scene cm23 with dissolve

    emt "Those same looks again… If James ever got his hands on me, I don’t even want to imagine what he’d do."

    em "Sounds perfect. [name] really hyped this up for me. He kept going on about how impressive Sharlet Moansson is, saying I wouldn’t even be able to tell the difference with AI. Got me curious."

    scene cm26 with dissolve

    jm "Oh, you’re in for a treat. Sharlet is… well, let’s just say she’s unlike anyone else. Even if it’s not your usual kind of movie, you’ll appreciate the artistry. It’s almost unsettling how real she seems."

    scene cm23 with dissolve

    em "I’ve seen a few clips here and there. It’s fascinating what technology can do now. For me, it’s more about curiosity than anything."

    scene cm26 with dissolve

    jm "I get that. This isn’t just a movie—it’s an experience. The AI-enhanced theater brings everything to life in a way that’s hard to explain. You’ll feel like you’re stepping into another world."

    jm "You know… the world’s not exactly the place it used to be. Most people who come here just want to remember what it felt like—to be around a real woman. Ever since the disaster, business has been booming."

    scene cm25 with dissolve

    jm "Sometimes I wonder… what I’d give just to remember what it was like. To feel something real again."

    jmt "Man, I’d give anything for just one ride with you."

    scene cm27 with dissolve

    em "Wow. That was… a lot to unpack."

    scene cm8 with dissolve

    em "Setting aside the tragic part of what you just said… the film does sound impressive. I’m really looking forward to it."

    scene cm26 with dissolve

    jm "Yeah… and if you need anything—snacks, drinks, or even just a little company—you know where to find me."

    scene cm23 with dissolve

    em "Thanks, James, but I think I’ll manage. Just the movie and a little quiet time is all I need tonight."

    scene cm26 with dissolve

    jm " Suit yourself. But hey, the offer stands. Enjoy the show, [fname]. And don’t be a stranger—you know where to find me."

    scene cm23 with dissolve

    em "Thanks, James. I’ll let you know how it goes."

    emt "Yeah, I bet he’d do just about anything to get me alone in there with him."

    scene cm29 with dissolve

    jm "Oh, I’m sure you will."

    scene ca1 with fade

    em "Wow… This feels so real. The detail, the atmosphere… It’s like I’m actually there. [name] wasn’t kidding about how immersive this is."

    scene ca2 with dissolve

    emt "Okay… This is definitely not a movie to watch alone. Why did I think this was a good idea?"

    scene ca3 with dissolve

    em "I should’ve dragged [name] here with me. He’d probably love this… maybe even more than me."

    scene ca4 with fade

    em "God, this is intense. It’s like it’s pulling me in completely…"

    scene ca5 with dissolve

    em "What if someone comes in?"

    jump cnm_prv

label cnm_prv:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"






    $ persistent.cnm_scene1_unlocked = True

    scene ca6 with dissolve

    em "No… It’s private, right? James promised. I’m safe…"

    scene ca7 with dissolve

    em "This is crazy. I’ve never felt this way—not just because of the movie, but because of the risk I’m taking. That thrill… it’s really turning me on"

    emt "Should I… maybe take something off? No one’s coming in, and even if they do… so what?"

    emt "I’m more open to new experiences now. Just like that thrill I felt when I blow that old man on the park…"

    scene ca8 with dissolve

    emt "This feels the same."

    scene ca9 with dissolve

    emt "The thought of someone other than [name] seeing my breasts… it’s turning me on."

    scene ca10 with dissolve

    emt "But what if… it doesn’t stop at just my breasts?"

    scene ca11 with dissolve

    emt "What if I want more--if I want to feel the air on all my skin?"

    emt "My outfit is one piece… If I take it off, I’ll be completely exposed."

    scene ca12 with dissolve

    emt "That’s too risky."

    scene ca13 with dissolve

    emt "But that idea… it just makes me even hotter.."

    scene ca14 with dissolve

    emt "[name] isn’t here, and someone else could catch a glimpse of my most intimate parts."

    scene ca15 with dissolve

    emt "What if they don’t just look? Touches me? Fingers me…?"

    scene ca16 with dissolve

    emt "Mmm… just the thought of it… God, what’s happening to me?"

    scene ca15 with dissolve

    emt "I wasn’t even wearing panties… I can feel how soaked I am."

    scene ca16 with dissolve

    emt "Maybe… maybe I should just take everything off."

    scene ca17 with fade

    emt "No barriers… nothing in the way… just me, completely exposed."

    scene ca18 with dissolve

    emt "What if someone walks in? No… James said it’s my private room. It’s fine…"

    scene ca19 with dissolve

    emt "This feels so risky. But it’s exciting too."

    scene ca20 with dissolve

    emt "How many people have sat here? Done things here?"

    scene ca19 with dissolve

    emt "What if there’s… someone’s… left something behind? Like… on the seat?"

    scene ca20 with dissolve

    emt "What if… what if there’s… something on the chair? And now it’s on me?"

    scene ca21 with dissolve

    emt "What if it… touched my skin? What if it’s… on my panties right now? Or even…"

    scene ca22 with dissolve

    emt "No way… Is that…?"

    scene ca23 with dissolve

    emt "It is. Oh my God… someone actually…"

    emt "It’s right there, dried onto the seat… proof of someone else’s pleasure, someone else’s release."

    emt "How many people have been here, lost in the same heat I’m feeling now?"

    scene ca24 with dissolve

    emt "This is insane. I shouldn’t even be thinking about this. It’s disgusting… isn’t it?"

    emt "But then… why does my body feel even hotter?"

    scene ca25 with dissolve

    emt "What if I just… leaned in a little closer? Just to see… to be sure?"

    scene ca26 with dissolve

    emt "It’s real. Someone… some man, just like [name], sat here, unable to hold back. Right here, in this very spot."

    emt "What if I… what if I sat here too? If I let myself feel what they felt?"

    scene ca27 with dissolve

    emt "No. I can’t. That’s crazy. It could be anyone’s. I don’t even know who—"

    emt "But that’s what makes it so forbidden… or maybe even more exciting."

    emt "I shouldn’t want this. I shouldn’t be even thinking about this."

    scene ca28 with dissolve

    emt "My body is reacting on its own. It knows something my mind refuses to admit."

    scene ca27 with dissolve

    emt "No barriers… no layers in between… Just me… pressed against it."

    emt "It’s not [name]’s… but maybe that’s why I want it even more."

    scene ca26 with dissolve

    emt "I want to feel it—press myself against it, rub against it"

    emt "Would it feel different? Would it make me lose myself completely?"

    scene ca27 with dissolve

    emt "I shouldn’t do this. I shouldn’t… but…"

    emt "God… I want to."

    scene ca29 with dissolve

    emt "It’s touching my lips right now… Another man’s… not my husband’s… Mmm."

    scene ca30 with dissolve

    emt "I’ve been… tainted by someone else."

    emt "What if it… what if it seeps inside me?"

    scene ca31 with dissolve

    emt "What if it’s not just on my lips?"

    emt "What if it’s deeper… soaking into me?"

    scene ca32 with dissolve

    emt "Am I… being claimed by someone I don’t even know?"

    emt "It’s so filthy… so wrong… but I can’t stop thinking about it."

    scene ca33 with dissolve

    emt "My body is trembling—not from fear."

    emt "I should pull away… I should get up and leave."

    scene ca30 with dissolve

    emt "But instead… I want to press down even harder."

    scene black with dissolve

    pause(0.01)

    scene m_sld1 with dissolve

    em "This… this is insane. I can’t stop…"

    scene ca34 with dissolve

    em "Mmmm…"

    scene ca35 with dissolve

    "***Fap Fap Fap***"

    scene ca36_5 with dissolve

    emt "Is there someone behind me, or is it just my imagination?"

    emt "Yes, someone is there. And… and are those sounds I’m hearing?"

    emt "Oh my God. How long has he been there?"

    emt "Could it be [name]? No… it can't be. Why would he sneak up on me?"

    scene ca36 with dissolve

    emt "How did I not hear him come in? I can't even turn around now… He’s seen everything."

    emt "I guess the smartest thing to do is let him finish and leave. Otherwise, this could get even more complicated. I’ll just act like he’s not there."

    scene ca37 with dissolve

    emt "Being watched…"

    scene ca38 with dissolve

    emt "It turns me on."

    scene ca39 with dissolve

    emt "What the hell?"

    emt "Too close, too close, too close."

    scene ca40 with dissolve

    emt "Ahh... my heart is pounding."

    scene ca41 with dissolve

    emt "If I turn my head… it feels like it could end up in my mouth."

    scene ca42 with dissolve

    emt "Ignoring him must have made him even bolder."

    scene ca43 with dissolve

    emt "Ahhh... I’m so turned on right now."

    emt "That scent… it’s so strong, overwhelming."

    scene ca44 with dissolve

    emt "It’s so strong, overwhelming. I can’t even describe. It’s masculine, raw, intoxicating"

    scene ca45 with dissolve

    emt "Mmm, I really need to fuck."

    scene black with dissolve

    pause(0.01)

    scene m_cnm1 with dissolve

    emt "Mmm."

    scene ca46 with flash

    pause

    scene ca47 with flash

    pause

    scene ca48 with flash

    emt "He came all over me. What am I going to do now? I'm a mess… [name] is coming to pick me up soon."

    scene ca49 with dissolve

    emt "I have nothing to clea. I have no choice but to put my clothes back on, all dirty like this."

    scene ca50 with dissolve

    emt "I have no choice… I have to put my clothes back on, just like this. Sticky, messy… tainted."

    emt "I feel so dirty. The warmth of it is still clinging to my skin… soaking into me."

    emt "I just hope [name] doesn’t try to hug me when he picks me up. I don’t know if I can handle that right now."

    emt "And the worst part? I still feel so turned on."

    emt "I should feel ashamed. I should be disgusted. But instead, I can still feel my body aching for more."

    emt "Even now… my legs feel weak, my breath is shaky."

    scene ca51 with dissolve

    emt "As soon as I get home… I need to have sex with [name]."

    em "I should get dressed... I really crossed the line today."

    $ renpy.end_replay()

    scene ca52 with dissolve

    em "Done."

    scene ca53 with dissolve

    em "Oh, he's here."

    em "Hey, you here?"

    em "No, no, don’t get out of the car honey. I’m coming to you."

    scene black with fade

    "End of the version 0.5. You can save here."


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
