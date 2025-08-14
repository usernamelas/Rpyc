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

    $ name = renpy.input("Nama saya", default ="Jake", length=15)
    $ persistent.name = name

    if name == "":
        $ mc = "Jake"
        $ mct = "Jake Tought"menu:"Apakah Anda yakin tentang Jake?"
            "Ya":
                Berhenti Sebentar"No,Please.":

                pause



    $ fname = renpy.input("Nama istri saya adalah", default ="Emily", length=15)
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

    mc "Aku tahu sayang, itu sangat rumit. Saya tidak percaya sudah hampir 1 tahun."adegan st6 dengan larut

    mct"This is my loyal wife, [fname]. We have been married for 5 years. We really love each other. We were happy but after that incident our life became a mess."mct"End of 2026 a virus occurred. Every single women are dead due to this virus except [fname] and few ones. Now everyone wants to be with my wife. I can't decide if I'm lucky or unlucky."mct"Tapi saya tahu satu hal yang selalu kita cintai satu sama lain apa pun yang terjadi."adegan hitam dengan larut

    berhenti sebentar

    adegan hm1 dengan fade

    MC"Sayang, apakah kamu ingin bicara?"adegan hm2 dengan larut

    berhenti sebentar

    adegan hm2 dengan larut

    MC"Saya pikir kita harus berbicara sekarang. Kami tidak dapat menunda konservasi ini lagi."adegan hm4 dengan larut

    em"Saya tidak tahu harus berbuat apa."adegan hm3 dengan larut

    MC"Kami mencoba setiap hari meskipun kami tahu faktanya saya tidak subur. Humanity migh akan berakhir karena kita dan saya merasa bersalah. Jika Anda mencoba dengan seseorang ..."adegan hm4 dengan larut

    em"Sayang, aku tidak bisa. Aku mencintaimu."adegan hm5 dengan larut

    berhenti sebentar

    adegan hm5 dengan larut

    ANC"Hanya 5 dari 15 wanita yang selamat setelah virus mampu melahirkan."adegan hm6 dengan larut

    ANC"Para ilmuwan memprediksi penurunan yang signifikan dalam populasi manusia, yang berpotensi menandakan akhir umat manusia."adegan hm7 dengan larut (1.0)

    ANC"Berita baiknya adalah bahwa keempat wanita ini membuat banyak pengorbanan dan menjadi penyelamat kemanusiaan."adegan hm8 dengan larut

    ANC"Sayangnya, ini tidak cukup."adegan hm9 dengan larut

    ANC"Masih belum ada berita dari wanita yang tinggal di kota-york kota."adegan hm10 dengan larut

    em"Sayang..."adegan hm11 dengan larut

    em"Saya akan mencoba. Saya harus ..."adegan hm12 dengan larut

    MC"Kita harus. Aku tidak akan pernah membiarkanmu sendirian. Aku akan selalu bersamamu."adegan hm11 dengan larut

    em"Terima kasih, sayang. Aku tidak bisa melakukan ini tanpamu, apa yang akan kita lakukan sekarang?"adegan hm12 dengan larut

    MC"Hanya satu orang yang muncul di pikiran saya."adegan hm11 dengan larut

    em"Siapa?"adegan hm13 dengan larut

    MC"Ermm ... yah ..."adegan hm14 dengan larut

    em"Menumpahkan kacang."adegan hm15 dengan larut

    MC"Dengan baik. Andrew?"adegan hm16 dengan larut

    em"B-tapi dia adalah sahabatmu."adegan hm15 dengan larut

    MC"Itu sebabnya saya menyarankannya, Andrew adalah homie saya yang bisa saya percayai."adegan hm17 dengan larut

    em"Yah saya sangat menyukai Andrew tapi ini sesuatu yang berbeda. Saya tidak yakin .."adegan hm18 dengan larut

    MC"Saya tahu ini sulit bagi kami berdua. Tapi kita harus. Jangan khawatir saya tidak mendorong Anda apa pun. Kami dapat bergerak langkah demi langkah sampai Anda merasa baik -baik saja."adegan hm19 dengan larut

    em"Oke."adegan hm19_5 dengan larut

    MC"Hei Andrew, aku membutuhkanmu. Bisakah kamu segera datang?"adegan hm19_5 dengan larut

    MC"Ya ya, saya akan menjelaskan saat Anda tiba."adegan hm20 dengan larut

    berhenti sebentar

    adegan hm22 dengan larut

    mct"Ini Andrew, saudaraku. Kami sudah menjadi teman terbaik sejak kami berusia lima tahun."mct"Dia selalu mendukung saya, terutama ketika harus berurusan dengan pengganggu selama masa kecil saya. Kami telah berbagi ikatan yang kuat sejak itu."mct"Andrew and [fname] get along pretty well too."adegan hm21 dengan larut

    aw"Apa masalahnya? Mengapa saya harus segera datang?"

    $ persistent.aw_unlock = True

    scene hm22 with dissolve

    mc "Kamu harus membantu kami."adegan hm21 dengan larut

    aw"Tentu, tentang whaat?"adegan hm23 dengan larut

    MC"There's no easy way to say this so I'll just say it directly. Get [fname] pregnant."adegan hm24 dengan larut

    aw"Apa fuuuck? Apakah kamu gila ??"adegan hm25 dengan larut

    MC"Anda tahu kondisi kesehatan saya. Kita harus melakukan ini demi kemanusiaan."adegan hm26 dengan larut

    aw"Dan apakah Anda baik dengan itu?"adegan hm27 dengan larut

    jeda (0,5)

    adegan hm28 dengan larut

    em"Ya."adegan hm29 dengan larut

    aw"Dude, I'm not sure about that. I mean [fname] is perfectly perfect. I really want to fuc, Ermm, I mean help you and [fname]."

    aw "Apakah Anda yakin ini tidak akan membahayakan hubungan Anda?"

    scene hm30 with dissolve

    mc "Kami Sudah Memicarakan Hal Itu, Tenjak Ada Yang Akan Mempengaruhi Pernikahan Kami. Ini Adalah Tugas Kita, Begitulah Adanya. Sayang Benar?"

    scene hm31 with dissolve

    em "Ya, Sayang."

    scene hm32 with dissolve

    mc "Jadi Apa Yang Kamu Katakan Bung? Apakah Anda Masuk Atau Keluar?"

    scene hm33 with dissolve

    aw "Im in."adegan hm34 dengan larut

    em"Saya tidak ingin terburu -buru apa pun yang saya sudah merasa gugup."adegan hm35 dengan larut

    MC"Jangan khawatir sayang, aku akan selalu bersamamu."

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

    aw "So when do we do it? "menu:"Push [fname] to sex":

            $ ntr_point += 1

            scene hm37 with dissolve

            mc "Now... There is no need to wait. There's no point in prolonging it. Just do it."adegan hm38 dengan larut

            em"Apakah kamu serius sekarang? ASTAGA! Bukankah kita membicarakan hal ini?"adegan hm39 dengan larut

            aw"Oke dinginkan teman -teman. Mengapa kita tidak meminumnya perlahan?"adegan hm40 dengan larut

            aw"Mari kita mengenal tubuh satu sama lain untuk saat ini."adegan hm41 dengan larut

            em"???"adegan hm42 dengan larut

            em"Seberapa besar hal itu?!"adegan hm43 dengan larut

            mct"I cant imagine [fname] take all of it."adegan hm44 dengan larut

            mct"Mengapa jantungku berdetak lebih cepat? Mengapa saya menjadi bersemangat?"adegan hm45 dengan larut

            jeda (0,5)

            adegan hm47 dengan larut

            jeda (0,5)

            adegan hm48 dengan larut

            berhenti sebentar

            adegan hm49 dengan larut

            berhenti sebentar

            adegan hm51 dengan larut

            em"Haruskah saya merasa bersalah karena menyukainya?"adegan hm50 dengan larut

            em"Itu nyaris tidak cocok di tangan saya."adegan hm52 dengan larut

            aw"Ah, benarkah? Anda adalah gadis pertama yang mengatakan itu. Hahahah!"adegan hm53 dengan larut

            mct"Saya tidak percaya saya membiarkan ini tetapi kita harus bertahan."adegan hm53_5 dengan larut

            mct"I wonder how [fname] is feeling right now?"adegan hitam dengan larut

            jeda (0,01)

            adegan hj1 dengan larut

            em"mmmm ..."aw"Oh-hhh! Tanganmu sangat kecil dan lembut."adegan hj2 dengan larut

            em"hhh ..."aw"Terus berlanjut..."adegan hm54 dengan larut

            berhenti sebentar

            adegan hm55 dengan larut

            mct"Kotoran!"adegan hm57 dengan larut

            em"Saya pikir kita harus berhenti untuk hari ini. Banyak yang harus diambil."adegan hm58_b dengan larut

            aw"Come on [fname]..."adegan hm59_b dengan larut

            aw"Kami sudah dalam hal ini."adegan hm60_b dengan larut

            aw"Kami tidak bisa berhenti begitu saja sekarang. Mungkin ini akan membuat Anda dalam mood."adegan hm61_b dengan larut

            berhenti sebentar

            adegan hm62_b dengan larut

            berhenti sebentar

            adegan hm64_b dengan larut

            mct"Holly! He literally put his penis between her legs. How will [fname] react to this?"mct"It's so exciting, I feel strange and really want to see what happens next. It looks like that big wet thing is inside [fname]."adegan hm63_b dengan larut

            EMT"Dia memelukku dengan sangat erat. Aku tidak bisa menghentikannya memaksaku melawannya. Ada sesuatu yang besar di antara kedua kakiku."EMT"Saya bisa merasakan kehangatan dan kekerasan seolah -olah saya tidak mengenakan celana pendek. Apa perasaan basah ini? Apakah saya basah?"EMT"Oh no. It's so embarrassing for [name] to see me like this. I don't want to go too fast. I have to stop it."em"BERHENTI!!!"adegan hm65_b dengan larut

            em"Andrew, tolong mengerti. Ini luar biasa bagi saya. Saya perlu waktu untuk memproses semuanya."adegan hm66_b dengan larut

            aw"Tapi kami tidak mampu menunggu. Kami memiliki tanggung jawab di sini."adegan hm67_b dengan larut

            em"Tidak, Andrew. Saya bilang tidak."adegan hm68_b dengan larut

            MC"We will continue however [fname] wants."adegan hm69_b dengan larut

            aw"Baik, lakukan dengan cara Anda. Tapi jangan lupa tujuannya di sini."aw"Saya pikir saya harus pergi sekarang. Saya akan memberi Anda ruang untuk memproses semua yang terjadi. Selamat tinggal."

            $ renpy.end_replay()
        "Encourage [fname]":


            $ nts_point += 1

            scene hm37 with dissolve

            mc "I don't want [fname] to feel bad."adegan hm38_a dengan larut

            MC"Mari kita lanjutkan langkah demi langkah. Kita harus mulai dari suatu tempat. Apakah Anda baik -baik saja dengan Andrew telanjang?"adegan hm40 dengan larut

            aw"Why am I the only naked person in the room, [fname] you have to naked too."adegan hm42_a dengan larut

            em"Saya belum merasa nyaman."adegan hm41_a dengan larut

            aw"Oke, tapi akhirnya kamu akan telanjang ..."adegan hm41 dengan larut

            em"???"adegan hm42 dengan larut

            em"Seberapa besar hal itu?!"adegan hm43 dengan larut

            mct"I cant imagine [fname] take all of it."adegan hm44 dengan larut

            mct"Mengapa jantungku berdetak lebih cepat? Mengapa saya menjadi bersemangat?"adegan hm45 dengan larut

            jeda (0,5)

            adegan hm47 dengan larut

            jeda (0,5)

            adegan hm48 dengan larut

            berhenti sebentar

            adegan hm49 dengan larut

            berhenti sebentar

            adegan hm51 dengan larut

            em"Haruskah saya merasa bersalah karena menyukainya?"adegan hm50 dengan larut

            em"Itu nyaris tidak cocok di tangan saya."adegan hm52 dengan larut

            aw"Ah, benarkah? Anda adalah gadis pertama yang mengatakan itu. Hahahah!"adegan hm53 dengan larut

            mct"Saya tidak percaya saya membiarkan ini tetapi kita harus bertahan."adegan hm53_5 dengan larut

            mct"I wonder how [fname] is feeling right now?"adegan hitam dengan larut

            jeda (0,01)

            adegan hj1 dengan larut

            em"mmmm ..."aw"Oh-hhh! Tanganmu sangat kecil dan lembut."adegan hj2 dengan larut

            em"hhh ..."aw"Terus berlanjut..."adegan hm54 dengan larut

            berhenti sebentar

            adegan hm55 dengan larut

            mct"Kotoran!"adegan hm57 dengan larut

            em"Saya pikir kita harus berhenti untuk hari ini. Banyak yang harus diambil."adegan hm67 dengan larut

            aw"Ya, ini intens. Kami tidak perlu terburu -buru."adegan hm68 dengan larut

            MC"Tentu saja, mari kita sambat -lambatnya. Kita semua bersama -sama, tidak perlu mendorong diri kita terlalu keras."adegan hm67_b dengan larut

            em"Terima kasih. Saya hanya perlu waktu untuk memproses semuanya."adegan hm69 dengan larut

            aw"Of course, [fname]. We'll go at your pace. "adegan hm70 dengan larut

            MC"Ayo duduk dan bicara sebentar. Kita bisa mencari cara terbaik untuk menangani ini bergerak maju."adegan hm71 dengan larut

            aw"Saya pikir yang terbaik jika saya pergi sekarang. Saya akan memberi Anda beberapa ruang untuk memproses apa yang terjadi. Anda harus duduk dan berbicara. Selamat tinggal."adegan hm67_b dengan larut

            em"Tunggu sebelum Anda pergi…"adegan hm73 dengan larut

            berhenti sebentar

            aw"Oh!"adegan hm74 dengan larut

            berhenti sebentar

            adegan hm75 dengan larut

            berhenti sebentar

            aw"Berengsek!!!"adegan hm72 dengan larut

            em"Anda bisa mengucapkan terima kasih ciuman atau hadiah lain kali ... selamat tinggal."adegan hm71 dengan larut

            aw"Oke ... saya- Saya kira sekarang karena saya punya hadiah, saya harus pergi."

            $ renpy.end_replay()


    scene hm76 with fade

    mc "Itu ... intens."adegan hm77 dengan larut

    em"Ya, saya tidak percaya kami benar -benar melakukannya."adegan hm76 dengan larut

    MC"Aku tahu. Itu sangat nyata. Saya merasa seperti kita berada dalam semacam mimpi buruk yang aneh."adegan hm78 dengan larut

    em"Apakah Anda pikir kami melakukan hal yang benar?"adegan hm76 dengan larut

    MC"Aku tidak tahu. Tapi pilihan apa yang kita miliki? Ini bukan hanya tentang kita lagi. Ini tentang kemanusiaan."adegan hm79 dengan larut

    em"Saya mengerti, tapi ... masih terasa salah. Maksud saya, kami saling mencintai, dan sekarang kami melibatkan orang lain dalam sesuatu yang sangat pribadi."adegan hm76 dengan larut

    MC"Saya merasakan hal yang sama. Ini memalukan, tapi ... kita harus mencoba, kan?"adegan hm77 dengan larut

    em"Ya, saya kira begitu. Saya tidak pernah membayangkan hidup kita akan berubah seperti ini."adegan hm76 dengan larut

    MC"Aku juga tidak. Tapi apa pun yang terjadi, kita akan menghadapinya bersama. Anda tidak sendirian dalam hal ini."adegan hm80 dengan larut

    em"Terima kasih. Saya sangat membutuhkannya sekarang. Itu sangat luar biasa."adegan hm81 dengan larut

    MC"Aku tahu, sayang. Kami akan melewati ini."adegan hm80 dengan larut

    em"Anda benar. Kami akan melewati ini. Bersama."adegan hm81 dengan larut

    MC"Bersama..."adegan hm82 dengan larut

    mct"Ketika saya menahannya, aroma yang akrab menghantam saya. Air mani."mct"Sisa -sisa dari apa yang baru saja terjadi. Yang mengejutkan saya, itu membangkitkan saya."mct"Tubuh saya merespons terlepas dari kebingungan dan rasa bersalah pikiran saya."adegan hm83 dengan larut

    mct"Oh tidak, tidak sekarang. Saya tidak bisa membiarkan dia memperhatikan."adegan hm84 dengan larut

    em"Saya merasa sangat malu dan bersalah karena mengatakan ini, tapi ... saya benar -benar terangsang sekarang. Bisakah kita pergi ke kamar tidur kita?"adegan hm85 dengan larut

    MC"Benar-benar? Maksud saya, saya - tentu, jika itu yang Anda inginkan."adegan hm86 dengan larut

    mct"So, [fname] was affected by what just happened too. After all, she's a woman."adegan hm87 dengan larut

    MC"Hei, tidak apa -apa. Kita bisa pergi ke kamar tidur. Tidak ada yang perlu malu. Kita bersama -sama, ingat?"adegan hm84 dengan larut

    em"Terima kasih. Saya hanya perlu merasa dekat dengan Anda sekarang."adegan hm85 dengan larut

    MC"Aku tahu sayang tapi bagaimana dengan ini? Ada bioskop erotis yang saya ingat dari masa lalu. Ini bisa menjadi gangguan yang menyenangkan dan membantu kami menghilangkan keanehan dari sebelumnya. Bagaimana menurutmu?"adegan hm88 dengan larut

    em"Benar-benar? Kedengarannya ... menarik. Ayo lakukan!"adegan hm89 dengan larut

    MC"Baiklah, mari kita cepat dan pergi sebelum bioskop ditutup."adegan hm90 dengan larut

    berhenti sebentar

    adegan CS1 dengan larut

    em"Saya sudah memikirkannya lagi. Apakah Anda yakin bioskopnya aman untuk saya? Saya sedikit khawatir."adegan CS2 dengan larut

    MC"Jangan khawatir, sayang. Saya tahu pemiliknya dan kami memiliki sejarah yang baik. Kami dapat mempercayai dia untuk memberi kami tempat pribadi yang bagus."adegan CS3 dengan larut

    MC"Selain itu kami memilikinya untuk melindungi kami."adegan cs3_5 dengan larut

    berhenti sebentar

    adegan CS4 dengan larut

    em"Terkadang saya lupa mereka ada di sekitar, tetapi saya tidak mempercayai mereka. Apakah Anda pikir mereka akan memperlakukan kami dengan cara yang sama ketika perjanjian pemerintah kami berakhir?"adegan CS5 dengan larut

    MC"Bisakah Anda berhenti!"adegan cs6 dengan larut

    MC"Sorry, [fname]. We don’t need to worry about that right now. Let’s just have a good time."adegan CS7 dengan larut

    em"Benar. Tidak ada gunanya memikirkan hal ini sekarang. Kami di sini untuk bersantai, jadi mari kita masuk ke dalam."

    scene ch1 with fade

    $ persistent.jm_unlock = True

    jm "Hei, sobat. Selamat datang! Saya sudah mengharapkan Anda."adegan ch2 dengan larut

    MC"Hai. Terima kasih telah menyiapkan ruangan untuk kami dengan sangat cepat. Maaf sudah menelepon pada menit terakhir."adegan ch3 dengan larut

    jm"Jangan khawatir, kawan. Saya selalu punya kamar untuk Anda, kapan saja. Hubungi saya, dan saya akan memastikan tempat yang siap untuk Anda."

    jm "Jika Perlu, Saya Bahkan Akan Menutup Salah Satu Salon SAYA SHINGGA ENA BERDUA DAPAT MEMILIKI Privasi."

    scene ch4 with dissolve

    mct "Ini Adalah James, Pemilik Teater Dewasa. Berlahun -Tahun Yang Lalu, Andrew Dan Saha Dulu Datang Ke Sini. Terkadar, Dia Mendirikan Kamar Pribadi Hanya UNTUK Kita Dan Pacar Kita."

    mct "James Telah Memperhatikan Kami Lebih Dari Yang Bisa Saha Hitung. Dia Bahkan Akan Meminjamkan Uang Kepami Saat Saat Kami Pendek."

    mct "Namun Seiring Waktu, Kami Kehilangan Kontak. Terakhir Kali Kami Bertemu Adalah Ketika Kami Pergi UNTUK MENYAMPAIKAN BELASUMKAWA SETELAH DIA KEHILangan ISTRINYA."

    scene ch5 with dissolve

    mc "Terima Kasih, James."

    scene ch6 with dissolve

    jm "SUATU KEHORMATAN UNTUK BERTEMU ISTRI Uda. SAYA HARUS MENGIKAN, ENA MEMILIKI WANITA YANG SANGAT COAN DAN ENLAN."

    scene ch7 with dissolve

    em "Terima Kasih Banyak, James. SENANG Bertemu GANGAN UNA JUGA."

    scene ch8 with dissolve

    jm "Kalau Begitu, Pergi Ke Dalam Dan Buat Dirima Di Rahat. Menikmati!"

    scene ch9 with dissolve

    mc "Terima Kasih, James."

    em "Terima Kasih"

    scene cs7_1 with fade

    pause

    scene cs7_2 with dissolve

    em "Wow. Tempat ini Jauh Lebih Bersih Dan ... Lebih Baik Baik Dari Yang Saha Harapkan!"

    scene cs7_3 with dissolve

    mc "Premium Kualitas."

    scene cs7_4 with dissolve

    mc "Mari Kita Duduk."

    scene cs7_5 with dissolve

    em "SAYA INGIN MELPASKAN INI."

    scene cs8 with dissolve

    pause

    scene cs8_5 with dissolve

    em "Mmm ..."adegan CS9 dengan larut

    em"Hhh ..."adegan CS10 dengan larut

    mct"She’s so wet, and I haven’t even started yet. I know what happened at home turns [fname] on even more, but it’s weird that she is still in the mood."mct"I like this version of [fname], but I can’t help wondering if it's Andrew's influence."adegan cs11 dengan larut

    em"Tenang, bocah terangsang."adegan CS12 dengan larut

    em"Jika kita akan bergerak secepat ini, kita bisa tinggal di rumah."adegan cs12_5 dengan larut

    MC"Saya tahu melakukannya di depan umum membuat Anda lebih banyak lagi."adegan cs12_6 dengan larut

    MC"Kemarilah."adegan cs13 dengan larut

    em"Seseorang tahu bagaimana menyenangkan istrinya. Anak yang baik."

    mc "ITU TUGAS SAYA DAN TUGASYA MENELEPON SENA."

    scene cs13_1 with dissolve

    em "Berbohong."

    em "Turun."adegan cs13_2 dengan larut

    MC"Ya, Bu."

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

    em "Karena Penismu, Tampan."

    scene rc2 with dissolve

    mc "Anda semakinin ketat ..."

    em "Ahhh ...."adegan cs14 dengan larut

    JMT"Saya harus lebih dekat."adegan CS15 dengan larut

    JMT"Lubang merah muda."JMT"Saya ingin menjilatnya."adegan cs16_5 dengan larut

    jm"*Mencucup*"adegan cs16 dengan larut

    JMT"Mari kita lihat apakah Anda bisa mengambil ujung jari saya."adegan cs17 dengan larut

    berhenti sebentar

    adegan cs18 dengan larut

    berhenti sebentar

    adegan CS19 dengan larut

    em"Mmm .. ah !!"adegan CS20 dengan larut

    em"Oh!! Sayang itu baru."mct"Saya tidak tahu apa yang dia bicarakan, tetapi saya tidak ingin merusak suasana hati dengan mengajukan pertanyaan."adegan CS21 dengan larut

    JMT"Sekarang, mari kita lihat apakah kita bisa melebarkan lubang Anda sedikit."adegan CS22 dengan larut

    em"Ahh, itu menyakitkan!"adegan CS23 dengan larut

    em"Mmm, lebih keras!"adegan cs23_5 dengan larut

    em"[name], do it harder!"adegan hm44 dengan eye_shut

    mct"Apa ini sekarang? Saya tidak ingin mengingat ini sekarang."adegan hm48 dengan larut

    mct"Kotoran! Saya tidak bisa mengendalikan pikiran saya. Mengingat hal -hal ini terasa benar -benar…"mct"sangat berbeda ..."adegan cs23 dengan eye_open

    em"Mmm ..."adegan hm51 dengan eye_shut

    EMT"Itu ..."EMT"Sangat besar."EMT"Rasanya seperti dari dunia lain."adegan hm52 dengan larut

    EMT"Jika ada di dalam diri saya sekarang, itu akan menghancurkan saya. Saya pikir saya hanya bisa mengambil ujungnya."EMT"Ahhh… Shit. Don’t think about this right now, don’t think about this right now, [fname]!"adegan cs24 dengan eye_open

    em"Hhh .."adegan CS25 dengan larut"*Mengendus*-*mengendus*"adegan CS26 dengan larut

    JMT"Saya harus pergi sekarang."adegan CS27 dengan larut

    JMT"Tapi segera, hal yang masuk akan ada lidahku."adegan hitam dengan larut

    jeda (0,01)

    adegan rc2 dengan larut

    em"*Bernafas sangat*ahhh ...*bernapas berat*"

    mc "* SANGAT BERNAFAS* SAYA AKAN CUM. *Bernafas Sangan*"

    em "* Bernafas Sangan* cum di dalam diriku. *Bernafas Sangan*"

    scene cs28 with dissolve

    em "*(Berteriak)*Ahh !!"

    scene cs29 with dissolve

    mc "*Ohh-hhh !!!"

    scene cs30 with dissolve

    pause

    scene cs13_1 with dissolve

    em "[name]. This was so... so good. Ahh… *Heavily Breathing*"

    scene cs13_2 with dissolve

    mc "Saya Suka Vagina Hangat Dan Ketat Anda. Ohh. *Bernafas Sangan*"

    scene cs13_3 with dissolve

    pause

    scene cs13_5 with dissolve

    em "Saya Sangat Lelah, Saya Perlu Mengisi Ulang Besok. Ayo Pulu, Sayang."

    scene cs13_2 with dissolve

    mc "Oke, Sayang."

    $ renpy.end_replay()

    scene ch10 with fade

    jm "Halo, Pasangan Muda Kami Yang Conalk!"

    scene ch11 with dissolve

    mc "Terima kasih unkul semuanya James."

    scene ch12 with dissolve

    jm "Tidak Perlu Berterima Kasih Kepada Saya; Lagi Pula, Saya Melayani Kemanusiaan. SAYA AKAN SELALU ADA DI SINI UNTUK Kalian."

    jm "MingGu Depan, film Baru Akan Keluar. Dan Tebak Siapa Bintangnya? Anda tidak Akan Pernah Menebak."

    scene ch13 with dissolve

    jm "Sharlet Moansson!"

    scene ch14 with dissolve

    em "Apakah dia masih menyembunyikan ??"

    mc "Benar-Benar?! Apakah dia MASIH HIDUP DAN MEMBINTangi Film -Film Dewasa?"

    scene ch15 with dissolve

    jm "Hahahah. Anda Berharap. Maksudku, Kita Semua Berharap."

    jm "Film ini Dibuat Gelang AI, Maksud Saya, Hanya Bagian -delannya Yang Dianimasikan. Semua Orang ITU NYATA, KECUALI DIA."

    scene ch16 with dissolve

    em "[name]! We need to go next week. I really want to see what she looks like."

    scene ch17 with dissolve

    jm "Even if [name] can't make it, I'll definitely be waiting for you!"

    scene ch18 with dissolve

    mc "Jangan Khawatir, Saya. Bagamanapun, Kita Harus Pergi Sekarang. Sampai Lompa."

    em "Bye, James ..."

    scene ch19 with dissolve

    pause

    scene ch20 with dissolve

    jm "*Mencium*"adegan ch21 dengan larut

    jm"Hmm..."adegan ch22 dengan larut

    jm"Lezat."adegan cs4 dengan fade

    em"Sayang, ada sesuatu yang mengganggu saya."adegan cs4_5 dengan larut

    MC"Apakah sesuatu terjadi?"adegan cs4_6 dengan larut

    em"Tidakkah menurut Anda sikap James berubah setelah film?"adegan cs4_5 dengan larut

    MC"Apa maksudmu?"adegan cs4_6 dengan larut

    em"Saya tidak tahu, itu seperti cara dia memandang saya berbeda. Seperti dia sedang menatapku."adegan cs4_5 dengan larut

    MC"Ya, Anda mungkin benar. Anda satu -satunya wanita yang dia lihat dalam waktu yang lama, jadi dia mungkin telah bertindak sedikit aneh."

    mc "TAPI JAMES ADALAH PRIA YANG BAIK. Dan Selain Itu, Saya di Sini Bersamamu."

    scene cs4_6 with dissolve

    em "Bahkan Jika Bukan Itu Masalahnya, Saya Telah Memutuskan Saya Tidak Ingin Memikirkanyaa Sekarang. Kami memilisi Pekerjaan Besok; Kita Perlu Bersiap -SIAP. Mari Kita Pulu, Mandi, Dan Tidur."

    scene cs4_5 with fade

    mc "SAYA SANGAT MEMATUHKANNAA JUGA."

    scene pass1 with dissolve

    pause

    scene hd1 with dissolve

    mc "Masih Belum Berpakaan?"

    scene hd2 with dissolve

    em "SAYA SUDAH BERPAKAIAN."

    scene hd3 with dissolve

    mc "Bukankah Theo Datash Hari ini?"

    scene hd2 with dissolve

    em "Ya, dia."adegan hd1_5 dengan fade:
        subpixel true
        Yalign 1.0
        jeda 1.5
        Linear 7.0 Yalign 0.0

    berhenti sebentar

    adegan hd3 dengan larut

    MC"Bukankah pakaian Anda sedikit terbuka?"adegan hd4 dengan larut

    em"Hahahahah."adegan hd4_5 dengan larut

    em"Dia hanya anak -anak."adegan hd5 dengan larut

    MC"Anak?! Dia berusia 18 tahun, dan Anda tahu seperti apa usia anak laki -laki itu."

    mc "Hormon Mereka Melalui ATAP, Dan Anda Satu -Satunya Wanita Yang Dilihatnya."

    scene hd7 with dissolve

    "Ketukan! Ketukan! Ketukan!"

    scene hd6 with dissolve

    em "Tollong Bertindak normal."

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

    em "Selamat Datang Theo!"

    scene hd11 with dissolve

    th "Hey, [fname]."

    scene hd12 with dissolve

    mc "Ada Apa Teman?"

    scene hd13 with dissolve

    th "Saya Baik Tuan…"

    scene hd14 with dissolve

    mc "Just call me [name]."

    scene hd15 with dissolve

    th "Okay. Thanks [name]!"

    scene hd16 with dissolve

    em "Baiklah, Cukup Berbicara. Mari Kita Mulai."

    scene hd17 with dissolve

    em "Mari Kita Lohat apa Yang Sedang Kita Kerjakan Hari Ini!"

    scene hd18 with dissolve

    th "Turunan ..."

    scene hd19 with dissolve

    em "Lagi?!"adegan hd20 dengan larut

    th"Ya."adegan hd21 dengan larut

    em"Oh sayang, maafkan aku. Kita bisa menanganinya. Jangan khawatir."adegan hd21_5 dengan larut

    berhenti sebentar

    adegan hd22 dengan larut

    mct"Anak ya?"menu:"Hentikan Theo":

            $ stp_th += 1

            $ nts_point += 1

            scene hd23_a with dissolve

            mc "Hey Theo!"adegan hd24_a dengan larut

            th"Hhh-uhh?"adegan hd25_a dengan larut

            MC"Saya tidak ingat pernah melihat Anda ini fokus."adegan hd26_a dengan larut

            th"Well-y-yess ... saya harus lulus."adegan hd27_a dengan larut

            MC"Saya terlambat bekerja. Saya harus pergi sekarang. Semoga berhasil dengan belajar Anda!"adegan hd28_a dengan larut

            MC"Bye Honey, Bye theo."em"Sampai jumpa, sayang."th"Bye, [name]."adegan pass2 dengan larut

            berhenti sebentar

            Jump Path_a"Biarkan Dia Menikmati Pemandangan":


            $ ntr_point += 1

            scene hd23_b with dissolve

            mct "Dia akan pingsan karena menatap."mct"Siapa yang tidak akan menatap jika mereka berada di tempatnya?"mct"I’m curious, will [fname] notice too?"adegan hd27_a dengan larut

            MC"Saya terlambat bekerja. Saya harus pergi sekarang. Semoga berhasil dengan belajar Anda!"adegan hd28_a dengan larut

            MC"Bye Honey, Bye theo."em"Sampai jumpa, sayang."th"Bye, [name]."adegan pass2 dengan larut

            berhenti sebentar

            Jump Path_B



