# These are dialogues and corresponding youtube links/stamps
# When a reddit user comments something with bhattu in it. we omit the word "bhattu" and match the rest with the dialogues over here. we reply with the best matching one when match is better than a pre-defined threshold (80%)
# So, it is okay to have a single youtube stamp linked to multiple dialogues if you think reddit user might use different variations of dialogue
bhattu_dialogue_and_stamp = {
    r"chepa chethilo chiraagga untundi gani, notlo divyanga untundi ra": r"https://www.youtube.com/watch?v=6X438MDx-BE&t=73s",
    r"nuvvu rara": r"https://youtu.be/6X438MDx-BE?t=83",
    r"emitra peru, burra takkuva vedhavalu kakapothenu": r"https://youtu.be/6X438MDx-BE?t=130",
    r"mana antunnaventra, ayanedo ni mavayya annattu": r"https://youtu.be/6X438MDx-BE?t=137",
    r"akkada kuda mana domination ye antava?": r"https://youtu.be/6X438MDx-BE?t=151",
    r"kicku ra kicku": r"https://youtu.be/6X438MDx-BE?t=154",
    r"munduga ravadam mukhyama muhurtaniki ravatam mukhyama?": r"https://youtu.be/6X438MDx-BE?t=159",
    r"orey chari, nuvvu konchem noti dhoola tagginchali ra": r"https://youtu.be/6X438MDx-BE?t=185",
    r"pilla p...": r"https://youtu.be/6X438MDx-BE?t=188",
    r"friendship ki age limit em lede!!": "https://youtu.be/6X438MDx-BE?t=258",
    r"abba! aapara aprachyapu anumanalu nuvvooonu!!": "https://youtu.be/6X438MDx-BE?t=268",
    r"charitrademundi ra, chimpeste chirigipotundi": "https://youtu.be/6X438MDx-BE?t=290",
    r"Bhattu blushing": "https://youtu.be/6X438MDx-BE?t=299",
    r"Kani naa bad luck": "https://youtu.be/6X438MDx-BE?t=324",
    r"aa tension naku undiroy": "https://youtu.be/6X438MDx-BE?t=340",
    r"aa pani mathram cheyyakuroy": "https://youtu.be/6X438MDx-BE?t=354",
    r"bagunnara": r"https://youtu.be/6X438MDx-BE?t=372",
    r"manam sponsor chesinavera": r"https://www.youtube.com/watch?v=6X438MDx-BE&t=400s",
    r"inka challe aapara": r"https://youtu.be/6X438MDx-BE?t=418",
    r"em chepthamu ra, prathi dantlo common ye kada": r"https://youtu.be/6X438MDx-BE?t=438",
    r"pilla p.....": r"https://youtu.be/6X438MDx-BE?t=465",
    r"nikenni saarlu cheppanu Bhattu ani pilavamani, Bhattuu...": r"https://youtu.be/6X438MDx-BE?t=503",
    r"velli oka beer pattura": r"https://youtu.be/6X438MDx-BE?t=590",
    r"rey reyRey rey": r"https://youtu.be/6X438MDx-BE?t=634",
    r"gap ivvara gap ivvu": r"https://youtu.be/6X438MDx-BE?t=687",
    r"navvu aapukuntunnav kadara": r"https://youtu.be/6X438MDx-BE?t=695",
    r"Pilla p....": r"https://youtu.be/6X438MDx-BE?t=757",
    r"Ika teesukelli tagalabetteseyyandayya": r"https://youtu.be/6X438MDx-BE?t=797",
    r"Manchi Shubhavartha chebuthanu, rara": r"https://youtu.be/6X438MDx-BE?t=854",
    r"ee feeling entra": r"https://youtu.be/6X438MDx-BE?t=939",
    r"vaadi ishtam tho manaku panenti, manam proceed ayipodam": r"https://youtu.be/6X438MDx-BE?t=1030",
    r"chala sepu suspense tarvata": r"https://youtu.be/6X438MDx-BE?t=1076",
    r"I did a mistake": r"https://youtu.be/6X438MDx-BE?t=1084",
    r"I will see, I will see": r"https://youtu.be/6X438MDx-BE?t=1086",
    r"raara bhattu ra, nee gurinche matladutukuntunnam": r"https://www.youtube.com/watch?v=6X438MDx-BE&t=1155s",
    r"vinnaa, anthaa vinnaa": r"https://youtu.be/6X438MDx-BE?t=1158",
    r"kurchuni chese pani, aa maatram guppedu potta undadha": r"https://youtu.be/6X438MDx-BE?t=1166",
    r"nuvvu antha harshga matladaku, nenu feel authanu": r"https://youtu.be/6X438MDx-BE?t=1176",
    r"Bhattu shocked": r"https://youtu.be/6X438MDx-BE?t=1189",
    r"Chi chi, miru siggupadakandi": r"https://www.youtube.com/watch?v=6X438MDx-BE&t=1198s",
    r"Naku mantralu ravu kabatti saripoyindi gani, vachunte shapinchevadini ra": r"https://youtu.be/6X438MDx-BE?t=1241",
    r"aa! nenu vasthanandi": r"https://youtu.be/6X438MDx-BE?t=1348",
    r"Nenu aadhukundhamanukunnanu, meeru adukundhamanukunnaru": r"https://youtu.be/6X438MDx-BE?t=1396",
    r"Pattudhala vasthe drawer ye marchukonu, yedhava manasu yentha": r"https://youtu.be/6X438MDx-BE?t=1555",
    r"aathma shaanthinchadhandi": r"https://youtu.be/6X438MDx-BE?t=1644",
    r"Oorukondi sir, edho flowlo anesanu": r"https://youtu.be/6X438MDx-BE?t=1686",
    r"untundhi ra": r"https://www.youtube.com/watch?v=6X438MDx-BE&t=337s",
}

