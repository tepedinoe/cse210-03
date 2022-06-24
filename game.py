from random import randint

class game:
    ''' The game class is the main classIt contains the main function, and the game loop. '''
    def __init__(self):
        self._term = term()
        self._animation = animation()
        self._word_list = word_list()
    
    def start_game(self):
        # Start_game function is the main function of the program. It contains the game loop.      
        vword = ['_']
        guess_word = self._word_list.random_word()
        vword = self._word_list.blank_word(guess_word)
        prct = self._animation.create_prct_line()

        while '_' in vword:
            self._term.word_line(vword)

            self._animation.print_prct_line(prct)
            user_guess = self._term.get_input()

            if user_guess in guess_word:
                vword = self._word_list.reveal_letter(guess_word, user_guess)
                print()

            elif user_guess not in guess_word:
                # remove the top prct line in the list
                prct.pop(0)

            if '_' not in vword:
                print(f"{guess_word}\n")
                print("You win!")

            if len(prct) == 5:
                prct[0] = '    x    '
                self._animation.print_prct_line(prct)
                print("You lose!")
                print("The word was: " + guess_word)
                break

class term:
    # prints interaction within the terminal. receives user input
    def get_input(self):
        print()
        guess_letter = input("Guess a letter [a-z]: ")
        print()
        return guess_letter

    def word_line(self, vword):
        # prints the word lin. receives user input

        for i in vword:
            print(i, end=" ")
        print()
        print()

class animation:
    # Need comments
    def __init__(self):
        # define variables to be used throughout the program

        self._prct_line = ""
        self._prct = []

    def create_prct_line(self):
        # create the prct line
        
        self._prct = [
            "  _____  ",
            " /_____\ ",
            " \     / ",
            "  \   /  ",
            "   \ /   ",
            "    O    ",
            "   /|\   ",
            "   / \   ",
            "         ",
            " ^^^^^^^ "
        ]
        print()

        return self._prct

    def print_prct_line(self, prct):
        # print the prct line
        
        for i in range(0, len(prct)):
            print(prct[i], flush=True)

        return prct
class word_list:
    # Contains a list of words to be used in the game.
    # The list is randomly chosen from.
    
    def __init__(self):
        # define variables to be used throughout the program

        self.guess_word = ""
        self.blank_list = []
        self._word_list = word_bank()

    def random_word(self):
        # randomly choose a word from the list
        # return the word
        words_list = self._word_list.list_of_words()
        self.guess_word = words_list[randint(0, len(words_list) - 1)]
        return self.guess_word

    def blank_word(self, guess_word):
        # return a blank word
        for i in range(len(guess_word)):
            self.blank_list.append("_")

        return self.blank_list

    def reveal_letter(self, guess_word, user_guess):
        # reveal the letter in the word
        for i in range(len(guess_word)):
            if guess_word[i] == user_guess:
                self.blank_list[i] = user_guess

        return self.blank_list
