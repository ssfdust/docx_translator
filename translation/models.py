from django.db import models

# Create your models here.

class catalog_ids(models.Model):

    """Create a catalogs table to record which id corresponds to a catalog.
       id  int type    catalog id
       catalog varchar type catalog
    """
    id = models.IntegerField(primary_key=True)
    catalog = models.CharField(max_length=50)

class catalog_000(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 000
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_001(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 001
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_002(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 002
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_003(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 003
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_004(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 004
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_005(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 005
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_006(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 006
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_007(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 007
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_008(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 008
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_009(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 009
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_010(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 010
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_011(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 011
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_012(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 012
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_013(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 013
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_014(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 014
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_015(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 015
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_016(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 016
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_017(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 017
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_018(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 018
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_019(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 019
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_020(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 020
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_021(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 021
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_022(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 022
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_023(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 023
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_024(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 024
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_025(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 025
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_026(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 026
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_027(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 027
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_028(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 028
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_029(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 029
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_030(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 030
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_031(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 031
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_032(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 032
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_033(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 033
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_034(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 034
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_035(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 035
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_036(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 036
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_037(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 037
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_038(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 038
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_039(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 039
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_040(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 040
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_041(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 041
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_042(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 042
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_043(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 043
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_044(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 044
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_045(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 045
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_046(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 046
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_047(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 047
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_048(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 048
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_049(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 049
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_050(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 050
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_051(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 051
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_052(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 052
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_053(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 053
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_054(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 054
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_055(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 055
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_056(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 056
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_057(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 057
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_058(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 058
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_059(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 059
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_060(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 060
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_061(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 061
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_062(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 062
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_063(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 063
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_064(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 064
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_065(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 065
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_066(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 066
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_067(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 067
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_068(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 068
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_069(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 069
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_070(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 070
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_071(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 071
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_072(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 072
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_073(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 073
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_074(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 074
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_075(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 075
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_076(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 076
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_077(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 077
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_078(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 078
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_079(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 079
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_080(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 080
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_081(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 081
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_082(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 082
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_083(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 083
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_084(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 084
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_085(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 085
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_086(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 086
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_087(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 087
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_088(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 088
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_089(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 089
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_090(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 090
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_091(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 091
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_092(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 092
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_093(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 093
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_094(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 094
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_095(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 095
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_096(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 096
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_097(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 097
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_098(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 098
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_099(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 099
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word

class catalog_100(models.Model):

    """Create a table which contains catalog id
       and word pair.
       The number of this catalog table is 100
       It contains three columns:
       id    int type    catalog id
       src_word char type  the source word which needs to be subsitute
       tar_word char type  the word that is translated from the source word 
    """
    id = models.IntegerField(primary_key=True)
    src_word = models.CharField(max_length=50)
    tar_word = models.CharField(max_length=50)

    # Return self info
    def __str__(self):
        return self.src_word + "-->" + self.tar_word
