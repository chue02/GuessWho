from game.models import League, Athlete, nflStats
import datetime

def run():
    # Clear table and recreate test table, do this to prevent duplicates in test table after re-running script
    # NOTE: BE CAREFUL ABOUT RUNNING THIS SCRIPT AFTER NON-TESTING DATA IS ADDED
    Athlete.objects.all().delete() # VERY DANGEROUS LINE

    # Create NFL Athletes and stats
    
    nfl = League.objects.get(league=League.LeagueChoices.NFL)

    
    MannEl00 = Athlete.objects.create(league=nfl, name="Eli Manning", teams="NYG", position="QB", birthdate=datetime.date(1981, 1, 3),
                                     college="Mississippi", draft="San Diego Chargers in the 1st round (1st overall) of the 2004 NFL Draft.",
                                     active=False, awards="4x Pro Bowl, 2x SB Champ, 2x SB MVP")

    MannEl00_stats = nflStats.objects.create(athlete=MannEl00, pass_yds=57023, pass_tds=366, pass_ints=244, pass_rtg=84.1, 
                                             qb_rec="117-117-0", pass_sks=411, pass_cmps=4895, pass_atts=8110,
                                             pass_cmp_pct=60.3, pass_yds_per_att=7.0)

    MahoPa00 = Athlete.objects.create(league=nfl, name="Patrick Mahomes", teams="KAN", position="QB", birthdate=datetime.date(1995, 9, 17),
                                     college="Texas Tech", draft="Kansas City Chiefs in the 1st round (10th overall) of the 2017 NFL Draft.",
                                     awards="6x Pro Bowl, 2x 1st Team All-Pro, 3x SB Champ, 2x AP MVP, 3x SB MVP, 2018 AP Off. PoY")

    MahoPa00_stats = nflStats.objects.create(athlete=MahoPa00, pass_yds=32352, pass_tds=245, pass_ints=74, pass_rtg=102.1, 
                                             qb_rec="89-23-0", pass_sks=184, pass_cmps=2778, pass_atts=4171,
                                             pass_cmp_pct=66.6, pass_yds_per_att=7.8)

    RandMo00 = Athlete.objects.create(league=nfl, name="Randy Moss", teams="MIN, OAK, NWE, TEN, SFO", position="WR", birthdate=datetime.date(1977, 2, 13),
                                    college="Marshall", draft="Minnesota Vikings in the 1st round (21st overall) of the 1998 NFL Draft.",
                                    active=False, awards="Hall of Fame, 6x Pro Bowl, 4x 1st Team All-Pro, 1998 Ap Off. RoY")

    RandMo00_stats = nflStats.objects.create(athlete=RandMo00, rec_yds=15292, rec_tds=156, recs=1741, rec_yds_per_att=15.6)

    GateAn00 = Athlete.objects.create(league=nfl, name="Antonio Gates", teams="SDG, LAC", position="TE", birthdate=datetime.date(1980, 6, 18),
                                    college="Kent St.", active=False, awards="Hall of Fame, 8x Pro Bowl, 3x 1st Team All-Pro")

    GateAn00_stats = nflStats.objects.create(athlete=GateAn00, rec_yds=11841, rec_tds=116, recs=955, rec_yds_per_att=12.4)

    SandBa00 = Athlete.objects.create(league=nfl, name="Barry Sanders", teams="DET", position="RB", birthdate=datetime.date(1968, 7, 16),
                                    college="Oklahoma St.", draft="Detroit Lions in the 1st round (3rd overall) of the 1989 NFL Draft.",
                                    active=False, awards="Hall of Fame, 10x Pro Bowl, 6x 1st Team All-Pro, 1997 AP MVP, 2x AP Off. PoY, 1989 AP Off. RoY")

    SandBa00_stats = nflStats.objects.create(athlete=SandBa00, rush_yds=15260, rush_tds=99, rush_atts=3062, 
                                            rush_yds_per_att=5.0)

    LawrTa00 = Athlete.objects.create(league=nfl, name="Lawrence Taylor", teams="NYG", position="LB", birthdate=datetime.date(1959, 2, 4),
                                    college="North Carolina", draft="New York Giants in the 1st round (2nd overall) of the 1981 NFL Draft.",
                                    active=False, awards="Hall of Fame, 10x Pro Bowl, 8x 1st Team All-Pro, 2x SB Champ, 1986 AP MVP, " 
                                    "3x AP Def, PoY, 1981 AP Def. RoY")

    LawrTa00_stats = nflStats.objects.create(athlete=LawrTa00, def_sks=142, def_ints=9, def_int_tds=2)

    WarnFe00 = Athlete.objects.create(league=nfl, name="Fred Warner", teams="SFO", position="LB", birthdate=datetime.date(1996, 11, 19),
                                    college="BYU", draft="San Francisco 49ers in the 3rd round (70th overall) of the 2018 NFL Draft.",
                                    active=True, awards="4x Pro Bowl, 4x 1st Team All-Pro")

    WarnFe00_stats = nflStats.objects.create(athlete=WarnFe00, solo_tkls=569, comb_tkls=897, def_sks=10, tfl=36,
                                            ffmbls=15, fmbl_tds=0, def_ints=10, def_int_tds=2)

    HendTr00 = Athlete.objects.create(league=nfl, name="Trey Hendrickson", teams="NOR, CIN", position="DE", birthdate=datetime.date(1994, 12, 5),
                                    college="Florida Atlantic", draft="New Orleans Saints in the 3rd round (103rd overall) of the 2017 NFL Draft.",
                                    awards="4x Pro Bowl, 1x 1st Team All-Pro")

    HendTr00_stats = nflStats.objects.create(athlete=HendTr00, solo_tkls=151, comb_tkls=220, def_sks=77, tfl=71,
                                            ffmbls=14)

    HarrRo00 = Athlete.objects.create(league=nfl, name="Rodney Harrison", teams="SDG, NWE", position="DB", birthdate=datetime.date(1972, 12, 15),
                                    college="Western Illinois", draft="San Diego Chargers in the 5th round (145th overall) of the 1994 NFL Draft.",
                                    active=False, awards="2x Pro Bowl, 2x 1st Team All-Pro, 2x SB Champ")

    HarrRo00_stats = nflStats.objects.create(athlete=HarrRo00, solo_tkls=920, comb_tkls=1206, def_sks=30.5, tfl=40,
                                            ffmbls=15, fmbl_tds=1, def_ints=34, def_int_tds=2)

    ReviDa00 = Athlete.objects.create(league=nfl, name="Darrelle Revis", teams="NYJ, TAM, NWE, KAN", position="DB", birthdate=datetime.date(1985, 7, 14),
                                    college="Pittsburgh", draft="New York Jets in the 1st round (14th overall) of the 2007 NFL Draft.",
                                    active=False, awards="Hall of Fame, 7x Pro Bowl, 4x 1st Team All-Pro, 1x SB Champ")

    ReviDa00_stats = nflStats.objects.create(athlete=ReviDa00, solo_tkls=411, comb_tkls=496, def_sks=2, tfl=9,
                                            ffmbls=4, def_ints=29, def_int_tds=3)

    LawrDe00 = Athlete.objects.create(league=nfl, name="Dexter lawrence", teams="NYG", position="DL", birthdate=datetime.date(1997, 11, 12),
                                    college="Clemson", draft="New York Giants in the 1st round (17th overall) of the 2019 NFL Draft.",
                                    active=True, awards="3x Pro Bowl")

    LawrDe00_stats = nflStats.objects.create(athlete=LawrDe00, solo_tkls=171, comb_tkls=310, def_sks=30, tfl=36,
                                            ffmbls=5)

