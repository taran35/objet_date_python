# Bonne chance pour la correction !
# Nombre d'heures perdues ici: beaucoup trop (j'ai perdu le compte) 
# Liste des méthodes dans le help(Date)
# Il y a des docstrings ! (65 tests pour être précis)

# Bref je me suis beaucoup amusé moi maintenant va falloir prendre un café avant de le corriger je pense que ça risque d'être long 
# Pour les tests: 2024 est bissextile

def est_bissextile(annee: int) -> bool:
    """
    -------------------------
    Vérifie si une année est bissextile
    -------------------------
    >>> est_bissextile(2024)
    True
    >>> est_bissextile(2023)
    False
    >>> est_bissextile(2000)
    True
    >>> est_bissextile(1900)
    False
    """
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def nb_jours(mois: int, annee: int) -> int:
    """
    -------------------------
    Retourne le nombre de jours dans un mois donné pour une année donnée
    -------------------------
    >>> nb_jours(1, 2024)
    31
    >>> nb_jours(2, 2024)
    29
    >>> nb_jours(2, 2023)
    28
    >>> nb_jours(4, 2024)
    30
    """
    if mois < 1 or mois > 12:
        raise ValueError("Le mois n'existe pas")
    
    if mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mois == 2:
        return 29 if est_bissextile(annee) else 28
    else:
        return 30
            