Label Path_a:

    adegan r1 dengan fade

    MC"Saya sangat lelah hari ini. Sangat menyenangkan akhirnya berada di rumah dengan Anda."

    mc "Bagaimana Belajar Anda?"

    scene r2 with dissolve

    em "ITU BAGUS. Saya Suka Mengajar Theo."

    em "Itu Mengingatkan SahA PAYA HARI -Hari Ketika Saya Adalah Seoran Guru, Jadi Saya Merasa Sangan Bahagia Ketika Dia Datang."

    scene r3 with dissolve

    mc "AKU SUKA MELIHATMU BAHAGIA."

    scene r4 with dissolve

    em "Aww, Kamu Manis."

    em "Oh, Apakah Sahebutkan Bahwa Theo Akan Dodang Lebih Sering Sekarang? Dias Masih Sedikit Berjuang."

    scene r5_a with dissolve

    mc "SAYA BISA MENEBAK ALASANNAA. Fokusnya Jelas Bukan Pada Studinya."

    scene r6_a with dissolve

    em "APA Maksudmu?"

    scene r7_a with dissolve

    mc "Sepertinya Dia Lebih Tertarik PAYA PAYUDARA dan PELAJARAN PELAJARAN."

    scene r8_a with dissolve

    em "Benar-Benar ?? SAYA TIDAK MENYADARI."

    scene r9_a with dissolve

    mc "Yah, Dia Bukan Anak Kecil Lagi. Dia Masih Muda Dan Sehat."

    mc "Jika Dunia Seperti Dulu, Dia Bahkan Bisa Memiliki Anak."

    scene r10_a with dissolve

    mc "Saya Sedang Berpikir--"

    scene r11_a with dissolve

    em "Ya?"adegan r10_a dengan larut

    MC"Haruskah kita memiliki rencana cadangan selain Andrew?"adegan r12_a dengan larut

    em"Dengan Theo?!"scene r13_a with dissolve

    MC"Dia masih muda, dan spermanya harus sehat. Peluang keberhasilan kami bisa tinggi."adegan r14_a dengan larut

    em"Anda ada benarnya, tapi ... Saya tidak tahu sayang."

    em "Sebenarnya, ITU BEMUAT SEDITIT SEDIH BAHWA DIA TIDAK AKAN PERNAH BERSAMA WANITA. Munckin Seperti ini, Saya Bisa Bisa Meringkan Hati Nurani Sahah."

    scene r15_a with dissolve

    mc "SAYA JUGA TIDAK SUKA, TETAPI BEGITU PAMI MEMILIKI BADI, Kami AKAN BEBAS."

    jump dream

label path_b:

    scene r1 with fade

    mc "SAYA SANGAT LELAH IPI INI. Sangan Menyenangkan Akhirnya Berada di RUMAH GANGAN UNGA."

    mc "Bagaimana Belajar Anda?"

    scene r2 with dissolve

    em "ITU BAGUS. Saya Suka Mengajar Theo."

    em "Itu Mengingatkan SahA PAYA HARI -Hari Ketika Saya Adalah Seoran Guru, Jadi Saya Merasa Sangan Bahagia Ketika Dia Datang."

    scene r3 with dissolve

    mc "AKU SUKA MELIHATMU BAHAGIA."

    scene r4 with dissolve

    em "Aww, Kamu Manis."

    em "Oh, Apakah Sahebutkan Bahwa Theo Akan Dodang Lebih Sering Sekarang? Dias Masih Sedikit Berjuang."

    scene r5_a with dissolve

    mc "SAYA BISA MENEBAK ALASANNAA. Fokusnya Jelas Bukan Pada Studinya."

    scene r6_a with dissolve

    em "SAYA Kira ITU KARENA SAYA. Kamu Benar."

    scene r7_a with dissolve

    mc "Suda Kubilan Dia Bukan Anak Kecil."

    scene r8_b with dissolve

    mc "Anda Seperti Guru -guru nakal di porno gangan tema semacam itu."

    scene r8_b1 with dissolve

    em "Hahahahah"adegan r8_a dengan larut

    em"Sebenarnya, ketika saya melihat Theo mengawasi saya hari ini, saya merasa kasihan padanya ..."

    em "Dan Terus Memikirkanya Sepanjang Pelajaran."

    scene r9_a with dissolve

    mc "Apa yang anda pikirkan?"

    scene r11_a with dissolve

    em "Tentang Situasi Bayi. Maksud Saya ..."

    em "SAYA TAHU PAMI AKAN MENCOBA DENGAN ANDREW, TETAPI MEMILIKI RENCANA CADI: AKAN BAGUS."

    scene r8_a with dissolve

    mct "Hearing this from [fname] surprised me."

    mct "Sepertinya Dia Menjadi Semakin Nyaman Dangannya."

    mct "SAYA TAHU DIA MENYHANANANSI INI UNTUK MASA DEPAN KITA, TAPI TETAP SAJA ..."

    scene r12_a with dissolve

    em "Jadi .. Apa Yang Anda Pikirkan Tentang ini?"

    scene r13_a with dissolve

    mc "Selama Anda Baik -Baik Saja Denggan Itu, Saya Tidak Panya Masalah."

    mc "SAYA TAHU ENA MERYargANAN INI UNTUK MASA DEPAN Kami. AKU PERCAYA PADAMU Dan MENCINTAIMU."

    scene r13_b with dissolve

    em "AKU RUGA SALANG."

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
        $ fname = "Emily"Adegan DR1 Dengar Fade

    Berhenti Sebentar

    Adegan DR2 DENGAN LARUT

    unk"*(Moans)*"adegan dr3 dengan larut

    mct"Apa suara -suara itu?"adegan dr4 dengan larut

    UNK2"Anda adalah guru terbaik di dunia. Saya tidak lagi memiliki masalah dengan turunan."unk"Mmm ... *Slurp * *-lurp * *rp *"unk"Saya siap melakukan apa pun yang Anda butuhkan untuk membantu Anda fokus."adegan dr5 dengan larut

    mct"WTF ?? Saya harus salah paham."adegan hitam dengan larut

    jeda (0,01)

    adegan bj1 dengan larut

    berhenti sebentar

    adegan dr7 dengan larut

    em"Mmmmm ...."

    mc "APA -APAAN?!"

    scene dr8 with dissolve

    em "Jangan Khawatir, Sayang. Saya Hanya Memantunya Delangan Turunan."

    scene dr9 with fade

    th "Saya Perlu Masuk Ke Dalam Diri Anda, Saya Tidak Bisa Menahan Diri Lagi."

    scene dr10 with dissolve

    em "Ayo, Ambil Turunan Saya."

    menu:
        "Tonton Saja":

            $ nts_point += 1

            scene dr11 with dissolve

            mct "Itu akan terjadi cepat atau lambat. Saya mungkin juga menikmatinya."

            scene dr11_a with dissolve

            em "Mmm ... Tolong Masukkan Perlahan, Theo."

            mct "Holly ..."
        "Cobalah unkula Berhenti":


            $ ntr_point += 1

            scene dr11 with dissolve

            mct "Oke, itu akan terjadi cepat atau lambat, tetapi saya tidak ingin itu dilakukan di belakang saya seperti ini."

            scene dr11_b with dissolve

            mc "WTF?! [fname]! STOP THIS!"


    scene black with dissolve

    "Ketukan! Ketukan! Ketukan!"

    scene dr12 with dissolve

    pause

    scene dr13 with dissolve

    mc "Astaga! Ini Sangan Nyata."

    $ renpy.end_replay()

    scene black with dissolve

    pause

    scene nm1 with dissolve

    unk2 "Hey [fname]... Ops.. Did I come early?"

    scene nm1 with dissolve

    em "Tidak, Tidak, Masuk. SAYA BARU SAJA KEMBALI DARI TENIS DAN MELAKUAN BEBERAPA LATUHAN RELAKSASI. BERI AKU 5 Menit, Oke?"

    scene nm1 with dissolve

    unk "Oke..."adegan nm2 dengan larut

    MC"Siapa ini?"

    mc "Oh ... Theo Seharusnya Datang Hari ini. SAYA TIDAK PUNYA PERKERJAAN, JADI SENA BISA Bergaul DGAN MEREKA. Biarkan Berpakaian Dan Pergi."

    scene nm3 with dissolve

    em "Kenapa Kamu Berdiri? Miliki Duduk, Sayang."

    scene nm4 with dissolve

    th "Saya Baik, Terima Kasih."

    scene nm5 with dissolve

    em "Oh, Kamu Bangun, Sayang. Apakah Ada Yang Salah? Apakah Anda Merasa Sangan?"

    scene nm6 with dissolve

    mc "Hai! Ya, Sahah Baik -Baik Saja. SAYA BERMIMMM, DAN SAYA PIKIR SENA MASIH TERPENGARUH OLEHNYA."

    scene nm7 with dissolve

    em "Apakah Itu Mimpi Yang Buruk?"

    menu:
        "Ya":


            $ ntr_point += 1

            scene nm8 with dissolve

            mc "I think it was... Do you have study today?"Lompat Theo_CM"Tidak":


            $ nts_point += 1

            scene nm8 with dissolve

            mc "Sejujurnya, itu adalah mimpi yang menyenangkan. Apakah Anda sudah belajar hari ini?"

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

    em "Yeah, silly, I told you that yesterday. Did you forget? Anyway, don’t distract me; I need to finish these exercises."adegan nm10 dengan larut

    berhenti sebentar

    adegan nm11 dengan larut

    berhenti sebentar

    adegan nm12 dengan larut

    berhenti sebentar

    Jika STP_TH == 1:

        adegan nm12 dengan larut

        mct"Am I seeing this wrong, or is [fname] intentionally teasing Theo? It seems that she has accepted what I suggested yesterday."kalau tidak:


        adegan nm12 dengan larut

        mct"Is [fname] already putting the plan she suggested to me yesterday into action? I'm surprised by how eager she is."adegan nm13 dengan larut

    em"Saya tidak bisa cukup meregangkan. Saya butuh bantuan."menu:"Tawarkan bantuan Anda.":

            $ ofr_mc += 1

            $ ntr_point += 1

            scene nm14_a with dissolve

            mc "Biarkan saya membantu Anda, sayang."adegan nm15_a dengan larut

            em"Saya tidak yakin Anda bisa melakukannya dengan benar."adegan nm16_a dengan larut

            em"THEO! Anda menyukai olahraga, bukan? Bisakah Anda membantu saya?"MC"Saya tahu kami memiliki rencana dengan Theo, tetapi apakah dia benar -benar perlu mengatakan saya tidak bisa mengelolanya."adegan nm15_b dengan larut

            th"Oh .. oke .. apakah kamu yakin?"adegan nm16_b dengan larut

            em"Lagi pula, Anda telah bermain basket sejak Anda masih kecil. Anda harus tahu beberapa trik."adegan nm17_b dengan larut

            mct"I think [fname] wants to make this process enjoyable and include me in the game. I'm getting excited..."adegan nm18_b dengan larut

            berhenti sebentar

            adegan nm19_b dengan larut

            em"Ayo, Theo, bukankah Anda akan membantu?"th"O-oke. Aku-aku akan melakukannya ..."adegan nm20_b dengan larut

            berhenti sebentar

            adegan nm21 dengan larut

            tht"Oh! Shit. I have a boner. I hope [fname] doesn't notice this."adegan nm22 dengan larut

            EMT"Apa?"EMT"Bagaimana dia sudah menjadi sulit? Saya bahkan belum melakukan apa pun!"adegan nm23 dengan larut

            EMT"Yah .. dia berhasil menggosoknya tepat di tempat."adegan nm24 dengan larut

            mct"Tidak ada keraguan ini lebih dari sekedar membantu latihan peregangan."adegan nm25 dengan larut

            em"Saya merasa jauh lebih baik sekarang! Terima kasih atas bantuannya. Mari kita hancurkan turunan ini."adegan nm26 dengan larut

            th"O-Oke…"adegan nm25 dengan larut

            mct"Yah, yah ... sepertinya seseorang memiliki kesalahan."

            $ renpy.end_replay()
        "Sarankan Theo untuk membantu.":



            $ nts_point += 1

            $ sgt_th += 1

            scene nm14_b with dissolve

            mc "Theo, mengapa Anda tidak membantu?"adegan nm15_b dengan larut

            th"Oh .. oke .. apakah kamu yakin?"adegan nm16_b dengan larut

            em"Lagi pula, Anda telah bermain basket sejak Anda masih kecil. Anda harus tahu beberapa trik."adegan nm17_b dengan larut

            mct"I think [fname] wants to make this process enjoyable and include me in the game. I'm getting excited..."adegan nm18_a dengan larut

            berhenti sebentar 

            adegan nm19_b dengan larut

            em"Ayo, Theo, bukankah Anda akan membantu?"th"O-oke. Aku-aku akan melakukannya ..."adegan nm20_b dengan larut

            berhenti sebentar

            adegan nm21 dengan larut

            tht"Oh! Shit. I have a boner. I hope [fname] doesn't notice this."adegan nm22 dengan larut

            EMT"Apa?"EMT"Bagaimana dia sudah menjadi sulit? Saya bahkan belum melakukan apa pun!"adegan nm23 dengan larut

            EMT"Yah .. dia berhasil menggosoknya tepat di tempat."adegan nm24 dengan larut

            mct"Tidak ada keraguan ini lebih dari sekedar membantu latihan peregangan."adegan nm25 dengan larut

            em"Saya merasa jauh lebih baik sekarang! Terima kasih atas bantuannya. Mari kita hancurkan turunan ini."adegan nm26 dengan larut

            th"O-Oke…"adegan nm25 dengan larut

            mct"Yah, yah ... sepertinya seseorang memiliki kesalahan."

            $ renpy.end_replay()

    scene nm27 with fade

    th "Saya selesai dengan tugas yang Anda berikan kepada saya kemarin!"adegan nm28 dengan larut

    berhenti sebentar

    adegan nm29 dengan larut

    em"Menurut saya…"adegan nm30 dengan eye_open

    em"Saya akan memberi Anda hadiah untuk itu."adegan nm31 dengan eye_shut

    jeda (2.0)

    adegan nm32 dengan eye_open

    th"Tha..tertanggungjawabkan. Anda tidak perlu memberi saya hadiah."adegan nm33 dengan larut

    berhenti sebentar

    adegan chl dengan larut

    berhenti sebentar



    Jika SGT_TH == 1:

        adegan A1 dengan larut

        MC"Anda tidak marah karena saya mengemukakan ide tentang Theo segera, bukan?"adegan a2 dengan larut

        em"TIDAK! Sebenarnya, itu sangat menyenangkan. Saya merasa sangat panas menggodanya seperti itu."adegan A3 dengan larut

        MC"Ha ha ha. Melihatmu seperti itu agak aneh, tapi ... kurasa aku menyukainya"adegan a4 dengan larut

        em"Ini adalah sesuatu yang baru untuk hubungan kami ... Saya harus mengakui, saya juga menyukainya. Tapi aku masih merasa aneh, sayang."em"Ketika semua ini dimulai, saya pikir semuanya akan sangat sulit, tetapi dengan Anda, semuanya terasa lebih mudah. Aku mencintaimu, sayang."adegan a6 dengan larut

        MC"Aku juga mencintaimu, lebih dari yang pernah kamu ketahui."jika OFR_MC == 1:


        adegan a2 dengan larut

        em"Saya harus mengakui, ini adalah pengalaman yang sangat berbeda. Saya merasa sangat panas menggodanya seperti itu."em"Theo mengalami ereksi tanpa saya melakukan apa pun. Saya menghibur saya untuk menempatkannya pada posisi yang canggung."adegan A1 dengan larut

        MC"Melihat Anda seperti itu membuat saya bersemangat, tetapi Anda benar -benar tidak harus melakukan itu."adegan a4 dengan larut

        em"Apa yang kamu bicarakan?"adegan A1 dengan larut

        MC"Saya berbicara tentang Anda mengatakan saya tidak akan bisa melakukannya."adegan a4 dengan larut

        em"Saya menempatkan rencana yang kami bicarakan kemarin beraksi. Kami membuat keputusan, dan saya baru saja melakukannya untuk memulai."em"You know I love you, [name]. I thought you wanted this too."adegan A1 dengan larut

        MC"Saya ingin ..."MC"Aku hanya ..."MC"Saya kira Anda benar. Itu adalah keputusan bersama kami. Anda baru saja membuat saya lengah."adegan a6 dengan larut

        MC"Dan aku juga mencintaimu, sayang."adegan 5m dengan larut

    berhenti sebentar

    adegan at1 dengan larut"*-CINCIN!! CINCIN!! CINCIN!!-"adegan at2 dengan larut

    berhenti sebentar

    adegan at2 dengan larut

    mct"Oh. Itu Andrew."adegan at3 dengan larut

    aw"Hei, bagaimana kabarmu? Kami belum berbicara sejak hari itu."

    aw "SAYA TIDAK INGIN BEMUAT HAL -HAL CANGGUND, TETAPI SENA HARUS BERYA - APAKAH MEMUTUSKAN UNTUK MUNGUR?"

    scene at4 with dissolve

    mc "Tidat, Kami Belum Mundur; Kami Hanya Memproses Apa Yang Terjadi. Sebenarnya, Saha Akan Menelepon Anda Hari ini. Apakah anda turun unkah lain lain selanjutnya?"

    scene at3 with dissolve

    aw "Saya Sibuk Sekarang, Tapi ... Oke, Saya Sedang Dalam Perjalanan!"

    scene at4 with dissolve

    mc "Oke, Bung."

    scene at5 with dissolve

    mc "Dia Akan Akan Dataang."

    scene at6 with dissolve

    em "Memilisi Beberapa Hari Berlalu Baik. Saya Merasa Jauh Lebih Santai Sekarang."

    scene at5 with dissolve

    mc "Saya Dapat Melihat Bahwa dan Lebih Santai Sekarang, Dan Itu ..."

    menu:
        "Membuatku khawatir":

            $ ntr_point += 1

            scene at6_a with dissolve

            mc "Saya tidak bisa tidak khawatir - bagaimana jika ini mempengaruhi hubungan kita? Bagaimana jika Anda mulai mengembangkan perasaan untuk Andrew?"

            scene at7_a with dissolve

            em "Jangan Konyol! AKU Mencintaimu. Semua ini Tidak Akan Mengubah apa pun di Antara Kami"
        "Menghibur Saya":


            $ nts_point += 1

            scene at6_b with dissolve

            mc "Saya tahu situasinya aneh, tetapi saya senang bahwa saya tidak melihat Anda stres lagi."

            scene at7_b with dissolve

            em "Saya Percaya Pada Cinta Kita. Tidak Peduli Apa Yang Terjadi, Kami Bersama -Sama."

    scene at8 with dissolve

    em "SAYA AKAN MINUM SATU ATAU DUA GELAS ANGGUR SEBELUM ANDREW TIBA DI SINI. Apakah dana buta Menginginkanya?"

    scene at9 with dissolve

    mc "Tidak, Terima Kasih Sayang."

    scene at9_5 with dissolve

    pause

    scene oneh with dissolve

    pause

    scene rt1 with dissolve

    aw "Hei, Kawan! SIAP UNTUK RONDE KEDUA?"

    scene rt2 with dissolve

    pause

    scene rt3 with dissolve

    aw "Hanya Lelucon, Kawan. Santai."

    scene rt4 with dissolve

    mc "Kami Melakukan ini karena suatu alasan, Ingat?"

    scene rt5 with dissolve

    aw "Okay,okay... Let's not keep [fname] waiting."

    scene rt6 with dissolve

    aw "Whoa, kamu terliihat luar biasa hari ini!"

    scene rt7 with dissolve

    em "Hei, Andrew!"

    scene rt8 with dissolve

    em "Baru Hari ini?"

    scene rt9 with dissolve

    aw "Ha ha ha. SAYA PIKIR YANG AKAN AKAN TEGANG SEPERTI TERAKHIR KALI."

    scene rt10 with dissolve

    em "SAYA SUDAH Terbiasa."

    scene rt11 with dissolve

    aw "Jadi, apakah anda siap untuk langkah selanjutnya?"

    mct "SAYA PIKIR MUMKKIN LEBIH BAIK JIKA SAYA TETAP SEDITIT SUNYI, DENGAN BEGITA SUASANA TIDAK AKAN BEGITA CANGGUNG."

    scene rt12 with dissolve

    em "Kukira..."mct"Ya, kami kira ..."adegan rt13 dengan larut

    aw"Apakah Anda akan melepas pakaian Anda saat ini?"adegan rt14 dengan larut

    em"Yah, tidak terlalu cepat. Aku bisa menyentuhmu seperti terakhir kali."adegan rt15 dengan larut

    aw"Ya ampun ... oke, kalau begitu."adegan rt16 dengan larut

    aw"Anda adalah bosnya."adegan rt17 dengan larut

    mct"I wonder what [fname] thinks right now. "mct"Kali ini, saya akan mundur sedikit. Mari kita lihat bagaimana kemajuan."adegan rt18 dengan larut

    berhenti sebentar

    adegan rt19 dengan larut

    aw"Tunggu."adegan rt20 dengan larut

    aw"Now… Better. Let’s move on [fname]."adegan rt21 dengan larut

    EMT"Saya bilang saya sudah terbiasa, tetapi ketika saya melihat hal besar itu, saya berubah pikiran. Bagaimana mungkin wanita mana pun terbiasa dengan ini?"adegan rt22 dengan larut

    EMT"Saya bisa merasakan beratnya di tangan saya. Semakin sulit dan lebih sulit di tangan saya."adegan hitam dengan larut

    jeda (0,01)

    adegan hj3_s dengan larut

    EMT"Andrew's penis has a different smell. It's a stronger scent. I can't quite describe it, but it's different from the [name]'s."adegan hitam dengan larut

    jeda (0,01)

    adegan hj3_f dengan larut

    berhenti sebentar

    adegan rt23 dengan larut

    Awt"Dia berbau seperti parfum dan anggur. Kali ini, saya tidak akan membiarkan Anda menyelesaikannya dengan cepat. Si kecil tidak hanya akan puas dengan tangan Anda kali ini."adegan hitam dengan larut

    jeda (0,01)

    adegan hj_s dengan larut

    berhenti sebentar

    adegan hj_f dengan larut

    EMT"Apakah saya salah? Sepertinya dia tidak akan cum dalam waktu dekat."adegan rt24 dengan larut

    em"Ugh. Saya lelah. Mengapa Anda belum bisa menyelesaikannya? Apakah Anda mengambil sesuatu atau apa?"adegan rt25 dengan larut

    aw"Whaaa… apa? Saya tidak minum pil atau apapun. Beginilah saya. Tidak ada yang bisa membuat saya cum hanya dengan tangan mereka."adegan rt26 dengan larut

    em"Benar-benar?! Jadi, apa yang perlu saya lakukan?"adegan rt25 dengan larut

    aw"Saya pikir Anda siap untuk seks. Biarkan diri Anda pergi dengan saya. Saya berjanji Anda akan merasa baik."adegan rt27 dengan larut

    em"Mustahil! Terlalu dini untuk itu!"adegan rt28 dengan larut

    aw"Oh .. Oke, bos. Kemudian setidaknya biarkan saya menggunakan mulut Anda."adegan rt29 dengan larut

    em"Dengan baik..."

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

    mct "I don't know if I want her to do this with someone else since she's rejected me about it so many times before."mct"Saya tahu kita perlu bergerak maju. Saya tidak yakin apakah saya ingin dia melakukan sesuatu dengan orang lain yang tidak ingin dia lakukan dengan saya."menu:"Bersikeras seks":

            $ ntr_point += 2

            scene rt32 with dissolve

            mc "Honey... You're going to have sex eventually. I think you're ready for it today"Adegan RT33 Delangar Larut

            em"Really? I told you I wasn’t ready! I cannot believe you. I’m gonna go with Andrew’s suggestion."em"Andrew Bisakah Anda bergerak seperti ini?"adegan rt34 dengan larut

            aw"Oke… saya akan berdiri di mana pun Anda menginginkan saya sekarang."adegan rt35_a dengan larut

            mct"[fname] is really mad at me. I felt inadequate and ended up ignoring her feelings. I’m not sure if she’s punishing me or if she just doesn’t care."mct"Dia bertingkah seolah -olah saya bahkan tidak ada di dalam ruangan."
        "Dukung Ide Blowjob":


            $ nts_point += 2

            scene rt32 with dissolve

            mc "Tidak apa -apa sayang. Saya tahu Anda belum siap untuk seks."

            scene rt29 with dissolve

            em "SAYA Kira SAYA HARUS MELAKUKAN ITU. Saya Belum Siap untuk Mengzil Bedada Itu Di ..."

            em "Anywways. Andrew, Bisakah Kamu Pindah Ke Sana?"

            scene rt34 with dissolve

            aw "Oke ... Saya Akan Berdiri Di Mana Pun Anda Mengingorga Saya Sekarang."

            scene rt35 with dissolve

            mct "Is [fname] trying to tease me? If so, it’s definitely working."

            scene rt36 with dissolve

            mct "She looks super sexy right now. It feels like me and [fname] are playing a game—a naughty game."

    scene rt37 with dissolve

    awt "Her mouth is so small and tight… It feels like I’m inside [fname] pussy."

    em "Mmm ... mmm."

    scene rt38 with dissolve

    awt "Sepertinya ini bukan pertama kalinya dia."

    aw "Hhh… [fname] y-you..."

    aw "HHH .. Kamu Sangan Sempurna."

    scene rt39 with dissolve

    em "Slurp..slurp… Slurp."

    aw "Rasananya Menyenangkan."

    scene black with dissolve

    pause(0.01)

    scene bj2 with dissolve

    aw "[fname], you have to stop! I am gonna.. CUM!!"

    scene rt40 with dissolve

    aw "OH!!!"adegan rt41 dengan larut

    em"Apa…"adegan rt42 dengan larut

    MC"Tunggu..."adegan rt43 dengan larut

    aw"Im sorry [fname], it was an accident. I couldn’t hold back anymore."adegan rt44 dengan larut

    MC"BUNG!"

    em "Apa dia ..."

    scene rt45 with dissolve

    aw "Oh, Saya Benar -Benar Lupa! SAYA PUNYA SESUATU UNTUK Dilakukan. SAYA HARUS PERGI. Selamat Tinggal!"

    scene rt46 with dissolve

    em "Apa itu ?? Ugh ... AKU AKAN MUGRAYHKAN."

    scene rt47 with dissolve

    mc "Oke..."

    $ renpy.end_replay()

    scene rt48 with dissolve

    pause

    scene rt49 with dissolve

    em "Saya pasti tidak mengharapkan hal itu terjadi."adegan RT50 dengan larut

    MC"Sama di sini, itu sangat aneh."adegan rt51 dengan larut

    mct"Dia berbau sangat kuat ... semen…"adegan rt52 dengan larut

    em"Saya akan berteriak padanya."adegan rt53 dengan larut

    em"Tetapi ketika saya melihatnya melarikan diri seperti itu, saya harus benar -benar menahan tawa saya."adegan rt54 dengan larut

    em"Saya pikir kami menangani hari ini dengan cukup baik, selain dari bagian terakhir."adegan rt51 dengan larut

    MC"Saya pikir begitu juga."

    mc "Jadi Saya Berpikir ..."

    scene rt55 with dissolve

    pause

    scene rt56 with dissolve

    em "Suasana hati Tidak Terlalu untuk ITU, Sayang."

    scene rt57 with dissolve

    mc "Ohh. Oke. MAAF SALANG."

    scene rt58 with dissolve

    mc "Oh! INI Telepon Andrew! Dia pasti menjatuhkanya. SAYA HARUS MEMBAWANYA KEPADERANA."

    scene rt59 with dissolve

    pause

    scene rt60 with dissolve

    em "Sekarang?"adegan rt61 dengan larut

    MC"Ya, saya akan segera kembali."adegan rt60 dengan larut

    em"Oke, sayang. Berkendara aman."adegan rt62 dengan larut

    berhenti sebentar

    adegan rt63 dengan larut

    MC"Hai! Sayang… Saya di rumah."adegan rt64 dengan larut

    mct"Oh…"mct"Apakah itu pengontrol jarak jauh?"

    scene black with dissolve

    pause

    jump expose