# When the user doesn't write proper dialogue, we don't get a matching dialogue from above dialogues.
# Then we tokenize (split the sentence into individual words) and see if we find a matching word from below, add corresponding dialogues to a list. select a random dialogue from that list and reply.
bhattu_text_and_link = {
    ("rara", "ra", "raa", "matladukuntunnam", "matladuthunna"): ["vinnaa, anthaa vinnaa", r"raara bhattu ra, nee gurinche matladutukuntunnam"],
    tuple(["knowledge"]): [r"chepa chethilo chiraagga untundi gani, notlo divyanga untundi ra",
                           r"friendship ki age limit em lede!!",
                           r"charitrademundi ra, chimpeste chirigipotundi",
                           r"kurchuni chese pani, aa maatram guppedu potta undadha",
                           r"Pattudhala vasthe drawer ye marchukonu, yedhava manasu yentha"
                           ],
    tuple(["domination"]): [r"akkada kuda mana domination ye antava?", r"kicku ra kicku"],
    ("come", "summon", "cum"): [r"nuvvu rara"],
    ("name", "peru"): [r"emitra peru, burra takkuva vedhavalu kakapothenu"],
    ("curse", "boothu", "angry", "anger"): [r"pilla p...", r"pilla p.....", r"Pilla p....", r"rey reyRey rey", r"Naku mantralu ravu kabatti saripoyindi gani, vachunte shapinchevadini ra"],
    ("pilla", "hook", "poo", "pook"): [r"pilla p...", r"pilla p.....", r"Pilla p...."],
    ("caution", "warn", "doola", "dhoola"): [r"orey chari, nuvvu konchem noti dhoola tagginchali ra", r"abba! aapara aprachyapu anumanalu nuvvooonu!!", r"aa pani mathram cheyyakuroy"],
    tuple(["tension"]): [r"aa tension naku undiroy"],
    ("bhattu_bot", "bhattubot"): [r"nikenni saarlu cheppanu Bhattu ani pilavamani, Bhattuu..."],
    ("drink", "mandu", "mandhu", "beer", "vodka"): [r"velli oka beer pattura"],
    ("happy", "joy", "kick"): [r"kicku ra kicku", r"Manchi Shubhavartha chebuthanu, rara", r"ee feeling entra"],
    tuple(["laugh"]): [r"navvu aapukuntunnav kadara"],
    ("hurt", "harsh"): [r"nuvvu antha harshga matladaku, nenu feel authanu"],
    ("blush", "siggu"): [r"Chi chi, miru siggupadakandi", r"Bhattu blushing"],
    tuple(["war", "wars"]): [r"Naku mantralu ravu kabatti saripoyindi gani, vachunte shapinchevadini ra"],
    ("emiti", "hello", "greet", "hi"): [r"bagunnara", r"inka challe aapara"],
    ("untundhi", "untundi", "beautiful", "beauty"): [r"untundhi ra"],
    tuple(["love", "prema"]): [r"Bhattu blushing"],
}

# Hoping to extend Bhattu bot to trigger replies when the keyword "Chaari" is used.
Chaari_dialogue_and_stamp = {

}

Chaari_text_and_link = {

}