class word_bank:
    # Contains a list of words to be used in the game.

    def list_of_words(self):
        # creates and returns the list of words to be used in the game
        words_list = ["computer","rumor","hero","soccer","happen","match","sail","sick","floor","summit","shadow","census","chorus","launch",
            "eject","resist","guilt","repeat","drama","easy","morsel","swipe","equip","reader","pray","grave",
            "cord","cheek","figure","rebel","native","rack","fade","basket","reform","hall","area","root",
            "breeze","shift","cane","cash","hour","galaxy","breed","straw","offset","speech","appear","porter",
            "mosque","flush","sheet","whip","finger","suite","glare","base","catch","cheque","critic","circle",
            "block","talk","salad","bronze","occupy","morale","policy","weak","narrow","essay","Koran","direct",
            "aware","worth","choose","outer","stamp","agile","weave","case","lift","shell","liver","safari",
            "linear","star","makeup","snack","snow","cope","fault","alive","ideal","foot","reduce","solid",
            "inch","arise","master","sigh","shelf","brake","admire","leader","tooth","coach","dare",
            "beam","sell","change","broken","edge","absorb","side","basin","mess","crown","effort","burst",
            "series","upset","beard","lane","palm","wing","torch","heaven","young","stand","polish","pardon",
            "mouth","sphere","charge","grace","back","writer","bridge","even","rent","endure","story","remain",
            "gloom","exile","need","revise","punch","future","date","forest","crash","bald","coup","coma",
            "soak","joint","begin","screen","apple","weight","yard","order","sermon","bird","pity","efflux",
            "mirror","stroll","menu","tube","guest","terms","reveal","long","scrap","rough","lake","score",
            "summer","orbit","seem","wonder","bold","thumb","attack","coffin","sketch","form","tumble","half",
            "member","bacon","rush","castle","poison","mail","steam","core","snail","seller","invite","disk",
            "ready","refer","indoor","kill","weapon","haunt","slice","fame","extent","knife","party",
            "margin","tray","number","medal","bottle","throw","cafe","driver","source","cook","frank","absent",
            "unique","bland","jury","sofa","bundle","brag","clock","debut","nuance","aisle","stroke","wrap",
            "real","wound","slump","friend","kick","powder","crouch","chord","shine","smile","garage","nerve",
            "mayor","depart","lock","oral","close","choke","virtue","tiger","honor","soft","stable","final",
            "pour","snake","prize","damage","donor","land","boat","patrol","light","park","ring","revoke",
            "field","method","widen","chance","revive","tile","watch","pillow","waist","spit","spirit","host",
            "dinner","dine","gown","slip","give","still","item","hurl","cancer","guitar","silk","moving",
            "fence","yearn","oppose","rank","goal","lawyer","turn","rear","hole","asylum","plant","output",
            "detail","soar","entry","full","swim","flex","draw","horn","curl","herd","rock","plan","zone",
            "groan","money","adopt","eaux","space","danger","tract","racism","month","stream","sample","knot",
            "outfit","decide","fair","runner","pain","brown","skate","dome","minor","text","wander","heel",
            "lemon","find","braid","gold","design","seal","title","abuse","bake","king","mile","wine","voice",
            "steep","take","club","jockey","seize","hold","center","filter","shower","blue","bread","enemy",
            "lean","dress","gravel","know","jacket","navy","tone","exact","arch","stake","last","slap","spell",
            "stitch","jest","tiptoe","grain","deck","fire","tired","fight","common","soil","wild","shiver",
            "bill","bishop","dawn","rice","bulb","free","dream","excuse","credit","miss","muscle","offend",
            "fine","chew","cousin","dull","acid","rifle","crew","Venus","truck","remind","trace","effect",
            "stun","debate","glory","crowd","slam","barrel","grief","store","chin","mercy","wall","pawn",
            "debt","layout","video","stem","copy","belief","sweep","appeal","army","hike","asset","brave",
            "list","thread","decade","noble","polite","pile","frame","fate","grip","virus","pure","tidy",
            "sodium","harbor","thigh","public","view","taxi","bait","riot","ridge","tongue","utter","build",
            "funny","scene","trip","movie","scan","ritual","planet","sale","fare","option","just","study",
            "note","tycoon","please","survey","ankle","double","poem","enjoy","useful","drug","theft","horse",
            "pack","instal","fear","quota","bowel","cover","arena","split","elite","allow","wake","abbey",
            "grind","doll","crime","cruel","remark","ditch","insure","clue","favor","topple","move","memory",
            "seed","chaos","X-ray","follow","swear","greet","tactic","column","style","smash","lend","tail",
            "coffee","press","wire","lead","bench","belt","penny","obese","taste","poll","quote","expand",
            "mask","golf","ignite","worm","dragon","tasty","sticky","ivory","spoil","strike","pepper","pilot",
            "iron","gene","reach","sight","bother","twin","heat","file","jelly","angle","desire","amber",
            "neck","vain","float","boom","sting","winter","facade","equal","dozen","valley","tell","want",
            "fairy","carry","bite","string","size","jump","ride","reward","site","teach","help","ignore",
            "gaffe","diet","rate","animal","camera","marble","jail","novel","horror","herb","banner","remedy",
            "mold","desk","aspect","lung","hero","course","fleet","angel","bring","banana","script","room",
            "answer","award","tread","impact","formal","solve","pump","scream","nature","theme","tumour",
            "sweat","ferry","idea","trust","visual","feast","misery","loose","kidnap","lobby","relate",
            "peace","onion","exempt","count","branch","test","harass","bolt","flag","brand","panel","drown",
            "bless","mark","layer","volume","player","dash","prince","locate","cotton","zero","lunch",
            "mature","bind","care","late","deputy","rider","drop","basic","ticket","wait","deep","storm",
            "short","wear","banish","robot","make","earwax","review","sleeve","thesis","black","bell","clear",
            "flock","mind","colony","market","loss","heroin","patent","love","snub","prison","refund","petty",
            "part","card","issue","drain","deadly","tempt","frown","goat","term","drag","vote","east",
            "turkey","flow","lamb","cycle","buffet","prove","moment","show","wage","cower","hammer","heavy",
            "spin","drawer","panic","salt","inside","pull","shrink","shorts","senior","square","lily","meet",
            "dairy","hand","canvas","hell","poor","embryo","meal","year","budget","viable","notice","marsh",
            "punish","shame","rung","wrist","nose","escape","elect","shave","smoke","fill","train","lost",
            "cheap","shop","mutter","fibre","faint","vague","arrest","stool","thaw","colon","high","family",
            "injury","work","enfix","Bible","fruit","person","crisis","pick","stock","bond","urge","fresh",
            "pride","fail","jewel","bloody","virgin","chalk","axis","ballet","laser","extend","desert",
            "cheat","marine","slab","preach","front","ladder","toast","safety","feel","woman","muggy","rise",
            "skip","echo","stage","chest","flight","tease","kidney","forbid","brick","origin","prey","color",
            "draft","team","cheese","agree","junior","carpet","maze","city","shot","suffer","lace","cinema",
            "basis","pastel","large","acquit","afford","organ","hair","power","chase","merit","elbow","energy",
            "place","velvet","exotic","growth","proud","thin","pair","fish","lodge","thank","labour","slime",
            "gain","belly","garlic","climb","latest","time","eagle","wife","pause","chop","kettle","green",
            "album","swell","matrix","rich","wood","sink","spring","worry","tick","voter","fist","plead",
            "relief","slant","bike","brush","fever","door","cable","profit","glass","path","dead","corpse",
            "creed","bang","scrape","minute","thick","jungle","moral","bride","handy","giant","death","start",
            "Sunday","squash","tune","clean","gossip","chain","sacred","father","salmon","tense","halt",
            "gutter","middle","class","method","function","variable","comment","program","python","jumper",
            "readme","church","road","house","mouse","dog","cat","tiger","book","fish"]

        return words_list