label halloween_event_label:

    $ disable_saving = True

    scene inf with dissolve

    pause

    scene black

    $ name = renpy.input("Nama saya", default ="Jake", length=15)
    $ persistent.name = name

    if name == "":
        $ mc = "Jake"
        $ mct = "Jake Tought"menu:"Apakah Anda yakin tentang Jake?"
            "Ya":
                Berhenti Sebentar"No,Please.":

                pause



    $ fname = renpy.input("Nama istri saya adalah", default ="Emily", length=15)
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

    mct "Women... She said she'd be ready in 10 minutes an hour ago, and she's still not ready."adegan h1 dengan larut

    MC"Are you still not ready, [fname]?"adegan h2 dengan larut

    em"Baiklah, baiklah! Lima menit lagi. Jangan terburu -buru."adegan h1 dengan larut

    MC"Jadi ... itu berarti Anda akan siap dalam setengah jam?"adegan h2 dengan larut

    em"Haha, kamu sangat imut. Percayalah, saya akan layak ditunggu."adegan h2 dengan larut

    em"Oh, omong -omong, sayang, apakah Anda mendapatkan anggur yang saya minta?"adegan h2_5 dengan larut

    mct"Oh, crap. How did I forget that? If I tell [fname], she’ll kill me."adegan h2_5 dengan larut

    MC"Uh ... ya, tentu saja! Saya bahkan sudah menurunkannya di Andrew."adegan h2_6 dengan larut

    em"Oh, kamu luar biasa!"adegan h2_7 dengan larut

    mct"James adalah satu -satunya yang bisa menangani ini dengan cepat. SMS lebih baik sekarang."adegan 30m dengan larut

    berhenti sebentar

    adegan h2_8 dengan fade

    em"Saya siap."Adegan H3 dengan Fade:
        subpixel true
        Yalign 1.0
        jeda 1.5
        Linear 7.0 Yalign 0.0

    MC"Wow!"adegan h4 dengan larut

    em"Tak bisa bicara?"adegan h4 dengan larut

    MC"Hmm… sayang?"menu:"Memperingatkannya tentang gaun yang menunjukkan terlalu banyak":

            Adegan H4_1 DGANGAN LARUT
            MC"Don’t you think the front of your dress is… well, a little too low?"adegan h4_2 dengan larut
            em"Ah, benarkah? Anda pikir begitu?"adegan h4_3 dengan larut
            MC"Maksud saya, jika Anda tidak berhati -hati, saya mungkin mengintip ... yah, Anda tahu."adegan h4_4 dengan larut
            em"Kurasa aku lebih baik ekstra hati -hati."adegan h4_4 dengan larut
            MC"Ha ha."

            $ persistent.warn_1 = False
        "Jangan Memperingatkanya":


            adegan h4_1 dengan larut
            MC"Kecantikan Anda hanya membuat saya terdiam sebentar di sana."adegan h4_1 dengan larut
            MC"Anda terlihat sangat menakjubkan."adegan h4_2 dengan larut
            em"Ohh ... terima kasih, sayang."

            $ persistent.warn_1 = True

    scene h4_1 with dissolve

    mc "Ayo ...."adegan h4_9 dengan larut

    em"Mwah!"adegan h4_5 dengan fade

    MC"Wow! Untuk apa itu?"

    em "Ini hanya ciuman permintaan maaf karena membuat anda menuntgu. Ayo, Kita Terlambat - Mari Kita Pergi!"

    scene 30m with dissolve

    pause

    scene h4_6 with dissolve

    mc "Wow! Andrew Benar -Benar Masuk Ke Dalam Semangat Halloween!"

    em "Ya, Saya Tenjak Berharap Dia Pergi Ke Semua Masalah Ini."

    em "Torgegu Torgu Torgu!"

    scene h4_7 with dissolve

    em "Apakah Saya Terlihat Seram Dan Seksi?"

    mc "Anda Selalu Melakukanya, Sayang."

    scene h4_8 with dissolve

    em "Hai?!"adegan h4_8_2 dengan larut

    aw"Apa yang kalian lakukan di sini?"

    aw "Tidak Berencana Masuk?"

    scene h4_8_3 with dissolve

    aw "Ngomong -ngomong, Slahahlah. SAERA BERKERJA Keras Pada Sambutan Sambutan, Jadi Begini!"

    scene h5 with dissolve

    aw "Selamat Datang di Pesta Halloween Legendaris Andrew!"

    mc "Kawan! Anda memabuat SAYA TAKUT!"

    em "Ahhhh! Astaga!"

    scene h5_5 with dissolve

    aw "Maaf! SAYA PIKIR ITU AKAN BERBUAT 'SAMBUTAN' YANG MENGESAN."

    em "Anda memabuat Sayaat Takut Setengah Mati Delan Sambutan Itu! TAPI KARENA INI HALLOWEEN, SAYA AKAN MEMBIARKANNAA MELUNCUR KALI INI."

    mc "Ya, kawan…"

    scene h6 with dissolve

    aw "Hei, Dari Mana Saja Kalian? SAYA MULAI BERPIKIR MANA TELAH MENYERAH PAYA DATANG."

    mc "Kami Terlambat. Anda Bisa Menebak Mengapa."

    scene h7 with dissolve

    aw "Biarkan Saya Menebak. ITU SEMUA Salahmu."

    mc "Ha ha ha."adegan h8 dengan larut

    em"Hai! Berhenti mengacaukan saya."

    aw "Tentu…"

    mc "Tentu Saja, Sayang!"

    em "Ayo, Mari Kita Pergi Ke Dalam."

    scene h9 with dissolve

    aw "Psst, hey man, bisakah kita bicara sebentar?"

    mc "Ya, Ada apa, Kawan? Apakah Ada Yang Salah?"

    scene h10 with dissolve

    aw "Anak yang anda undang muncul, tetapi apakah anda yakin dia berusia 18 tahun?"

    mc "Ya, ya. Dia hanya terlihat sedikit lebih muda, tetapi tidak ada masalah."

    scene h11 with dissolve

    aw "Jika Anda Berkata Begitu ..."

    aw "Dia Tampak Agak ... Aneh. Dan Kostum Itu ...?"

    mc "Ada apa Kostumnya?"

    aw "Anda Akan Melihat. Ayo, Mari Kita Masuk Ke Dalam."

    scene h12 with fade

    pause

    scene h13 with Dissolve(3.5)

    unk2 "Aaaaargh ..."

    scene h14 with Dissolve(1.5)

    unk2 "Ha ha ha!"adegan H15 dengan larut (1.5)

    UNK2"Mari bersenang -senang."adegan h12 dengan larut (3.5)

    berhenti sebentar

    adegan h16 dengan fade

    jm"Would you mind if I check the fabric of your dress, [fname]?"

    em "Hah?"

    th "Ya, Tolong, Bisakah Saha Merasakanyaa Jeda?"

    scene h17 with dissolve

    jm "Hey! Welcome, [name]."

    mc "Terima Kasih."

    th "Welcome, [name]."

    mc "Terima Kasih, Sobat."

    mc "SEJUJURNYA SENA TIDAK BERHARAP MANA MELAKUKAN BANYAK UPAYA DALAM KOSTUM INI. Itu Terlihat Sangan Realistis."

    scene h18 with dissolve

    jm "Ya. SAYA DAN ISTRI SAYA DULU PERGI KE PESTA KOSTUM SETIAP TAHUN, Dan ADA ... Berbagai Fantas ... ahem. Pokoknya, Terima Kasih."

    scene h17 with dissolve

    th "Ya, sangat memping Bagi Saya. Ini pertama kalinya Saya Menghadiri Pesta Halloween."

    mc "ITU BAGUS. TAPI THEO, SEPERTINYA MANA LUPA BERPAKAIAN, SOBAT. Ada apa Kostumnya?"

    scene h19 with dissolve

    th "Ini Kostum Bonecrusher! Beginilah Cara Diaanian. Sebenarnya, dia jahat jahat, tapi dia Menghancurkan Orang Jahat Lainnya. Dia Karakster Yang Solid."

    scene h20 with dissolve

    emt "Wow. SAYA Kira Suda Saatnya SAYA MENERIMA BAHWA THEO MULAI TUMBUH DEWASA. Sepertinya Dia Mendorong Sesuatu Yang Besar Ke Dalam Pakaan Dalamnya, Dan Pakaan Dalamnya Akan Meleda."

    scene h19 with dissolve

    mc "Do I see this right, or is [fname] looking at Theo’s penis?"

    mc "Apakah Ukuran Yang Menarik Perhatiannya? Bisakah Dia Menyukainya?"

    mc "Wanita Yang SAYA CINTAI SEDANG MELIAT AYAM BESAR PRIA MADA LAINYA. Kotoran. SAYA BAHKAN TIDAK TAHU BABAIMANA PERASAANANAA."

    mc "Saya Seharusnya Tidak Memikirkan Hal ini Sekarang, ATAU AKHIRYA SAYA AKAN MENJADI SULIT."

    scene h21 with dissolve

    jm "Baiklah, Tenanglah. Biarkan SAYA BEMUAT KIA MINUM. Anda Perlu Sedikit Melonggarkan!"

    scene h22 with dissolve

    "Ya!"adegan h22_5 dengan larut

    JMT"Sekarang…"adegan h23 dengan larut

    JMT"Mari kita tambahkan beberapa campuran khusus Paman James dan ..."adegan h23_5 dengan larut

    JMT"Biarkan pesta menjadi lebih menarik."adegan h24 dengan larut

    em"... Itu adalah pokok dari pesta kuliah kami ..."adegan h25 dengan larut

    jm"Siapa yang mau anggur? Ini sangat bagus - yang berumur dengan sempurna."adegan h26 dengan larut

    JMT"Wow! What a sight. One day, I’m going to bite those nipples of yours, [fname]."adegan h27 dengan larut

    em"Apakah Anda bercanda? Saya sudah menunggu ini sepanjang minggu!"adegan h27 dengan larut

    MC"Sama di sini."

    th "SAYA MENGINGINKANNANA JUGA!"

    aw "Hitung Aku! SAYA TIDAK KEHILANG ITU."

    scene h28 with dissolve

    em "Jadi, Andrew, Apakah ini Halloween Yang Terkenal Yang Telah Anda Hipati?"

    aw "Oh, Kamu Bertaruh! Kemudian Malam ini, Saya Telah Mengatur Hantu Hantu Mary Berdarah Muncul. Dia Akan MEMBAWA PESTA KE TINGATYA BERIKUTYA!"

    th "Mengapa Mereka Memanggilnya * Horny * Mary?"

    em "Percayalah, Theo. Anda Tidak Ingin Tahu."

    mc "Ayo, Jangan Memenuhi Kepalanya Gelangan Omong Kosong ini."

    jm "Hehehe ..."

    scene h28 with dissolve

    aw "Horny Mary Adalah Legenda Berdarah. Mereka Mengatakan Dia Muncul Di Cermin, Mengzil Alih Tubuh Wanita, Dan Anggota Pria Waktu Hidup Mereka ..."

    aw "Sampai Dia Menggerkan Penis Mereka Kerik Dari Setiap Tetes Darah Terakhir. Dia Tidak Berhenti Sampai Sama Sekali Tulise Ada Yang Tersisa!"

    th "Whoa."

    em "Ha ha..."adegan h29 dengan larut

    mct"Is this old bastard staring at [fname]’s breasts?"Jika persistent.warn_1 == true:

        adegan h29 dengan larut

        mct"Dia bahkan belum bergabung dengan percakapan atau menggerakkan kepalanya sama sekali."mct"Sulit untuk mengatakan dengan tepat di mana dia melihat dengan topeng itu. Topeng itu menutupi matanya."adegan h31 dengan larut

        mct"WTF? Apakah dia ... membelai dirinya sendiri?"mct"I should’ve warned [fname]. He’s masturbating right in front of me while staring at her breasts."adegan h30 dengan larut

        mct"Dia sangat dekat. Hanya sedikit lagi, dan dia bisa menggosok bahunya. Atau bahkan di wajahnya."mct"Kotoran. Berpikir tentang ini membuatku sulit. Pikiran James tua menggosok penisnya di wajah istri saya yang cantik sangat membangkitkan gairah. Apakah alkoholnya?"mct"Anyway, he’s not really hurting anyone. Stay calm, [name]. Just enjoy the moment."kalau tidak:


        adegan h30_5 dengan larut

        mct"Haha... Looks like [fname] noticed too. She must’ve remembered the warning I gave her at home."adegan h31_5 dengan larut

        jm"Grrr ..."mct"Kemudian, lama James, tetapi saya harus menyerahkannya kepada Anda untuk upaya ini."adegan h33 dengan larut

    em"Sayang, di mana kamu menemukan anggur ini? Vino Rouge d'Argent ... Sudah bertahun -tahun sejak saya terakhir memiliki beberapa."adegan h32 dengan larut

    MC"Seorang pesulap tidak pernah mengungkapkan rahasianya."

    jm "Ha ha ha!"adegan h33 dengan larut

    em"Mungkin pesulap yang menemukan anggur ini layak mendapatkan hadiah. Di penghujung malam ..."adegan h32 dengan larut

    jm"Hmm..."mct"Kotoran."

    mc "Ya, Sayang. Anda pasti Harus Menghadiahinya."

    scene h33 with dissolve

    em "Haha ... Saya Berharap dan Bisa melihat raut wajah anda. Anda Tersipu, Bukan? IMUT-IMUT SEKALI."

    mct "Jika Anda Tahu Sahu Baru Saja Mendengar Anda Mengatakan ingin Anggota Hadiah Kepada James Di Tempat Tidur, Anda Akansti Mengapa Wajah Seja Terlihat Seperti Ini."

    scene h34 with Dissolve(3.5)

    unk2 "Ah, Kelompok Yang Hidup."

    scene h35 with Dissolve(2.0)

    unk2 "Biarkan AKu…"

    scene h36 with Dissolve(2.0)

    unk2 "Aduk Sedikit."

    scene h37 with Dissolve(2.0)

    unk2 "Kecantikan Seperti Itu ... Layak untuk Dihargai Oleh Semua Orang."

    scene h38 with Dissolve(2.0)

    unk2 "Apakah Kita Jada Sedikit Bermain Delangus? MAKA ITU SEMPURNA. Bersenang -senang, Kecantikan ..."

    scene h39 with Dissolve(3.5)

    em "Pokoknya ... terima kasih telah menemukan anggur ini, Sayang."

    scene h40 with dissolve

    em "Itu ... Sangan Aneh. Saya Merasakan Dingin Sejenak di Sana."

    em "Mengapa Semua Orang Menatapku Seperti Itu?"

    mc "Uh... [fname]..."

    scene h41 with dissolve

    th "SAYA ... SAYA PIKIR GAUN KUSA ..."

    aw "Membuka. Itu ... Terbuka."

    em "Apa?"adegan h42 dengan larut

    em"Astaga!"

    em "Bagaimana Ini Bisa Terjadi?!"

    scene h43 with dissolve

    mc "Sayang, Kamu Baik -Baik Saja?"

    em "Tidak, Saya Tidak Baik -Baik Saja! Ini Memalukan!"

    em "Mereka Melihat Segalanya!"

    scene h44 with dissolve

    jm "Hei, eh, Minjkin anggurnya? Sudah Malam Yang Aneh ..."

    th "Ya, ya Dan Tenjak Ada Yang Melihat Apapun! Aku Bersumpah!"

    aw "Theo, Kita Semua Melihat Segalanya."

    em "Andrew! Tidak Membantu!"

    scene h45 with dissolve

    mc "[fname], let’s step outside for a second. Take a breather, okay?"

    em "... bagus. Hanya ... Beri Aku Waktu Sejenak."

    em "SAYA PIKIR SAYA HARUS Sendirian Sebentar ... Di Mana Kamar Mandi?"

    aw "Di Lantai Atas, Di Sebelah Kanan."

    scene h46 with dissolve

    jm "Yah ... Itu ... Tidak Terduga."

    aw "Jadi, eh, Siapa Yang Mau Lebih Banyak Anggur?"

    scene h47 with fade

    em "Ya Tuhan ... Mereka Semua Melihat Saya."

    em "Andrew, James, Bahkan Theo! Mereka Semua Menatapku Seperti—"

    em "Bagaimana Munckin Sahithatikan Gaun SAYA? Tuhan, ITU SANGAT MEMALUKAN ..."

    em "They were looking at me like they wanted to devour me... And I was standing there, showing everything with [name] right next to me."

    scene h48 with dissolve

    em "They were looking at me like they wanted to devour me... And I was standing there, showing everything with [name] right next to me."

    scene h48 with dissolve

    em "Thinking about them while they stared, with [name] by my side... It felt so…"

    scene h49 with dissolve

    unk2 "SUNGGUH PEMANDIGAN YANG INDAH ... SEMUA Mata MEREKA TERTUJU PADA Anda, MINUM SETIAP INCI."

    scene h49 with dissolve

    unk2 "Gaun Itu ... Memelukmu Dengan Sangat Sempurna. Dan Kemudian, Cara Membuka, Mengungkapkan Rahasia Anda. GODAAN SEPERTI ITU ... Bahkan Jika Anda Tidak Bermaksud Demikian."

    scene h50 with dissolve

    unk2 "Saya Bisa Merasakan Keinginan Mereka Mengisi Ruangan, Sama Seperti Mereka Ingin Mengisi Anda. Tidak Bisakah Kamu?"

    scene h50 with dissolve

    unk2 "Tubuh ini ... Sangan Hangat, Sangan Lembut. Itu milikku sekarang."

    scene h50 with dissolve

    unk2 "IZIKAN SENA MENUNJUKKAN KEPADA dan APA Yang MEREKA BAYANGKAN. Biarkan SAYA BEMANU dan MERAKKUL KESENIGAN INI Yang Telah Anda Tetap Terkubur."

    scene h50 with dissolve

    unk2 "Mmm ... ya. Inilah Yang Pantas Anda Dapatkan ... Untukur Merasa Dipuja, Disembah, Diinginkan."

    scene h51 with dissolve

    pause

    scene h52 with dissolve

    pause

    scene h53 with dissolve

    unk2 "Hmm…"adegan h54 dengan larut

    jm"Baiklah, teman -teman, saya secara resmi pada batas saya. Saya terlalu tua untuk anggur sebanyak ini. Panggilan alam, dan ini sangat mendesak!"adegan h54 dengan larut

    jm"Is there another bathroom around here? Looks like [fname]’s using the one upstairs."adegan h55 dengan larut

    aw"Ya, ada satu lagi di kamar saya. Kepala ke atas, dan itu adalah pintu ke kiri."adegan h56 dengan larut

    jm"Punya, terima kasih."adegan h56_5 dengan larut

    berhenti sebentar

    adegan h57 dengan larut

    JMT"Wait... is [fname]?"adegan h57_5 dengan larut

    JMT"Suci - apa dia ...?"Adegan H58 dengan Fade:
        subpixel true
        Yalign 1.0
        jeda 1.5
        Linear 7.0 Yalign 0.0

    JMT"Apa ini? Apakah dia ... apakah ini semacam lelucon?"JMT"Did she leave the door open on purpose? Maybe [name] and [fname] are into something kinky, and I’ve just stumbled upon it..."adegan h59 dengan larut

    em"James ... Saya tahu Anda di sana. Mendekati."adegan h59 dengan larut

    jm"[fname], is this... is this a joke? Are you and [name] testing me or something?"adegan h60 dengan larut

    em"Apakah ini terlihat seperti lelucon bagi Anda?"adegan h60 dengan larut

    JMT"Sialan ... ini tidak bisa nyata. Apakah dia benar -benar ... mengundang saya?"adegan h60 dengan larut

    jm"[fname], I... Look, if you’re serious about this, I’m not one to say no, but this has to be between us. You know [name] can’t find out."adegan h60 dengan larut

    em"[name]? Oh, James... Forget about him. Right now, it’s just you and me."adegan h60 dengan larut

    em"Sekarang, James ... mengapa Anda tidak menunjukkan apa yang telah Anda pikirkan sepanjang malam?"adegan h61 dengan larut

    jm"Jangan pedulikan jika saya melakukannya, sayang."adegan h62 dengan larut

    em"Jadi, katakan padaku, James ..."adegan h62 dengan larut

    em"Apa yang akan Anda lakukan dengan tubuh ini? Maksudku ... apa yang akan kamu lakukan padaku?"adegan h62 dengan larut

    jm"Ermm ... aku ingin mencium bau vaginamu. Dan kemudian cicipi itu."adegan h62 dengan larut

    em"Anda akan mencium bau dan merasakan vagina seorang wanita yang suaminya berada di lantai bawah menikmati pesta? Suamiku bahkan belum mencium bau vaginaku."adegan h62 dengan larut

    jm"Kemudian biarkan saya berhasil di mana suami Anda gagal. Biarkan lidah saya menjelajahi di dalam."adegan h63 dengan larut

    JMT"Ahh…"adegan h63 dengan larut

    JMT"Mmm ..."adegan h63 dengan larut

    JMT"Bau itu. Seperti bunga liar yang basah kuyup dalam dosa. Begitu mentah, sangat kotor ... Tuhan, itu membuat saya gila."adegan h64 dengan larut

    em"Apakah Anda menyukainya?"adegan h64 dengan larut

    jm"Kulit muda dan halus seperti itu ... untuk pria seusia saya, ini di luar mimpi."adegan h64 dengan larut

    em"Ahh ..."adegan h64 dengan larut

    jm"Saya tidak percaya suami Anda berada di lantai bawah saat Anda membiarkan saya mengendus vagina Anda di sini."adegan h64 dengan larut

    em"Saya hanya berharap dia bisa menonton apa yang akan Anda lakukan pada saya. Anda dapat melakukan apa pun yang Anda inginkan untuk vagina saya James."adegan h65 dengan larut

    jm"Kemudian berbaring di sana."adegan h65 dengan larut

    em"Tapi aku harus memperingatkanmu. Anda tidak punya banyak waktu. Anda hanya dapat memenuhi satu keinginan untuk saat ini."adegan h65 dengan larut

    jm"Satu -satunya keinginan saya adalah mencicipi pot madu Anda."adegan h66 dengan larut

    em"Hmm..."adegan h66 dengan larut

    em"Kemudian?"adegan h67 dengan larut

    jm"Ha ha."adegan h68 dengan larut

    berhenti sebentar

    adegan h69 dengan larut

    berhenti sebentar

    adegan h70 dengan larut

    berhenti sebentar

    adegan h71 dengan larut

    berhenti sebentar

    adegan h72 dengan larut

    em"Ahh…"adegan h72 dengan larut

    em"Jalankan lidah Anda di dalam diri saya."adegan h73 dengan larut

    jm"*Mencucup*"adegan h73 dengan larut

    em"Ahhh… ah…"adegan h73 dengan larut

    jm"Mmmm…"adegan h73 dengan larut

    em"Saya cumming."adegan h74 dengan larut

    em"That felt so good. I’m sure you’ve completely consumed [fname] while savoring her essence."adegan h74 dengan larut

    jm"[fname], what do you mean?"adegan h74 dengan larut

    em"Tidak peduli, itu bukan urusan Anda, bajingan tua."adegan h74 dengan larut

    jm"O-o-okay ... Anda tiba-tiba menjadi sedikit keras."adegan h74 dengan larut

    em"Untuk seseorang yang menjilati vagina wanita yang sudah menikah, Anda secara mengejutkan sopan. Hah! Sekarang, sudah kembali ke bawah."adegan h75 dengan larut

    em"Tapi tunggu ... sebelum Anda pergi, izinkan saya memberi Anda sedikit hadiah."adegan h76 dengan larut

    em"Ambil ini. Itu semua milikmu. Saya tidak akan membutuhkannya lagi malam ini."adegan h76 dengan larut

    jm"Apa kamu yakin?"adegan h76 dengan larut

    em"Ya. Ambil saja."adegan h76 dengan larut

    jm"Sampai jumpa di lantai bawah."adegan h76 dengan larut

    em"Selamat tinggal…"adegan h77 dengan larut

    em"Alright, [fname]."adegan h77 dengan larut

    em"Saya membiarkan Anda pergi sekarang. Turun dan mari bersenang -senang bersama."adegan h78 dengan larut

    berhenti sebentar

    adegan h47 dengan larut

    berhenti sebentar

    adegan h79 dengan larut

    em"…aneh. Hah? Apa?"adegan h79 dengan larut

    em"Rasanya seperti dingin lagi. Itu membuat menggigil di tulang belakang saya."adegan h79 dengan larut

    em"Apa? Benar -benar ada dingin. Saya bisa merasakannya di bawah rok saya."adegan h80 dengan larut

    em"Orang udik? Apa ... apa ini?!"adegan h81 dengan larut

    em"Ya Tuhan, dimana celana dalamku?! Apa yang telah terjadi?!"adegan h81 dengan larut

    em"Apakah saya ... tidak pernah memakainya? Saya ingat mengenakannya ketika saya meninggalkan rumah."adegan h81 dengan larut

    em"Sial, sial, sial. Apakah saya kehilangan akal?"adegan h80 dengan larut

    em"Apa basah ini?"adegan h80 dengan larut

    em"Aku bersumpah aku tidak merasa seperti ini beberapa saat yang lalu."adegan h80 dengan larut

    em"Ini sangat menakutkan. Saya tidak ingin sendirian lagi."adegan h82 dengan fade

    EMT"Jika saya tidak hati -hati, mereka mungkin melihat sesuatu yang seharusnya tidak mereka lakukan."adegan h82 dengan larut

    EMT"I need to tell [name] about this strange thing that happened, but without drawing too much attention."adegan h83 dengan larut

    em"Sayang"adegan h83 dengan larut

    em"Apakah Anda bercanda?! Hei, bangun. Ayo, jangan tertidur di sini."adegan h83 dengan larut

    aw"Good luck with that, [fname]. He’s out cold. Guess the wine hit him harder than he thought."adegan h84 dengan larut

    em"Tidak sekarang…."adegan h85 dengan fade

    UNK2"Wakey, wakey, sayang ..."adegan h86 dengan larut

    MC"Hah? Siapa—?"adegan h88 dengan larut

    UNK2"Shh ... jangan berjuang. Anda belum bangun dari ini, belum."adegan h89 dengan larut

    MC"Apa ...? Dimana saya? Siapa kamu?"adegan h89 dengan larut

    MC"Beberapa saat yang lalu saya ... apa yang terjadi?"adegan h89 dengan larut

    MC"Where is [fname]?"adegan h88 dengan larut

    UNK2"You’ll find out soon enough. Let’s just say… I’m here to play. And [fname] Oh, she’s part of the game now."adegan h90 dengan larut

    MC"Apa yang kamu?!"adegan h90 dengan larut

    MC"Tinggalkan dia dari ini!"adegan h88 dengan larut

    UNK2"Tapi di mana kesenangannya? Anda akan menjawab pertanyaan saya, sayang. Buatlah mereka dengan benar, dan mungkin - mungkin saja - saya akan menghindarinya."adegan h88 dengan larut

    UNK2"But every wrong answer… Well, let’s just say, [fname] won’t enjoy it as much as I will."adegan h91 dengan larut

    UNK2"Oh, mungkin dia juga akan ..."adegan h91 dengan larut

    UNK2"Kalau begitu, mari kita mulai dengan pertanyaan pertama ... pertanyaan-pertanyaan pengujian hubungan ... mari kita lihat apakah Anda benar-benar suami yang baik."adegan h91 dengan larut

    UNK2"Here’s the first one. What’s [fname]’s favorite wine?"menu:"Vino Rouge d'Or":

            Adegan H92 GANGAN LARUT

            MC"Vi-Vino Rouge D’or?"adegan h93 dengan larut

            UNK2"Hahaha. You lie to [fname], pretending you were the one who got the wine, yet you can’t even remember its name properly."adegan h93 dengan larut

            UNK2"You truly are a terrible husband, and for that, we must punish [fname] right before your eyes."adegan h90 dengan larut

            MC"Kotoran. Apa yang akan kamu lakukan padanya?"adegan h93 dengan larut

            UNK2"Saya tidak akan melakukan apapun. Duduk saja dan perhatikan."adegan h94_5 dengan larut

            UNK2"Ah, [fname]... looks like you’ve joined the party too. You must be confused, huh? Well, let me fill you in—this is all part of the game. The game where things get a little... complicated."adegan h95 dengan larut

            jeda 0,5

            adegan h96 dengan larut

            em"Apa yang terjadi? Mengapa Anda di sini ... dan mengapa ini terjadi pada saya?"adegan h94_5 dengan larut

            UNK2"Oh, [fname]... You’ve been part of this game since the moment you entered Andrew's house. It’s a little test, a little challenge for your husband. All I want is to see how far he’ll go, and whether he’ll pass or fail."adegan h97 dengan larut

            em"Game? Apa maksudmu? Game apa yang kamu bicarakan? Ini tidak menyenangkan, ini tidak benar—"adegan h94_5 dengan larut

            UNK2"Oh, itu semua bagian yang menyenangkan, sayangku. Aturannya sederhana: suami Anda menjawab pertanyaan saya, dan setiap jawaban yang salah mengarah pada sesuatu ..."adegan h94_5 dengan larut

            UNK2"tidak menyenangkan untukmu. Dan, tentu saja, setiap jawaban yang benar membuat Anda tetap aman ... tetapi tidak selalu."adegan h98 dengan larut

            MC"Jangan khawatir, sayang. Saya akan mengeluarkan Anda dari ini. Aku akan menghentikannya, aku bersumpah."adegan h99 dengan larut

            em"W-apa? Anda akan menghentikannya? Tapi bagaimana caranya? Kami terjebak di sini ..."adegan h94_5 dengan larut

            UNK2"Dia mungkin mencoba menyelamatkan Anda, tetapi ingat, setiap kesalahan yang dia buat akan dikenakan biaya. Mari kita lihat apakah dia cukup kuat untuk menangani apa yang akan terjadi."adegan h100 dengan larut

            UNK2"Come on, [name]... Let’s bring the punishment here."adegan h101 dengan larut

            em"What's going on. [name] what's that?"MC"Hentikan!"adegan h102 dengan larut

            UNK2"Mari kita basah lebih dulu, kan? Melompat lurus mungkin bukan ide terbaik."adegan hitam dengan larut

            jeda (0,01)

            adegan td dengan larut

            em"Saya tidak bisa menggerakkan tubuh saya. Ahh ..."em"Punggungnya menyakiti saya, dan sangat dingin."UNK2"Jangan khawatir. Anda akan menghangatkannya dengan panci madu Anda sedikit."UNK2"So... how’s the view from there, [name]?"adegan h90 dengan larut

            MC"Pergi ke neraka!"adegan hitam dengan larut

            jeda (0,01)

            adegan td2 dengan larut

            UNK2"Ha ha ha. Saya sudah datang dari sana."UNK2"Karena Anda cukup basah, Anda siap mengambilnya."em"Ahhh…. Hhhh…."em"Berhenti!"UNK2"Saya tidak bisa membantu tetapi membuat Anda membayar hukuman Anda, maaf."MC"Kotoran!"em"Itu terlalu besar ... itu h ... sakit ..."adegan h103 dengan larut

            UNK2"Saya pikir kita bisa beralih ke pertanyaan berikutnya sekarang…"adegan h104 dengan larut

            UNK2"Mari kita pindahkan dia seperti ini sehingga Anda dapat melihat mainan seks kami lebih jelas."em"Hhhh…"mct"She’s really holding [fname] like a lifeless plastic sex toy."UNK2"Saya kira Anda menikmati pemandangan."UNK2"Maaf menarik Anda menjauh darinya, tetapi kami harus melanjutkan."
        "Vino Rouge D'Argent":


            adegan h90 dengan larut

            MC"Tentu saja saya tahu ini. Vino Rouge D'Argent."

            scene h93 with dissolve

            unk2 "Yah ... anda terlalu malas tutkeK membeli anggur favorit istri anda, tetapi anda masih tahu yang mana."

            unk2 "Meskipun Anda Mendapatkan Jawabananya Gelangan Benar, Karena Penipuan Kecil Anda, Anda Masih Layak Mendapatkan Hukuman Kecil."

            scene h90 with dissolve

            mc "Tidak! SAYA MELAKUKANNA GANGAN BENAR. Tetap Berpahat Pada Kata Anda."

            scene h94 with dissolve

            unk2 "Ia! Dan Cobalah Tidak Tidak Membuatku Marah."

            scene h95 with dissolve

            unk2 "Ah, [fname]... looks like you’ve joined the party too. You must be confused, huh? Well, let me fill you in—this is all part of the game. The game where things get a little... complicated."

            scene h96 with dissolve

            em "Apa Yang Terjadi? Mengapa Anda di Sini ... Dan Mengapa Ini Terjadi Pada Sah?"

            scene h94_5 with dissolve

            unk2 "[fname]... You’ve been part of this game since the moment you entered Andrew's house. It’s a little test, a little challenge for your husband."

            unk2 "Yang Saya Intiban Hanyyah Melihat Seberapa Jauh Dia Akan Melangkah, Dan Apakah Dia Akan Lewat Atau Gagal."

            scene h97 with dissolve

            em "Permainan? APA Maksudmu? Game apa Yangu Kamu Bicarakan? Ini Tidak Menyenangkan, Ini Tidak Benar—"

            scene h94_5 with dissolve

            unk2 "Oh, Itu Semua Bagian Yang Menyenangkan, Sayangan. ATURANNAA SEDERHANA: SUAMI ENA MENJAWAB PERANYAAN SENA, DAN SETIAP JAWABAN YANG SALAH MEMARAH PAYA SESUATU ..."

            unk2 "Tidak Menyenangkan Untucmu. Dan, Tentu Saja, Setiap Jawaban Yang Benar Memkna dan Tetap Aman ... Tetapi Tidak Selalu."

            scene h98 with dissolve

            mc "Jangan Khawatir, Sayang. SAYA AKAN MENGELUARIRAN YANAAN DARI INI. AKU AKAN MENGENTIKANYA, AKU BERSUMPAH."

            scene h99 with dissolve

            em "W-APA? Anda Akan Menghentikananya? TAPI BAGAIMANA CARANYA? Kami Terjebak di Sini ..."

            scene h94_5 with dissolve

            unk2 "Dia Munckin Mencoba Menyelamatkan Anda, Tetapi Ingat, Setiap Kesalanan Yang Dia Barat Akan Denakan Biaya. Mari Kita LiHat Apakah Dia Cukup Kuat Unkuk Menangani apa yang Akan Akan Terjadi."

            scene h93 with dissolve

            unk2 "Come on, [name]... Let’s bring along the magician who figured out our wine."

            scene h105 with dissolve

            unk2 "Ayo Bawa James Ke Sini. Sebagai Hasil Dariban Yang Baru Baru Saja Anda Berikan, Kami Dapat Mengatakan Bahwa Anda MeneGah Masuknya Sesuatu Yang Lebih Tebal, Tetapi Tetap Saja Jari -J James Yang Kota Dan Tua Haru Mendi Piriswa. Ayo James ..."

            mc "James! MEMBURU!"

            scene h106 with dissolve

            unk2 "Jangan Repot -Repot Berjuang. James Berada Di Bawah Kendali Saya Sekarang - Sama Seperti Yang Lainnya Di Sini ... dan Semua Adalah Boneka Kecil Saya!"

            scene h107 with dissolve

            em "ITU TIDAK BISA!…"

            unk2 "Ah ... ya, Andaik unkingatkan saah sada Kehadiran anda."

            scene h108 with dissolve

            unk "Mari Kita Masuk Ke Posisi Yang Bagus Dan Nyaman. Apa Yangu Kamu Katakan?"

            scene h109 with dissolve

            em "I can’t move my body. [name] help!"

            mc "Sialan! SAYA JUGA TIDAK BISA BERGERAK."

            unk2 "Ayo, Pesulap, Mari Kita Lohat Pertunjukan Anda."

            scene h110 with dissolve

            jm "Grrr…."em"[name], he is toucing me."MC"Saya tidak bisa melakukan apa pun! Kotoran!"MC"My whole body is paralyzed, except for one part. Why the hell does the thought of this monstrous thing touching [fname]'s private parts turn me on?"MC"Deep down, I knew I enjoyed imagining [fname] with others, but... this..-"adegan h111 dengan larut

            em"[name]! He is getting closer!"em"HHH ... James, bangun!"UNK2"Ha ha ha. Percayalah, Anda tidak ingin dia bangun sekarang. Jika Anda tahu hal -hal yang ingin dia lakukan untuk Anda, Anda tidak akan pernah mendekatinya lagi."em"[name], he’s touching my..."adegan h112 dengan larut

            jm"Hmm..."em"Dapatkan tangan kotormu dari aku… ahhh!"adegan h113 dengan larut

            MC"Wanita yang saya cintai ... dia akan diraba, dan saya tidak bisa melakukan apa -apa tentang itu!"adegan h114 dengan larut

            em"Dia ... dia bergerak ..-"adegan h113 dengan larut

            em"Jarinya di dalam vaginaku!"adegan h114 dengan larut

            MC"Selesaikan hukuman ini! Silakan!"UNK2"Kami baru saja punya beberapa hal lagi yang harus dilakukan dengan James."adegan h115 dengan larut

            jm"Ha ha ha…"adegan h116 dengan larut

            em"*Orang udik*!!"adegan h117 dengan larut

            em"Hhh ..."adegan h118 dengan larut

            em"Ahh!"adegan h120 dengan larut

            em"Dia mendorongnya ..."adegan h119 dengan larut

            em"Sangat dalam ..!"adegan h89 dengan larut

            MC"Apakah ini mimpi buruk?"adegan h119 dengan larut

            em"Mmm…"adegan h120 dengan larut

            berhenti sebentar

            adegan h119 dengan larut

            em"Jika dia terus berjalan seperti ini…"adegan h120 dengan larut

            em"Mmm ... saya tidak bisa bertahan."adegan h119 dengan larut

            em"Mmm…"adegan h120 dengan larut

            berhenti sebentar

            adegan h119 dengan larut

            em"Hhhh…"adegan h120 dengan larut

            em"Ahh ..."adegan h94_5 dengan larut

            UNK2"Saya pikir kita bisa beralih ke pertanyaan berikutnya."UNK2"Nah ... hukuman Anda sudah cukup."adegan h108 dengan larut

            UNK2"Anda bebas sekarang, James ... Anda bisa pergi."adegan h91 dengan larut

    UNK2"Sekarang, mari kita beralih ke pertanyaan kedua dan terakhir."UNK2"Saya sarankan Anda menjawab ini dengan bijak. Kali ini jawaban yang salah yang Anda berikan mungkin tidak memiliki obat."menu:
        UNK2"Apakah pikiran seseorang mengacaukan istri Anda?"
        "Ya":

            Adegan H90 GANGAN LARUT

            MC"Yes! Damn it, yes. I like it. I'm telling the truth, now leave her alone!"adegan h121 dengan larut

            em"Sayang ... apakah kamu yakin?"adegan h125 dengan larut

            MC"[fname]? But you... You can move..."adegan h122 dengan larut

            em"Ya. Saya bisa selama ini."adegan h125 dengan larut

            MC"Maksudmu ... apakah semua yang baru saja terjadi pilihanmu sendiri? Apakah Anda Bertindak?"adegan h123 dengan larut

            MC"Bagaimana ini mungkin? Matamu ... itu tidak bisa nyata."adegan h122 dengan larut

            em"Bagaimana jika kita fokus untuk mewujudkan keinginan Anda?"adegan h126 dengan larut

            MC"Saya ... Saya tidak yakin."adegan h122 dengan larut

            em"Kami akan meluangkan waktu dan memastikan Anda menikmatinya, tetapi pada akhirnya, saya akan kacau oleh seseorang. Bersiaplah untuk itu."adegan h127 dengan larut

            MC"O-Oke, cintaku."adegan h124 dengan larut

            em"Apakah tidak apa -apa jika saya menginginkan Andrew?"MC"Oke..."adegan h128 dengan larut

            aw"Hai sobat. Saya pikir seseorang membutuhkan saya."adegan h129 dengan larut

            em"Welcome. Yes, I really need you, but I will only do this so that [name]'s desires are fulfilled. Know this."aw"Oke. Seperti yang Anda katakan ..."aw"Jadi, bisakah saya menggunakan kalian semua?"em"I don't know, we need to get [name]'s permission."menu:
                em"Apa yang kamu katakan, sayang?"
                "Gunakan vaginanya":

                    ADEGAN H129 DENGAN LARUT

                    MC"You can use her pussy."adegan h130 dengan larut

                    em"Apakah kamu yakin sayang?"em"Sekarang?"MC"Ya, saya tidak ingin menunggu lagi."adegan h134 dengan larut

                    em"Oh.."MC"Apa yang telah terjadi?"adegan h132 dengan larut

                    em"Tidak ada yang hanya saya…"adegan h133 dengan larut

                    aw"Ya sobat… tidak ada yang terjadi…"adegan h132 dengan larut

                    em"*Berbisik*Bagaimana bisa sebesar ini? Rasanya seperti cabang pohon besar yang meluncur di antara pipiku.*Bisikan*"adegan h135 dengan larut

                    MC"Apa yang kamu katakan sayang?"adegan h132 dengan larut

                    berhenti sebentar

                    adegan h133 dengan larut

                    berhenti sebentar

                    adegan h136 dengan larut

                    em"Hhh… tidak ada sayang…"adegan h145 dengan larut

                    aw"Bung, saya harus berterima kasih karena telah berbagi istri Anda yang berharga dengan saya."adegan h132 dengan larut

                    berhenti sebentar

                    adegan h133 dengan larut

                    berhenti sebentar

                    adegan h145 dengan larut

                    em"Mmm…"adegan h146 dengan larut

                    MC"Apa yang kamu lakukan padanya?"adegan h146 dengan larut

                    aw"Aku..? Tidak ada ... hanya berkeliaran."adegan h146 dengan larut

                    aw"Ayo lakukan sesuatu dengan benar?"adegan h148 dengan larut

                    em"Apa? Sayang?"Adegan H149 dengan Fade:
                        subpixel true
                        yalign 0.0
                        jeda 1.5
                        Linear 7.0 Yalign 1.0

                    MC"What? What? [fname]?"adegan h147 dengan larut

                    MC"Motherf…"adegan h147 dengan larut

                    aw"Bukankah saya berjanji kepada kalian itu akan menjadi pesta yang mengesankan?"adegan h147 dengan larut

                    em"Saya tidak bisa mengatakan saya tidak terkesan."adegan hitam dengan larut

                    jeda (0,01)

                    scene hrub with dissolve

                    aw"Lalu mari kita geser sedikit di atasnya."em"Ahhh ... sangat dekat dengan lubang."em"[name], it’s almost going in."em"Sangat licin. Saya pikir itu akan meluncur."aw"Bukankah sudah waktunya untuk memasukkannya?"aw"Mari kita peregangan Anda sedikit."adegan h150 dengan larut

                    aw"Ini dia…"adegan h125 dengan larut

                    MC"Tidak, belum berhenti!"MC"NOOOOOO!"adegan h154 dengan fade

                    MC"TOOO!"adegan h155 dengan larut

                    MC"Oh. Itu pasti mimpi buruk."em"Apa yang terjadi, sayang? Anda membangunkan saya."MC"Tidak ada apa-apa. Ini hanya mimpi buruk."em"Oke. Selamat malam, sayang."MC"Selamat malam, babygirl saya."adegan h156 dengan larut

                    em"HHH ... Sayang?"MC"Ya."em"Bagaimana kita pulang? Saya tidak ingat."em"Dan saya merasakan sakit di antara kaki saya."adegan h154 dengan larut

                    MC"Kamu bilang apa!?"adegan h94 dengan fade

                    berhenti sebentar

                    adegan inf2 dengan larut

                    berhenti sebentar"Gunakan Mulutnya":


                    adegan h129 dengan larut

                    MC"Anda bisa menggunakan mulutnya"adegan h131 dengan larut

                    em"Saya tidak tahu bagaimana itu akan pas di mulut saya, tetapi saya akan mencobanya, hanya untuk Anda."aw"Jangan khawatir, saya yakin Anda bisa mengambil semuanya."em"Kemudian…"adegan h137 dengan larut

                    em"Mmm…"adegan h138 dengan larut

                    em"* Muck* mmmm… tidak bisakah aku menciumnya?"em"[name], Honey... It barely fits in my hand... How am I supposed to put it in my mouth?"MC"Wow [fname], please... I want to see you try."adegan h139 dengan larut

                    em"Mmm ... muck"em"Karena itulah yang Anda inginkan ..."adegan h142 dengan larut

                    em"Mmm…"adegan h141 dengan larut

                    em"** Gag ** Gag **"adegan h143 dengan larut

                    em"Sangat besar…"em"[name], this is almost twice the size of yours."mct"Saya sudah sulit untuk sementara waktu sekarang. Saya akan merobek celanaku."adegan hitam dengan larut

                    jeda (0,01)

                    adegan hbj dengan larut

                    em"Mmmm… mmm…"em"*Mencucup*"MC"Sangat besar! Bagaimana dia bisa mengambil semuanya? Itu pasti di tenggorokannya."aw"Mulut yang sangat ketat."aw"Ambillah sepanjang jalan."aw"Thank you for letting me use your wife's mouth, [name]."MC"Sayang, Anda bisa berhenti kapan saja Anda mau."em"Mmm… mmm…"mct"Cara dia melihat ke mata saya membuat saya begitu banyak."aw"Saya pikir saya cumming!"adegan h151 dengan larut

                    em"Mmm ..."aw"OPSS ..."adegan h152 dengan larut

                    em"Mmmwa…"aw"Anda perlu menelan."em"Hhh ... cwame ... di ... my ... mwouth ..."adegan h153 dengan larut

                    em"*Meneguk*"em"Maaf, Sayang. Saya tidak sengaja menelan saat mencoba berbicara."MC"Tapi ... tapi ... Anda belum pernah menelan milik saya sebelumnya."em"Maaf, Sayang."adegan h89 dengan larut

                    MC"NOOOOOO!"adegan h154 dengan fade

                    MC"TOOO!"adegan h155 dengan larut

                    MC"Oh. Itu pasti mimpi buruk."em"Apa yang terjadi, sayang? Anda membangunkan saya."MC"Tidak ada apa-apa. Ini hanya mimpi buruk."em"Oke. Selamat malam, sayang."MC"Selamat malam, babygirl saya."adegan h156 dengan larut

                    em"HHH ... Sayang?"MC"Ya."em"Bagaimana kita pulang? Saya tidak ingat."em"Dan saya merasakan sakit di antara kaki saya."adegan h154 dengan larut

                    MC"Kamu bilang apa!?"adegan h94 dengan fade

                    berhenti sebentar

                    adegan inf2 dengan larut

                    berhenti sebentar"Gunakan Keduanya":


                    adegan h129 dengan larut

                    MC"Anda dapat menggunakan bagian apa pun dari dirinya yang Anda inginkan."adegan h130 dengan larut

                    em"Apakah kamu yakin, sayang?"em"Apakah dia memiliki izin untuk menggunakan semuanya?"MC"Ya. Saya memberikan izin."em"Sekarang?"MC"Ya, saya tidak ingin menunggu lagi."em"Saya tidak bisa menerimanya sekarang, jadi saya harus membasahi terlebih dahulu."MC"Hmm..."aw"Saya menyukai ide itu."adegan h137 dengan fade

                    em"Mmm…"adegan h138 dengan larut

                    em"* Muck* mmmm… tidak bisakah aku menciumnya?"em"[name], Honey... It barely fits in my hand... How am I supposed to put it in my mouth?"MC"Wow [fname], please... I want to see you try."adegan h139 dengan larut

                    em"Mmm ... muck"em"Karena itulah yang Anda inginkan ..."adegan h142 dengan larut

                    em"Mmm…"adegan h141 dengan larut

                    em"** Gag ** Gag **"adegan h143 dengan larut

                    em"Sangat besar…"em"[name], this is almost twice the size of yours."mct"Saya sudah sulit untuk sementara waktu sekarang. Saya akan merobek celanaku."adegan hitam dengan larut

                    jeda (0,01)

                    adegan hbj dengan larut

                    em"Mmmm… mmm…"em"*Mencucup*"MC"Sangat besar! Bagaimana dia bisa mengambil semuanya? Itu pasti di tenggorokannya."aw"Mulut yang sangat ketat."aw"Ambillah sepanjang jalan."aw"Thank you for letting me use your wife's mouth, [name]."MC"Sayang, Anda bisa berhenti kapan saja Anda mau."em"Mmm… mmm…"mct"Cara dia melihat ke mata saya membuat saya begitu banyak."adegan h143 dengan larut

                    em"Cukup licin sekarang."adegan h134 dengan larut

                    em"Oh.."adegan h132 dengan larut

                    em"Aku hanya…"adegan h133 dengan larut

                    aw"Do you feel that [fname]?"adegan h132 dengan larut

                    em"*Berbisik*Bagaimana bisa sebesar ini? Rasanya seperti cabang pohon besar yang meluncur di antara pipiku.*Bisikan*"adegan h135 dengan larut

                    MC"Apa yang kamu katakan, sayang?"adegan h136 dengan larut

                    em"Hhh… tidak ada, sayang…"adegan h145 dengan larut

                    aw"Bung, saya harus berterima kasih karena telah berbagi istri Anda yang berharga dengan saya."adegan h132 dengan larut

                    berhenti sebentar

                    adegan h133 dengan larut

                    berhenti sebentar

                    adegan h145 dengan larut

                    em"Mmm… sayang, aku ingin ..."adegan h146 dengan larut

                    em"Andrew menggosok pinggulku, dan aku ..."MC"Apakah kamu menyukainya?"adegan h146 dengan larut

                    aw"Ya, dia menyukainya."adegan h146 dengan larut

                    aw"Jadi ... mari kita lakukan sesuatu, kan?"adegan h148 dengan larut

                    em"Apa? Sayang?"Adegan H149 dengan Fade:
                        subpixel true
                        yalign 0.0
                        jeda 1.5
                        Linear 7.0 Yalign 1.0

                    MC"What? What? [fname]?"adegan h147 dengan larut

                    MC"Motherf…"adegan h147 dengan larut

                    aw"Bukankah saya berjanji kepada kalian itu akan menjadi pesta yang mengesankan?"adegan h147 dengan larut

                    em"Saya tidak bisa mengatakan saya tidak terkesan."adegan hitam dengan larut

                    jeda (0,01)

                    adegan hrub dengan larut

                    aw"Lalu mari kita geser sedikit di atasnya."em"Ahhh ... sangat dekat dengan lubang."em"[name], it’s almost going in."em"Sangat licin. Saya pikir itu akan meluncur."aw"Bukankah sudah waktunya untuk memasukkannya?"aw"Mari kita peregangan Anda sedikit."adegan h150 dengan larut

                    aw"Ini dia…"adegan h125 dengan larut

                    MC"Tidak, saya belum siap untuk melakukan ini, berhenti!"adegan h154 dengan fade

                    MC"TOOO!"adegan h155 dengan larut

                    MC"Oh. Itu pasti mimpi buruk."em"Apa yang terjadi, sayang? Anda membangunkan saya."MC"Tidak ada apa-apa. Ini hanya mimpi buruk."em"Oke. Selamat malam, sayang."MC"Selamat malam, babygirl saya."adegan h156 dengan larut

                    em"HHH ... Sayang?"MC"Ya."em"Bagaimana kita pulang? Saya tidak ingat."em"Dan saya merasakan sakit di antara kaki saya."adegan h154 dengan larut

                    MC"Kamu bilang apa!?"adegan h94 dengan fade

                    berhenti sebentar

                    adegan inf2 dengan larut

                    berhenti sebentar"Tidak":




            adegan h157 dengan fade

            MC"TOOO!"adegan h158 dengan larut

            MC"Oh. Itu pasti mimpi buruk."adegan h159 dengan larut

            MC"Hey. Where is [fname]?"adegan h91 dengan fade

            UNK2"Sekarang, mari kita beralih ke pertanyaan kedua dan terakhir."UNK2"Saya sarankan Anda menjawab ini dengan bijak. Kali ini jawaban yang salah yang Anda berikan mungkin tidak memiliki obat."adegan h157 dengan larut

            MC"TOOO!"

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

    em "Mmm ..."mct"Dia sangat menyukainya, dia bahkan tidak mendengar saya masuk. Dia terlihat sangat terangsang."adegan vt2 dengan larut

    mct"Haruskah saya meninggalkannya sendirian, atau haruskah saya bergabung?"adegan vt3 dengan larut

    mct"Saya bahkan tidak tahu harus berpikir apa."menu:"Terus menonton":

            Adegan VT4 DGANG LARUT

            mct"I shouldn’t be watching this… but I can’t take my eyes off her."mct"Dia terlihat sangat cantik seperti ini ... sangat rentan, begitu tersesat dalam dirinya."adegan vt3 dengan larut

            mct"Apa artinya ini bagi kita? Untuk saya? Ya Tuhan, aku seharusnya tidak merasakan hal ini dihidupkan, haruskah aku?"adegan vt11 dengan larut

            mct"Saya diam -diam mengawasi istri saya dan menyentuh diri saya sendiri."adegan vt13_5 dengan larut

            mct"Bagaimana kita sampai pada titik ini?"mct"Apakah saya benar -benar kehilangan nafsu?"adegan vt12 dengan larut

            berhenti sebentar 

            adegan vt13 dengan larut

            em"Hah?"adegan vt17 dengan larut

            em"Astaga! Apa yang kamu lakukan?!"adegan vt18 dengan larut

            MC"[fname], I—uh—"adegan vt19 dengan larut

            em"Apakah Anda hanya berdiri di sana ... mengawasi saya?!"em"Dan apa itu? Apakah Anda ... menyentuh diri sendiri?!"adegan vt20 dengan larut

            MC"[fname], I— I couldn’t help it… You were just…"adegan vt21 dengan larut

            em"Astaga! Ada apa denganmu?!"adegan vt22 dengan larut

            EMT"Saya tidak percaya ini sedang terjadi! Tapi ... mungkin alasan saya sangat marah bukan hanya karena dia mengawasi saya ... itu karena Andrew. Apa yang kami lakukan…"EMT"Itu membuat saya merasa sangat bersalah dan begitu ... dinyalakan pada saat yang sama. Ya Tuhan, apa yang salah denganku? Mungkin berteriak padanya adalah satu -satunya cara saya bisa mengatasi rasa malu ini."adegan vt23 dengan larut

            mct"Saya tahu saya seharusnya tidak menonton ... tetapi melihatnya seperti itu, saya tidak bisa berhenti. Ya Tuhan, aku telah mengacaukan banyak waktu."MC"Honey, [fname]… I’m sorry. I shouldn’t have… done that. It was wrong, and I crossed a line. I wasn’t thinking."adegan vt24 dengan larut

            em"Anda benar, Anda melewati garis!"adegan vt25 dengan larut

            EMT"Saya berteriak padanya, tapi ... apakah benar -benar dia marah? Atau apakah itu saya? Semuanya terasa di luar kendali sejak Andrew. Dan sekarang ini ... tapi mungkin saya melangkah terlalu jauh."adegan vt26 dengan larut

            em"Saya ... maaf juga. Saya seharusnya tidak berteriak seperti itu. Semua ini hanya ... sangat luar biasa."adegan vt27 dengan larut

            MC"Tidak, Anda benar untuk marah. Saya menginvasi privasi Anda, dan saya seharusnya tidak melakukannya. Itu salahku."em"Mungkin ... tapi saya juga tidak bersalah di sini. Ada begitu banyak rasa bersalah yang saya bawa akhir -akhir ini, dan itu hanya ... sulit untuk ditangani."adegan vt28 dengan larut

            MC"Mungkin kita bisa ... membicarakannya? Bersama? Aku benci melihatmu seperti ini, dan aku tidak ingin memperburuk keadaan."adegan vt29 dengan larut

            em"Ya ... mungkin kita harus melakukannya. Kami tidak bisa terus seperti ini. Itu tidak baik untuk kita berdua."adegan vt28 dengan larut

            MC"I just want us to figure this out, [fname]. I love you, no matter what."adegan vt30 dengan larut

            em"Aku pun mencintaimu. Bahkan jika Anda kadang -kadang idiot."adegan vt31 dengan larut

            MC"Anda tahu ... mungkin sudah saatnya kita berbicara dengan seseorang tentang semua ini. Saya tidak ingin terus mendorong semuanya."MC"Kami telah melalui banyak hal, dan mungkin kami bisa menggunakan bantuan untuk memahaminya."adegan vt32 dengan larut

            em"Seorang terapis? Apakah kamu serius?"adegan vt33 dengan larut

            MC"Saya tidak tahu ... Saya pikir itu bisa membantu kami. Maksud saya, semua yang kami hadapi - saya, Anda, Andrew ... ada begitu banyak hal yang terjadi."MC"Mungkin kita membutuhkan seseorang untuk membimbing kita melalui ini."adegan vt34 dengan larut

            em"Saya kira ... tidak ada salahnya. Saya merasa sangat tersesat akhir -akhir ini. Tapi ... bagaimana jika itu membuat semuanya lebih buruk? Dan saya tidak tahu, saya merasa seperti saya berubah. Saya bahkan tidak mengenali diri saya lagi."adegan vt33 dengan larut

            MC"Saya mengerti. Tapi itulah sebabnya kami membutuhkan bantuan. Kami tidak dapat melakukan ini sendirian, dan kami tidak perlu melakukannya."adegan vt35 dengan larut

            em"Ya, saya sudah lama menahan semua ini, dan saya hanya ... Saya tidak tahu siapa saya. Ini menakutkan."adegan vt36 dengan larut

            MC"I understand, [fname]. But whatever happens, we’ll go through it together. We’ll figure it out. I’m here for you."adegan vt35 dengan larut

            em"Oke… Aku percaya padamu. Ayo coba. Mari kita bicara dengan seseorang."adegan vt36 dengan larut

            MC"Kemudian saya akan memesan janji dengan terapis yang telah diatur pemerintah untuk Anda sesegera mungkin."adegan vt37 dengan larut

            em"Oke."
        "Menyela Dia":


            adegan vt4 dengan larut

            MC"[fname]?"adegan vt5 dengan larut

            berhenti sebentar

            adegan vt6 dengan larut

            MC"Apa yang sedang kamu lakukan?"adegan vt17 dengan larut

            em"Astaga! Saya tidak berpikir Anda akan segera kembali!"adegan vt18 dengan larut

            MC"Ya, saya baru saja menurunkan telepon Andrew dan langsung pulang. Tapi ... um, saya kira saya mengganggu sesuatu."adegan vt20_b dengan larut

            em"TIDAK! Maksudku ... ya ... Maksudku ... Ya Tuhan, ini sangat memalukan!"adegan vt21_b dengan larut

            MC"Hei, hei, tidak apa -apa. Benar-benar. Kita semua memiliki kebutuhan, Anda tahu? Tidak ada yang perlu malu."adegan vt20 dengan larut

            em"Tapi ini ... ini terasa berbeda. Rasanya ... entah bagaimana salah. Setelah Andrew, saya ... saya seharusnya tidak merasa seperti ini."adegan vt25 dengan larut

            MC"Look, [fname], maybe we need to talk about this. These feelings you’re having, this guilt… It’s eating you up, and I hate seeing that."adegan vt26 dengan larut

            em"Apakah saya ... apakah saya beralih ke orang lain atau ... ya ampun! Saya orang yang mengerikan. Kenapa kamu begitu baik padaku?"adegan vt28 dengan larut

            MC"Tidak, tidak, jangan berpikir seperti itu. Anda tidak mengerikan. Sesuatu terjadi dengan kami, dan mungkin ... mungkin kami membutuhkan seseorang untuk membantu kami mengetahuinya. Bersama."adegan vt29 dengan larut

            em"Apakah Anda mengatakan ... seorang terapis?"adegan vt28 dengan larut

            MC"Ya. Merasa bersalah itu alami, tetapi kita tidak boleh membiarkannya mengambil alih. Dan jujur saja ... Saya mencoba mencari tahu perasaan saya sendiri juga. Situasi ini ... itu memengaruhi saya dengan cara yang tidak saya harapkan."adegan vt29 dengan larut

            em"Apa maksudmu? Apakah Anda mengatakan bahwa apa yang terjadi dengan Andrew dan saya tidak ... mengganggu Anda?"adegan vt29_b dengan larut

            mct"Permainan kecil yang dia mainkan dengan Theo, cara dia membawa Andrew ke mulutnya - hanya memikirkannya membuat saya keras."mct"Saya tidak bisa mengakuinya sekarang, tetapi mungkin seorang terapis dapat membantu saya mengetahui mengapa ini membuat saya begitu banyak."adegan vt28 dengan larut

            MC"Saya tidak akan mengatakan itu tidak mengganggu saya. Tetapi pada saat yang sama ... sepertinya memengaruhi saya dengan cara yang berbeda. Hampir seperti ... Saya tidak tahu, seperti saya baik -baik saja dengan itu. Mungkin bahkan ... saya tidak tahu ..."adegan vt32 dengan larut

            em"Apakah kamu serius?"adegan vt33 dengan larut

            MC"Ya, saya pikir begitu. Tapi itu sesuatu yang perlu saya pikirkan juga. Itu sebabnya saya pikir melihat seseorang dapat membantu kami. Kami berdua."adegan vt29 dengan larut

            em"Oke. Mungkin Anda benar. Layak dicoba."adegan vt28 dengan larut

            MC"Kami akan melewati ini. Bersama. Saya berjanji."adegan vt30 dengan larut

            em"Oke sayang, aku percaya padamu."adegan vt31 dengan larut

            MC"Kemudian saya akan memesan janji dengan terapis yang telah diatur pemerintah untuk Anda sesegera mungkin."adegan vt30 dengan larut

            em"Oke."adegan vt38 dengan larut

    em"Saya tidak tahu mengapa, tetapi tiba -tiba saya sangat gugup."adegan vt39 dengan larut

    MC"Benar-benar? Anda tampak baik -baik saja di sini."adegan vt40 dengan larut

    em"Saya, tapi sekarang ... gagasan duduk di sana, membuka diri kepada beberapa pria yang bahkan tidak saya ketahui, rasanya begitu ... mengintimidasi."adegan vt41 dengan larut

    MC"Hey, he’s not just ‘some guy.’ He’s a professional, [fname]. This is his whole thing—helping people feel better."adegan vt42 dengan larut

    em"Saya tahu, tapi ... lebih dari itu. Terkadang saya merasa seperti saya bahkan tidak perlu membutuhkan ini. Seperti, dari semua orang, saya harus bisa menanganinya."

    em "Maksud Saya, Saya Salah Satu Dari Sedikit Wanita Yang Tersisa Di Dunia Yang Tenjak Terpengaruh Oleh Virus Itu. Dan Alih -alih Merasa ... Spesial Atau Bersyukur, Saya Merasa Tersesat. Seperti Saya Gagal."

    scene vt43 with dissolve

    mc "[fname], you’re not failing. No one is expecting you to carry the weight of the world just because of this. You’re human, and it’s okay to need help."

    scene vt44 with dissolve

    em "SULT UNTUK DIJELASKAN. SAYA Merasa Seperti Saya Tidak Hanya Mengecewakan Diri Sahah Tetapi Jua ... Semua Orang BuGA."

    scene vt45 with dissolve

    mc "Anda Tidak Mengecewakan Siapa Pun. Anda Di Sini, Anda Mencoba, Dan Itu Lebih Dari Yang Akan Dilakukan Kebatakan Orang. Anda Diizikansan Mengalami Hari -Hari Yang Buruk."

    mc "That doesn’t make you weak, [fname]. It makes you human."

    scene vt44 with dissolve

    em "Saya Kira Itu Sebabnya Saya Di Sini, Kan? UNTUK MENCARI TAHU SEMUA INI."

    scene vt45 with dissolve

    mc "Tepat. Dan Lohat, Anda Tidak Sendirian Dalam Hal ini. SAYA AKAN BERADA DI SINI, SETIAP LANGKAH."

    scene vt44 with dissolve

    em "Anda Benar -Benar Pandai Dalam Hal Pembicaraan Ini, Anda Tahu Itu?"

    scene vt45 with dissolve

    mc "Itu Hadiah. Sekarang, Mari Kita Masuk Ke Sana Sebelum Anda Memutuskan untuk Mengikats. Kami Mendapatkan ini."

    scene vt46 with dissolve

    em "Baiklah. Tetapi Jika ini Berjalan Mengerikan, dan Berutang Makan Malam Kepada Saya ... Hidangan Penutup .... Pijat Puncgung…. Dan anggota duat dan ..."

    scene vt47 with dissolve

    mc "Wow, Anda Benar -Benar menaikkan tarakanya di Sini. Apa selanjutnya? Menencuci mobil Mobil Andada?"

    scene vt48 with dissolve

    em "Sebenarnya, Itu Bukan Ide Yang Buruk."

    scene vt49 with dissolve

    mc "Jangan Mendorongnya."

    scene vt50 with dissolve

    em "Hei, Saya Hanya Mengatakan, Motivasi Itu Penting."

    scene vt51 with dissolve

    mc "Baik, Tetapi Hanya Jika Anda Selamat Dari Sesi Tanpa Kehabisan Pintu Berteriak."

    scene vt52 with dissolve

    em "Kesepakatan Adalah Kesepakatan. TAPI JANGAN BERPIKIR SAYA TIDAK AKAN MERAHAN MANA UNTUK SEMUA ITU."

    scene vt53 with dissolve

    mc "Dicatat. Sekarang, Mari Kita Pergi Sebelum Daftar Ini Menjadi Lebih Lama."

    scene vt54 with fade

    psy "Selamat Datang, Tollong, Duduklah. SAYA SENANG ENA BERDUA BISA MEMBUATYA HARI INI."

    psy "Mari Kita Mulai Delanan Perkenalan. Saya Dr. Matt Wise, Dan Saya Di Sini Untuchantu Gangan Tantangan apa pun yang Munckin Anda Hadapi."

    psy "I must say, it’s not every day I get to meet someone like you, [fname]. You’re truly one of the rare ones. It’s an honor to have you here."

    scene vt55 with dissolve

    psy "Ini Adalah Ruang Yang Aman, Jadi Jangan Ragu Unkukspresikan apa pun yang ada di pikiran anda."

    scene vt56 with dissolve

    mc "Kami Telah Melalui Beberapa Hal Akhir -akhir ini ... sulit unkak Dijelaskan, Tetapi Itu ... Itu memengaruhi hubungan Kami."

    scene vt57 with dissolve

    psy "TIDAK APA -APA. HUBUNGAN BISA MENJADI RUMIT. JENIS TANTI: APA UNA HADAPI?"

    scene vt58 with dissolve

    em "Ya, Itu ... Saya Merasa Banyak Kesalanan Dan Kebingungan, Terutama Delan Semua Yang Terjadi."

    em "Sepertinya Saya Terpecah Antara Apa Yang Sua Rasakan Dan Apa Yang Diharapkan Dari Saya."

    em "Dan Saya Kira, Kami di Sini Karena Kami Tidak Tahu Bagaimana Menghadapi Semua Ini. Itu ... ITU Mengacaukan Kedua Kita Kita."

    scene vt59 with dissolve

    mc "Ya, Maksud Saya, Itu Hanya ... Sahah Sadio memahami Perasaan Sendiri. Ini Banyak Tekanan, Dan Saya Tidak Ingin Hal -hal Menjadi Lebih Buruk Di Antara Kami."

    mc "Kami Datang Karena ... Saya Pikir Kami Perlu Bantuan Menavigasi Ini, Anda Tahu?"

    scene vt57 with dissolve

    psy "Ada Baiknya dan Berdua di Sini Bersama. Hubungan bisa melalui tempat -tempat siter,"

    psy "Tetapi Delangal Alat Dan Pemahaman Yang Tepat, Banyak Hal Dapat Dilakukan. SAYA DI SINI UNTUK BERTUK MEMBURNYA MELLALUI ITU."

    psy "Before we proceed, I need to run a quick test with [name] to better understand the confusion you’re both facing."

    scene vt60 with dissolve

    mc "Wait, what? me? You’re doing a test on me? I thought we were here [fname]..."

    scene vt61 with dissolve

    psy "Ya, Tentu Saja. Tetapi UNTUK MEMAHAMI SEMUANYA SEPENUHYA, PENTING UNTUTU PERTALAI DENGAN BERFOKUS PAYA ANDA."

    psy "Ini adalah bagian Dari proses untuk melihata bagaimana perasaan dana berdua secara individu."

    scene vt62 with dissolve

    mc "Baiklah, Oke ... Kurasa Itu Masuk Akal."

    scene vt63 with dissolve

    psy "Kami Akan Sampai Pada Anda Berdua, Jangan Khawatir. Tapi Pertama -Tama, Memahami Dari Mana Anda Berasal, Sangan Penting. Kami Akans Mengzil Satu Langkah Pada Satu Waktu."

    scene vt64 with dissolve

    em "Sepertinya Dia Mulai Delanmu, Sayang."

    scene vt63 with dissolve


    menu:
        psy "Katakanlah Anda Seoran Petani, Dan Benih Tahun Ini Tidak Menghasilkan Hasil Yang Anda Harapkan. Bagaimana Anda Mendekati Situasi ini?"
        "Terlihat lebih Baik Biji":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "Saya akan mencari biji berkualitas lebih baik dan mencoba lagi."
        "Biarkan Ladi Kosong":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "Saya akan meninggalkan musim kosong dan menunggu yang lebih beruntung tahun depan."

    scene vt66 with dissolve

    psy "Hmm..."adegan vt63 dengan larut


    menu:
        psy"Anda akan melakukan perjalanan dengan seseorang di sisi Anda, dan tiba -tiba, orang lain bergabung dengan Anda. Bagaimana perasaan Anda pada saat itu?"
        "Merasa Bersemangat":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "Saya merasa bersemangat, seperti awal yang baru dengan teman baru."
        "Merasa Tidak Nyaman":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "Saya merasa tidak nyaman, karena kehadiran orang lain mengganggu keseimbangan."

    scene vt66 with dissolve

    psy "Jadi Begitu ..."

    scene vt63 with dissolve


    menu:
        psy "Di Taman, Dua Bunga Tumbuh Berdampingan. Ketika mela melihat bahwa yang satu sedikit lebih besar dan lebih menarik perhatian Daripada Yang lain, Bagaimana Perasaan Anda?"
        "Rasananya Seimbang":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "Rasanya seperti keseimbangan alami, dan saya merasakan bahwa mereka saling melengkapi."
        "Fokus Saya Bergeser":


            $ ntr_point += 1

            mc "Fokus saya terganggu, dan saya merasa tidak nyaman."

    scene vt66 with dissolve

    psy "Menarik ... Anda Hampir Menyelesaan Tes, Hanya Beberapa Pertanya Lagi."

    scene vt63 with dissolve

    psy "Ketika Anda Masih Kecil, Apakah Anda Pernah Berharak Saudara Kandung?"

    scene vt65 with dissolve

    mc "APA HUBUNKANYA INI DENGAN SESUATU? SAYA TIDAK MENDAPATKAN KONEKSI."

    scene vt67 with dissolve

    psy "Tolong, Jawab Saja Sejujur Munckin. Ini Adalah Bidang Profesional Saya, Dan Sahah Tenjak Akan Mengomentari Interpretasi Hasil Dulu."

    scene vt60 with dissolve

    mc "MAAF, Anda Benar. Mari Kita Lanjutkan."

    scene vt63 with dissolve


    menu:
        psy "Bukan Masalah! Lalu ... Ketika dana Masih Kecil, Apakah Anda Pernah Berharak anda Memilisi Saudara Kandung?"
        "Ya":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "I've always wanted a sibling."
        "TIDAK":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "No, I've always wanted to be an only child."adegan vt66 dengan larut

    psy"Hmm..."adegan vt63 dengan larut


    menu:
        psy"Apakah Anda orang kucing atau anjing?"
        "Anjing":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "I'm a dog person. I love the loyalty and companionship."
        "Kucing":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "I'm a cat person. I enjoy the independence and mystery."adegan vt66 dengan larut

    psy"Hmm ... mencatat."psy"Pertanyaan dilakukan."adegan vt63 dengan larut

    psy"Thank you for answering. Now, we’ll continue alone with [fname] for a bit. You can wait outside."adegan vt68 dengan larut

    MC"Terima kasih, Dok. Aku akan menunggumu tepat di luar pintu, sayang."adegan vt64 dengan larut

    em"Oke, sayang."adegan vt63 dengan larut

    psy"Yes... Now that we’re alone... What brought you here today [fname]? Please tell me your feelings and thoughts, in all their nakedness."adegan vt70 dengan larut

    em"Dimana saya harus memulai?"

    em "Pertama, Izikan Saya Anggota Tahu dan Tentang apa yang telah Kami lalui sejauh inih."

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

    em "JUGA, Andrew Benar -Benar Lebih Tebal Dan Lebih Panjang Dari Lengan Saya."

    em "SAYA BAHKAN TIDAK TAHU BAGAIMANA ITU COCOK DI MULUT SENA. SAYA BISA MERASAKANNAA MENGISI TENGGOROKAN SENA DAN INI TIDAK MEMBUAT SENA JIJIK SAMA SEKALI."

    scene vt70 with dissolve

    em "Normally, I wouldn’t do this with [name]. I’d be disgusted, but in that moment, taking Andrew in my mouth actually aroused me."

    em "I'm feeling such mixed emotions. If I let myself go, it feels like a horrible person will come out. I don’t want [name] to be upset, but what I’m experiencing excites me."

    em "On the other hand, I love [name], and somehow these things don't feel right. I don't know how to explain it. It's hard to put into words."

    em "SAYA TAHU SERA SANGAT MENCINTINANYA ... SAYA KHAWATIR ITU AKAN MEMBAHAYAKAN HUBUNGAN KITA."

    scene vt73 with dissolve

    em "MAAF, SAYA PIKIR SAYA Berbicara Sedikit Terlalu Terbuka."

    scene vt76 with dissolve

    psy "Tidak, Tidak. Yang Saya Intiban Di Sini Adalah Persis ini - menjadi transparan delana Saya. Jika Anda Bisa Transparan Delana SAYA, Anda Minjkin Minjkin Mendengar Suara Yang Anda Coba Hening Di Dalam."

    psy "Saya Mengerti Bahwa Anda Saat Ini Terjebak Antara Id Dan Superego Anda."

    psy "Sederhananya, Kepribadian dan Terdiri Dari Tiga Bagian: ID, Ego, Dan Superego."

    psy "Saat ini, Anda Berfungsi melalui ego Anda, Tetapi Superego Anda Menekan ID Anda, Khususnya Keinginan Seksual Anda."

    psy "Macet perasaan ini mesenciptakan. Semakin Anda Menekan, Semakin Kuat Kesalanan Anda. Ini bisa menjadi alasan tutkan ledakan anda."

    psy "Anda Perlu Membiarkan Diri dan Kebebasan - Terhubung Delan ID Anda Lagi. Hancurkan Tabu. DENGAN MELAKUKANNAA, ASA AKAN MENEMUMAN KESEIMBANGAN."

    scene vt72 with dissolve

    em "Itu Masuk Akal ... TAPI ITU SULIT. Saya Selalu Diajarkan untuk menjaga semuanya Tetap Terkendali."

    em "Rasananya Jika Saya Melepaskananya, Segalanya Bisa Lepas Kendali. SAYA TIDAK TAHU APAKAH SAYA BISA MEMPERCAYAI Diri Sendiri untuk melepaskananya."

    scene vt76 with dissolve

    psy "Dapat Dimengerti Bahwa Anda Ragu -Ragu. Proses Membebaska Diri Dari Apa Yang Telah Diaajarkan Kepada dan Bisa Luar Biasa, Tetapi ini Merupakan Langkah Yang Diperlukan Untuce Menemukan Kedamaian Pribadi."

    psy "Ini Bukan Tentang Meninggalkan Kontrol, Tetapi Tentang Menemukan Kesimbangan Yang Lebih Sehat. Apakah dana pikir dana mungkkin siap untuk menjelajijahi ini?"

    scene vt70 with dissolve

    em "SAYA AKAN MENCOBA."

    scene vt77 with dissolve

    psy "Sesi Kami Hampir Berakhir, Tetapi Sebelum Anda Pergi, Mari Kita Berlatih Cepat."

    scene vt70 with dissolve

    em "Oke."adegan vt76 dengan larut

    psy"Sekarang, dengan teknik ini, mari kita keluarkan energi psikis Anda."adegan vt75 dengan larut

    em"Apa yang perlu saya lakukan?"adegan vt76 dengan larut

    psy"Sekarang bangun, pergi ke belakang sofa, peluk diri Anda seperti ini dengan tangan Anda, dan tutup mata Anda."adegan vt78 dengan larut

    em"Seperti ini? Haruskah saya memeluk diri saya seperti ini?"adegan vt77 dengan larut

    psy"Tidak, tidak seperti itu. Biarkan saya membantu Anda sampai Anda terbiasa."adegan vt79 dengan larut

    psy"Angkat lengan Anda, dan saya akan membimbing Anda - pikirkan saya sebagai lengan Anda untuk saat ini."

    em "Oke, Dokter Bijaksana."

    psy "Di Sana, Begitu Saja. Santai, Ambil Napas Dalam -dalam, Dan ..."

    scene vt79_5 with dissolve

    psy "Rasakan Pergeseran Energi di Dalam Diri Anda. Lepaska Ketankangan APA Pun - Trust Prosesnya."

    scene vt80 with dissolve

    em "Uh ... apakah punu yakin Begitulah Seharusnya dilakukan?"

    scene vt81 with dissolve

    psy "Sangat. Percayalah Kepadaku. Teknik Ini Sangane Efektif Jika Dilakukan Delan Benar. FOKUS SAJA PERNAPASAN MANA DAN BIARKAN Diri dan Rilis Merasakan."

    scene vt82 with dissolve

    em "SAYA ... SAYA TIDAK TAHU APAKAH INI TERASA BENAR. Apakah dana yakin ini adalah bagian Dari teknik ini?"

    scene vt83 with dissolve

    psy "Anda Dataang Ke Sini UNTUK BANTUAN SAYA, Dan INI ADALAH TEKNIK YANG DIRANCANG UNTUK MELEPASKAN ENERGI DALAM JIWA ANDA."

    psy "Jika Saya Tidak Terlalu Terampil Dalam Pekerjaan Saha, Negara Bagian Tidak Akan Memperayakan Saha Bekerja Gangan Seseoran Seperti Anda."

    psy "TOLONG, AMBIL NAPAS DALAM -DALAM DAN BAYANGKAN ENERGI MEMALIR KELUAR KELUAR DARI TUBUH ENA SAAT SAYA MEMBIMBINGNYA PENGAN SENuhan SAYA."

    em "Hhh…"adegan vt84 dengan larut

    psy"Aku bisa merasakan keringat di dada dan jantungmu berdetak lebih cepat. Apakah teknik saya membuat Anda bersemangat?"

    em "APA? Menyenangkan Saya? Tidak, Itu Hanya ... RASANYA RUI: Sedikit Lebih Hangat, Itu Saja."

    scene vt83 with dissolve

    psy "Oh, mondar -mandir. Nah, Sesi Kami Hampir Berakhir. Sekarang, latihan terakhir ..."

    psy "Saya ingin anda menutup mata lagi dan membayangkan ini: Semua hala laki -laki Anda, merantai anda ..."

    psy "Dan Membuat dan Terkendali Tersedot Melalui menempatkan Anda Dan Mengalir Ke Luar."

    emt "Apakah Itu Berbisik di Telingaku? I -i fe -..."

    scene vt79 with dissolve

    psy "Bagus. Sekarang, Ambil Napas Dalam -Dalam Dan Rasakan Energi di Dalam Diri Anda. Lepaska Ketankangan. Percayalah Pada Dirima Sendiri."

    em "Ini ... aneh. SAYA Merasa ... Lebih Tenang, Tetapi buta Sedikit Terbuka."

    psy "Itu Benar -Benar Normal. Ini Adalah Proses. Teknik ini Membantu Melepaska Stres Dan Kecemasan Yang Dibangun, Memungkinkan dan UNTUK KEMBALI KEMBALI DENGAN Diri Batin Anda."

    scene vt85 with dissolve

    em "SAYA PIKIR SEYA BISA MERASKANYANA. Ini ... Tidak Nyaman, Tetapi Delangan Yang Yang Baik, Saya Kira."

    scene vt86 with dissolve

    psy "ITU KEMJUAN. Ingat, Anda Tidak Harus memilisi Semua Jawaban Sekarang. Tidak APA -APA UNTUK TIDAK PASTI."

    psy "TEKNIK INI CUKUP KUAT. Saya Mengembangkangkana Menggambar Insplatasi Dari Karya Freud. Ini membtu melepaskan ketahangan membangun Dan Menghasilkan Katarsis, yang merupakan langkah pertama dalam proses yang lebih dalam."

    psy "Saat Kami Melanjutkan, Kami Akan Melewati Tahap BerIKUTNYA."

    psy "ITU CUKUP BULTU HARI INI. Mari Kita Bawa Pasangan dan BuGA."

    if ntr_point >= nts_point:

        scene vt87_5 with fade

        mc "HEI, APAKAH SESIMU SUDAH BERAKHIR?"

        scene vt88_5 with dissolve

        psy "Ya, Kita Bisa Membungus Semuanya Hari ini."

        scene vt89_5 with dissolve

        mc "Jadi, Bagaimana Hasilnya Tanpaku? Apakah Anda Bisa Mengeluarkan Semuanya?"

        scene vt90_5 with dissolve

        em "Erm ... haha ... Saya Baru Saja Berbicara Tentang Semua Yang Telah Kami Lalui Akhir -akhir ini, Sayang."

        scene vt91_5 with dissolve

        psy "[fname] was very open during our session."

        scene vt92_5 with dissolve

        psy "Itu selalu Menyegarkan Ketika seseoran Benar -Benar bisa Telanjang Sendiri - Secara Emosional, Tentu Saja. Ini memunckinan kita tuk menjelajiahi kedalaman tersembunyi anda secara lebih efektif."

        scene vt93_5 with dissolve

        em "Ya. Saya Merasa Saha Hancur Bebas Dari Rantai Saha. SAYA PIKIR BEBERAPA BERGIBEUNGAN SAYA TELAH DISELESAIKAN."

        scene vt94_5 with dissolve

        mc "Rantai APA? Wow, Bahkan Satu sesi Tampaknya Memiliki Dampak Besar Pana Anda. Anda Terlihat lebih Percaya diri."

        scene vt95_5 with dissolve

        em "Saya Kira Dr. Wise Sangan Pandai Dalam Apa Yang Dia Lakukan."

        scene vt96_5 with dissolve

        psy "Ha ha ha. Terima Kasih, Tapi Sahah Tidak Melakukan Apa -APA. Segala sesuatu Yang Dicapai di Sini Adalah Berkat Upaya Dan Kememaan Klien Saya."

        scene vt98_5 with dissolve

        psy "Sesi Saya BerIKUTNYA AKAN DIMULAI. SAYA AKAN MENGARAPKAN UNGAI LAGI MINGGU DEPAN. Sampai Lompa."

        scene vt99_5 with dissolve

        em "Selamat Tinggal, Dr. Wise."

        scene vt100_5 with dissolve

        mc "Terima Kasih, Dr. Wise."

        jump first_ntr
    else:


        scene vt87 with fade

        mc "HEI, APAKAH SESIMU SUDAH BERAKHIR?"

        scene vt88 with dissolve

        psy "Ya, Kita Bisa Membungus Semuanya Hari ini."

        scene vt89 with dissolve

        mc "Jadi, Bagaimana Hasilnya Tanpaku? Apakah Anda Bisa Mengeluarkan Semuanya?"

        scene vt90 with dissolve

        em "Erm ... haha ... Saya Baru Saja Berbicara Tentang Semua Yang Telah Kami Lalui Akhir -akhir ini, Sayang."

        scene vt91 with dissolve

        psy "[fname] was very open during our session."

        scene vt92 with dissolve

        psy "Itu selalu Menyegarkan Ketika seseoran Benar -Benar bisa Telanjang Sendiri - Secara Emosional, Tentu Saja. Ini memunckinan kita tuk menjelajiahi kedalaman tersembunyi anda secara lebih efektif."

        scene vt93 with dissolve

        em "Uh ... ya, Itu ... Berwawasan Luas."

        scene vt94 with dissolve

        mc "[fname], is everything okay? Your cheeks are all red, and you seem like you’re breathing a little faster... Are you alright?"

        scene vt95 with dissolve

        em "APA? Tidak, Tidak, Tidak ada Yang Terjadi! Maksudku, Semuanya Baik -Baik Saja! Itu Hanya ... Anda Tahu, Berbicara. ITU SAJA."

        scene vt96 with dissolve

        psy "It’s normal to feel a little off after such an honest session. But don’t worry, [fname], you handled it very well."

        scene vt97 with dissolve

        em "Ya, Sungguh! Tenjak Ada Yang Perlu Dikhawatirkan ... Kan?"

        scene vt98 with dissolve

        psy "Kalau Begitu, Sampai Leta Lagi Minggu Depan. Hati-Hati Di Jalan."

        scene vt99 with dissolve

        em "Selamat Tinggal, Dr. Wise."

        scene vt100 with dissolve

        mc "Terima Kasih, Dr. Wise."

        jump first_nts