class Date:
    """
    Methodes disponibles:
        > __sub__ et __add__ 
        --> ajoute / enleve j jours à la date donnée et renvoie une nouvelle date
        > __str__ et __repr__ 
        > .annee() , .mois() , .jour() 
        --> Retourne uniquement la donnée demandée
        > comparaisons: == , != , < , > , <= , >= , 
        > .difference(Date(j/m/aaaa))
        --> retourne la différence en jours entre deux dates (entier positif)
        > .difference_signee(Date(j/m/aaaa))
        --> retourne la différence en jours entre deux dates (entier signé)
        > .bissextile() 
        --> retourne une valeur booléenne si l'année est bissextile ou non
        > .progression_annee()
        --> retourne le numéro du jour dans l'année pour la date donnée (ex: 1er janvier = 1, 31 décembre = 365 ou 366 si bissextile)
        > .jours_restants_annee()
        --> retourne le nombre de jours restants dans l'année pour la date donnée (ex: 1er janvier = 365 ou 366 si bissextile, 31 décembre = 0)

    Alias:
        annees = a, mois = m, jour = j, 
        bissextile = biss, 
        progression_annee = pa, 
        difference = diff,
        difference_signee = diff_s,
        jours_restants_annee = jra


    <!> Definir les dates sans les 0 devant les chiffres (ex: 1/1/2024 et non 01/01/2024) 
    Pareil dans les methodes (ex: .difference(Date(1,1,2024)) et non .difference(Date(01,01,2024)))
    -> Les dates seront affichées avec le format (jj/mm/yyyy) via un f-string
    """
    def __init__(self, day: int, month: int, year: int):
        """
        -------------------------
        initialise une instance de la classe Date avec le jour, le mois et l'année spécifiés
        -------------------------
        >>> Date(29, 2, 2023)
        Traceback (most recent call last):
        ...
        ValueError: Le jour n'existe pas

        >>> Date(32, 1, 2024)
        Traceback (most recent call last):
        ...
        ValueError: Le jour n'existe pas

        >>> Date(1, 13, 2024)
        Traceback (most recent call last):
        ...
        ValueError: Le mois n'existe pas
        """

        if month < 1 or month > 12:
            raise ValueError("Le mois n'existe pas")
        
        if day < 1 or day > nb_jours(month, year):
            raise ValueError("Le jour n'existe pas")

        self.year = year
        self.month = month
        self.day = day



    #__________________________________#
    #_________AFFICHAGE________________#
    #__________________________________#


    def __str__(self):
        """-------------------------
        Retourne la date sous le format (jj/mm/aaaa)
        ----------------------------
        >>> str(Date(1, 1, 2024))
        '(01/01/2024)'
        >>> str(Date(31, 12, 2023))
        '(31/12/2023)'
        """
        return f"({self.day:02d}/{self.month:02d}/{self.year:04d})"

    def __repr__(self):
        """"-------------------------
        retourne la date comme __str__
        -----------------------------
        >>> str(Date(1, 1, 2024))
        '(01/01/2024)'
        >>> str(Date(31, 12, 2023))
        '(31/12/2023)'
        """
        return self.__str__()

    def annee(self):
        """-------------------------
        Retourne l'année de la date
        ----------------------------
        >>> Date(1, 1, 2024).annee()
        2024
        >>> Date(31, 12, 2023).annee()
        2023
        """
        return self.year

    def mois(self):
        """-------------------------
        Retourne le mois de la date
        ----------------------------
        >>> Date(1, 1, 2024).mois()
        1
        >>> Date(31, 12, 2023).mois()
        12
        """
        return self.month
    
    def jour(self):
        """-------------------------
        Retourne le jour de la date
        ----------------------------
        >>> Date(1, 1, 2024).jour()
        1
        >>> Date(31, 12, 2023).jour()
        31
        """
        return self.day



    #__________________________________#
    #_________ADD / SUB________________#
    #__________________________________#



    def __add__(self, j: int):
        """
        -------------------------
        Ajoute j jours à la date actuelle et retourne une nouvelle date
        -> Fonctionne aussi pour la soustraction
        (j'ai réussi en récursif heheh) 
        -------------------------
        >>> Date(30, 1, 2009) + 365 * 10
        (28/01/2019)

        >>> Date(28, 2, 2024) + 1
        (29/02/2024)

        >>> Date(28, 2, 2023) + 1
        (01/03/2023)

        >>> Date(31, 12, 2009) + 1
        (01/01/2010)
        """
        d_temp = self.day + j
        m_temp = self.month
        y_temp = self.year


        jours = nb_jours(m_temp, y_temp)

        
        if d_temp > jours:
            d_temp -= jours
            m_temp += 1

            if m_temp > 12:
                m_temp = 1
                y_temp += 1

            return Date(1, m_temp, y_temp).__add__(d_temp - 1)

        
        if d_temp < 1:
            m_temp -= 1

            if m_temp < 1:
                m_temp = 12
                y_temp -= 1

            
            jours = nb_jours(m_temp, y_temp)

            return Date(jours, m_temp, y_temp).__add__(d_temp)

        return Date(d_temp, m_temp, y_temp)


    def __sub__(self, j: int):
        """
        -------------------------
        Soustrait j jours à la date actuelle et retourne une nouvelle date
        -------------------------
        >>> Date(1, 1, 2010) - 1
        (31/12/2009)

        >>> Date(1, 3, 2024) - 1
        (29/02/2024)

        >>> Date(1, 3, 2023) - 1
        (28/02/2023)
        >>> Date(23,12,2023) - 365*4
        (24/12/2019)
        """
        return self.__add__(-j)


    #__________________________________#
    #_________COMPARAISON______________#
    #__________________________________#


    def __eq__(self, other):
        """
        -------------------------
        Vérifie si deux dates sont égales
        -------------------------
        >>> Date(10, 2, 2009) == Date(10, 2, 2009)
        True
        >>> Date(10, 2, 2009) == Date(11, 2, 2009)
        False
        """
        if not isinstance(other, Date):
            raise TypeError("Comparaison avec un objet non Date")
        
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other):
        """
        -------------------------
        Vérifie si la date actuelle est antérieure à une autre date
        -------------------------
        >>> Date(10, 2, 2009) < Date(11, 2, 2009)
        True
        >>> Date(10, 2, 2009) < Date(10, 2, 2009)
        False
        >>> Date(10, 2, 2009) < Date(9, 2, 2009)
        False
        """
        if not isinstance(other, Date):
            raise TypeError("Comparaison avec un objet non Date")
        
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                return self.day < other.day





    def __le__(self, other):
        """
        -------------------------
        Vérifie si la date actuelle est antérieure ou égale à une autre date
        -------------------------
        >>> Date(10, 2, 2009) <= Date(11, 2, 2009)
        True
        >>> Date(10, 2, 2009) <= Date(10, 2, 2009)
        True
        >>> Date(10, 2, 2009) <= Date(9, 2, 2009)
        False
        """
        return self < other or self == other

    def __gt__(self, other):
        """
        -------------------------
        Vérifie si la date actuelle est postérieure à une autre date
        -------------------------
        >>> Date(11, 2, 2009) > Date(10, 2, 2009)
        True
        >>> Date(10, 2, 2009) > Date(10, 2, 2009)
        False
        >>> Date(9, 2, 2009) > Date(10, 2, 2009)
        False
        """
        return not (self <= other)

    def __ge__(self, other):
        """
        -------------------------
        Vérifie si la date actuelle est postérieure ou égale à une autre date
        -------------------------
        >>> Date(11, 2, 2009) >= Date(10, 2, 2009)
        True
        >>> Date(10, 2, 2009) >= Date(10, 2, 2009)
        True
        >>> Date(9, 2, 2009) >= Date(10, 2, 2009)
        False
        """
        return not (self < other)

    def __ne__(self, other):
        """
        -------------------------
        Vérifie si deux dates sont différentes
        -------------------------
        >>> Date(10, 2, 2009) != Date(11, 2, 2009)
        True
        >>> Date(10, 2, 2009) != Date(10, 2, 2009)
        False
        """
        return not (self == other)


    def difference(self, other):
        """
        -------------------------
        Calcule la différence en jours entre deux dates
        -------------------------
        >>> Date(10, 2, 2009).difference(Date(10, 2, 2010))
        365
        >>> Date(11, 2, 2008).difference(Date(10, 2, 2009))
        365
        >>> Date(10, 2, 2009).difference(Date(10, 2, 2009))
        0
        """
        if not isinstance(other, Date):
            raise TypeError("Comparaison avec un objet non Date")
        
        jours = 0
        date = self

        if self.year > other.year or (self.year == other.year and self.month > other.month) or (self.year == other.year and self.month == other.month and self.day > other.day):
            return other.diff(self)

        while date != other:
            date = date + 1
            jours += 1

        return jours

    def difference_signee(self, other):
        """
        -------------------------
        Calcule la différence en jours entre deux dates, avec le signe approprié
        -------------------------
        >>> Date(10, 2, 2009).difference_signee(Date(10, 2, 2010))
        365
        >>> Date(10, 2, 2009).difference_signee(Date(10, 2, 2009))
        0
        >>> Date(10, 2, 2010).difference_signee(Date(10, 2, 2009))
        -365
        """
        if not isinstance(other, Date):
            raise TypeError("Comparaison avsec un objet non Date")
        
        if self > other:
            return -other.diff(self)
        return self.diff(other)


    #__________________________________#
    #_________METHODES DIVERSES________#
    #__________________________________#


    def bissextile(self):
        """
        -------------------------
        Vérifie si l'année de la date est bissextile
        -------------------------
        >>> Date(1, 1, 2024).bissextile()
        True
        >>> Date(1, 1, 2023).bissextile()
        False
        >>> Date(1, 1, 2000).bissextile()
        True
        >>> Date(1, 1, 1900).bissextile()
        False
        >>> Date(1, 1, 2400).bissextile()
        True
        >>> Date(1, 1, 2100).bissextile()
        False
        """
        return est_bissextile(self.year)

    def progression_annee(self):
        """-------------------------
        Retourne le numéro du jour dans l'année pour la date donnée
        -------------------------
        >>> Date(1, 1, 2024).progression_annee()
        1
        >>> Date(31, 12, 2023).progression_annee()
        365
        >>> Date(1, 3, 2024).progression_annee()
        61
        >>> Date(1, 3, 2023).progression_annee()
        60
        """
        jours = self.day

        for mois in range(1, self.month):
            jours += nb_jours(mois, self.year)

        return jours

    def jours_restants_annee(self):
        """-------------------------
        Retourne le nombre de jours restants dans l'année pour la date donnée
        -------------------------
        >>> Date(1, 1, 2024).jours_restants_annee()
        365
        >>> Date(31, 12, 2023).jours_restants_annee()
        0
        >>> Date(1, 3, 2024).jours_restants_annee()
        305
        >>> Date(1, 1, 2023).jours_restants_annee()
        364
        """
        total = 366 if self.biss() else 365
        return total - self.pa()



    # Alias car j'aime pas les longues fonctions
    pa = progression_annee 
    diff = difference
    diff_s = difference_signee
    biss = bissextile
    jra = jours_restants_annee
    j = jour
    m = mois
    a = annee







if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
