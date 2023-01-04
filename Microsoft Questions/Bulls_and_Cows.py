class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = []
        c = Counter(secret)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                c[guess[i]] -= 1
                l.append(i)

            x = len(l)

        y = 0

        for i in range(len(guess)):
            if guess[i] in c and guess[i] != secret[i] and c[guess[i]] > 0:
                c[guess[i]] -= 1
                y += 1

        return "{}A{}B".format(x, y)

        return "{}A{}B".format(x, y)