label first_ntr:

    scene vt101 with fade

    mc "Ayo ... Hanya Satu Gigitan. Anda tidak Akan mati karena berbagi."

    scene vt102 with dissolve

    em "Tidak. Tidak Terjadi ... Saya Mendapatkan Ice Cream Fair Dan Persegi ini."

    scene vt101 with dissolve

    mc "TAPI SANGAT SANGAT MENGINKINKANYA SEKARANG."

    scene vt103 with dissolve

    em "Nah, Anda Seharusnya Mendapatkan Milik Anda. Ketika Saya Bertanya, Anda Mengatakan dan Tidak Ingin."

    scene vt104 with dissolve

    mc "Saus Itu! Hal -hal Berubah, Terutama Ketika Saya Melihat dana Sangan Menikmatinya."

    scene vt105 with dissolve

    em "Sayang Sekali. Burung Awal Mendapatkan Cacing - Atau Dalam Hal Ini, Es Krim."

    scene vt106 with dissolve

    mc "Ayo, Gigitan Hanya Satu. Anda tidak Akan mati ... Meskipun Jika Itu Andrew, Anda Munckin Akan Membiarkannya Menjilat Es Krim, Ya?"

    scene vt107 with dissolve

    em "Andrew? Darimana Dia Berasal?"

    scene vt108 with dissolve

    em "Oh ... Maksudmu Hal Blowjob."

    scene vt108_5 with dissolve

    em "Anda Bercanda, Bukan? Anda Sepertinya Tidak Terlalu Terganggu Dangan Apa Yang Anda Lohat."

    scene vt106_5 with dissolve

    mc "Terakhir kali, anda anggota blowjob. Saya Pikir dan Tidak MenyUKai Hal Semacam Itu. SEJUJURNYA, SENA TIDAK TERLALU TERGANGGU DENGAN APA PAHANG SENA LIHAT."

    scene vt109 with dissolve

    em "APA Maksudmu? Jika Saya Pergi Ke Pria Itu Sekarang Dan Anggota Blowjob, Bukankah ITU Menggangku Anda?"

    scene vt110 with dissolve

    mc "AKU TIDAK TAHU ..."

    scene vt111 with dissolve

    em "Setelah Berbicara Gangan Terapis, Saya Merasa Sedikit Berbeda. Saya Pikir Beberapa Batasan Perlu Didorong Jika Kita Akan Menyelamatkan Dunia."

    scene vt112 with dissolve

    mc "Batas Macam apa, misalnya?"

    scene vt113 with dissolve

    em "Ketika Saya Bertanya Apakah dana Akan Terganggu Jika Saha Mengzil Pria Itu Di Mulut Saha, Anda Mengatakan dana Tidak Tahu. SAYA Kira ADA CARA TUKUHUIDA."

    scene vt114 with dissolve

    em "Bisakah Anda Memurs Es Krim Saya? Jika Anda Mau, Anda Bisa Menggigit, Sayang."

    mc "Hey [fname]!"

    scene vt115 with dissolve

    mc "APAKAH KAMU SERIUS?"

    scene vt116 with dissolve

    em "Hai! Saya Perhatikan dan telah melihat Saya para Menjilat es Krim Sejak Saya Tiba Di Sini."

    scene vt117 with dissolve

    em "Anda Menatap Saya Seperti Anda Ingin memakan Saya. Apakah anda ingin penyakit menjilat es krim anda?"

    scene vt118 with dissolve

    unk "S-SURE ..."

    scene vt119 with dissolve

    unk "WTF? Apakah Saya Mati Atau Sesuatu? Apakah Saya Di Surga?"

    em "Wow ... Mengapa Semua Orang Begitu Besar?"

    scene vt120 with dissolve

    unk "Ha ha ha."adegan vt121 dengan larut

    unk"Bukankah itu suamimu di sana? Apa yang terjadi di antara kalian berdua?"

    em "Anda Benar -Benar Ingin Berbicara Tentang Suami Saya Sekarang?"

    scene vt122 with dissolve

    unk "Oke ... Oke ... Terus Berjalan."

    scene vt123 with dissolve

    mct "I can’t believe [fname] changed this much after just one session. Are they talking about me?"

    scene vt124 with dissolve

    mct "Apakah Begitulah Hidup Saya Dari Sekarang?"

    mct "Dia Biasa Mengatakan Dia Tidak Suka Mengzil Milikku Di Mulutnya."

    mct "Now, she’s taking an old man’s without hesitation, even going all the way. As much as I hate to admit it, seeing [fname] like this fucking turns me on."

    scene black with dissolve

    pause (0.01)

    scene p_bj with dissolve

    pause

    scene vt126 with dissolve

    mct "Sial ... Kurasa Suda Berakhir Sekarang."

    scene vt127 with dissolve

    mc "Sayang. Mulutmu…"

    scene vt128 with dissolve

    em "Terima Kasih, Sayang. Saya Merasa Lelah, Bisakah Kita Pulu?"

    scene vt129 with dissolve

    em "Saya Pikir Adaapa Hal Yang Perlu Kita Bicarakan Sesudahnya."

    scene vt130 with dissolve

    mc "O-oke ... Tentu, Sayang."

    scene black with dissolve

    pause

    jump ntr_path_cont

