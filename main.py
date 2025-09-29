'''Compte le nombres de lettres dans un mot'''

#### Imports et définition des variables globales ###

### Mandatory for the recursive solution to work on large inputs ###
import sys
sys.setrecursionlimit(2000)

### Fonctions secondaires ###

def artcode_i(s):
    '''Partie itérative'''

    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = s[i]
            count = 1

    result.append((current_char, count))
    return result

def artcode_r(s):
    '''Partie récursive'''

    if not s:
        return []

    first_char = s[0]
    count = 1

    while count < len(s) and s[count] == first_char:
        count += 1

    return [(first_char, count)] + artcode_r(s[count:])

### Fonction principale ###

def main():
    '''Fonction principale'''

    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
