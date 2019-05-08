class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def protect_ya_neck(self):
        for line in self.lyrics:
            print(line)


method_lyrics = Song(["It's the Method Man for short Mr. Meth ",
                      "Movin on your left, aah! ",
                      "And set it off, get it off, let it off like a gat ",
                      "I wanna break full, cock me back ",])

odb_lyrics = Song(["First things first man you're fuckin with the worst",
                   "I'll be stickin pins in your head like a fuckin nurse",
                   "I'll attack any nigga who's slack in his mack",
                   "Come fully packed with a fat rugged stack",
                   "Shame on you when you stepped through to",
                   "The Ol Dirty Bastard straight from the Brooklyn Zoo"])

method_lyrics.protect_ya_neck()
odb_lyrics.protect_ya_neck()