label first_nts:

    scene vt101 with fade

    mc "Ayo ... Hanya Satu Gigitan. Anda tidak Akan mati karena berbagi."

    scene vt102 with dissolve

    em "Tidak. Tidak Terjadi ... Saya Mendapatkan Ice Cream Fair Dan Persegi ini."

    scene vt101 with dissolve

    mc "TAPI SANGAT SANGAT MENGINKINKANYA SEKARANG."

    scene vt103 with dissolve

    em "Nah, Anda Seharusnya Mendapatkan Milik Anda. Ketika Saya Bertanya, Anda Mengatakan dan Tidak Ingin."

    scene vt104 with dissolve

    mc "Saus Itu! Hal -hal Berubah, Terutama Ketika Saya Melihat dana Sangan Menikmatinya."

    scene vt105 with dissolve

    em "Sayang Sekali. Burung Awal Mendapatkan Cacing - Atau Dalam Hal Ini, Es Krim."

    scene vt106 with dissolve

    mc "Ayo, Gigitan Hanya Satu. Anda tidak Akan mati ... Meskipun Jika Itu Andrew, Anda Munckin Akan Membiarkannya Menjilat Es Krim, Ya?"

    scene vt107 with dissolve

    em "Andrew? Darimana Dia Berasal?"

    scene vt108 with dissolve

    em "Oh ... Maksudmu Hal Blowjob."

    scene vt108_5 with dissolve

    em "Anda Bercanda, Bukan? Anda Sepertinya Tidak Terlalu Terganggu Dangan Apa Yang Anda Lohat."

    scene vt106_5 with dissolve

    mc "Terakhir kali, anda anggota blowjob. Saya Pikir dan Tidak MenyUKai Hal Semacam Itu. SEJUJURNYA, SENA TIDAK TERLALU TERGANGGU DENGAN APA PAHANG SENA LIHAT."

    scene vt111 with dissolve

    em "Apakah Anda Benar -Benar Baik -Baik Saja Delan Semuanya? Dengan Bagaimana Keadaan Akhir -akhir ini?"

    scene vt112 with dissolve

    mc "SAYA Baik-Baik Saja. Itu Hanya ... Berbeda, TAPI ITU TIDAK BBEBED. Saya Kira Sua Suda Menerimanya."

    scene vt131 with dissolve

    em "Senang Mendengarnya. Sayang, Bisakah Kita Duduk Dan Berbicara Sebentar?"

    scene vt132 with dissolve

    em "Saya Suda Banyak Memikirkan apa yang dikatakan terapis. Mungkkin Kita Terlalu Menahan Banyak Hal. Ada Hal -hal Yang Bisa Kami Coba Buat Menjadi Lebih Baik."

    scene vt133 with dissolve

    mc "JENIS APA?"

    scene vt132 with dissolve

    em "Nah, ini Tentang Mendorong Batasan. Tulisgan Cara Yang Buruk, Hanya ... Batas Penguji. Mencari Tahu Apa Yang Berhasil Bagi Kami Berdua."

    scene vt133 with dissolve

    mc "Batas, ya? Saya Kira Tenjak Ada Salahnya Mengkeksplorasi, Selama Kita Berdua Nyaman."

    scene vt134 with dissolve

    em "Tepat. Ini Tentang Komunikasi, Kepercayaan ... Dan Anda Tahu, Munckin Bersenang -senang Saata Kami Melakukanya."

    scene vt135 with dissolve

    em "Kami Bahkan Bisa Mengubah ini menjadi permaitan, jika anda siap untuk tuk itu. Tantangan. TUKU MELIAT SEBERAPA Jauh Kami BERSEDIA UNTUK SALING PERGI."

    scene vt136 with dissolve

    mc "Tantangan, ya? Saya Tertarik. Game Seperti apa Yang Kita Bicarakan?"

    scene vt137 with dissolve

    em "Nah, Anda Melihat Pria Itu Berdiri Di Sana?"

    em "Dia Telah Menatapku Sejak Aku Duduk. SAYA BISA MERASAKAN MATANYA PAYA SAYA. Ini Semacam ... Menarik."

    scene vt138 with dissolve

    mc "Benar-Benar? Apa Kamu Yakin?"

    scene vt139 with dissolve

    em "Oh, Saya Yakin. Saya Perhatikan Cara Dia Menatap Saha. Hampiri Seperti dia Membayangkan Melakukan sesuatu kepada Saya. TAPI, SAYA Bertanya -tanya ... apa pendapat anda tentang itu?"

    scene vt138 with dissolve

    mc "SAYA KIRA SAYA TIDAK BISA MENYALAHKANNYA. Anda Terlihat Bagus Hari ini."

    scene vt140 with dissolve

    em "Hmm, Munckin. TAPI SAYA PIKIR ADA LEBIH DARI ITU. BABAIMANA JIKA KITA MEMBUAT Permaita INI? Mari Kita Lihat Seberapa Jauh Kita Bisa Mengzil ini."

    mc "Game, ya? APA Gunanya?"

    scene vt141 with dissolve

    em "Intinya Adalah TUK MELHAT SEBERAPA NYAMAN KITA BISA MENDAPATKAN HAL -HAL YANG BIASANYA TIDAK KITA COTA. Mari Kita LiHat Apakah dan Bisa Menanganinya."

    em "Jika Sahu Anggota Tahu Dia Bahwa Sahwa Menonton Menonton, Maukah Anda Cemburu, Atau Anda Akan Menikmati Menonton Saya Bermain Bermain Bersama?"

    scene vt142 with dissolve

    mc "Anda Tidak Serius, Bukan? Anda ingin Menggoda Dia, Di Depan Saya?"

    scene vt143 with dissolve

    em "Jangan Menyebutnya Godaan Delangan Tepat, Tapi Munckin Kita Membiarkannya Menonton Dari Kejauhan, Bagaimana Menurut Anda?"

    scene vt144 with dissolve

    em "MENGATIGA YERAIK -BAIK SAJA DENGAN MENGEKSPLORASI HAL -HAL ... MARI KITA LIHAT APAKAH MANA BENAR -BENAR BERSUNGGUH -SUNGGUH."

    scene vt145 with dissolve

    em "Terlihat Madu…."

    scene vt146 with dissolve

    mc "Wow ... Bisakah Aku Payah?"

    em "Haha ... Tenjak Sekarang. Permainan hanya hanya hanya sekarang."

    scene vt147 with dissolve

    mc "Sepertinya seseoran Agak Terlalu Bersemangat untuk Persenan Bergabung Gangan Permaind."

    em "Anda Menjadi Terlalu Bersemangat, Bukan?"

    scene vt146 with dissolve

    mc "Bisakah dana Menyalahkan Saya? Anda mergodaku seperti orang gila sekarang."

    scene vt148 with dissolve

    em "Hmm, Munckin Sahus Haru Berbalik Dan Membiarkannya Melihat Semuanya?"

    scene vt149 with dissolve

    mc "SAYA TIDAK TAHU APAKAH SEYA BISA MIANGANI LEBIH BANYAK, TETAPI SENA JELAS TIDAK MENGIKAN TIDAK."

    scene vt148 with dissolve

    em "Baiklah, Mari Kita Naikkan Taluhanya Sedikit."

    scene vt149 with dissolve

    em "Di Sana. Bagaimana Itu Unk Sedikit Sensasi?"

    scene vt148 with dissolve

    mc "Anda Benar -Benar Bermain Delang Api Di Sini ... TAPI SENA MENYUKAINYA."

    scene vt149 with dissolve

    em "Bagus. SEKARANG, BABAIMAN JIKA SAYA MEMBIOKAN DIA MELIAT SEDITIT LAGI?"

    scene vt150 with dissolve

    mc "Anda Serius? Anda Akan Melakukanya?"

    em "Mengapa Tidak? ITU HANYA Permaind, Bukan? Mari Kita Lohat Betapa Berani Kita Dapatkan."

    scene vt148 with dissolve

    em "Bagus. Mari Kita Terus Berjalan Sebentar Lagi. TAPI INGAT, INI ADALAH Permaita Kami. Kami Mengontrol Seberapa Jauh Kelanjutanya."

    scene vt149 with dissolve

    mc "Sangat."adegan vt147 dengan larut

    em"Mungkin aku harus membiarkan dia menyentuhku? Atau mungkin saya harus menunjukkannya lebih banyak lagi? Bagaimana menurutmu?"

    mc "Ohh…"adegan vt151 dengan larut

    em"Saya pikir sudah waktunya bagi saya untuk berbalik."

    em "Dia Tampak Terdiam. HARUSKAN SAYA PERGI Dan MEMBIARKANNAA PAYUDARAKU SEKALI?"

    mc "O-oke."adegan vt152 dengan larut

    em"Ha ha ha. Sepertinya Anda juga benar -benar masuk ke dalam permainan."

    em "Selain Itu, Jika Kita Membuka Kunci Semua Pencapaian Sekaligus, Bukankah Permaita Menjadi Membosankan?"

    mc "Haha, Kamu Benar, Itu Akan Terjadi."

    scene vt153 with dissolve

    em "Oh tidak…"adegan vt154 dengan larut

    em"Saya pikir dia ingin mengambil semuanya lebih jauh."

    mc "Oh sial!"adegan vt155 dengan larut

    em"Ayo ... Saya sangat dihidupkan, kita harus pulang dan berhubungan seks sekarang."adegan vt156 dengan larut

    MC"O-Oke ... Tentu, Sayang."Jump Second_nts

Label ntr_path_cont:

    adegan int1 dengan fade

    mct"[fname] has changed. It started with her hair—she was at the salon almost every other day. Then came the wardrobe makeover."mct"Setiap pakaian baru yang dia pilih tampaknya dirancang untuk memamerkan kepercayaan dirinya, daya pikatnya. Dan saya harus mengakui ... dia terlihat luar biasa."mct"Tapi itu bukan hanya penampilannya. Cara dia bertindak di sekitar saya ... itu juga berubah."adegan int4 dengan larut

    mct"Aku masih bisa merasakan cintanya, tapi tatapannya ... sekarang berbeda. Ada sesuatu di matanya, sesuatu yang tidak bisa saya pikirkan. Dan kemudian ada hari itu di taman ..."mct"Saya tidak bisa mengguncangnya. Mengawasinya dengan orang asing itu, lelaki tua itu ... Aku tidak tahu harus berpikir apa. Itu mendebarkan, tentu saja, tetapi pada saat yang sama, sangat meresahkan."adegan int1 dengan larut

    mct"Since that day, there have been times when she just disappears—quick trips, her phone off, completely unreachable. I can’t help but worry. Is she safe? Is she still the same [fname] I know?"adegan int3 dengan larut

    mct"Pilihan yang saya buat baru -baru ini telah membawa kami ke sini. Saya tidak bisa membantu tetapi bertanya -tanya ... apa yang harus saya lakukan secara berbeda?"adegan hm48_2 dengan fade

    mct"Mungkin saya mendorongnya terlalu cepat."adegan hm52_2 dengan larut

    mct"Tuhan ... pertama kali dia menyentuh ayam besar Andrew ... Aku tidak bisa mengeluarkannya dari kepalaku. Itu bahkan tidak muat di tangannya."adegan hd20_2 dengan larut

    mct"I remember the way he looked at [fname]… and the way she met his gaze, unflinching. Back then, I didn’t fully grasp it. But now? Now, everything is crystal clear."adegan nm8_2 dengan larut

    mct"Tuhan ... hatiku berdebar kencang. Saya tahu persis ke mana arahnya, namun ... Saya tidak menghentikannya. Karena jauh di lubuk hati ... saya ingin ini."adegan nm20_b_2 dengan larut

    mct"I couldn’t look away… [fname]’s hips pressing against Theo’s bulge… And in that moment…"adegan rt32_2 dengan larut

    mct"That look in [fname]’s eyes… burning, intense, completely unguarded. It wasn’t just desire—it was permission."mct"Undangan diam -diam. Dan alih -alih menolak ... saya mendapati diri saya ingin melihat seberapa jauh dia pergi."adegan rt42_2 dengan larut

    mct"God… For the first time, someone else came on [fname]’s face. I had fantasized about it before, imagined the scenario in my mind."mct"Tapi menontonnya terungkap, melihatnya menerimanya ... itu menghantam berbeda."mct"Itu terjadi begitu tiba -tiba ... bahkan sekarang, saya tidak tahu apa yang seharusnya saya rasakan. Haruskah saya marah? Haruskah saya menghentikan ini? Atau ... haruskah saya merangkulnya?"adegan vt115_2 dengan larut

    mct"[fname] handed me her ice cream, no words, just a soft, knowing smile before she turned and walked away. And in that moment, something deep inside me stirred."adegan vt118_2 dengan larut

    mct"Saya melihatnya mendekati seorang pria tua yang duduk di bangku. Dadaku menegang, denyut nadi saya berduri. Apa yang dia lakukan?"mct"Saya tidak perlu mendengar percakapan mereka - saya sudah tahu. Tuhan ... itu terjadi. Di sana, tepat di depanku. Sebuah fantasi yang telah saya mainkan di kepala saya berkali -kali ... tapi sekarang itu nyata."adegan vt123_2 dengan larut

    mct"When the old man unzipped his pants, I caught the look on [fname]’s face. Not a single trace of hesitation. No second thoughts. As if… as if she had been waiting for this."adegan vt124_2 dengan larut

    mct"Bibir yang saya cium setiap hari sekarang melilit ayam lelaki tua."mct"Apakah ini mimpi? Atau apakah saya akhirnya menghidupkan fantasi saya? Rasanya nyata, hampir mustahil ... namun, sensasi yang mengalir melalui saya tidak dapat dipungkiri."adegan int4 dengan fade

    mct"Saya bertanya -tanya apakah membawanya ke psikolog itu adalah kesalahan. Apakah saya memulai sesuatu yang tidak bisa saya kendalikan? Apakah saya kehilangan dia? Pikiran itu menggerogoti saya."adegan int1 dengan larut

    mct"Saya tidak bisa menyangkal betapa bahagianya dia sekarang. Dan saya tidak bisa menjauhkan diri untuk mengambilnya darinya. Jika jalan baru ini menggairahkannya, maka saya akan menemukan cara untuk beradaptasi."adegan int4 dengan larut

    mct"Saya akan memberinya ruang, mendukungnya - apa pun ini. Saya tidak ingin kehilangan dia. Jika inilah yang membuatnya tetap di sisi saya, maka saya akan menanggungnya. Karena terlepas dari segalanya ... aku masih mencintainya."adegan hitam dengan larut

    jeda (0,5)

    Jump home_nmorning

label home_nmorning:

    adegan nm1 dengan larut

    mct"Saya mendengar suara datang dari dalam lagi. Tapi ... suaranya tidak akrab."adegan nm2 dengan larut

    MC"Ahh ... aku harus bergegas dan berpakaian. Saya sudah terlambat bekerja."adegan nr1 dengan fade

    mct"Siapa orang ini? Dan bagaimana mereka begitu terjebak dalam percakapan mereka sehingga mereka bahkan tidak memperhatikan saya di sini?"adegan nr2 dengan larut

    MC"Apa yang terjadi di sini?"adegan nr3 dengan larut

    em"Oh, selamat pagi! Ini adalah Taylor - siswa yang saya ceritakan, yang saya temui di toko. Kami harus berbicara, dan dia bertanya apakah saya bisa mengajarinya. Jadi, ini dia."

    $ persistent.ty_unlock = True

    scene nr4 with dissolve

    ty "Yo, what’s up, man? Just grabbing some coffee. [fname]’s gonna help me out with numbers."adegan nr5 dengan larut

    MC"Matematika, ya? Dan Anda hanya ... di sini?"adegan nr6 dengan larut

    em"Ya, seperti yang saya katakan, saya mengajarinya. Pikir akan baik untuk mengobrol sedikit terlebih dahulu, mengenalnya lebih baik sebelum melompat ke matematika."adegan nr5 dengan larut

    MC"I see… But, [fname], you never mentioned tutoring anyone else besides Theo."adegan nr6 dengan larut

    em"Saya tidak berpikir itu layak disebutkan. Taylor membutuhkan bantuan, jadi saya menawarkan. Ini benar -benar bukan masalah besar."adegan nr4 dengan larut

    ty"Yeah, man, just tryna get my numbers right. [fname]'s been mad patient with me."adegan nr5 dengan larut

    MC"Right... Wasn’t expecting this. Uh, Taylor, just… make sure you don’t give [fname] a hard time, alright? You should be grateful she’s even helping you."adegan nr7 dengan larut

    ty"Chill, man, I got it. We’re just vibin’—math and coffee, no drama. I appreciate it, for real. [fname]’s got skills, and I’m just here to learn."adegan nr8 dengan larut

    em"Oh, tolong, Anda membuatnya terdengar seperti saya mengajari Anda rahasia alam semesta. Itu hanya matematika."adegan nr9 dengan larut

    MC"Ya, terserah. Saya punya pekerjaan, jadi saya akan meninggalkan kalian berdua. Just ... jaga agar semuanya tetap dingin, oke?"

    mc "Kami Akan Berbicara Nanti."

    scene nr10 with dissolve

    ty "Pasti, Kawan. Kami Baik -Baik Saja. Tidak Perlu Stres. Dan Hei, Jaga Dirima, Orang Tua. Kami Akan Menahan Benteng Di Sini."

    scene nr11 with dissolve

    mct "Honestly, I don’t feel comfortable leaving [fname] alone with him in the house."

    scene nr12 with dissolve

    em "Sayang, Jangan Lupa - Kita Akan Pergi Ke Bioskop Malam ini. Anda Ingat, Kan?"

    scene nr13 with dissolve

    mc "Tentu Saja, Saya Akan Berada Di Sana. Saya Berbicara Gelan Bos Saha, Dan Saya Akan Meninggalkan Pekerjaan Satu Jam Lebih Awal untuk Menemui dan Teater Di Teater."

    scene nr12 with dissolve

    em "Baiklah, Saya Akan Menunggu Anda Di Sana. Jangan membuat ayah Terlalu Lama Menunggu."

    scene nr14 with dissolve

    mc "Mengerti, Sayang. Sampai LimaPa Lagi."

    em "Sampai Lompa."

    ty "Bye-bye, Daddy-O!"

    scene nr15 with dissolve

    mct "Pria Yang Menjengkelkan."

    scene nr16 with fade

    ty "Alright, [fname], now that [name]’s outta the picture, we can get back to our convo."

    scene nr17 with dissolve

    em "Ya, Dimana Kita?"

    scene nr18 with dissolve

    ty "Oh ya - jadi apa masalahnya gargan dana dan matematika? Anda Selalu Meladi Angka Dan Semua Itu?"

    scene nr19 with dissolve

    em "Itu selalu menghi Gairah. SAYA SUKA LOGIKA DAN SANGTUR. INI SEPERTI MEMECAHKAN TEKA -TEKI."

    scene nr18 with dissolve

    ty "Man, Teka -Teki? SAYA SAMPAH PAYA ITU. TAPI HEI, SAYA MENDAPAT BAKAT UNTUK MENCARI TAHU ORANG. Seperti, Saya Sew Bisa Tahu - Anda Mendapatkan Kesabaran Gila."

    scene nr20 with dissolve

    em "Nah, Kesabaran Itu Penting, Terutama Saat Mengajar."

    scene nr21 with dissolve

    ty "Ya, Anda Seperti Ratu Dingin. AKU Yakin Tidakwa Ada Yang Bisa Terjadi Padamu."

    scene nr22 with dissolve

    em "SAYA MENCOBA UNTUK TETAP TENANG. ITU BEMBUAT PENJARAN LEBIH MUDAH."

    scene nr23 with dissolve

    ty "Yo, Sungguh, Jika Saya Adalah Seoran Guru, Saya Akan Kehilangan Akal. ANAK -ANAK HARI INI Liar."

    scene nr22 with dissolve

    em "Ini Bisa Menantang, Tetapi BagA Bermanfaat. Melihat seseoran akhirnya memahami sesuatu adalah perasaan yang hebat."

    scene nr24 with dissolve

    ty "ITU DALAM. Anda Pernah Berpikir untuk Melakukan Sesuatu Yang Lain? Seperti, SAYA TIDAK TAHU, RAP ATAU SEMACAMYA? Anda Mendapatkan Getaran Keren Itu."

    scene nr25 with dissolve

    em "Rapping?"adegan nr26 dengan larut

    em"Ha ha ha."adegan nr20 dengan larut

    em"Itu ... ide yang menarik. Saya tidak berpikir saya memiliki bakat untuk itu."adegan nr27 dengan larut

    ty"Nah, Anda akan membunuhnya. Anda mendapat kehadirannya. Dan, mari kita menjadi nyata, Anda akan terlihat bersemangat dalam video musik."adegan nr28 dengan larut

    em"Yah, terima kasih atas dorongan kepercayaan diri, tapi saya pikir saya akan tetap mengajar."adegan nr29 dengan larut

    ty"Cukup adil. Tetapi jika Anda ingin mencoba, saya adalah pria hype Anda."adegan nr30 dengan larut

    em"Saya akan mengingatnya."adegan nr31 dengan larut

    ty"Jadi, apa yang Anda lakukan untuk bersenang -senang? Anda sepertinya memiliki beberapa hobi tersembunyi."adegan nr32 dengan larut

    em"Hmm..."adegan nr33 dengan larut

    em"Saya menikmati membaca, yoga, dan terkadang melukis."adegan nr34 dengan larut

    ty"Yo, lukisan? Itu obat bius. Saya yakin Anda pandai dalam hal itu. Anda mendapatkan energi kreatif itu."adegan nr35 dengan larut

    em"Itu hanya hobi. Sesuatu untuk bersantai."adegan nr36 dengan larut

    ty"Sobat, Anda seperti paket total. Cerdas, kreatif, dan dingin. Anda seperti guru impian."adegan nr37 dengan larut

    berhenti sebentar

    adegan nr37_5 dengan larut

    em"Anda menyanjung saya, Taylor."adegan nr38 dengan larut

    ty"Nah, saya hanya membuatnya nyata, mengajar. Bicaralah fakta."adegan nr37 dengan larut

    EMT"Dia berbicara banyak omong kosong, tapi entah bagaimana, itu menghibur. Dan, saya harus mengakui ... fisiknya mengesankan. Jika dunia tidak berantakan, saya ragu dia akan kesulitan menjauhkan gadis -gadis itu."adegan nr38_5 dengan larut

    ty"Hai! Ada apa? Tiba -tiba Anda sangat sunyi. Apa yang ada di pikiran Anda?"adegan nr39 dengan larut

    em"Oh, tidak ada. Hanya memikirkan apa yang Anda katakan."adegan nr40 dengan larut

    ty"Haha, jadi aku punya kamu berpikir ', ya? Mungkin saya lebih mengesankan dari yang saya kira."adegan nr39 dengan larut

    em"Keyakinan tidak selalu merupakan hal yang buruk."adegan nr34 dengan larut

    ty"Tepat. Anda tidak bisa pergi ke mana pun tanpa itu, bukan?"adegan nr41 dengan larut

    em"Benar, tetapi terlalu banyak kepercayaan diri terkadang bisa membuat Anda mendapat masalah."adegan nr38 dengan larut

    ty"Hei, saya suka mengambil risiko. Di situlah kesenangan dimulai."adegan nr46 dengan larut

    em"Mengambil risiko, ya? Anda yang menarik."adegan nr40 dengan larut

    ty"Terima kasih, ajarkan. Dan Anda lebih menyenangkan dari yang saya harapkan."adegan nr48 dengan larut

    em"Sepertinya kami saling mengejutkan."adegan nr49 dengan larut

    ty"Ya? Yah, saya suka kejutan."

    ty "Membuat sesuatu ... lebih menarik."

    scene nr50 with dissolve

    em "Hati -Hati Sekarang, Taylor. Beberapa Kejutan Datang Delangan Konskuensi."

    scene nr49 with dissolve

    ty "Oh, Saya Bisa Menangani Sedikit Masalah. Peranyanya Adalah ... Bisakah Kamu?"

    scene nr52 with dissolve

    em "Hmm ... Berbicara Tentang Masalah, Saya Pikir 'Pelajaran Matematika' Anda dan Sudah Berakhir TUKUH Hari INI."

    scene nr49 with dissolve

    ty "Sial, Tepat Saat ITU BAGUS. Kira Saya Haru Menunggu Kelas BerIKUTNYA."

    scene nr51 with dissolve

    em "Kesabaran, Taylor. Munckin Lain Kali, Anda Akan Benar -Benar Mempelajari Sesuatu."

    scene nr49 with dissolve

    ty "Oh, Saya Sudah Belajar Banyak, Mengajar. Anda Belum Mengahuinya."

    ty "Sial, Kira Aku Haru Bangkit. TAPI JANGAN KHAWATIR, AJOKAN - SENA AKAN KEMBALI. Anda Tahu Saya Bukan Tipe untuk Melewatkan Kelas."

    scene nr48 with dissolve

    em "Itu Adalah Obrolan Yang Bagus, Taylor. Tidak Terduga, Tapi ... Menarik."

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

    ty "Yeah? Then how ‘bout a proper goodbye? No handshake kinda thing—I'm talkin’ real warm, real close. A little farewell hug, teach?"adegan nr53 dengan larut

    em"Tentu saja, datang ke sini."adegan nr54 dengan larut

    ty"Mmm, sekarang itulah yang saya sebut selamat tinggal. Anda berbau harum, mengajar. Berengsek."adegan nr55 dengan larut

    em"Wow ... itu sedikit lebih hangat dari yang saya harapkan. Yang lebih ketat, dan saya mungkin mulai berpikir Anda tidak ingin pergi."

    ty "Kotoran! Saya Bisa Tinggal Jika Anda Memintaku."

    scene nr56 with dissolve

    em "ITU LELUCON, TAYLOR."

    scene nr57 with dissolve

    ty "Aight, Aight. TAPI MANA BERMAIN DENGAN API, Menganjar. Anda Beruntung Saya Mendapat Kontrol Diri."

    scene nr58 with dissolve

    emt "Apakah dia ... Mencoba Dadaku? APA?"

    scene nr59 with dissolve

    tyt "Sial, payudarananya Berbau Harum Sekali. Seperti vanilla hangat atuu sesuatu. Jika Saha Mendorong Wajah Sahah Hanya Sedikit Lebih Dekat ... Saya Bersumpah Saha Akana."

    tyt "Man, this fool [name] don’t even know how lucky he is. Got me feelin’ all kinds of jealous. Straight up blessed, that dude."

    emt "Jika Saya Tenjak Menghentikanyaa Sekarang, Dia Akan Mulai Mengingikans Lebih ..."

    scene nr60 with dissolve

    em "Hmm, Kita Akan Melihat Tentang Itu Lain Kali. SAYA BERHARAP ENA Tepat Waktu untuk Sesi Kami BerIKUTNYA. Dan Saya Berjanji ... Perkakapan Kami Akan Lebih Menarik."

    scene nr61 with dissolve

    ty "Oh, Sekarang Kamu Benar -Benar membuatku hyped. Anda Mengatakan Saya Mendapat Pelajaran Lain?"

    scene nr62 with dissolve

    em "Katakan Saja ... Saya Akan Anggota dan Beberapa Pelajaran Lagi Tentang Apa Artinya Menjadi Seorang Pria."

    scene nr65 with dissolve

    ty "Sial, dari Slahah menjadi guru favorit Saya."

    scene nr64 with dissolve

    em "Sampai Lompa Minggu Depan, Taylor."

    scene nr65 with dissolve

    ty "Ya, ya. TAPI JANGAN MEMBUATKU MERUNGGU TERLALU LAMA, Mengajar. Seorang pria haru tetap tajar."

    $ renpy.end_replay()

    scene cm1 with fade

    em "Ahh ... Mengapa Anda Tidak Menjagab Telepon Anda?"

    scene cm2 with dissolve

    em "SAYA TELAH Terjebak di Sini Di Malam Hari, Bahkan Tidak Yakin Apakah Saya Haru Makarh Atau Tidak."

    scene cm3 with dissolve

    em "You are so dead, [name]!"

    scene cm4 with dissolve

    em "Hah."adegan cm5 dengan larut

    em"Akhirnya!"

    em "KEMANA SAJA KAMU? Saya Sudah Menunggu di Luar Selama Setengah Jam!"

    scene cm6 with dissolve

    mc "Maaf, Sayang. Pertemuan Darurat Muncul. Perusak Dalam Krisis, Mereka Pada Dasarnya Menyatakan Keadaan Darurat. Saya Bahkan Munckin Kehilangan Pekerjaan."

    scene cm7 with dissolve

    em "Tundgu, apa?!"

    scene cm8 with dissolve

    em "Oh Tidak ... Maafkan Aku, Sayang."

    scene cm9 with dissolve

    mc "Tidak, Tidak. SAYA HARUS MEMinta MAAF. Aku Seharusnya Tidak Meninggalkanmu Menunggu di Luar Selama ini. Mari Kita Hubungi Saja Saat Ini. Anda haru pulu."

    scene cm10 with dissolve

    em "Serius Delan? SAYA MERUNGGU SELAMA INI, SENA MUMKIN MUMKIN BAGA SAJA MASUK Dan Menonton film Sialan Itu."

    scene cm11 with dissolve

    mc "Dan Apa Yang Akan Anda Lakukan Di Film Tanpa Sah?"

    scene cm12 with dissolve

    em "Jangan Terlalu Memikirkanya. Lagipula Aku Sebagi Besar Di Sini Unkulett Johansson."

    scene cm13 with dissolve

    mc "Tentu Saja Anda."

    scene cm14 with dissolve

    em "Selain Itu, Tidak Bisakah Anda Meminta James Untuc Membuat Pemutaran Film Pribadi untuk Saya? Bola, bulong, bulong ..."

    scene cm15 with dissolve

    mc "... bagus. SAYA AKAN MENELEPON JAMES. Slahah Masuk Ke Dalam, Jangan Lebih Menonjol di Sini. Saya AKAN DATANG MENJEMPUT dan film setelah."

    scene cm16 with dissolve

    em "Ha! Kesepakatan. Anda Yang Terbaik. Terima Kasih, Sayang. AKU Mencintaimu!"

    scene cm17 with dissolve

    mc "Menca."

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

    em "Saya Menghargai Itu. Tidak setiap Hari dan BISA melihat sesuatu seperti ini, dan penyakit Mengingikans Pengalaman Penuh."

    scene cm24 with dissolve

    jm "Dan Anda Akan Mendapatkananya. Kamar Pribadi Suda Siap - Tidak Ada Gangguan, Suara Sempurna, Kursi Terbaik Di Rumah. Tempat Anda yang sama"

    scene cm25 with dissolve

    jmt "Sial, Lihat Saja Kaki -kaki Itu ... Halus, Kencang, Hanya Mohon Unkulici. Jika Saha memilisi Jalan, Saya Akan Menan Menjalankan Lidah Saya Setiap Inci, Lambat Dan Dalam, Sampai Dia Menggigil."

    jmt "I wonder… since [name] ain't around, maybe she’d let me hit it from the back just this once?"

    scene cm23 with dissolve

    emt "Itu Terlihat Sama Lagi ... Jika James Pernah Mendapatkan Saya, Saya Bahkan Tidak Ingin Membayangkan apa yang Akan Akan Lakukan."

    em "Sounds perfect. [name] really hyped this up for me. He kept going on about how impressive Sharlet Moansson is, saying I wouldn’t even be able to tell the difference with AI. Got me curious."

    scene cm26 with dissolve

    jm "Oh, Anda Siap untuk Mengobati. Sharlet Adalah ... Yah, Katakan Saja Dia Tidak Seperti Orang Lain. Bahkan Jika Itu Bukan Jenis Film Anda Yang Biasa, Anda Akan Menghargai Seni. Hampira Meresahkan Betapa Nyata Dia."

    scene cm23 with dissolve

    em "SAYA TELAH MELHAT BEBERAPA KLIP DI SANA -SINI. SANGAT MENARIK APA Yang Dapat Dilakukan Teknologi Sekarang. BABI SENA, INI LEBIH TENTANG RASA INGIN TAHU DAHIPADA APA PUN."

    scene cm26 with dissolve

    jm "Saya Mengerti. Film ini Bukan Hanya - Ini Adalah Pengalaman. Teater Yang Ditingkatkan Ai Menghidupkan Segalanya Delangan Cara Yang Sulit Dijelaskan. Anda akankan merasa seperti melangkah ke dunia lain."

    jm "Anda Tahu ... Dunia Bukan Tempat Yang Dulu. Kebanyakan Orang Yang Datang Ke Sini Hanya Ingin Mengingat Bagaimana Rasananya - Berada Di Sekitar Wanita Sejati. Sejak Bencana, bisnis telah booming."

    scene cm25 with dissolve

    jm "Terkadar SAYA Bertanya -tanya ... apa yang Saya Berikan Hanya Unkingat Seperti apa Rasanya. Merasakan Sesuatu Yang Nyata Lagi."

    jmt "Sobat, Saya Akan Anggota apaapa Saja Hanya untuk Satu Perjalanan Gangan Anda."

    scene cm27 with dissolve

    em "Wow. Itu ... Banyak Yang Haruus Dibongkar."

    scene cm8 with dissolve

    em "Mengesampingkan Bagian Tragis Dari Apa Yang Baru Saja Anda Katakan ... Film Ini Terdengar Mengesannan. SAYA SANGAT MERANTIKANYA."

    scene cm26 with dissolve

    jm "Ya ... Dan Jika Anda Membutuhkan Sesuatu - Nada, Minuman, Atau Bahkan Hanya Sebuah Perausaan Kecil - Anda Tahu di Mana Menemukan Sahah."

    scene cm23 with dissolve

    em "Terima Kasih, James, Tapi Saya Pikir Saha Akan Mengelola. Film Hanya Dan Sedikit Waktu Yang Sepi Adalah Yang Sua Butuhkan Malam ini."

    scene cm26 with dissolve

    jm " Suit yourself. But hey, the offer stands. Enjoy the show, [fname]. And don’t be a stranger—you know where to find me."

    scene cm23 with dissolve

    em "Terima Kasih, James. SENA AKAN MANGANI TAHU MANA BAJAIMANA KELANJUTANNAA."

    emt "Ya, Saya Yakin Dia Akan Melakukan apa Saja Untuce memba Saya Sendirian di Sana Bersamanya."

    scene cm29 with dissolve

    jm "Oh, Sahah Yakin Anda Akan Melakukanya."

    scene ca1 with fade

    em "Wow… This feels so real. The detail, the atmosphere… It’s like I’m actually there. [name] wasn’t kidding about how immersive this is."

    scene ca2 with dissolve

    emt "Oke ... ini jelas bukan film untuk tuk dironton sendirian. Mengapa Saya Pikir ini Ide Yang Bagus?"

    scene ca3 with dissolve

    em "I should’ve dragged [name] here with me. He’d probably love this… maybe even more than me."

    scene ca4 with fade

    em "Ya Tuhan, ini intens. Sepertinya menarik sausa sepenuhnya ..."

    scene ca5 with dissolve

    em "Bagaimana Jika Seseoran Masuk?"

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

    em "No… It’s private, right? James promised. I’m safe…"adegan ca7 dengan larut

    em"Ini gila. Saya tidak pernah merasakan hal ini - bukan hanya karena filmnya, tetapi karena risiko yang saya ambil. Garam itu ... itu benar -benar membuat saya bersemangat"EMT"Haruskah saya ... mungkin melepas sesuatu? Tidak ada yang masuk, dan bahkan jika mereka melakukannya ... jadi apa?"EMT"Saya lebih terbuka untuk pengalaman baru sekarang. Sama seperti sensasi yang saya rasakan ketika saya meniup lelaki tua itu di taman ..."adegan ca8 dengan larut

    EMT"Ini terasa sama."adegan ca9 dengan larut

    EMT"The thought of someone other than [name] seeing my breasts… it’s turning me on."adegan ca10 dengan larut

    EMT"Tapi bagaimana jika ... itu tidak berhenti hanya di payudaraku?"adegan ca11 dengan larut

    EMT"Bagaimana jika saya ingin lebih-jika saya ingin merasakan udara di semua kulit saya?"EMT"Pakaian saya adalah satu bagian ... jika saya melepasnya, saya akan benar -benar terbuka."adegan ca12 dengan larut

    EMT"Itu terlalu berisiko."adegan ca13 dengan larut

    EMT"Tapi ide itu ... itu hanya membuatku lebih panas .."adegan ca14 dengan larut

    EMT"[name] isn’t here, and someone else could catch a glimpse of my most intimate parts."adegan ca15 dengan larut

    EMT"Bagaimana jika mereka tidak melihat saja? Menyentuh saya? Jari saya…?"adegan ca16 dengan larut

    EMT"Mmm ... hanya memikirkannya ... Tuhan, apa yang terjadi pada saya?"adegan ca15 dengan larut

    EMT"Aku bahkan tidak memakai celana dalam ... Aku bisa merasakan betapa basahnya aku."adegan ca16 dengan larut

    EMT"Mungkin ... mungkin aku harus melepas semuanya."adegan ca17 dengan fade

    EMT"Tidak ada hambatan ... tidak ada apa -apa di jalan ... hanya saya, benar -benar terbuka."adegan ca18 dengan larut

    EMT"Bagaimana jika seseorang masuk? Tidak ... James bilang itu kamar pribadi saya. Tidak apa -apa ..."adegan ca19 dengan larut

    EMT"Ini terasa sangat berisiko. Tapi itu juga menyenangkan."adegan ca20 dengan larut

    EMT"Berapa banyak orang yang duduk di sini? Melakukan hal -hal di sini?"adegan ca19 dengan larut

    EMT"Bagaimana jika ada ... seseorang ... meninggalkan sesuatu? Seperti ... di kursi?"adegan ca20 dengan larut

    EMT"Bagaimana jika ... bagaimana jika ada ... sesuatu di kursi? Dan sekarang ada pada saya?"adegan ca21 dengan larut

    EMT"Bagaimana jika itu ... menyentuh kulit saya? Bagaimana jika itu ... di celana saya sekarang? Atau bahkan ..."adegan ca22 dengan larut

    EMT"Tidak mungkin ... apakah itu ...?"adegan ca23 dengan larut

    EMT"Dia. Ya Tuhan… seseorang sebenarnya…"EMT"Itu ada di sana, mengering ke kursi ... bukti kesenangan orang lain, pembebasan orang lain."EMT"Berapa banyak orang di sini, tersesat dalam panas yang sama seperti yang saya rasakan sekarang?"adegan ca24 dengan larut

    EMT"Ini gila. Saya seharusnya tidak memikirkan hal ini. Itu menjijikkan ... bukan?"EMT"Tapi kemudian ... mengapa tubuh saya terasa lebih panas?"adegan ca25 dengan larut

    EMT"Bagaimana jika saya hanya ... bersandar sedikit lebih dekat? Hanya untuk melihat ... pasti?"adegan ca26 dengan larut

    EMT"It’s real. Someone… some man, just like [name], sat here, unable to hold back. Right here, in this very spot."EMT"Bagaimana jika saya ... bagaimana jika saya duduk di sini juga? Jika saya membiarkan diri saya merasakan apa yang mereka rasakan?"adegan ca27 dengan larut

    EMT"Tidak. Saya tidak bisa. Itu gila. Bisa jadi siapa saja. Saya bahkan tidak tahu siapa—"EMT"Tapi itulah yang membuatnya begitu terlarang ... atau mungkin bahkan lebih menarik."EMT"Saya seharusnya tidak menginginkan ini. Saya seharusnya tidak memikirkan hal ini."adegan ca28 dengan larut

    EMT"Tubuh saya bereaksi sendiri. Ia tahu sesuatu yang ditolak pikiran saya untuk mengakui."adegan ca27 dengan larut

    EMT"Tidak ada hambatan ... tidak ada lapisan di antara ... hanya aku ... menekannya."EMT"It’s not [name]’s… but maybe that’s why I want it even more."adegan ca26 dengan larut

    EMT"Saya ingin merasakannya - menekankan diri saya terhadapnya, menggosoknya"EMT"Apakah rasanya berbeda? Apakah itu akan membuat saya kehilangan diri saya sepenuhnya?"adegan ca27 dengan larut

    EMT"Saya seharusnya tidak melakukan ini. Saya seharusnya tidak ... tapi ..."EMT"Tuhan… Saya ingin."adegan ca29 dengan larut

    EMT"Itu menyentuh bibir saya sekarang ... pria lain ... bukan suamiku ... mmm."adegan ca30 dengan larut

    EMT"Saya telah ... dinodai oleh orang lain."EMT"Bagaimana jika itu ... bagaimana jika itu merembes ke dalam diri saya?"adegan ca31 dengan larut

    EMT"Bagaimana jika itu bukan hanya di bibirku?"EMT"Bagaimana jika itu lebih dalam ... merendam saya?"adegan ca32 dengan larut

    EMT"Apakah saya ... diklaim oleh seseorang yang bahkan tidak saya kenal?"EMT"Sangat kotor ... sangat salah ... tapi saya tidak bisa berhenti memikirkannya."adegan ca33 dengan larut

    EMT"Tubuh saya gemetar - bukan karena ketakutan."EMT"Saya harus menarik diri ... Saya harus bangun dan pergi."adegan ca30 dengan larut

    EMT"Tapi sebaliknya ... Saya ingin menekan lebih keras."adegan hitam dengan larut

    jeda (0,01)

    adegan m_sld1 dengan larut

    em"Ini ... ini gila. Saya tidak bisa berhenti ..."adegan ca34 dengan larut

    em"Mmmm…"adegan ca35 dengan larut"*** fap fap fap ***"adegan ca36_5 dengan larut

    EMT"Apakah ada seseorang di belakangku, atau hanya imajinasi saya?"EMT"Ya, seseorang ada di sana. Dan ... dan apakah suara -suara itu saya dengar?"EMT"Astaga. Sudah berapa lama dia di sana?"EMT"Could it be [name]? No… it can't be. Why would he sneak up on me?"adegan ca36 dengan larut

    EMT"Bagaimana saya tidak mendengarnya masuk? Aku bahkan tidak bisa berbalik sekarang ... dia melihat segalanya."EMT"Saya kira hal yang paling cerdas untuk dilakukan adalah membiarkannya selesai dan pergi. Kalau tidak, ini bisa menjadi lebih rumit. Saya hanya akan bertindak seolah dia tidak ada di sana."adegan ca37 dengan larut

    EMT"Diawasi…"adegan ca38 dengan larut

    EMT"Itu membuat saya menyala."adegan ca39 dengan larut

    EMT"Apa-apaan?"EMT"Terlalu dekat, terlalu dekat, terlalu dekat."adegan ca40 dengan larut

    EMT"Ahh ... jantungku berdebar kencang."adegan ca41 dengan larut

    EMT"Jika saya menoleh ... rasanya seperti itu bisa berakhir di mulut saya."adegan ca42 dengan larut

    EMT"Mengabaikannya pasti membuatnya lebih berani."adegan ca43 dengan larut

    EMT"Ahhh ... Aku sangat hidup sekarang."EMT"Aroma itu ... sangat kuat, luar biasa."adegan ca44 dengan larut

    EMT"Sangat kuat, luar biasa. Saya bahkan tidak bisa menjelaskan. Itu maskulin, mentah, memabukkan"adegan ca45 dengan larut

    EMT"Mmm, aku benar -benar perlu bercinta."adegan hitam dengan larut

    jeda (0,01)

    adegan m_cnm1 dengan larut

    EMT"Mmm."adegan ca46 dengan flash

    berhenti sebentar

    adegan ca47 dengan flash

    berhenti sebentar

    adegan ca48 dengan flash

    EMT"He came all over me. What am I going to do now? I'm a mess… [name] is coming to pick me up soon."adegan ca49 dengan larut

    EMT"Saya tidak punya apa -apa untuk Clea. Saya tidak punya pilihan selain mengenakan pakaian saya kembali, semua kotor seperti ini."adegan ca50 dengan larut

    EMT"Saya tidak punya pilihan ... Saya harus mengenakan pakaian saya kembali, seperti ini. Lengket, berantakan ... ternoda."EMT"Saya merasa sangat kotor. Kehangatannya masih melekat pada kulit saya ... merendam saya."EMT"I just hope [name] doesn’t try to hug me when he picks me up. I don’t know if I can handle that right now."EMT"Dan bagian terburuk? Saya masih merasa sangat terangsang."EMT"Saya harus merasa malu. Saya harus jijik. Tetapi sebaliknya, saya masih bisa merasakan tubuh saya sakit untuk lebih."EMT"Bahkan sekarang ... kakiku terasa lemah, napasku goyah."adegan ca51 dengan larut

    EMT"As soon as I get home… I need to have sex with [name]."

    em "SAYA HARUS BERPAKAIAN ... SAYA BENAR -BENAR MELEWATI BATAS HARI INI."

    $ renpy.end_replay()

    scene ca52 with dissolve

    em "Selesai."adegan ca53 dengan larut

    em"Oh, dia di sini."

    em "Hei, Kamu di Sini?"

    em "Tidak, Tidak, Jangan Keluar Dari Mobil Madu. Saya Mendatangi Anda."

    scene black with fade

    "Akhir Versi 0.5. Anda Bisa Menyimpan Di Sini."


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
